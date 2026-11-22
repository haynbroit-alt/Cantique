"""Production d'un CBOM CycloneDX 1.6 (composants « cryptographic-asset »)
à partir des constats du scanner de code et de la sonde TLS.

- un composant « algorithm » par algorithme distinct (RSA-2048, AES-256-GCM…),
  avec toutes ses occurrences dans evidence.occurrences ;
- un composant « protocol » par version TLS observée, avec ses suites ;
- un composant « certificate » par certificat distinct, relié à l'algorithme
  de signature et à sa clé publique (« related-crypto-material ») ;
- un composant « related-crypto-material » par clé privée trouvée dans les fichiers.

Sortie déterministe : numéro de série dérivé du contenu, composants triés.
"""
from __future__ import annotations

import hashlib
import json
import re
import uuid
from datetime import datetime, timezone

from . import __version__
from .familles import FAMILLES, Algo, niveau_classique, niveau_quantique, oid_de, resoudre

_PRIMITIVES = {"drbg", "mac", "block-cipher", "stream-cipher", "signature", "hash", "pke", "xof", "kdf",
               "key-agree", "kem", "ae", "combiner", "other", "unknown"}
_FONCTIONS = {"generate", "keygen", "encrypt", "decrypt", "digest", "tag", "keyderive", "sign", "verify",
              "encapsulate", "decapsulate", "other", "unknown"}
_MODES = {"cbc", "ecb", "ccm", "gcm", "cfb", "ofb", "ctr", "other", "unknown"}
_REMPLISSAGES = {"pkcs5", "pkcs7", "pkcs1v15", "oaep", "raw", "other", "unknown"}
_RANG = {"elevee": 3, "moyenne": 2, "faible": 1}
P = "pqc-inventaire:"


def _slug(texte: str) -> str:
    return re.sub(r"[^a-z0-9.]+", "-", texte.lower()).strip("-") or "inconnu"


def _algo_depuis(c: dict) -> Algo:
    p = c.get("parametres") or {}
    return Algo(c["famille"], p.get("algorithme") or c["famille"], p.get("primitive") or "unknown",
                taille=p.get("taille_cle"), courbe=p.get("courbe"), mode=p.get("mode"),
                remplissage=p.get("remplissage"))


def _jeu_parametres(a: Algo) -> str | None:
    if a.famille in ("RSA", "DH", "DSA", "AES") and a.taille:
        return str(a.taille)
    m = re.fullmatch(r"(?:ML-KEM|ML-DSA|FN-DSA)-(\d+)", a.nom)
    if m:
        return m.group(1)
    m = re.fullmatch(r"SLH-DSA-(.+)", a.nom)
    if m:
        return m.group(1)
    m = re.fullmatch(r"SHA3?-(\d{3})(?:/(\d{3}))?|SHAKE(\d{3})", a.nom)
    if m:
        return m.group(2) or m.group(1) or m.group(3)
    return None


def _occurrence(c: dict) -> dict:
    occ = {"location": c["fichier"], "line": max(int(c.get("ligne") or 0), 0)}
    occ["additionalContext"] = f"{c['regle']}; {c.get('contexte', '?')}; confiance {c.get('confiance', '?')}"
    return occ


class _Cbom:
    def __init__(self) -> None:
        self.composants: dict[str, dict] = {}
        self.occurrences: dict[str, dict[tuple, dict]] = {}
        self.meta: dict[str, dict] = {}

    def _composant(self, ref: str, nom: str, proprietes_crypto: dict) -> dict:
        if ref not in self.composants:
            self.composants[ref] = {"type": "cryptographic-asset", "bom-ref": ref, "name": nom,
                                    "cryptoProperties": proprietes_crypto}
            self.occurrences[ref] = {}
            self.meta[ref] = {"familles": set(), "contextes": set(), "confiance": 0, "fonctions": set(), "extra": {}}
        return self.composants[ref]

    def _noter(self, ref: str, c: dict) -> None:
        occ = _occurrence(c)
        self.occurrences[ref].setdefault((occ["location"], occ["line"], c["regle"]), occ)
        m = self.meta[ref]
        if c.get("famille"):
            m["familles"].add(c["famille"])
        m["contextes"].add(c.get("contexte", "?"))
        m["confiance"] = max(m["confiance"], _RANG.get(c.get("confiance"), 0))

    def algorithme(self, a: Algo, c: dict) -> str:
        ref = f"crypto/algorithm/{_slug(a.nom)}"
        props: dict = {"primitive": a.primitive if a.primitive in _PRIMITIVES else "unknown"}
        jeu = _jeu_parametres(a)
        if jeu:
            props["parameterSetIdentifier"] = jeu
        if a.courbe:
            props["curve"] = a.courbe
        if a.mode in _MODES:
            props["mode"] = a.mode
        if a.remplissage in _REMPLISSAGES:
            props["padding"] = a.remplissage
        for cle, val in (("classicalSecurityLevel", niveau_classique(a)), ("nistQuantumSecurityLevel", niveau_quantique(a))):
            if val is not None:
                props[cle] = val
        crypto = {"assetType": "algorithm", "algorithmProperties": props}
        oid = oid_de(a)
        if oid:
            crypto["oid"] = oid
        self._composant(ref, a.nom, crypto)
        self._noter(ref, c)
        fonctions = (c.get("parametres") or {}).get("fonctions") or []
        self.meta[ref]["fonctions"].update(f for f in fonctions if f in _FONCTIONS)
        return ref

    def protocole(self, c: dict) -> None:
        p = c.get("parametres") or {}
        version = p.get("version_tls") or p.get("algorithme") or ""
        if not re.fullmatch(r"(?:TLS|SSL) \d\.\d", version):
            version = "TLS"
        ref = f"crypto/protocol/{_slug(version)}"
        props: dict = {"type": "tls"}
        if version != "TLS":
            props["version"] = version.split()[1] if version.startswith("TLS") else version
        self._composant(ref, version if version != "TLS" else "TLS (version non précisée)",
                        {"assetType": "protocol", "protocolProperties": props})
        self._noter(ref, c)
        extra = self.meta[ref]["extra"]
        ids = p.get("identifiants_suites") or {}
        for s in p.get("suites") or []:
            if re.fullmatch(r"TLS_[A-Z0-9_]+", s):
                extra.setdefault("suites", {})[s] = ids.get(s) or []
            else:
                extra.setdefault("chaines", set()).add(s)

    def certificat(self, c: dict, cert: dict, cle: Algo | None) -> None:
        empreinte = cert.get("empreinte_sha256") or hashlib.sha256(json.dumps(cert, sort_keys=True).encode()).hexdigest()
        ref = f"crypto/certificate/{empreinte[:16]}"
        props: dict = {"certificateFormat": "X.509"}
        for cle_cdx, cle_cert in (("subjectName", "sujet"), ("issuerName", "emetteur"),
                                  ("notValidBefore", "not_before"), ("notValidAfter", "not_after")):
            if cert.get(cle_cert):
                props[cle_cdx] = cert[cle_cert]
        ext = c["fichier"].rsplit(".", 1)[-1].lower() if "." in c["fichier"].rsplit("/", 1)[-1] else ""
        if ext in ("pem", "crt", "cer", "der"):
            props["certificateExtension"] = ext
        composant = self._composant(ref, cert.get("sujet") or f"certificat {empreinte[:12]}",
                                    {"assetType": "certificate", "certificateProperties": props})
        self._noter(ref, c)
        self.meta[ref]["extra"]["empreinte"] = empreinte
        sig = resoudre(cert.get("signature") or "")
        if sig:
            props["signatureAlgorithmRef"] = self.algorithme(sig[0], {**c, "parametres": {"fonctions": ["sign"]}})
        if cle:
            ref_algo = self.algorithme(cle, c)
            ref_cle = f"crypto/related-crypto-material/cle-publique-{empreinte[:16]}"
            rcm = {"type": "public-key", "algorithmRef": ref_algo}
            if cle.taille:
                rcm["size"] = int(cle.taille)
            self._composant(ref_cle, f"clé publique {cle.nom} ({cert.get('sujet') or empreinte[:12]})",
                            {"assetType": "related-crypto-material", "relatedCryptoMaterialProperties": rcm})
            self._noter(ref_cle, c)
            props["subjectPublicKeyRef"] = ref_cle
        composant["cryptoProperties"]["certificateProperties"] = props

    def cle_privee(self, c: dict, ref_algo: str | None, taille: int | None) -> None:
        ref = f"crypto/related-crypto-material/cle-privee-{_slug(c['fichier'])}-{c.get('ligne', 0)}"
        rcm: dict = {"type": "private-key"}
        if ref_algo:
            rcm["algorithmRef"] = ref_algo
        if taille:
            rcm["size"] = int(taille)
        self._composant(ref, f"clé privée stockée dans {c['fichier']}",
                        {"assetType": "related-crypto-material", "relatedCryptoMaterialProperties": rcm})
        self._noter(ref, c)

    def finaliser(self) -> list[dict]:
        res = []
        noms_confiance = {3: "elevee", 2: "moyenne", 1: "faible", 0: "inconnue"}
        for ref in sorted(self.composants):
            comp = self.composants[ref]
            m = self.meta[ref]
            crypto = comp["cryptoProperties"]
            if crypto["assetType"] == "algorithm":
                crypto["algorithmProperties"]["cryptoFunctions"] = sorted(m["fonctions"]) or ["unknown"]
            if crypto["assetType"] == "protocol":
                suites = m["extra"].get("suites") or {}
                if suites:
                    crypto["protocolProperties"]["cipherSuites"] = [
                        {"name": n, **({"identifiers": ids} if ids else {})} for n, ids in sorted(suites.items())]
            comp["evidence"] = {"occurrences": sorted(self.occurrences[ref].values(),
                                                      key=lambda o: (o["location"], o["line"], o["additionalContext"]))}
            proprietes = [{"name": P + "occurrences", "value": str(len(self.occurrences[ref]))},
                          {"name": P + "contextes", "value": ",".join(sorted(m["contextes"]))},
                          {"name": P + "confiance_max", "value": noms_confiance[m["confiance"]]}]
            for fam in sorted(m["familles"]):
                proprietes += [{"name": P + "famille", "value": fam}, {"name": P + "classe", "value": FAMILLES[fam]}]
            for chaine in sorted(m["extra"].get("chaines", ())):
                proprietes.append({"name": P + "chaine_suites", "value": chaine})
            if "empreinte" in m["extra"]:
                proprietes.append({"name": P + "empreinte_sha256", "value": m["extra"]["empreinte"]})
            comp["properties"] = proprietes
            res.append(comp)
        return res


def construire_cbom(constats: list[dict], a_verifier: list[dict] | None = None, nom: str | None = None,
                    sources: list[str] | None = None, horodatage: str | None = None) -> dict:
    b = _Cbom()
    for c in constats:
        p = c.get("parametres") or {}
        if c["famille"] in ("TLS_SUITE", "TLS_LEGACY"):
            b.protocole(c)
            continue
        a = _algo_depuis(c)
        if p.get("certificat"):
            notes = p.get("notes") or []
            est_cle = "cert_signature" not in notes and "tls_cert_signature" not in notes
            b.certificat(c, p["certificat"], a if est_cle else None)
            if not est_cle:
                b.algorithme(a, c)
            continue
        ref = b.algorithme(a, c)
        if "cle_privee" in (p.get("notes") or []):
            b.cle_privee(c, ref, a.taille)
    for c in a_verifier or []:
        p = c.get("parametres") or {}
        if p.get("certificat"):
            b.certificat(c, p["certificat"], None)
        elif "cle_privee" in (p.get("notes") or []):
            b.cle_privee(c, None, None)
    composants = b.finaliser()
    corps = json.dumps(composants, sort_keys=True, ensure_ascii=False)
    serie = uuid.uuid5(uuid.NAMESPACE_URL, "urn:pqc-inventaire:" + hashlib.sha256(corps.encode()).hexdigest())
    meta: dict = {
        "timestamp": horodatage or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tools": {"components": [{"type": "application", "name": "pqc-inventaire", "version": __version__}]},
        "component": {"type": "application", "bom-ref": "cible-analysee", "name": nom or "cible analysée"},
        "properties": [{"name": P + "avertissement",
                        "value": "Inventaire issu d'une analyse statique et de sondes TLS : faux positifs et "
                                 "omissions possibles ; à relire par un humain avant toute décision."}],
    }
    for s in sources or []:
        meta["properties"].append({"name": P + "source", "value": s})
    return {
        "$schema": "http://cyclonedx.org/schema/bom-1.6.schema.json",
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{serie}",
        "version": 1,
        "metadata": meta,
        "components": composants,
    }


def valider_cbom(cbom: dict) -> list[str] | None:
    """Valide contre le schéma CycloneDX 1.6 officiel (via cyclonedx-python-lib).

    Renvoie None si le validateur n'est pas installé, [] si le document est valide,
    sinon la liste des erreurs."""
    try:
        from cyclonedx.schema import SchemaVersion
        from cyclonedx.validation.json import JsonStrictValidator
    except ImportError:
        return None
    erreurs = JsonStrictValidator(SchemaVersion.V1_6).validate_str(json.dumps(cbom), all_errors=True)
    if erreurs is None:
        return []
    return [str(getattr(e, "data", e)) for e in erreurs]
