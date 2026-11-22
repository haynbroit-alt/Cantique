#!/usr/bin/env python3
"""Contrôle opportunites.jsonl (et saisies_manuelles.jsonl) contre activite/CONTRAT.md.

Vérifications :
  * structure : JSON valide, champs exacts du contrat (ni manquants ni en trop), types ;
  * vocabulaires : nature, statut, confiance, segments, types d'organisation ;
  * pays : codes ISO alpha-2 (ou XK) ou groupes définis dans groupes_pays.json (avec _sources) ;
  * dates : format AAAA-MM-JJ, ouverture <= clôture, date de vérification renseignée ;
  * cohérence temporelle relative à --aujourdhui : un statut « ouvert » ou « a_venir » ne peut
    pas avoir une clôture passée, « clos » doit avoir une clôture passée, « a_venir » ne doit
    pas avoir une ouverture passée (avertissement) ;
  * URL : `url` et `source_url` présentes et en http(s) ;
  * confiance « faible » accompagnée d'une note explicative ; identifiants uniques ;
  * montants entiers positifs, montant par projet <= budget total (avertissement).

Usage : python3 valider_opportunites.py [--aujourdhui 2026-11-22] [--fichier opportunites.jsonl]
Code de sortie 1 en cas d'erreur (les avertissements n'échouent pas, sauf --strict).
"""
import argparse
import datetime as dt
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
CHAMPS = ["id", "financeur", "programme", "intitule", "identifiant_appel", "nature", "url", "statut",
          "ouverture", "cloture", "budget_total_eur", "montant_par_projet_eur", "pays_eligibles",
          "types_eligibles", "consortium_requis", "taille_min_consortium", "segments", "trl",
          "taux_financement", "mots_cles", "note", "source_url", "confiance", "date_verification"]
NATURES = {"subvention", "marche_public", "pret", "fonds_propres", "prix", "autre"}
STATUTS = {"ouvert", "a_venir", "clos"}
CONFIANCES = {"elevee", "moyenne", "faible"}
SEGMENTS = {"calcul", "capteurs", "communication", "composants", "logiciel", "pqc", "transverse", "inconnu"}
TYPES = {"PME", "grande_entreprise", "universite", "recherche", "autre"}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PAYS = re.compile(r"^[A-Z]{2}$")
OBLIGATOIRES_NON_VIDES = ["id", "financeur", "programme", "intitule", "nature", "url", "statut", "source_url",
                          "confiance", "date_verification"]


def date_ok(v):
    if v is None:
        return True
    if not isinstance(v, str) or not DATE.match(v):
        return False
    try:
        dt.date.fromisoformat(v)
        return True
    except ValueError:
        return False


def charger_groupes(chemin):
    with open(chemin, encoding="utf-8") as f:
        g = json.load(f)
    erreurs = []
    sources = g.get("_sources", {})
    for nom, pays in g.items():
        if nom.startswith("_"):
            continue
        if not isinstance(pays, list) or not all(isinstance(p, str) and PAYS.match(p) for p in pays):
            erreurs.append(f"groupes_pays.json : groupe {nom} mal formé")
        s = sources.get(nom)
        if not s or not s.get("url") or not s.get("date_verification"):
            erreurs.append(f"groupes_pays.json : groupe {nom} sans _sources (url + date_verification)")
    return {k for k in g if not k.startswith("_")}, erreurs


def valider(chemin, aujourdhui, groupes, strict=False):
    erreurs, avert = [], []
    ids = set()
    n = 0
    with open(chemin, encoding="utf-8") as f:
        lignes = f.readlines()
    for i, ligne in enumerate(lignes, 1):
        ligne = ligne.strip()
        if not ligne or ligne.startswith("//"):
            continue
        n += 1
        ou = f"{os.path.basename(chemin)}:{i}"
        try:
            r = json.loads(ligne)
        except ValueError as e:
            erreurs.append(f"{ou} JSON invalide : {e}")
            continue
        rid = r.get("id", "?")
        ou += f" [{rid}]"
        manquants = [c for c in CHAMPS if c not in r]
        en_trop = [c for c in r if c not in CHAMPS]
        if manquants:
            erreurs.append(f"{ou} champs manquants : {manquants}")
        if en_trop:
            erreurs.append(f"{ou} champs hors contrat : {en_trop}")
        for c in OBLIGATOIRES_NON_VIDES:
            if not r.get(c):
                erreurs.append(f"{ou} champ obligatoire vide : {c}")
        if rid in ids:
            erreurs.append(f"{ou} id en double")
        ids.add(rid)
        if r.get("id") and not re.match(r"^[a-z0-9][a-z0-9._-]*$", r["id"]):
            erreurs.append(f"{ou} id non normalisé (minuscules, chiffres, . _ -)")
        if r.get("nature") not in NATURES:
            erreurs.append(f"{ou} nature inconnue : {r.get('nature')}")
        if r.get("statut") not in STATUTS:
            erreurs.append(f"{ou} statut inconnu : {r.get('statut')}")
        if r.get("confiance") not in CONFIANCES:
            erreurs.append(f"{ou} confiance inconnue : {r.get('confiance')}")
        for c in ("url", "source_url"):
            v = r.get(c)
            if v and not re.match(r"^https?://\S+$", str(v)):
                erreurs.append(f"{ou} {c} invalide : {v}")
        for c in ("ouverture", "cloture", "date_verification"):
            if not date_ok(r.get(c)):
                erreurs.append(f"{ou} date invalide {c} : {r.get(c)}")
        o, cl = r.get("ouverture"), r.get("cloture")
        if date_ok(o) and date_ok(cl) and o and cl and o > cl:
            erreurs.append(f"{ou} ouverture {o} postérieure à la clôture {cl}")
        if date_ok(r.get("date_verification")) and r.get("date_verification") and r["date_verification"] > aujourdhui:
            erreurs.append(f"{ou} date_verification dans le futur")
        st = r.get("statut")
        if date_ok(cl) and cl:
            if st in ("ouvert", "a_venir") and cl < aujourdhui:
                erreurs.append(f"{ou} statut {st} mais clôture passée ({cl} < {aujourdhui})")
            if st == "clos" and cl >= aujourdhui:
                erreurs.append(f"{ou} statut clos mais clôture future ({cl})")
        if st == "clos" and not cl:
            avert.append(f"{ou} statut clos sans date de clôture")
        if st == "a_venir" and date_ok(o) and o and o <= aujourdhui:
            avert.append(f"{ou} statut a_venir mais ouverture passée ({o})")
        if st == "ouvert" and date_ok(o) and o and o > aujourdhui:
            erreurs.append(f"{ou} statut ouvert mais ouverture future ({o})")
        if cl and date_ok(cl) and cl > "2028-12-31":
            avert.append(f"{ou} clôture hors fenêtre du calendrier ({cl})")
        for c in ("budget_total_eur", "montant_par_projet_eur", "taille_min_consortium"):
            v = r.get(c)
            if v is not None and (not isinstance(v, int) or isinstance(v, bool) or v < 0):
                erreurs.append(f"{ou} {c} doit être un entier positif ou null : {v!r}")
        b, m = r.get("budget_total_eur"), r.get("montant_par_projet_eur")
        if isinstance(b, int) and isinstance(m, int) and m > b:
            avert.append(f"{ou} montant par projet ({m}) supérieur au budget total ({b})")
        pays = r.get("pays_eligibles")
        if not isinstance(pays, list) or not pays:
            erreurs.append(f"{ou} pays_eligibles vide ou non liste")
        else:
            for p in pays:
                if not (p in groupes or (isinstance(p, str) and PAYS.match(p))):
                    erreurs.append(f"{ou} pays ou groupe inconnu : {p}")
        types = r.get("types_eligibles")
        if not isinstance(types, list) or not types or any(t not in TYPES for t in types):
            erreurs.append(f"{ou} types_eligibles invalides : {types}")
        segs = r.get("segments")
        if not isinstance(segs, list) or not segs or any(s not in SEGMENTS for s in segs):
            erreurs.append(f"{ou} segments invalides : {segs}")
        if r.get("consortium_requis") not in (True, False, None):
            erreurs.append(f"{ou} consortium_requis doit être booléen ou null")
        if r.get("consortium_requis") is False and isinstance(r.get("taille_min_consortium"), int) and r["taille_min_consortium"] > 1:
            avert.append(f"{ou} consortium non requis mais taille minimale > 1")
        if not isinstance(r.get("mots_cles"), list):
            erreurs.append(f"{ou} mots_cles doit être une liste")
        for c in ("identifiant_appel", "trl", "taux_financement", "note"):
            if r.get(c) is not None and not isinstance(r.get(c), str):
                erreurs.append(f"{ou} {c} doit être une chaîne ou null")
        if r.get("confiance") == "faible" and len(str(r.get("note") or "")) < 40:
            erreurs.append(f"{ou} confiance faible sans note explicative")
        if r.get("pays_eligibles") == ["US"] and "AMÉRICAIN" not in str(r.get("note", "")).upper():
            avert.append(f"{ou} opportunité américaine sans mention explicite de l'éligibilité réservée aux entreprises américaines")
        if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", ligne):
            avert.append(f"{ou} adresse électronique détectée : vérifier l'absence de données personnelles")
    return n, erreurs, avert


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--aujourdhui", default=dt.date.today().isoformat())
    ap.add_argument("--fichier", action="append", help="fichier(s) à valider (par défaut opportunites.jsonl et saisies_manuelles.jsonl)")
    ap.add_argument("--groupes", default=os.path.join(ICI, "groupes_pays.json"))
    ap.add_argument("--strict", action="store_true", help="les avertissements font aussi échouer")
    a = ap.parse_args()
    if not date_ok(a.aujourdhui):
        sys.exit("--aujourdhui doit être au format AAAA-MM-JJ")
    groupes, err_g = charger_groupes(a.groupes)
    fichiers = a.fichier or [os.path.join(ICI, "opportunites.jsonl"), os.path.join(ICI, "saisies_manuelles.jsonl")]
    total_err = list(err_g)
    total_av = []
    for f in fichiers:
        if not os.path.exists(f):
            total_err.append(f"fichier absent : {f}")
            continue
        # les saisies manuelles portent un statut indicatif, recalculé par le script de construction
        n, e, w = valider(f, a.aujourdhui, groupes)
        if os.path.basename(f) == "saisies_manuelles.jsonl":
            w += [x for x in e if "statut" in x]
            e = [x for x in e if "statut" not in x]
        print(f"{os.path.basename(f)} : {n} enregistrements, {len(e)} erreur(s), {len(w)} avertissement(s)")
        total_err += e
        total_av += w
    for x in total_err:
        print("ERREUR  ", x)
    for x in total_av:
        print("AVERTIS.", x)
    if total_err or (a.strict and total_av):
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
