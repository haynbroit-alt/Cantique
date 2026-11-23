"""Parcours d'une arborescence de sources et production des constats au
format du contrat (referentiel/SCHEMA.md). Aucun accès réseau.

Sortie : {"constats": [...], "a_verifier": [...], ...}. « a_verifier »
regroupe ce qui est cryptographique mais dont la famille n'a pas pu être
établie (certificat illisible, clé privée chiffrée…) : ces éléments ne sont
pas des constats du contrat, faute d'identifiant de famille.
"""
from __future__ import annotations

import base64
import fnmatch
import os
import re
from pathlib import Path

from . import __version__
from .analyse_python import analyser_python
from .familles import FAMILLES, Algo, composer_detail, nom_avec_taille, resoudre
from .modele import REGISTRE, Detection, enregistrer
from .pem import MOTIF_PEM, MOTIF_SSH_PUB, algo_cle_ssh, analyser_bloc_pem, analyser_certificat, masquer
from .regles_scan import appliquer_regles

R_PEM_PRIVEE = enregistrer("pem-cle-privee", "tous",
                           "Bloc PEM de clé privée (PKCS#1, SEC1, PKCS#8, OpenSSH) : algorithme et taille lus, contenu masqué")
R_PEM_CERT = enregistrer("pem-certificat", "tous",
                         "Certificat X.509 (PEM, ou DER pour .der/.cer/.crt) : clé publique, signature, expiration")
R_PEM_PUBLIQUE = enregistrer("pem-cle-publique", "tous", "Clé publique, CSR ou paramètres DH/EC au format PEM")
R_PEM_AUTRE = enregistrer("pem-autre", "tous", "Autre bloc PEM (PGP…) : algorithme non analysé, à vérifier")
R_SSH_PUB = enregistrer("ssh-cle-publique", "tous", "Clé publique OpenSSH (authorized_keys, *.pub, known_hosts…)")

EXCLUS_DEFAUT = {"node_modules", "venv", ".venv", "__pycache__", "dist", "build", ".tox", ".mypy_cache",
                 ".pytest_cache", "vendor", "third_party", "site-packages", "bower_components", "target"}
EXCLUS_TOUJOURS = {".git", ".hg", ".svn"}
TAILLE_MAX_DEFAUT = 2 * 1024 * 1024

_EXTENSIONS = {
    ".py": "python", ".pyw": "python", ".java": "java", ".kt": "kotlin", ".kts": "kotlin", ".go": "go",
    ".js": "javascript", ".mjs": "javascript", ".cjs": "javascript", ".jsx": "javascript",
    ".ts": "typescript", ".tsx": "typescript", ".mts": "typescript", ".cts": "typescript",
    ".c": "c", ".h": "c", ".cc": "cpp", ".cpp": "cpp", ".cxx": "cpp", ".hpp": "cpp", ".hh": "cpp", ".hxx": "cpp",
    ".conf": "config", ".cnf": "config", ".cfg": "config", ".ini": "config", ".yaml": "config", ".yml": "config",
    ".properties": "config", ".toml": "config",
    ".pem": "pem", ".crt": "pem", ".cer": "pem", ".key": "pem", ".pub": "pem", ".csr": "pem", ".der": "pem",
}
_DER = {".der", ".cer", ".crt"}

_DOSSIERS_TEST = {"test", "tests", "__tests__", "testing", "testdata", "test-data", "test_data", "spec", "specs",
                  "fixtures", "__mocks__", "mocks", "e2e"}
_DOSSIERS_EXEMPLE = {"example", "examples", "sample", "samples", "demo", "demos", "exemple", "exemples",
                     "tutorial", "tutorials", "quickstart"}
_DOSSIERS_DOC = {"doc", "docs", "documentation"}
_EXT_DOC = {".md", ".rst", ".txt", ".adoc"}
_FICHIERS_TEST = re.compile(
    r"^test_.*\.py$|.*_test\.(?:py|go)$|.*Tests?\.(?:java|kt)$|.*IT\.java$|.*\.(?:test|spec)\.[cm]?[jt]sx?$|^conftest\.py$")
_RANG_CONFIANCE = {"elevee": 3, "moyenne": 2, "faible": 1}


def langage_de(chemin: Path) -> str:
    nom = chemin.name.lower()
    if nom in ("sshd_config", "ssh_config") or nom.endswith(".sshd_config") or \
            (chemin.parent.name in ("sshd_config.d", "ssh_config.d") and nom.endswith(".conf")):
        return "ssh-config"
    return _EXTENSIONS.get(chemin.suffix.lower(), "texte")


def classer_contexte(chemin_relatif: str) -> str:
    """test / exemple / documentation / production, d'après le chemin seul."""
    parts = [p.lower() for p in Path(chemin_relatif).parts]
    dossiers, nom = parts[:-1], Path(chemin_relatif).name
    if any(d in _DOSSIERS_TEST for d in dossiers) or _FICHIERS_TEST.match(nom):
        return "test"
    if any(d in _DOSSIERS_EXEMPLE for d in dossiers) or re.match(r"^(?:example|sample|demo)[_.-]", nom.lower()):
        return "exemple"
    if any(d in _DOSSIERS_DOC for d in dossiers) or Path(nom).suffix.lower() in _EXT_DOC:
        return "documentation"
    return "production"


# ---------------------------------------------------------------------------
# Matériel cryptographique (PEM, DER, clés SSH)
# ---------------------------------------------------------------------------
def _ligne_de(texte: str, pos: int) -> int:
    return texte.count("\n", 0, pos) + 1


def _detections_certificat(ligne: int, infos: dict, extrait: str, regle: str) -> list[Detection]:
    extra = {"certificat": {k: infos[k] for k in ("sujet", "emetteur", "not_before", "not_after", "signature",
                                                  "empreinte_sha256", "analyseur")}}
    dets = []
    cle = infos.get("cle")
    if cle:
        cle.notes.append("certificat")
        dets.append(Detection(ligne, regle, cle, "elevee", ("verify",), [], extra, extrait))
    else:
        dets.append(Detection(ligne, regle, None, "faible", (), ["certificat"], extra, extrait))
    for a in resoudre(infos.get("signature") or ""):
        if not cle or a.famille != cle.famille:
            a.notes.append("cert_signature")
            dets.append(Detection(ligne, regle, a, "elevee", ("sign",), [], {}, extrait))
    return dets


def _materiel(texte: str) -> tuple[list[Detection], list[tuple[int, int]]]:
    """Blocs PEM et clés SSH publiques. Renvoie aussi les plages de lignes des clés privées."""
    dets: list[Detection] = []
    plages: list[tuple[int, int]] = []
    for m in MOTIF_PEM.finditer(texte):
        type_bloc = m.group(1)
        debut, fin = _ligne_de(texte, m.start()), _ligne_de(texte, m.end())
        res = analyser_bloc_pem(type_bloc, m.group(2))
        prive = "cle_privee" in res["notes"]
        extrait = f"-----BEGIN {type_bloc}----- [contenu masqué]" if prive else f"-----BEGIN {type_bloc}-----"
        if prive:
            plages.append((debut, fin))
        if res["certificat"] is not None:
            dets.extend(_detections_certificat(debut, res["certificat"], extrait, R_PEM_CERT))
            continue
        regle = R_PEM_PRIVEE if prive else (R_PEM_PUBLIQUE if res["algos"] or "PUBLIC" in type_bloc
                                            or "REQUEST" in type_bloc or "PARAMETERS" in type_bloc else R_PEM_AUTRE)
        if type_bloc in ("CERTIFICATE", "TRUSTED CERTIFICATE", "X509 CERTIFICATE"):
            regle = R_PEM_CERT
        for a in res["algos"]:
            a.notes.extend(n for n in res["notes"] if n not in a.notes)
            dets.append(Detection(debut, regle, a, "elevee", (), [], {}, extrait))
        if not res["algos"]:
            dets.append(Detection(debut, regle, None, "faible", (), list(res["notes"]), {"type_pem": type_bloc}, extrait))
    for m in MOTIF_SSH_PUB.finditer(texte):
        try:
            a = algo_cle_ssh(base64.b64decode(m.group(2)))
        except Exception:  # blob illisible : on ignore la ligne
            a = None
        if a:
            a.notes.append("ssh_cle_publique")
            dets.append(Detection(_ligne_de(texte, m.start()), R_SSH_PUB, a, "elevee", ("verify",), [], {},
                                  f"{m.group(1)} [clé masquée]"))
    return dets, plages


# ---------------------------------------------------------------------------
# Mise au format du contrat
# ---------------------------------------------------------------------------
def _parametres(d: Detection) -> dict:
    p: dict = {}
    a = d.algo
    if a:
        p["algorithme"] = nom_avec_taille(a)
        p["primitive"] = a.primitive
        for cle, val in (("taille_cle", a.taille), ("courbe", a.courbe), ("mode", a.mode), ("remplissage", a.remplissage)):
            if val:
                p[cle] = val
    if d.fonctions:
        p["fonctions"] = list(d.fonctions)
    notes = (a.notes if a else []) + [n for n in d.notes if not a or n not in a.notes]
    if notes:
        p["notes"] = notes
    p.update(d.extra)
    return p


def _constat(d: Detection, fichier: str, langage: str, contexte: str, lignes: list[str]) -> dict:
    p = _parametres(d)
    source = lignes[d.ligne - 1] if 0 < d.ligne <= len(lignes) else ""
    return {
        "famille": d.algo.famille if d.algo else None,
        "classe": FAMILLES[d.algo.famille] if d.algo else None,
        "detail": composer_detail(p, "fr") if d.algo else composer_detail({"algorithme": p.get("type_pem", "?"), **p}, "fr"),
        "fichier": fichier,
        "ligne": d.ligne,
        "extrait": masquer(d.extrait if d.extrait is not None else source),
        "langage": langage,
        "regle": d.regle,
        "confiance": d.confiance,
        "contexte": contexte,
        "parametres": p,
    }


def _rang(d: Detection) -> tuple:
    a = d.algo
    renseigne = sum(1 for v in (a.taille, a.courbe, a.mode) if v) if a else 0
    return _RANG_CONFIANCE[d.confiance], renseigne


def _dedupliquer(dets: list[Detection]) -> list[Detection]:
    """Même ligne et même famille : deux règles différentes = un seul constat (le plus sûr) ;
    une même règle peut en revanche produire plusieurs éléments distincts (liste de versions, de JWT…)."""
    gardes: list[Detection] = []
    for d in dets:
        fam = d.algo.famille if d.algo else None
        doublon = False
        for i, k in enumerate(gardes):
            kfam = k.algo.famille if k.algo else None
            if k.ligne != d.ligne or kfam != fam:
                continue
            if k.regle == d.regle and (not d.algo or nom_avec_taille(k.algo) != nom_avec_taille(d.algo)):
                continue
            doublon = True
            if _rang(d) > _rang(k):
                gardes[i] = d
            break
        if not doublon:
            gardes.append(d)
    familles_utilisees = {d.algo.famille for d in gardes if d.algo and "import" not in d.algo.notes}
    return [d for d in gardes if not (d.algo and "import" in d.algo.notes and d.algo.famille in familles_utilisees)]


def analyser_fichier(chemin: Path, relatif: str, taille_max: int = TAILLE_MAX_DEFAUT) -> tuple[list[dict], list[dict], str]:
    """Renvoie (constats, a_verifier, statut) ; statut ∈ {"analyse", "binaire", "taille", "illisible"}."""
    try:
        if chemin.stat().st_size > taille_max:
            return [], [], "taille"
        brut = chemin.read_bytes()
    except OSError:
        return [], [], "illisible"
    langage = langage_de(chemin)
    contexte = classer_contexte(relatif)
    dets: list[Detection] = []
    if b"\x00" in brut[:8192]:
        infos = analyser_certificat(brut) if chemin.suffix.lower() in _DER else None
        if not infos:
            return [], [], "binaire"
        dets = _detections_certificat(0, infos, f"[certificat DER binaire, SHA-256 {infos['empreinte_sha256'][:16]}…]",
                                      R_PEM_CERT)
        texte = ""
    else:
        texte = brut.decode("utf-8", errors="replace")
        materiel, plages = _materiel(texte)
        if langage == "python":
            code = analyser_python(texte)
            code = appliquer_regles(texte, "python-texte") if code is None else code
        else:
            code = appliquer_regles(texte, langage)
        code = [d for d in code if not any(a <= d.ligne <= b for a, b in plages)]
        dets = materiel + code
    dets.sort(key=lambda d: (d.ligne, d.regle, d.algo.famille if d.algo else "", d.algo.nom if d.algo else ""))
    dets = _dedupliquer(dets)
    lignes = texte.splitlines()
    affiche = {"python-texte": "python"}.get(langage, langage)
    constats, a_verifier = [], []
    for d in dets:
        (constats if d.algo else a_verifier).append(_constat(d, relatif, affiche, contexte, lignes))
    return constats, a_verifier, "analyse"


def scanner(racine: str | os.PathLike, inclure_vendor: bool = False, exclure: list[str] | None = None,
            taille_max: int = TAILLE_MAX_DEFAUT) -> dict:
    racine = Path(racine)
    exclure = exclure or []
    stats = {"fichiers_analyses": 0, "binaire": 0, "taille": 0, "illisible": 0, "lien": 0, "exclu": 0}
    constats: list[dict] = []
    a_verifier: list[dict] = []

    def traiter(chemin: Path, relatif: str) -> None:
        if any(fnmatch.fnmatch(relatif, motif) for motif in exclure):
            stats["exclu"] += 1
            return
        c, v, statut = analyser_fichier(chemin, relatif, taille_max)
        stats["fichiers_analyses" if statut == "analyse" else statut] += 1
        constats.extend(c)
        a_verifier.extend(v)

    if racine.is_file():
        traiter(racine, racine.name)
    else:
        for dossier, sous_dossiers, fichiers in os.walk(racine):
            sous_dossiers[:] = sorted(
                s for s in sous_dossiers
                if s not in EXCLUS_TOUJOURS and (inclure_vendor or s not in EXCLUS_DEFAUT)
                and not os.path.islink(os.path.join(dossier, s)))
            for nom in sorted(fichiers):
                chemin = Path(dossier, nom)
                if chemin.is_symlink():
                    stats["lien"] += 1
                    continue
                traiter(chemin, chemin.relative_to(racine).as_posix())
    cle_tri = lambda c: (c["fichier"], c["ligne"], c["famille"] or "", c["regle"], c["detail"])  # noqa: E731
    return {
        "format": "pqc-inventaire/constats",
        "version_format": 1,
        "outil": {"nom": "pqc-inventaire", "version": __version__},
        "type": "code",
        "projet": racine.resolve().name,
        "statistiques": {**stats, "regles": len(REGISTRE)},
        "constats": sorted(constats, key=cle_tri),
        "a_verifier": sorted(a_verifier, key=cle_tri),
    }


def charger_constats(chemins: list[str]) -> tuple[list[dict], list[dict], list[dict]]:
    """Lit des fichiers de constats (code ou TLS). Accepte aussi une simple liste de constats.

    Renvoie (documents, constats, a_verifier)."""
    import json

    documents, constats, a_verifier = [], [], []
    for chemin in chemins:
        with open(chemin, encoding="utf-8") as f:
            doc = json.load(f)
        if isinstance(doc, list):
            doc = {"type": "inconnu", "constats": doc}
        doc["_source"] = os.path.basename(chemin)
        documents.append(doc)
        for c in doc.get("constats") or []:
            if c.get("famille") not in FAMILLES:
                a_verifier.append(c)
            else:
                constats.append(c)
        a_verifier.extend(doc.get("a_verifier") or [])
    return documents, constats, a_verifier


__all__ = ["scanner", "analyser_fichier", "classer_contexte", "charger_constats", "langage_de", "Algo"]
