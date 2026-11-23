"""Interface en ligne de commande : pqc-inventaire scan-code | cbom | rapport | regles."""
from __future__ import annotations

import argparse
import json
import sys

from . import __version__


def _ecrire(texte: str, sortie: str | None) -> None:
    if sortie and sortie != "-":
        with open(sortie, "w", encoding="utf-8") as f:
            f.write(texte)
    else:
        sys.stdout.write(texte)


def _scan(args) -> int:
    from .scanner import scanner

    doc = scanner(args.chemin, inclure_vendor=args.inclure_vendor, exclure=args.exclure, taille_max=args.taille_max)
    _ecrire(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", args.o)
    print(f"{len(doc['constats'])} constat(s), {len(doc['a_verifier'])} élément(s) à vérifier, "
          f"{doc['statistiques']['fichiers_analyses']} fichier(s) analysé(s).", file=sys.stderr)
    return 0


def _cbom(args) -> int:
    from .cbom import construire_cbom, valider_cbom
    from .scanner import charger_constats

    docs, constats, a_verifier = charger_constats(args.constats)
    nom = args.nom or next((d.get("projet") for d in docs if d.get("projet")), None)
    cbom = construire_cbom(constats, a_verifier, nom=nom, sources=[d["_source"] for d in docs], horodatage=args.date)
    _ecrire(json.dumps(cbom, ensure_ascii=False, indent=2) + "\n", args.o)
    if args.validate:
        erreurs = valider_cbom(cbom)
        if erreurs is None:
            print("Validation impossible : installer cyclonedx-python-lib[json-validation].", file=sys.stderr)
            return 2
        if erreurs:
            print(f"CBOM NON VALIDE ({len(erreurs)} erreur(s)) :", file=sys.stderr)
            for e in erreurs[:20]:
                print(f"  - {e}", file=sys.stderr)
            return 1
        print("CBOM valide (schéma CycloneDX 1.6).", file=sys.stderr)
    return 0


def _rapport(args) -> int:
    from .rapport import generer_rapport
    from .scanner import charger_constats

    docs, constats, a_verifier = charger_constats(args.constats)
    with open(args.regles, encoding="utf-8") as f:
        regles = json.load(f)
    if args.juridictions:
        gardees = {j.strip().upper() for j in args.juridictions.split(",") if j.strip()}
        regles = {**regles, "referentiels": [r for r in regles.get("referentiels") or []
                                             if (r.get("juridiction") or "").upper() in gardees]}
    texte = generer_rapport(docs, constats, a_verifier, regles, args.client, langue=args.langue, marque=args.marque,
                            date=args.date, regles_chemin=args.regles.replace("\\", "/").rsplit("/", 1)[-1],
                            max_lignes=args.max_lignes)
    _ecrire(texte, args.o)
    return 0


def _regles(args) -> int:
    from . import analyse_python, scanner  # noqa: F401  (enregistre les règles)
    from .modele import REGISTRE

    for rid, (langages, description) in sorted(REGISTRE.items()):
        print(f"{rid}\t{langages}\t{description}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="pqc-inventaire", description="Inventaire cryptographique, CBOM et rapport PQC.")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sp = p.add_subparsers(dest="commande", required=True)

    s = sp.add_parser("scan-code", help="analyser une arborescence de sources")
    s.add_argument("chemin")
    s.add_argument("-o", help="fichier de sortie JSON (défaut : sortie standard)")
    s.add_argument("--inclure-vendor", action="store_true",
                   help="analyser aussi node_modules, venv, dist, build, vendor… (.git reste exclu)")
    s.add_argument("--exclure", action="append", default=[], metavar="MOTIF", help="motif glob de chemin relatif à exclure")
    s.add_argument("--taille-max", type=int, default=2 * 1024 * 1024, metavar="OCTETS")
    s.set_defaults(fn=_scan)

    c = sp.add_parser("cbom", help="produire un CBOM CycloneDX 1.6")
    c.add_argument("constats", nargs="+", help="fichiers de constats JSON (code, TLS)")
    c.add_argument("-o", help="fichier de sortie (défaut : sortie standard)")
    c.add_argument("--validate", "--valider", action="store_true", help="valider contre le schéma CycloneDX 1.6 officiel")
    c.add_argument("--nom", help="nom de l'application analysée")
    c.add_argument("--date", help="horodatage ISO 8601 (pour une sortie reproductible)")
    c.set_defaults(fn=_cbom)

    r = sp.add_parser("rapport", help="produire le rapport Markdown")
    r.add_argument("constats", nargs="+")
    r.add_argument("--regles", required=True, help="chemin de regles.json")
    r.add_argument("--client", required=True)
    r.add_argument("--langue", choices=("fr", "en"), default="fr")
    r.add_argument("--marque", help="nom du partenaire (marque blanche : aucune mention de l'atelier)")
    r.add_argument("--date", help="date du rapport AAAA-MM-JJ (défaut : aujourd'hui)")
    r.add_argument("--juridictions", metavar="LISTE",
                   help="ne garder que ces juridictions du référentiel, ex. INT,EU,FR (défaut : toutes)")
    r.add_argument("--max-lignes", type=int, default=400, help="lignes maximales du tableau par emplacement")
    r.add_argument("-o", help="fichier de sortie (défaut : sortie standard)")
    r.set_defaults(fn=_rapport)

    g = sp.add_parser("regles", help="lister les règles de détection")
    g.set_defaults(fn=_regles)

    args = p.parse_args(argv)
    return args.fn(args)
