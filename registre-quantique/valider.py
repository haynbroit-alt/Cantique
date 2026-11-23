#!/usr/bin/env python3
"""Valide affirmations.jsonl contre schema.json (bibliothèque standard uniquement).

Contrôles : chaque ligne est un objet JSON ; champs obligatoires présents et aucun
champ inconnu ; valeurs d'énumération valides ; dates ISO (AAAA, AAAA-MM ou
AAAA-MM-JJ) réelles ; identifiants uniques ; liens vers des identifiants existants ;
URL commençant par http ; règles de statut (un statut verifie_tiers, contredit,
en_retard ou retire exige statut_source_url ; une réfutation pointe vers ce qu'elle
conteste). Si le paquet jsonschema est installé, chaque ligne est en plus validée
contre schema.json (draft 2020-12).

Usage : python3 valider.py [affirmations.jsonl] [--schema schema.json]
                           [--aujourdhui AAAA-MM-JJ] [--strict]
Code de sortie : 0 si aucune erreur, 1 sinon (avec --strict, les avertissements
comptent comme des erreurs).
"""

import argparse
import calendar
import datetime as dt
import json
import re
import sys
from collections import Counter
from pathlib import Path

ICI = Path(__file__).resolve().parent
RE_DATE_PARTIELLE = re.compile(r"^(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?$")
RE_DATE_COMPLETE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RE_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RE_URL = re.compile(r"^https?://\S+$")
STATUTS_A_JUSTIFIER = {"verifie_tiers", "contredit", "en_retard", "retire"}


def bornes_date(texte):
    """Renvoie (premier jour, dernier jour) d'une date partielle, ou None si invalide."""
    if not isinstance(texte, str):
        return None
    m = RE_DATE_PARTIELLE.match(texte)
    if not m:
        return None
    annee = int(m.group(1))
    try:
        if m.group(3):
            jour = dt.date(annee, int(m.group(2)), int(m.group(3)))
            return jour, jour
        if m.group(2):
            mois = int(m.group(2))
            dernier = calendar.monthrange(annee, mois)[1]
            return dt.date(annee, mois, 1), dt.date(annee, mois, dernier)
        return dt.date(annee, 1, 1), dt.date(annee, 12, 31)
    except ValueError:
        return None


class Regles:
    """Vocabulaires et structure lus dans schema.json, seule source de vérité."""

    def __init__(self, schema):
        props = schema["properties"]
        defs = schema["$defs"]
        self.schema = schema
        self.requis = list(schema["required"])
        self.champs = set(props)
        self.types = set(props["type"]["enum"])
        self.statuts = set(props["statut"]["enum"])
        self.types_source = set(props["source_type"]["enum"])
        self.precisions = set(props["precision_date"]["enum"])
        self.comparateurs = set(defs["comparateur"]["enum"])
        self.metriques = set(defs["metrique"]["enum"])
        self.champs_mesure = set(defs["mesure"]["properties"])
        self.requis_mesure = set(defs["mesure"]["required"])
        self.champs_source = set(defs["source"]["properties"])


def verifier_entree(e, r, err, avert, aujourdhui):
    def est_texte(champ, vide_ok=False):
        v = e.get(champ)
        if not isinstance(v, str) or (not vide_ok and not v.strip()):
            err(f"« {champ} » doit être une chaîne non vide")
            return False
        return True

    def date_ok(champ, nullable=False, complete=False):
        v = e.get(champ)
        if v is None and nullable:
            return None
        if complete and not (isinstance(v, str) and RE_DATE_COMPLETE.match(v)):
            err(f"« {champ} » doit être une date complète AAAA-MM-JJ (reçu {v!r})")
            return None
        b = bornes_date(v)
        if b is None:
            err(f"« {champ} » n'est pas une date ISO valide (reçu {v!r})")
        return b

    def url_ok(valeur, champ):
        if not (isinstance(valeur, str) and RE_URL.match(valeur)):
            err(f"« {champ} » doit commencer par http:// ou https:// (reçu {valeur!r})")

    def nombre(v):
        return isinstance(v, (int, float)) and not isinstance(v, bool)

    for champ in r.requis:
        if champ not in e:
            err(f"champ obligatoire manquant : « {champ} »")
    for champ in e:
        if champ not in r.champs:
            err(f"champ inconnu : « {champ} »")

    if "id" in e and not (isinstance(e["id"], str) and RE_ID.match(e["id"]) and len(e["id"]) <= 96):
        err(f"« id » doit être un slug en minuscules (reçu {e['id']!r})")
    for champ in ("acteur", "enonce", "source_titre"):
        if champ in e:
            est_texte(champ)

    for champ, permis in (("type", r.types), ("statut", r.statuts), ("source_type", r.types_source),
                          ("metrique", r.metriques)):
        if champ in e and e[champ] not in permis:
            err(f"« {champ} » hors vocabulaire : {e[champ]!r}")
    if "precision_date" in e and e["precision_date"] not in r.precisions:
        err(f"« precision_date » hors vocabulaire : {e['precision_date']!r}")
    if "comparateur" in e and e["comparateur"] not in r.comparateurs:
        err(f"« comparateur » hors vocabulaire : {e['comparateur']!r}")

    if "valeur" in e and not (nombre(e["valeur"]) or isinstance(e["valeur"], str)):
        err("« valeur » doit être un nombre ou une chaîne")
    for champ in ("valeur_min", "valeur_max"):
        if champ in e and not nombre(e[champ]):
            err(f"« {champ} » doit être un nombre")
    if nombre(e.get("valeur_min")) and nombre(e.get("valeur_max")) and e["valeur_min"] > e["valeur_max"]:
        err("« valeur_min » est supérieure à « valeur_max »")
    for champ in ("unite", "conflit_interet", "note"):
        if champ in e and e[champ] is not None and not isinstance(e[champ], str):
            err(f"« {champ} » doit être une chaîne ou null")
    if "verbatim" in e and not isinstance(e["verbatim"], bool):
        err("« verbatim » doit être true ou false")

    b_affirmation = date_ok("date_affirmation") if "date_affirmation" in e else None
    b_echeance = date_ok("echeance_promise", nullable=True) if "echeance_promise" in e else None
    b_consultation = date_ok("date_consultation", complete=True) if "date_consultation" in e else None
    b_saisie = date_ok("date_saisie", complete=True) if "date_saisie" in e else None
    b_statut = date_ok("statut_date", nullable=True) if "statut_date" in e else None

    if b_affirmation and b_saisie and b_affirmation[0] > b_saisie[0]:
        err("« date_affirmation » est postérieure à « date_saisie »")
    if b_affirmation and b_consultation and b_affirmation[0] > b_consultation[0]:
        err("« date_affirmation » est postérieure à « date_consultation »")

    if "source_url" in e:
        url_ok(e["source_url"], "source_url")
    if e.get("statut_source_url") is not None:
        url_ok(e["statut_source_url"], "statut_source_url")

    for champ in ("acteurs_associes", "liens", "mesures_complementaires", "sources_complementaires"):
        if champ in e and not isinstance(e[champ], list):
            err(f"« {champ} » doit être une liste")
    if isinstance(e.get("acteurs_associes"), list):
        for a in e["acteurs_associes"]:
            if not isinstance(a, str) or not a.strip():
                err("« acteurs_associes » ne doit contenir que des chaînes non vides")
        if len(set(map(str, e["acteurs_associes"]))) != len(e["acteurs_associes"]):
            err("« acteurs_associes » contient des doublons")
        if e.get("acteur") in e["acteurs_associes"]:
            err("l'acteur principal figure aussi dans « acteurs_associes »")
    if isinstance(e.get("liens"), list):
        for lien in e["liens"]:
            if not (isinstance(lien, str) and RE_ID.match(lien)):
                err(f"lien invalide : {lien!r}")
        if len(set(map(str, e["liens"]))) != len(e["liens"]):
            err("« liens » contient des doublons")
    if isinstance(e.get("mesures_complementaires"), list):
        for i, m in enumerate(e["mesures_complementaires"], 1):
            if not isinstance(m, dict):
                err(f"mesure complémentaire n° {i} : objet attendu")
                continue
            for c in r.requis_mesure - set(m):
                err(f"mesure complémentaire n° {i} : champ « {c} » manquant")
            for c in set(m) - r.champs_mesure:
                err(f"mesure complémentaire n° {i} : champ inconnu « {c} »")
            if "metrique" in m and m["metrique"] not in r.metriques:
                err(f"mesure complémentaire n° {i} : métrique hors vocabulaire {m['metrique']!r}")
            if "valeur" in m and not (nombre(m["valeur"]) or isinstance(m["valeur"], str)):
                err(f"mesure complémentaire n° {i} : « valeur » doit être un nombre ou une chaîne")
            if "comparateur" in m and m["comparateur"] not in r.comparateurs:
                err(f"mesure complémentaire n° {i} : comparateur hors vocabulaire {m['comparateur']!r}")
            if "unite" in m and m["unite"] is not None and not isinstance(m["unite"], str):
                err(f"mesure complémentaire n° {i} : « unite » doit être une chaîne ou null")
    if isinstance(e.get("sources_complementaires"), list):
        for i, s in enumerate(e["sources_complementaires"], 1):
            if not isinstance(s, dict) or set(s) != r.champs_source:
                err(f"source complémentaire n° {i} : objet {{url, titre}} attendu")
                continue
            url_ok(s["url"], f"sources_complementaires[{i}].url")
            if not isinstance(s["titre"], str) or not s["titre"].strip():
                err(f"source complémentaire n° {i} : titre vide")

    # Règles de statut : consigner sans trancher, mais tout changement de statut est sourcé.
    statut = e.get("statut")
    if statut in STATUTS_A_JUSTIFIER and not e.get("statut_source_url"):
        err(f"le statut « {statut} » exige « statut_source_url » (source tierce ou déclaration ultérieure de l'acteur)")
    if statut == "en_retard":
        if b_echeance is None:
            err("le statut « en_retard » exige une « echeance_promise »")
        else:
            reference = (b_statut or b_consultation or (aujourdhui, aujourdhui))[1]
            if b_echeance[1] >= reference:
                err("statut « en_retard » alors que l'échéance n'est pas dépassée à la date de la source de statut")
    if e.get("type") == "refutation" and isinstance(e.get("liens"), list) and not e["liens"]:
        err("une entrée de type « refutation » doit pointer vers l'affirmation contestée (« liens »)")
    if statut == "promis" and b_echeance and b_echeance[1] < aujourdhui:
        avert(f"échéance {e.get('echeance_promise')} dépassée avec le statut « promis » : à réexaminer sur source")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("fichier", nargs="?", default=str(ICI / "affirmations.jsonl"))
    ap.add_argument("--schema", default=str(ICI / "schema.json"))
    ap.add_argument("--aujourdhui", help="date de référence pour les avertissements (défaut : date du jour)")
    ap.add_argument("--strict", action="store_true", help="les avertissements font échouer la validation")
    args = ap.parse_args()

    aujourdhui = dt.date.fromisoformat(args.aujourdhui) if args.aujourdhui else dt.date.today()
    schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
    regles = Regles(schema)

    validateur = None
    try:
        import jsonschema  # facultatif

        validateur = jsonschema.Draft202012Validator(schema)
        try:
            from importlib.metadata import version

            version_js = " " + version("jsonschema")
        except Exception:
            version_js = ""
        mode = f"validation complète par jsonschema{version_js} en plus des contrôles internes"
    except ImportError:
        mode = "contrôles internes uniquement (jsonschema non installé)"

    erreurs, avertissements = [], []
    entrees = []  # (numéro de ligne, objet)
    lignes = Path(args.fichier).read_text(encoding="utf-8").split("\n")
    if lignes and lignes[-1] == "":
        lignes.pop()
    for n, ligne in enumerate(lignes, 1):
        if not ligne.strip():
            erreurs.append(f"ligne {n} : ligne vide")
            continue
        try:
            obj = json.loads(ligne)
        except json.JSONDecodeError as exc:
            erreurs.append(f"ligne {n} : JSON invalide ({exc.msg}, colonne {exc.colno})")
            continue
        if not isinstance(obj, dict):
            erreurs.append(f"ligne {n} : un objet JSON est attendu")
            continue
        ident = obj.get("id", "?")
        verifier_entree(
            obj, regles,
            lambda m, n=n, i=ident: erreurs.append(f"ligne {n} [{i}] : {m}"),
            lambda m, n=n, i=ident: avertissements.append(f"ligne {n} [{i}] : {m}"),
            aujourdhui,
        )
        if validateur is not None:
            for ve in sorted(validateur.iter_errors(obj), key=lambda x: list(x.path)):
                chemin = "/".join(str(p) for p in ve.path) or "(racine)"
                erreurs.append(f"ligne {n} [{ident}] : jsonschema, {chemin} : {ve.message}")
        entrees.append((n, obj))

    vus = {}
    for n, e in entrees:
        ident = e.get("id")
        if isinstance(ident, str):
            if ident in vus:
                erreurs.append(f"ligne {n} [{ident}] : identifiant déjà utilisé ligne {vus[ident]}")
            else:
                vus[ident] = n
    for n, e in entrees:
        for lien in e.get("liens", []) if isinstance(e.get("liens"), list) else []:
            if lien == e.get("id"):
                erreurs.append(f"ligne {n} [{lien}] : une entrée ne peut pas pointer vers elle-même")
            elif isinstance(lien, str) and lien not in vus:
                erreurs.append(f"ligne {n} [{e.get('id')}] : lien vers un identifiant inexistant « {lien} »")

    objets = [e for _, e in entrees]
    print(f"Fichier : {args.fichier}")
    print(f"Mode : {mode}")
    print(f"Entrées lues : {len(objets)}")

    def bloc(titre, compteur):
        print(f"\n{titre}")
        for cle, nb in sorted(compteur.items(), key=lambda kv: (-kv[1], str(kv[0]))):
            print(f"  {nb:4d}  {cle}")

    bloc("Par type :", Counter(e.get("type") for e in objets))
    bloc("Par statut :", Counter(e.get("statut") for e in objets))
    bloc("Par acteur :", Counter(e.get("acteur") for e in objets))
    bloc("Par type de source :", Counter(e.get("source_type") for e in objets))
    apt = sum(1 for e in objets if e.get("precision_date") == "au_plus_tard")
    print(f"\nDates « au plus tard » (source non datée) : {apt}")

    if avertissements:
        print(f"\nAvertissements ({len(avertissements)}) :")
        for a in avertissements:
            print(f"  - {a}")
    if erreurs:
        print(f"\nErreurs ({len(erreurs)}) :")
        for m in erreurs:
            print(f"  - {m}")
    echec = bool(erreurs) or (args.strict and bool(avertissements))
    print("\nRésultat : " + ("ÉCHEC" if echec else "OK") +
          f" ({len(erreurs)} erreur(s), {len(avertissements)} avertissement(s))")
    return 1 if echec else 0


if __name__ == "__main__":
    sys.exit(main())
