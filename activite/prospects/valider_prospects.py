#!/usr/bin/env python3
"""Valide prospects.jsonl, prospects_recherche.jsonl et prospects.csv contre activite/CONTRAT.md.

Contrôles bloquants (code de sortie 1 si au moins une erreur) :
  * JSON valide, une organisation par ligne, identifiants uniques entre les deux fichiers ;
  * champs obligatoires du contrat et types ;
  * vocabulaires : type_org, segment, programme, role ;
  * dates ISO AAAA-MM-JJ (ou null), pays ISO 3166-1 alpha-2 ;
  * cohérence : nb_projets = nombre de financements, total_obtenu_eur = somme des contributions,
    derniere_activite = date la plus tardive des financements ;
  * URLs de sources publiques en https (cordis.europa.eu, gtr.ukri.org) ; site_web null ou URL ;
  * répartition des fichiers : entreprises (PME, grande_entreprise) dans prospects.jsonl,
    universités / recherche / autre dans prospects_recherche.jsonl ;
  * aucune donnée personnelle : pas de clé de type e-mail, téléphone, personne, contact... et
    aucune adresse e-mail ni numéro de téléphone dans les valeurs ;
  * fenêtre temporelle : financements terminés le 2019-01-01 ou après (ou sans date de fin) ;
  * conversion de devise documentée dans `note` pour les montants GtR ;
  * champs optionnels nb_projets_total (entier >= nb_projets), part_quantique (0-1, 2 décimales,
    = nb_projets / nb_projets_total) et profil_consultant_ue (booléen), null acceptés ;
  * prospects.csv : en-tête attendu (12 colonnes, ou 15 avec les trois champs optionnels) et une
    ligne par entreprise.
Avertissements (non bloquants) : libellés ressemblant à un nom de personne, ville manquante, etc.

Usage : python3 -I valider_prospects.py [--dossier DOSSIER]
"""
import argparse
import csv
import datetime
import json
import os
import re
import sys

TYPES = {"PME", "grande_entreprise", "universite", "recherche", "autre"}
TYPES_ENTREPRISE = {"PME", "grande_entreprise"}
SEGMENTS = {"calcul", "capteurs", "communication", "composants", "logiciel", "pqc", "transverse", "inconnu"}
PROGRAMMES = {"Horizon Europe", "H2020", "EIC", "Digital Europe", "EuroHPC", "Chips JU", "UKRI", "Innovate UK", "autre"}
ROLES = {"coordinateur", "participant", "beneficiaire_unique"}
REQUIS = ["id", "nom", "pays", "ville", "site_web", "type_org", "segment", "segment_justification",
          "financements_obtenus", "total_obtenu_eur", "nb_projets", "derniere_activite", "sources", "date_extraction"]
REQUIS_FIN = ["programme", "projet", "acronyme", "id_projet", "debut", "fin", "contribution_eur", "role", "source_url"]
DOMAINES_SOURCES = ("https://cordis.europa.eu/", "https://gtr.ukri.org/")
CSV_ENTETE = ["nom", "pays", "ville", "type_org", "segment", "nb_projets", "total_obtenu_eur", "derniere_activite",
              "a_coordonne", "programmes", "site_web", "lien_source_principal"]
CSV_ENTETE_ETENDU = CSV_ENTETE + ["nb_projets_total", "part_quantique", "profil_consultant_ue"]
DEBUT_FENETRE = "2019-01-01"

# ISO 3166-1 alpha-2 (249 codes officiellement attribués) + XK (Kosovo, code utilisateur employé par la CE).
ISO = set("""AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ BL BM BN BO BQ BR BS BT BV BW
BY BZ CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ DK DM DO DZ EC EE EG EH ER ES ET FI FJ FK FM FO
FR GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO
JP KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS
MT MU MV MW MX MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS RU
RW SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TL TM TN TO TR TT TV TW TZ UA
UG UM US UY UZ VA VC VE VG VI VN VU WF WS YE YT ZA ZM ZW XK""".split())

CLES_PERSONNELLES = re.compile(
    r"(^|_)(e_?mail|mail|courriel|telephone|t[ée]l[ée]phone|phone|tel|fax|mobile|portable|contact|contacts|"
    r"personne|personnes|person|persons|people|prenom|pr[ée]nom|firstname|first_name|lastname|last_name|surname|"
    r"nom_contact|investigat\w*|pi|chercheur|responsable|signataire|linkedin)($|_)", re.I)
RX_EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
RX_UUID = re.compile(r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}")
RX_TEL = re.compile(r"(\+\d{1,3}[\s.-]?)?(\(?\d{2,4}\)?[\s.-]?){3,}\d{2,4}")
RX_TEL_STRICT = re.compile(r"(\+\d{2,3}|\b0\d)[\s.-]?\d{1,4}([\s.-]\d{2,4}){2,4}\b")
RX_ORG = re.compile(r"\b(LTD|LIMITED|PLC|LLP|LLC|INC|GMBH|MBH|AG|SE|SAS|SASU|SARL|SA|SL|SLU|SRL|SPA|BV|NV|AB|OY|OYJ|AS|ASA|APS|"
                    r"KG|UG|SRO|KFT|ZRT|DOO|AE|IKE|UAB|SIA|LDA|CORP|CO|COMPANY|TECHNOLOG\w*|QUANTUM|SYSTEMS?|SOLUTIONS?|"
                    r"UNIVERSIT\w*|INSTITUT\w*|INSTITUTE|CENTRE|CENTER|LAB\w*|FOUNDATION|FUNDACI\w*|FONDAZIONE|STIFTUNG|"
                    r"ASSOCIA\w*|SOCIET\w*|SOCIEDAD|AGENCY|COUNCIL|GROUP|GRUPPO|CONSORZIO|CONSORTIUM|NETWORK|PHOTONICS|"
                    r"PARTNERS|CONSULT\w*|RESEARCH|INNOVATION|SCIENCES?|ENGINEERING|SERVICES|EUROPE|INTERNATIONAL|"
                    r"HOLDING|INDUSTR\w*|ELECTRONIC\w*|SEMICONDUCTOR\w*|DEVICES|SOFTWARE|NETWORKS|LIMITADA|AKTIENGESELLSCHAFT|"
                    r"FRANCE|ITALIA|ITALY|DEUTSCHLAND|ESPANA|IBERICA|NEDERLAND|BELGIUM|SUISSE|UK|ENERGY|ENERGIE|OPTICS|"
                    r"DIAMOND|WAVES?|FIRM|PROJECT|PLATFORM\w*|BUNDESANSTALT|KORKEAKOULU\w*|UNIWERSYTET|SAATIO|"
                    r"PHARMA\w*|DEVELOPPEMENT|DEVELOPMENT|CIRCUITS|BRIDGE|BV|SPA|SRL|SPZOO|ZOO|"
                    r"[A-Z]*TECH|[A-Z]*SOFT|[A-Z]*SYS|[A-Z]*LABS?|[0-9]+)\b")


def ressemble_personne(nom):
    """Heuristique d'alerte : 2-3 mots alphabétiques sans aucun marqueur d'organisation
    (forme sociale, mot d'organisation, sigle, chiffre). Ne bloque pas : liste à revoir à la main."""
    u = re.sub(r"\b([A-Za-z])\.(?=[A-Za-z]\.?)", r"\1", nom)  # B.V. -> BV., S.R.L. -> SRL.
    u = re.sub(r"[^A-Za-z0-9À-ÿ' -]", " ", u).upper()
    mots = u.split()
    if len(mots) not in (2, 3) or RX_ORG.search(u):
        return False
    if any(len(w) <= 3 for w in mots):  # sigles (SA, OU, DD, PC...)
        return False
    return all(re.fullmatch(r"[A-ZÀ-Ý][A-ZÀ-Ý'-]+", w) for w in mots)


def iso_date(s):
    if s is None:
        return True
    if not isinstance(s, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        return False
    try:
        datetime.date.fromisoformat(s)
        return True
    except ValueError:
        return False


def scan_personnel(obj, chemin, erreurs):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if CLES_PERSONNELLES.search(k):
                erreurs.append("%s : clé interdite (donnée personnelle potentielle) « %s »" % (chemin, k))
            scan_personnel(v, chemin + "." + k, erreurs)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            scan_personnel(v, "%s[%d]" % (chemin, i), erreurs)
    elif isinstance(obj, str):
        if RX_EMAIL.search(obj):
            erreurs.append("%s : adresse e-mail détectée" % chemin)
        if "/persons/" in obj or "contact-form" in obj:
            erreurs.append("%s : lien vers une personne / formulaire de contact" % chemin)
        obj = RX_UUID.sub(" ", obj)  # identifiants GtR (UUID) : pas des numéros de téléphone
        if not obj.startswith("http") and RX_TEL_STRICT.search(obj) and not re.search(r"\d{4}-\d{2}-\d{2}", obj):
            m = RX_TEL_STRICT.search(obj).group(0)
            if len(re.sub(r"\D", "", m)) >= 9 and not re.search(r"(PIC|GtR|EUR|GBP|%|\d+[.,]\d+)", obj[max(0, obj.find(m) - 12):obj.find(m) + len(m) + 6]):
                erreurs.append("%s : numéro de téléphone possible « %s »" % (chemin, m))


def valider_ligne(r, n, fichier, erreurs, avert):
    ou = "%s:%d" % (fichier, n)
    for k in REQUIS:
        if k not in r:
            erreurs.append("%s : champ obligatoire manquant « %s »" % (ou, k))
    if erreurs and any(e.startswith(ou) for e in erreurs[-len(REQUIS):]):
        if not all(k in r for k in ("id", "financements_obtenus")):
            return
    if not isinstance(r.get("id"), str) or not re.fullmatch(r"(cordis|gtr)-[A-Za-z0-9-]+", r.get("id") or ""):
        erreurs.append("%s : id invalide %r" % (ou, r.get("id")))
    if not isinstance(r.get("nom"), str) or not r["nom"].strip():
        erreurs.append("%s : nom vide" % ou)
    elif r.get("type_org") in TYPES_ENTREPRISE and ressemble_personne(r["nom"]):
        avert.append("%s : le libellé « %s » pourrait être un nom de personne (à vérifier)" % (ou, r["nom"]))
    if r.get("pays") is not None and r.get("pays") not in ISO:
        erreurs.append("%s : pays non ISO 3166-1 alpha-2 %r" % (ou, r.get("pays")))
    if r.get("pays") is None:
        avert.append("%s : pays inconnu (null) pour « %s »" % (ou, r.get("nom")))
    if r.get("ville") is not None and not isinstance(r["ville"], str):
        erreurs.append("%s : ville doit être une chaîne ou null" % ou)
    sw = r.get("site_web")
    if sw is not None and (not isinstance(sw, str) or not re.match(r"^https?://[^\s/]+\.[^\s]+", sw)):
        erreurs.append("%s : site_web invalide %r" % (ou, sw))
    if r.get("type_org") not in TYPES:
        erreurs.append("%s : type_org hors vocabulaire %r" % (ou, r.get("type_org")))
    if r.get("segment") not in SEGMENTS:
        erreurs.append("%s : segment hors vocabulaire %r" % (ou, r.get("segment")))
    if not isinstance(r.get("segment_justification"), str) or not r["segment_justification"].strip():
        erreurs.append("%s : segment_justification vide" % ou)
    for k in ("derniere_activite", "date_extraction"):
        if not iso_date(r.get(k)):
            erreurs.append("%s : date non ISO dans %s : %r" % (ou, k, r.get(k)))
    if r.get("date_extraction") is None:
        erreurs.append("%s : date_extraction obligatoire" % ou)
    fins = r.get("financements_obtenus")
    if not isinstance(fins, list) or not fins:
        erreurs.append("%s : financements_obtenus doit être une liste non vide" % ou)
        fins = []
    total = 0.0
    dates = []
    gtr = False
    for i, f in enumerate(fins):
        of = "%s financements[%d]" % (ou, i)
        for k in REQUIS_FIN:
            if k not in f:
                erreurs.append("%s : champ manquant « %s »" % (of, k))
        if f.get("programme") not in PROGRAMMES:
            erreurs.append("%s : programme hors vocabulaire %r" % (of, f.get("programme")))
        if f.get("role") not in ROLES:
            erreurs.append("%s : role hors vocabulaire %r" % (of, f.get("role")))
        for k in ("debut", "fin"):
            if not iso_date(f.get(k)):
                erreurs.append("%s : date non ISO %s=%r" % (of, k, f.get(k)))
        if f.get("fin") and iso_date(f.get("fin")) and f["fin"] < DEBUT_FENETRE:
            erreurs.append("%s : projet terminé avant %s (%s)" % (of, DEBUT_FENETRE, f["fin"]))
        c = f.get("contribution_eur")
        if not isinstance(c, (int, float)) or isinstance(c, bool) or c < 0:
            erreurs.append("%s : contribution_eur invalide %r" % (of, c))
        else:
            total += c
        if not isinstance(f.get("projet"), str) or not f["projet"].strip():
            erreurs.append("%s : titre de projet vide" % of)
        if not isinstance(f.get("id_projet"), str) or not f["id_projet"]:
            erreurs.append("%s : id_projet vide" % of)
        if f.get("acronyme") is not None and not isinstance(f["acronyme"], str):
            erreurs.append("%s : acronyme doit être une chaîne ou null" % of)
        su = f.get("source_url")
        if not isinstance(su, str) or not su.startswith(DOMAINES_SOURCES):
            erreurs.append("%s : source_url non publique/inattendue %r" % (of, su))
        if isinstance(su, str) and su.startswith("https://gtr.ukri.org/"):
            gtr = True
        for k in ("fin", "debut"):
            if f.get(k) and iso_date(f[k]):
                dates.append(f[k]); break
    if isinstance(r.get("nb_projets"), bool) or not isinstance(r.get("nb_projets"), int) or r.get("nb_projets") != len(fins):
        erreurs.append("%s : nb_projets (%r) != nombre de financements (%d)" % (ou, r.get("nb_projets"), len(fins)))
    t = r.get("total_obtenu_eur")
    if not isinstance(t, (int, float)) or abs(t - total) > 0.05 + 1e-9 * abs(total):
        erreurs.append("%s : total_obtenu_eur (%r) != somme des contributions (%.2f)" % (ou, t, total))
    if dates and r.get("derniere_activite") != max(dates):
        erreurs.append("%s : derniere_activite (%r) != max des dates (%s)" % (ou, r.get("derniere_activite"), max(dates)))
    srcs = r.get("sources")
    if not isinstance(srcs, list) or not srcs:
        erreurs.append("%s : sources doit contenir au moins une URL" % ou)
    else:
        for s in srcs:
            if not isinstance(s, str) or not s.startswith(DOMAINES_SOURCES):
                erreurs.append("%s : source non publique/inattendue %r" % (ou, s))
        manquantes = set(f.get("source_url") for f in fins) - set(srcs)
        if manquantes:
            erreurs.append("%s : source_url absentes de sources : %s" % (ou, sorted(manquantes)[:3]))
    if gtr and not re.search(r"GBP.*EUR|EUR.*GBP", r.get("note") or ""):
        erreurs.append("%s : montant GtR sans taux de conversion GBP->EUR dans note" % ou)
    # Champs optionnels : nb_projets_total, part_quantique, profil_consultant_ue.
    nbt = r.get("nb_projets_total")
    if nbt is not None:
        if isinstance(nbt, bool) or not isinstance(nbt, int) or nbt < 1:
            erreurs.append("%s : nb_projets_total invalide %r" % (ou, nbt))
        elif isinstance(r.get("nb_projets"), int) and nbt < r["nb_projets"]:
            erreurs.append("%s : nb_projets_total (%d) < nb_projets (%d)" % (ou, nbt, r["nb_projets"]))
    pq = r.get("part_quantique")
    if pq is not None:
        if isinstance(pq, bool) or not isinstance(pq, (int, float)) or not 0 <= pq <= 1 or round(pq, 2) != pq:
            erreurs.append("%s : part_quantique doit être un nombre entre 0 et 1 à 2 décimales ou null : %r" % (ou, pq))
        elif isinstance(nbt, int) and nbt > 0 and isinstance(r.get("nb_projets"), int) \
                and abs(pq - round(r["nb_projets"] / nbt, 2)) > 0.005:
            erreurs.append("%s : part_quantique (%r) != nb_projets / nb_projets_total" % (ou, pq))
        elif nbt is None:
            erreurs.append("%s : part_quantique renseignée sans nb_projets_total" % ou)
    if r.get("profil_consultant_ue") is not None and not isinstance(r["profil_consultant_ue"], bool):
        erreurs.append("%s : profil_consultant_ue doit être un booléen ou null" % ou)
    if "a_coordonne" in r and not isinstance(r["a_coordonne"], bool):
        erreurs.append("%s : a_coordonne doit être un booléen" % ou)
    if r.get("ville") is None:
        avert.append("%s : ville inconnue pour « %s »" % (ou, r.get("nom")))
    scan_personnel(r, ou, erreurs)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dossier", default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--max-messages", type=int, default=40)
    a = ap.parse_args()
    erreurs, avert = [], []
    ids = {}
    noms_entreprises = []
    comptes = {}
    for fichier, attendus in (("prospects.jsonl", TYPES_ENTREPRISE), ("prospects_recherche.jsonl", TYPES - TYPES_ENTREPRISE)):
        chemin = os.path.join(a.dossier, fichier)
        if not os.path.exists(chemin):
            erreurs.append("%s : fichier absent" % fichier)
            continue
        n = 0
        with open(chemin, encoding="utf-8") as f:
            for n, ligne in enumerate(f, 1):
                if not ligne.strip():
                    erreurs.append("%s:%d : ligne vide" % (fichier, n)); continue
                try:
                    r = json.loads(ligne)
                except ValueError as e:
                    erreurs.append("%s:%d : JSON invalide (%s)" % (fichier, n, e)); continue
                if not isinstance(r, dict):
                    erreurs.append("%s:%d : la ligne n'est pas un objet JSON" % (fichier, n)); continue
                valider_ligne(r, n, fichier, erreurs, avert)
                if r.get("type_org") in TYPES and r.get("type_org") not in attendus:
                    erreurs.append("%s:%d : type_org %s ne doit pas figurer dans ce fichier" % (fichier, n, r["type_org"]))
                if r.get("id") in ids:
                    erreurs.append("%s:%d : id dupliqué %s (déjà dans %s)" % (fichier, n, r.get("id"), ids[r["id"]]))
                ids[r.get("id")] = "%s:%d" % (fichier, n)
                if fichier == "prospects.jsonl":
                    noms_entreprises.append(r.get("nom"))
        comptes[fichier] = n
    chemin_csv = os.path.join(a.dossier, "prospects.csv")
    if os.path.exists(chemin_csv):
        with open(chemin_csv, encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))
        entete = rows[0] if rows else None
        if entete not in (CSV_ENTETE, CSV_ENTETE_ETENDU):
            erreurs.append("prospects.csv : en-tête inattendu %r" % entete)
        elif len(rows) - 1 != len(noms_entreprises):
            erreurs.append("prospects.csv : %d lignes pour %d entreprises" % (len(rows) - 1, len(noms_entreprises)))
        else:
            for i, (row, nom) in enumerate(zip(rows[1:], noms_entreprises), 2):
                if len(row) != len(entete):
                    erreurs.append("prospects.csv:%d : %d colonnes" % (i, len(row)))
                    continue
                if entete == CSV_ENTETE_ETENDU:
                    if row[14] not in ("oui", "non"):
                        erreurs.append("prospects.csv:%d : profil_consultant_ue doit valoir oui/non" % i)
                    if row[13] and not re.fullmatch(r"(0\.\d{2}|1\.00)", row[13]):
                        erreurs.append("prospects.csv:%d : part_quantique invalide %r" % (i, row[13]))
                    if row[12] and not row[12].isdigit():
                        erreurs.append("prospects.csv:%d : nb_projets_total invalide %r" % (i, row[12]))
                if row[0] != nom:
                    erreurs.append("prospects.csv:%d : ordre/nom différent du JSONL (%r vs %r)" % (i, row[0], nom))
                elif row[8] not in ("oui", "non"):
                    erreurs.append("prospects.csv:%d : a_coordonne doit valoir oui/non" % i)
                for cell in row:
                    if RX_EMAIL.search(cell):
                        erreurs.append("prospects.csv:%d : adresse e-mail détectée" % i)
    else:
        erreurs.append("prospects.csv : fichier absent")
    print("Lignes : %s" % ", ".join("%s=%d" % kv for kv in comptes.items()))
    print("Erreurs : %d ; avertissements : %d" % (len(erreurs), len(avert)))
    for e in erreurs[:a.max_messages]:
        print("ERREUR  " + e)
    resume_av = {}
    for w in avert:
        cle = re.sub(r"^[^:]+:\d+ : ", "", w)
        cle = re.sub(r"« .* »", "«…»", cle)
        resume_av[cle] = resume_av.get(cle, 0) + 1
    for k, v in sorted(resume_av.items(), key=lambda x: -x[1]):
        print("AVERT.  %5d × %s" % (v, k))
    for w in [w for w in avert if "personne" in w][:a.max_messages]:
        print("        " + w)
    sys.exit(1 if erreurs else 0)


if __name__ == "__main__":
    main()
