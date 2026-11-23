#!/usr/bin/env python3
"""Construit le calendrier des opportunités de financement et de marchés publics
pour les entreprises du quantique (format défini dans activite/CONTRAT.md).

Parties automatisées (récupération et analyse reproductibles) :
  * Portail Funding & Tenders de la Commission (API de recherche SEDIA, POST multipart) :
    topics ouverts / à venir, et topics clos depuis --clos-depuis, filtrés sur des termes
    quantiques dans le titre, la description et les mots-clés ;
  * TED (marchés publics de l'UE, API v3 anonyme) : avis de marché et consultations
    préalables mentionnant le quantique ;
  * SBIR.gov (copie des sujets SBIR/STTR américains ouverts contenant « quantum ») ;
  * Find a Tender (Royaume-Uni, flux OCDS) et Contracts Finder (Royaume-Uni, API de recherche) ;
  * taux de change de référence de la BCE pour convertir les montants en euros.

Partie manuelle : saisies_manuelles.jsonl (une ligne JSON par opportunité, même format
que la sortie). Une saisie manuelle portant le même « id » qu'un enregistrement généré
le remplace.

Sorties (dans le dossier du script) :
  * opportunites.jsonl : une ligne par opportunité, triée par date de clôture ;
  * candidats_sedia.tsv : tous les topics SEDIA examinés, avec leur score de pertinence
    et la décision (retenu / écarté), pour relecture humaine ;
  * CALENDRIER.md : calendrier en français (tableau chronologique, rythme, lacunes).

Usage :
  python3 construire_opportunites.py --aujourdhui 2026-11-22
  python3 construire_opportunites.py --hors-ligne        # relit les réponses mises en cache
Options utiles : --cache DOSSIER, --sans-ted, --sans-sbir, --sans-uk, --jours-fts 60.
Dépendances : requests, beautifulsoup4 (et lxml).
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import tempfile
import time
from collections import Counter, defaultdict

import requests
from bs4 import BeautifulSoup

ICI = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
SEDIA_URL = "https://api.tech.ec.europa.eu/search-api/prod/rest/search"
TOPIC_URL = "https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/{}"
SEDIA_SOURCE = "https://api.tech.ec.europa.eu/search-api/prod/rest/search?apiKey=SEDIA&text=***"
TED_URL = "https://api.ted.europa.eu/v3/notices/search"
SBIR_SEARCH = "https://www.sbir.gov/topics?keywords=quantum&status=Open&page={}"
FTS_URL = "https://www.find-tender.service.gov.uk/api/1.0/ocdsReleasePackages"
CF_URL = "https://www.contractsfinder.service.gov.uk/api/rest/2/search_notices/json"
ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"

CHAMPS = ["id", "financeur", "programme", "intitule", "identifiant_appel", "nature", "url", "statut",
          "ouverture", "cloture", "budget_total_eur", "montant_par_projet_eur", "pays_eligibles",
          "types_eligibles", "consortium_requis", "taille_min_consortium", "segments", "trl",
          "taux_financement", "mots_cles", "note", "source_url", "confiance", "date_verification"]

# ----------------------------------------------------------------------------- pertinence
# Termes « forts » : un seul suffit à rendre un texte pertinent s'il est dans le titre.
FORT = re.compile(r"quantum|quantique|quanten|qubit|\bQKD\b|\bPQC\b|post-quantum|quantum-safe|entanglement|"
                  r"trapped[- ]ion|neutral[- ]atom|cold[- ]atom|rydberg|\bNV[- ]cent|atom interferom|"
                  r"spin qubit|dilution refrigerator|cu[aá]ntic|quantistic|kwantow|kwantum|kvant|EuroQCI", re.I)
PQC = re.compile(r"post-quantum|\bPQC\b|quantum-safe|quantum[- ]resistant|quantum threat", re.I)
# Mentions qui ne signalent pas un contenu quantique (renvois à des initiatives, marques).
BRUIT = re.compile(r"Quantum Flagship|Quantum Europe Strategy|Quantum Blue|Quantum Scalar|StorNext", re.I)
SEGMENTS = [
    ("pqc", re.compile(r"post-quantum|\bPQC\b|quantum-safe|quantum[- ]resistant|cryptanaly|gitterbasiert", re.I)),
    ("communication", re.compile(r"\bQKD\b|quantum key|quantum communication|quantum network|quantum internet|repeater|"
                                 r"EuroQCI|\bQCI\b|comunica[tț]ie cuantic|chiavi quantistiche|quantum random number|QRNG", re.I)),
    ("capteurs", re.compile(r"sensing|sensor|gravimet|metrolog|inertial navigation|magnetomet|atom interferom|"
                            r"atomic clock|rydberg|capteur", re.I)),
    ("composants", re.compile(r"cryogen|cryo-|dilution|laser|photonic integrated|control electronics|readout|packaging|"
                              r"pilot line|frequency comb|peine de frecuencias|wafer|single[- ]photon detector|SNSPD|optical ground station|criogenic", re.I)),
    ("logiciel", re.compile(r"algorithm|software|machine learning|compiler|benchmark|simulation tool|orchestration", re.I)),
    ("calcul", re.compile(r"quantum comput|qubit|QPU|trapped[- ]ion|neutral[- ]atom|superconducting|quantum processor|"
                          r"error correct|obliczeń kwantowych|quantum machine learning|fault[- ]tolerant", re.I)),
]
# Topics SEDIA génériques (sans thème quantique) retenus car explicitement ouverts au quantique.
SEDIA_GENERIQUES = {
    "HORIZON-EIC-2027-PATHFINDEROPEN-two-stage": "Appel blanc EIC Pathfinder Open : tous domaines, dont le quantique.",
    "HORIZON-EIC-2027-DEFENCE-01": "EIC STEP Scale Up Defence : fonds propres pour technologies critiques de défense, pertinent pour capteurs/communications quantiques à double usage.",
}
# Topics SEDIA saisis manuellement par date limite (exclus de la génération automatique).
SEDIA_EXCLUS = {"HORIZON-EIC-2027-ACCELERATOR-01", "HORIZON-EIC-2027-STEP", "HORIZON-EIC-2026-ACCELERATOR-01"}
# Sollicitations SBIR saisies manuellement (NSF : une ligne par date limite).
SBIR_SOLLICITATIONS_MANUELLES = {"NSF 26-510"}

NOMS_PAYS = {
    "albania": "AL", "armenia": "AM", "austria": "AT", "belgium": "BE", "bosnia-herzegovina": "BA",
    "bosnia and herzegovina": "BA", "bulgaria": "BG", "croatia": "HR", "cyprus": "CY", "czechia": "CZ",
    "denmark": "DK", "estonia": "EE", "faroe islands": "FO", "finland": "FI", "france": "FR", "germany": "DE",
    "georgia": "GE", "greece": "GR", "hungary": "HU", "iceland": "IS", "ireland": "IE", "israel": "IL",
    "italy": "IT", "kosovo": "XK", "latvia": "LV", "lithuania": "LT", "luxembourg": "LU", "malta": "MT",
    "moldova": "MD", "montenegro": "ME", "netherlands": "NL", "north macedonia": "MK", "norway": "NO",
    "poland": "PL", "portugal": "PT", "romania": "RO", "serbia": "RS", "slovakia": "SK", "slovenia": "SI",
    "spain": "ES", "sweden": "SE", "switzerland": "CH", "türkiye": "TR", "turkey": "TR",
    "united kingdom": "GB", "ukraine": "UA", "canada": "CA", "japan": "JP", "new zealand": "NZ",
    "republic of korea": "KR", "tunisia": "TN", "egypt": "EG",
}
ISO3 = {"AUT": "AT", "BEL": "BE", "BGR": "BG", "HRV": "HR", "CYP": "CY", "CZE": "CZ", "DNK": "DK", "EST": "EE",
        "FIN": "FI", "FRA": "FR", "DEU": "DE", "GRC": "GR", "HUN": "HU", "IRL": "IE", "ITA": "IT", "LVA": "LV",
        "LTU": "LT", "LUX": "LU", "MLT": "MT", "NLD": "NL", "POL": "PL", "PRT": "PT", "ROU": "RO", "SVK": "SK",
        "SVN": "SI", "ESP": "ES", "SWE": "SE", "NOR": "NO", "ISL": "IS", "LIE": "LI", "CHE": "CH", "GBR": "GB",
        "SRB": "RS", "MKD": "MK", "MNE": "ME", "ALB": "AL", "TUR": "TR", "UKR": "UA", "MDA": "MD", "BIH": "BA"}
UE27 = {"AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "ES", "FI", "FR", "GR", "HR", "HU", "IE", "IT", "LT",
        "LU", "LV", "MT", "NL", "PL", "PT", "RO", "SE", "SI", "SK"}


def texte(html):
    if not html:
        return ""
    if isinstance(html, list):
        html = " ".join(str(x) for x in html)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", str(html))).strip()


def jour(v):
    if not v:
        return None
    m = re.match(r"(\d{4}-\d{2}-\d{2})", str(v))
    return m.group(1) if m else None


def segments_de(t):
    segs = [nom for nom, rx in SEGMENTS if rx.search(t)]
    if not segs:
        return ["transverse"] if FORT.search(t) else ["inconnu"]
    if len(segs) >= 4:
        segs.append("transverse")
    return segs


def mots_cles_de(t, n=8):
    c = Counter(m.group(0).lower() for m in re.finditer(
        r"quantum [a-z-]+|post-quantum [a-z]+|\bQKD\b|qubits?|trapped[- ]ions?|neutral[- ]atoms?|cold[- ]atoms?|"
        r"superconducting|photonic|gravimetry|cryogenic[a-z]*|\bPQC\b|quantum-safe [a-z]+", t, re.I))
    vides = {"quantum and", "quantum or", "quantum technologies", "quantum technology", "quantum the", "quantum to", "quantum in"}
    return [k for k, _ in c.most_common(n + len(vides)) if k not in vides][:n]


# ----------------------------------------------------------------------------- HTTP + cache
class Client:
    def __init__(self, cache, hors_ligne):
        self.cache = cache
        self.hors_ligne = hors_ligne
        os.makedirs(cache, exist_ok=True)
        self.memo = {}
        self.s = requests.Session()
        self.s.headers["User-Agent"] = UA

    def _chemin(self, cle):
        return os.path.join(self.cache, hashlib.sha1(cle.encode()).hexdigest() + ".bin")

    def get(self, url, cle=None, **kw):
        return self._req("GET", url, cle, **kw)

    def post(self, url, cle=None, **kw):
        return self._req("POST", url, cle, **kw)

    def _req(self, meth, url, cle, **kw):
        """En ligne : interroge toujours la source et met la réponse en cache.
        Hors ligne : relit la réponse enregistrée lors d'une exécution précédente."""
        cle = cle or (meth + " " + url + " " + json.dumps(kw.get("params") or kw.get("json") or "", sort_keys=True))
        p = self._chemin(cle)
        if p in self.memo:
            return self.memo[p]
        if self.hors_ligne:
            if not os.path.exists(p):
                raise RuntimeError("absent du cache (mode hors ligne) : " + cle[:120])
            with open(p, "rb") as f:
                self.memo[p] = f.read()
            return self.memo[p]
        for essai in range(4):
            try:
                r = self.s.request(meth, url, timeout=kw.pop("timeout", 90), **kw)
                if r.status_code == 429:
                    time.sleep(5 * (essai + 1))
                    continue
                r.raise_for_status()
                with open(p, "wb") as f:
                    f.write(r.content)
                self.memo[p] = r.content
                return r.content
            except requests.RequestException as e:
                if essai == 3:
                    raise
                time.sleep(3 * (essai + 1))
        raise RuntimeError("échec : " + url)


# ----------------------------------------------------------------------------- BCE
def taux_bce(cl):
    try:
        x = cl.get(ECB_URL, cle="ECB").decode()
        date = re.search(r"time='([\d-]+)'", x).group(1)
        taux = {m.group(1): float(m.group(2)) for m in re.finditer(r"currency='(\w+)' rate='([\d.]+)'", x)}
        return date, taux
    except Exception as e:  # noqa: BLE001
        print("  ! taux BCE indisponibles :", e, file=sys.stderr)
        return None, {}


def en_euros(montant, devise, fx):
    if montant is None:
        return None, ""
    devise = (devise or "EUR").upper()
    if devise == "EUR":
        return round(float(montant)), ""
    date, taux = fx
    if devise not in taux:
        return None, f" Montant {montant} {devise} non converti (taux indisponible)."
    return round(float(montant) / taux[devise]), f" Conversion {devise}→EUR au taux BCE du {date} (1 EUR = {taux[devise]} {devise})."


# ----------------------------------------------------------------------------- SEDIA
def sedia_pages(cl, types, statuts, tri=None, max_pages=60, arret=None):
    """Parcourt l'API SEDIA (POST multipart). `arret(resultats)` permet d'interrompre la pagination."""
    query = {"bool": {"must": [{"terms": {"type": types}}, {"terms": {"status": statuts}},
                               {"terms": {"programmePeriod": ["2021 - 2027"]}}]}}
    tous = []
    for page in range(1, max_pages + 1):
        files = {"query": (None, json.dumps(query), "application/json"),
                 "languages": (None, json.dumps(["en"]), "application/json")}
        if tri:
            files["sort"] = (None, json.dumps(tri), "application/json")
        params = {"apiKey": "SEDIA", "text": "***", "pageSize": 100, "pageNumber": page}
        cle = "SEDIA " + json.dumps([types, statuts, tri, page])
        brut = cl.post(SEDIA_URL, cle=cle, params=params, files=files)
        d = json.loads(brut)
        res = d.get("results", [])
        tous += res
        if len(res) < 100 or (arret and arret(res)):
            break
    return tous


def budget_topic(m, ident):
    try:
        bo = json.loads((m.get("budgetOverview") or ["{}"])[0])
    except ValueError:
        return None, None, None
    total, mini, maxi, n = 0, None, None, None
    trouve = False
    for actions in (bo.get("budgetTopicActionMap") or {}).values():
        for a in actions:
            if not str(a.get("action", "")).startswith(ident + " "):
                continue
            trouve = True
            total += sum(float(v) for v in (a.get("budgetYearMap") or {}).values() if v)
            mini = a.get("minContribution") or mini
            maxi = a.get("maxContribution") or maxi
            n = a.get("expectedGrants") or n
    if not trouve:
        return None, None, None
    return (round(total) or None), (mini, maxi), n


def pays_sedia(ident, cond):
    c = cond
    m = re.search(r"\[\[(.+?)\]\]", c)
    if m and "ineligible" in c[m.end():m.end() + 40]:
        noms = [x.strip().lower() for x in re.split(r",| and ", m.group(1)) if x.strip()]
        codes = sorted({NOMS_PAYS[n] for n in noms if n in NOMS_PAYS})
        if codes:
            hors_ue = [x for x in codes if x not in UE27]
            return ["UE27"] + hors_ue, "Pays éligibles listés dans les conditions du topic (restriction art. 22(5))."
    if re.search(r"limited to legal entities established in Member States, Norway and Iceland", c):
        return ["UE27", "NO", "IS"], "Participation limitée aux États membres, à la Norvège et à l'Islande (art. 22(5))."
    m = re.search(r"limited to legal entities established in Member States, Iceland and Norway and the following "
                  r"additional associated countries: ([^.]+)\.", c)
    if m:
        noms = [x.strip().lower().replace("the ", "") for x in re.split(r",| and ", m.group(1)) if x.strip()]
        extra = [NOMS_PAYS[n] for n in noms if n in NOMS_PAYS]
        return ["UE27", "IS", "NO"] + extra, "Participation limitée à l'UE, IS, NO et certains pays associés (art. 22(5))."
    if re.search(r"limited to legal entities established in Member States and Associated Countries", c):
        return ["UE27", "HE_ASSOCIES"], "Participation limitée aux États membres et pays associés ; entités contrôlées depuis un pays non éligible exclues."
    if ident.startswith("DIGITAL"):
        return ["UE27", "DEP_ASSOCIES"], "Éligibilité Digital Europe : vérifier le document d'appel (art. 12(5)/12(6) DEP pour la cybersécurité)."
    if ident.startswith("HORIZON-EIC"):
        return ["UE27", "HE_ASSOCIES_PROGRAMME_COMPLET"], "Éligibilité EIC : voir l'Annexe 2 du programme de travail EIC."
    return ["UE27", "HE_ASSOCIES"], "Éligibilité standard Horizon Europe supposée (aucune restriction détectée automatiquement)."


def financeur_sedia(ident):
    if "EUROHPC" in ident:
        return "EuroHPC JU", "Horizon Europe (EuroHPC JU)"
    if "CHIPS" in ident.upper():
        return "Chips JU", "Horizon Europe / Digital Europe (Chips JU)"
    if ident.startswith("HORIZON-EIC"):
        return "EIC (EISMEA)", "Horizon Europe – Pilier III (EIC)"
    if ident.startswith("DIGITAL-ECCC"):
        return "ECCC (Centre de compétences en cybersécurité)", "Digital Europe"
    if "ECCC" in ident:
        return "Commission européenne / ECCC", "Horizon Europe – Cluster 3"
    if ident.startswith("HORIZON-CL4") and "SPACE" in ident:
        return "Commission européenne (DG DEFIS / HaDEA)", "Horizon Europe – Cluster 4 (Espace)"
    if ident.startswith("HORIZON-CL"):
        return "Commission européenne", "Horizon Europe – Cluster " + ident.split("-")[1][2:]
    if ident.startswith("DIGITAL"):
        return "Commission européenne", "Digital Europe"
    if ident.startswith("EDF"):
        return "Commission européenne (DG DEFIS)", "Fonds européen de la défense"
    if ident.startswith("HORIZON"):
        return "Commission européenne", "Horizon Europe"
    return "Commission européenne", "Programme de l'UE"


def type_action(m):
    toa = " ".join(m.get("typesOfAction") or [])
    acts = " ".join(m.get("actions") or [])
    if "Equity" in toa or "EQU" in acts:
        return "fonds_propres", ["PME", "grande_entreprise"], False, None, None
    if "Prize" in toa or "PRIZE" in acts:
        return "prix", ["PME", "grande_entreprise", "universite", "recherche", "autre"], False, None, None
    if "EIC Accelerator" in toa:
        return "subvention", ["PME"], False, None, None
    if "Coordination and Support" in toa or "-CSA" in acts:
        return "subvention", ["PME", "grande_entreprise", "universite", "recherche", "autre"], True, 3, "100 % des coûts éligibles (CSA, taux standard Horizon Europe)"
    if "Innovation Action" in toa and "Research and" not in toa:
        return "subvention", ["PME", "grande_entreprise", "universite", "recherche"], True, 3, "70 % des coûts éligibles (100 % pour les entités sans but lucratif) – taux standard IA, à confirmer"
    if "Research and Innovation" in toa:
        return "subvention", ["PME", "grande_entreprise", "universite", "recherche"], True, 3, "100 % des coûts éligibles (taux standard RIA Horizon Europe)"
    return "subvention", ["PME", "grande_entreprise", "universite", "recherche"], None, None, None


def trl_de(t):
    m = re.search(r"start at TRL ?(\d)(?:/(\d))? and (?:to )?achieve TRL ?(\d)(?:[-/](\d))?", t)
    if m:
        return f"{m.group(1)}-{m.group(4) or m.group(3)}"
    m = re.search(r"achieve TRL ?(\d)(?:[-–/](\d))? by the end", t)
    if m:
        return f"{m.group(1)}-{m.group(2)}" if m.group(2) else m.group(1)
    return None


def score_sedia(m, r):
    titre = texte(m.get("title")) + " " + str(r.get("summary") or "")
    desc = texte(m.get("descriptionByte")) + " " + texte(m.get("description")) + " " + texte(m.get("beneficiaryAdministration"))
    desc = BRUIT.sub(" ", desc)
    kw = " ".join(m.get("keywords") or []) + " " + " ".join(m.get("tags") or [])
    nt, nd, nk = len(FORT.findall(titre)), len(FORT.findall(desc)), len(FORT.findall(kw))
    npqc = len(PQC.findall(desc))
    if nt:
        niveau = "forte"
    elif nd >= 10:
        niveau = "forte"
    elif nd >= 5 or npqc >= 2:
        niveau = "moyenne"
    elif nd or nk:
        niveau = "faible"
    else:
        niveau = None
    return niveau, nt, nd, nk, titre, desc


def convertir_sedia(r, m, ident, niveau, desc, aujourdhui, generique=None):
    titre = texte(m.get("title")) or ident
    dls = sorted({jour(x) for x in (m.get("deadlineDates") or m.get("deadlineDate") or []) if jour(x)})
    try:
        acts = json.loads((m.get("actions") or ["[]"])[0])
        dls2 = sorted({d for a in acts for d in (a.get("deadlineDates") or [])})
        dls = dls2 or dls
    except (ValueError, TypeError):
        pass
    futures = [d for d in dls if d >= aujourdhui]
    cloture = futures[0] if futures else (dls[-1] if dls else None)
    ouverture = jour((m.get("startDate") or [None])[0])
    budget, bornes, ngr = budget_topic(m, ident)
    mini, maxi = bornes or (None, None)
    nature, types, cons, tmin, taux = type_action(m)
    cond = texte(m.get("topicConditions"))
    pays, note_pays = pays_sedia(ident, cond + " " + desc)
    if re.search(r"at least three legal entities|at least 3 legal entities", cond + " " + desc):
        cons, tmin = True, 3
    fin, prog = financeur_sedia(ident)
    if taux and "-JU-" in ident:
        taux += " ; à confirmer : une entreprise commune peut appliquer des taux propres"
    segs = segments_de(titre + " " + desc) if not generique else ["transverse"]
    notes = []
    if generique:
        notes.append("Appel générique retenu manuellement : " + generique)
    else:
        notes.append(f"Pertinence quantique {niveau} (détection automatique de termes quantiques dans {'le titre' if niveau == 'forte' and FORT.search(titre) else 'la description'}).")
    if len(dls) > 1:
        notes.append("Dates limites : " + ", ".join(dls) + ".")
    if mini or maxi:
        notes.append(f"Contribution UE par projet : {int(mini or 0):,} à {int(maxi or 0):,} €".replace(",", " ") + (f", {ngr} projet(s) attendu(s)." if ngr else "."))
    notes.append(note_pays)
    toa = "; ".join(m.get("typesOfAction") or [])
    if toa:
        notes.append("Type d'action : " + toa + ".")
    if m.get("type", ["1"])[0] == "8":
        notes.append("Appel en cascade (financement de tiers par un projet UE).")
    return {
        "id": "sedia-" + ident.lower(), "financeur": fin, "programme": prog, "intitule": titre,
        "identifiant_appel": ident, "nature": nature,
        "url": TOPIC_URL.format(ident) if m.get("type", ["1"])[0] in ("1", "2") else r.get("url"),
        "statut": None, "ouverture": ouverture, "cloture": cloture,
        "budget_total_eur": budget, "montant_par_projet_eur": round(maxi) if maxi else None,
        "pays_eligibles": pays, "types_eligibles": types, "consortium_requis": cons, "taille_min_consortium": tmin,
        "segments": segs, "trl": trl_de(desc), "taux_financement": taux,
        "mots_cles": mots_cles_de(titre + " " + desc) if not generique else [],
        "note": " ".join(notes), "source_url": SEDIA_SOURCE, "confiance": "elevee",
        "date_verification": aujourdhui,
    }


def collecter_sedia(cl, aujourdhui, clos_depuis, tsv):
    print("SEDIA : topics ouverts / à venir…")
    res = []
    for t in ["1", "2", "8"]:
        res += sedia_pages(cl, [t], ["31094501", "31094502"], tri={"field": "identifier", "order": "ASC"})
    print(f"  {len(res)} résultats")
    print("SEDIA : topics clos depuis", clos_depuis, "…")

    def arret(page):
        dls = [jour((x["metadata"].get("deadlineDate") or [None])[-1]) or "0000" for x in page]
        return max(dls) < clos_depuis
    clos = sedia_pages(cl, ["1", "2", "8"], ["31094503"], tri={"field": "deadlineDate", "order": "DESC"}, max_pages=10, arret=arret)
    print(f"  {len(clos)} résultats examinés")
    out, vus = [], set()
    lignes = ["identifiant\ttitre\tstatut_api\tdate_limite\tpertinence\tn_titre\tn_desc\tn_motscles\tdecision"]
    for r, est_clos in [(x, False) for x in res] + [(x, True) for x in clos]:
        m = r.get("metadata", {})
        ident = (m.get("identifier") or [None])[0] or r.get("reference")
        cle = (ident, r.get("url"), r.get("summary"))
        if cle in vus:
            continue
        vus.add(cle)
        dls = sorted(jour(x) for x in (m.get("deadlineDate") or []) if jour(x))
        if est_clos and (not dls or dls[-1] < clos_depuis):
            continue
        niveau, nt, nd, nk, titre, desc = score_sedia(m, r)
        generique = SEDIA_GENERIQUES.get(ident)
        if dls and dls[-1] < clos_depuis:
            decision = "écarté (date limite passée, statut API périmé)"
        elif ident in SEDIA_EXCLUS:
            decision = "saisie manuelle"
        elif generique:
            decision = "retenu (générique)"
        elif niveau in ("forte", "moyenne"):
            decision = "retenu"
        else:
            decision = "écarté"
        if niveau or generique or ident in SEDIA_EXCLUS:
            lignes.append("\t".join(str(x) for x in [ident, texte(m.get("title"))[:120], (m.get("status") or [""])[0],
                                                     ",".join(dls), niveau or "-", nt, nd, nk, decision]))
        if decision.startswith("retenu"):
            rec = convertir_sedia(r, m, ident, niveau, desc, aujourdhui, generique)
            if rec["cloture"] and rec["cloture"] < clos_depuis:
                continue
            out.append(rec)
    with open(tsv, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")
    print(f"  {len(out)} topics retenus (détail : {os.path.basename(tsv)})")
    return out


# ----------------------------------------------------------------------------- TED
TED_REQ = ('(FT~"quantum" OR FT~"qubit" OR FT~"quanten*" OR FT~"quantique*" OR FT~"cuántic*" OR FT~"quantistic*" '
           'OR FT~"kwantow*" OR FT~"kvant*" OR FT~"kwantum*" OR FT~"QKD" OR FT~"post-quantum" OR FT~"EuroQCI") '
           'AND PD>={pd} AND notice-type IN (cn-standard cn-social cn-desg pin-cfc-standard pin-cfc-social pin-only pin-rtl pmc)')
TED_CHAMPS = ["publication-number", "notice-title", "buyer-name", "buyer-country", "deadline-receipt-tender-date-lot",
              "notice-type", "publication-date", "classification-cpv", "estimated-value-lot", "estimated-value-cur-lot",
              "description-lot", "title-lot", "description-proc"]
# CPV écartés : travaux (45), médical (33), services juridiques (791), architecture/ingénierie (71), supports de stockage (30233).
TED_CPV_EXCLUS = re.compile(r"^(45|33|791|71|30233|48|72)")
TED_MARQUES = re.compile(r"Quantum (Scalar|StorNext|Cube|365|Costmaster|Blue)|StorNext|Campus Quantum", re.I)


def premier(v):
    if isinstance(v, dict):
        for k in ("eng", "fra", "deu"):
            if k in v:
                x = v[k]
                return x[0] if isinstance(x, list) else x
        x = next(iter(v.values()), "")
        return x[0] if isinstance(x, list) else x
    if isinstance(v, list):
        return v[0] if v else ""
    return v or ""


def collecter_ted(cl, aujourdhui, fx, depuis_pub):
    print("TED : avis mentionnant le quantique publiés depuis", depuis_pub, "…")
    notices, page = [], 1
    while page <= 15:
        corps = {"query": TED_REQ.format(pd=depuis_pub.replace("-", "")), "fields": TED_CHAMPS, "limit": 100,
                 "page": page, "scope": "ALL", "paginationMode": "PAGE_NUMBER"}
        d = json.loads(cl.post(TED_URL, cle="TED " + json.dumps(corps, sort_keys=True), json=corps))
        notices += d.get("notices", [])
        if len(d.get("notices", [])) < 100:
            break
        page += 1
    print(f"  {len(notices)} avis examinés")
    out, doublons = [], {}
    for n in notices:
        titre = str(premier(n.get("notice-title")))
        desc = " ".join(str(premier(n.get(k))) for k in ("description-proc", "description-lot", "title-lot"))
        cpv = [str(x) for x in (n.get("classification-cpv") or [])]
        typ = n.get("notice-type")
        dls = sorted(jour(x) for x in (n.get("deadline-receipt-tender-date-lot") or []) if jour(x))
        dl = dls[-1] if dls else None
        if typ.startswith("cn") and (not dl or dl < aujourdhui):
            continue
        if cpv and (TED_CPV_EXCLUS.match(cpv[0]) or all(TED_CPV_EXCLUS.match(c) for c in cpv)):
            continue
        if TED_MARQUES.search(titre + " " + desc):
            continue
        nt = len(FORT.findall(titre))
        nd = len(FORT.findall(desc))
        if not (nt or nd >= 2 or re.search(r"\bQCI\b|EuroQCI", desc)):
            continue
        pays = ISO3.get(str(premier(n.get("buyer-country"))), str(premier(n.get("buyer-country")))[:2])
        acheteur = str(premier(n.get("buyer-name")))
        sujet = re.sub(r"^[^–]+–[^–]+–\s*", "", titre).strip()
        cle_dbl = (acheteur, sujet[:80], dl)
        val = (n.get("estimated-value-lot") or [None])
        cur = (n.get("estimated-value-cur-lot") or ["EUR"])
        try:
            montant = sum(float(x) for x in val if x) if val and val[0] else None
        except (TypeError, ValueError):
            montant = None
        eur, note_fx = en_euros(montant, cur[0] if cur else "EUR", fx)
        pub = jour(n.get("publication-date"))
        num = n["publication-number"]
        segs = segments_de(titre + " " + desc)
        if typ.startswith("cn"):
            statut_note = "Avis de marché ouvert."
        else:
            statut_note = ("Consultation préalable du marché / avis de pré-information publié le " + str(pub) +
                           " : pas encore d'appel d'offres formel ; l'avis de marché suivra éventuellement.")
        rec = {
            "id": "ted-" + num, "financeur": acheteur + f" ({pays})", "programme": "Marché public (TED, UE/EEE)",
            "intitule": sujet[:300], "identifiant_appel": num, "nature": "marche_public",
            "url": f"https://ted.europa.eu/en/notice/-/detail/{num}", "statut": None,
            "ouverture": pub, "cloture": dl, "budget_total_eur": eur, "montant_par_projet_eur": eur,
            "pays_eligibles": ["EEE"],
            "types_eligibles": ["PME", "grande_entreprise", "universite", "recherche"],
            "consortium_requis": False, "taille_min_consortium": None, "segments": segs, "trl": None,
            "taux_financement": None, "mots_cles": mots_cles_de(titre + " " + desc),
            "note": (f"Type d'avis TED : {typ}. Pays de l'acheteur : {pays}. CPV : {', '.join(sorted(set(cpv)))[:120]}. " + statut_note +
                     " Les marchés publics sont en principe ouverts aux opérateurs de l'EEE et des pays signataires de l'AMP ; vérifier les critères de sélection." + note_fx),
            "source_url": f"https://ted.europa.eu/en/notice/-/detail/{num}", "confiance": "elevee",
            "date_verification": aujourdhui,
        }
        if "European Space Agency" in acheteur:
            rec["pays_eligibles"] = ["UE27", "NO", "CH", "GB"]
            rec["note"] += (" Acheteur ESA : la participation est en principe limitée aux États participant au programme ESA concerné "
                            "(retour géographique) ; liste de pays indicative (États membres de l'ESA dans l'UE + NO, CH, GB), à vérifier sur esa-star.")
        if not typ.startswith("cn"):
            rec["cloture"] = None
            rec["ouverture"] = None  # date de publication conservée dans la note ; l'appel d'offres est à venir
            rec["statut"] = "a_venir"
            rec["confiance"] = "moyenne"
        if cle_dbl in doublons:  # republication / rectificatif : garder la plus récente
            ancien = doublons[cle_dbl]
            if (ancien["ouverture"] or "") >= (pub or ""):
                ancien["note"] += f" Republication/rectificatif : {num}."
                continue
            out.remove(ancien)
            rec["note"] += f" Remplace l'avis {ancien['identifiant_appel']} (même objet)."
        doublons[cle_dbl] = rec
        out.append(rec)
    print(f"  {len(out)} avis retenus")
    return out


# ----------------------------------------------------------------------------- SBIR.gov
def collecter_sbir(cl, aujourdhui, fx):
    print("SBIR.gov : sujets ouverts contenant « quantum »…")
    sujets = []
    for page in range(0, 6):
        soup = BeautifulSoup(cl.get(SBIR_SEARCH.format(page)), "lxml")
        liens = [a for a in soup.find_all("a", href=True) if re.match(r"^/topics/\d+$", a["href"])]
        if not liens:
            break
        for a in liens:
            sujets.append((a.get_text(" ", strip=True), "https://www.sbir.gov" + a["href"]))
        if not soup.find("a", href=re.compile(r"page=%d" % (page + 1))):
            break
    sujets = list(dict.fromkeys(sujets))
    print(f"  {len(sujets)} sujets")
    groupes = defaultdict(list)
    for titre, url in sujets:
        t = BeautifulSoup(cl.get(url), "lxml").get_text("\n")
        t = re.sub(r"\n\s*\n+", "\n", t)

        def champ(nom, n=1):
            m = re.search(nom + r"\s*:?\s*\n\s*([^\n]+)" + (r"\n\s*([^\n]+)" if n == 2 else ""), t)
            return [g.strip() for g in m.groups()] if m else [None] * n
        agence = " ".join(x for x in champ("Funding Agency", 2) if x and ":" not in x)
        sol = champ("Solicitation Number")[0]
        ouv = champ("Open Date")[0]
        clo = champ("Close Date")[0]
        offi = None
        soup = BeautifulSoup(cl.get(url), "lxml")
        for a in soup.find_all("a", href=True):
            if "Official Solicitation" in a.get_text():
                offi = a["href"]

        def iso(x):
            try:
                return dt.datetime.strptime(x.strip(), "%B %d, %Y").date().isoformat()
            except (ValueError, AttributeError):
                return None
        groupes[(agence or "?", sol or "?", iso(clo))].append(dict(titre=titre, url=url, ouverture=iso(ouv), officiel=offi))
    out = []
    for (agence, sol, clo), lst in groupes.items():
        if sol in SBIR_SOLLICITATIONS_MANUELLES:
            continue
        if not clo or clo < aujourdhui:
            continue
        titres = [x["titre"] for x in lst]
        intitule = titres[0] if len(titres) == 1 else f"{len(titres)} sujets quantiques ({'; '.join(titres)[:200]})"
        txt = " ".join(titres)
        out.append({
            "id": "sbir-" + re.sub(r"[^a-z0-9]+", "-", f"{agence}-{sol}-{clo}".lower()).strip("-"),
            "financeur": f"{agence} (États-Unis)", "programme": "SBIR/STTR (fédéral, États-Unis)",
            "intitule": intitule, "identifiant_appel": sol, "nature": "subvention",
            "url": lst[0]["officiel"] or lst[0]["url"], "statut": None,
            "ouverture": min((x["ouverture"] for x in lst if x["ouverture"]), default=None), "cloture": clo,
            "budget_total_eur": None, "montant_par_projet_eur": None, "pays_eligibles": ["US"],
            "types_eligibles": ["PME"], "consortium_requis": False, "taille_min_consortium": None,
            "segments": segments_de(txt), "trl": None, "taux_financement": None, "mots_cles": titres[:8],
            "note": ("RÉSERVÉ AUX PETITES ENTREPRISES AMÉRICAINES (règles SBA de propriété et de localisation). "
                     "Données lues sur SBIR.gov, qui avertit que ses fiches sont des copies des sollicitations des agences : "
                     "vérifier sur la sollicitation officielle. Fiches : " + ", ".join(x["url"] for x in lst)),
            "source_url": lst[0]["url"], "confiance": "moyenne", "date_verification": aujourdhui,
        })
    print(f"  {len(out)} groupes de sujets retenus")
    return out


# ----------------------------------------------------------------------------- Royaume-Uni
def collecter_uk(cl, aujourdhui, fx, jours):
    out = []
    print("Contracts Finder : avis ouverts « quantum »…")
    try:
        corps = {"searchCriteria": {"keyword": "quantum", "statuses": ["Open"]}, "size": 100}
        d = json.loads(cl.post(CF_URL, cle="CF " + json.dumps(corps), json=corps))
        for x in d.get("noticeList", []):
            it = x["item"]
            dl = jour(it.get("deadlineDate"))
            titre = it.get("title") or ""
            if not dl or dl < aujourdhui or not FORT.search(titre + " " + (it.get("description") or "")):
                continue
            eur, nfx = en_euros(it.get("valueHigh") or it.get("valueLow"), "GBP", fx)
            out.append({"id": "cf-" + it["id"], "financeur": (it.get("organisationName") or "") + " (GB)",
                        "programme": "Marché public (Contracts Finder, Royaume-Uni)", "intitule": titre,
                        "identifiant_appel": it["id"], "nature": "marche_public",
                        "url": "https://www.contractsfinder.service.gov.uk/Notice/" + it["id"], "statut": None,
                        "ouverture": jour(it.get("publishedDate")), "cloture": dl, "budget_total_eur": eur,
                        "montant_par_projet_eur": eur, "pays_eligibles": ["GB"],
                        "types_eligibles": ["PME", "grande_entreprise"], "consortium_requis": False,
                        "taille_min_consortium": None, "segments": segments_de(titre), "trl": None,
                        "taux_financement": None, "mots_cles": mots_cles_de(titre),
                        "note": "Avis Contracts Finder ouvert." + nfx,
                        "source_url": "https://www.contractsfinder.service.gov.uk/Notice/" + it["id"],
                        "confiance": "elevee", "date_verification": aujourdhui})
        print(f"  {d.get('hitCount')} résultats, {len(out)} ouverts et pertinents")
    except Exception as e:  # noqa: BLE001
        print("  ! Contracts Finder indisponible :", e, file=sys.stderr)
    print(f"Find a Tender (OCDS) : {jours} derniers jours…")
    fin = dt.date.fromisoformat(aujourdhui)
    vus = set()
    n = 0
    for i in range(jours):
        a = fin - dt.timedelta(days=i + 1)
        for st in ("tender", "planning"):
            params = {"stages": st, "limit": 100, "updatedFrom": a.isoformat() + "T00:00:00",
                      "updatedTo": (a + dt.timedelta(days=1)).isoformat() + "T00:00:00"}
            try:
                d = json.loads(cl.get(FTS_URL, params=params))
            except Exception as e:  # noqa: BLE001
                print("  ! FTS", a, st, e, file=sys.stderr)
                continue
            for x in d.get("releases", []):
                n += 1
                t = x.get("tender") or {}
                txt = " ".join([str(t.get("title", "")), str(t.get("description", ""))] +
                               [str(l.get("description", "")) for l in t.get("lots", [])])
                if x["id"] in vus or not (FORT.search(txt) or re.search(r"cryogen[- ]free|single[- ]photon", txt, re.I)):
                    continue
                vus.add(x["id"])
                dl = jour((t.get("tenderPeriod") or {}).get("endDate"))
                if st == "tender" and (not dl or dl < aujourdhui):
                    continue
                acheteur = next((p.get("name") for p in x.get("parties", []) if "buyer" in p.get("roles", [])), "")
                val = (t.get("value") or {})
                eur, nfx = en_euros(val.get("amount"), val.get("currency", "GBP"), fx)
                url = "https://www.find-tender.service.gov.uk/Notice/" + x["id"]
                out.append({"id": "fts-" + x["id"], "financeur": acheteur + " (GB)",
                            "programme": "Marché public (Find a Tender, Royaume-Uni)", "intitule": t.get("title", ""),
                            "identifiant_appel": x["id"], "nature": "marche_public", "url": url, "statut": None,
                            "ouverture": jour(x.get("date")), "cloture": dl if st == "tender" else None,
                            "budget_total_eur": eur, "montant_par_projet_eur": eur, "pays_eligibles": ["GB"],
                            "types_eligibles": ["PME", "grande_entreprise"], "consortium_requis": False,
                            "taille_min_consortium": None, "segments": segments_de(txt), "trl": None,
                            "taux_financement": None, "mots_cles": mots_cles_de(txt),
                            "note": (f"Procédure : {t.get('procurementMethodDetails') or '?'}. Étape OCDS : {st}. "
                                     "Fournisseurs étrangers en principe admis (accords commerciaux du Royaume-Uni) ; vérifier le dossier. "
                                     "Couverture Find a Tender partielle : l'API OCDS consultée par fenêtres d'un jour renvoie peu d'avis." + nfx),
                            "source_url": url, "confiance": "elevee", "date_verification": aujourdhui})
    print(f"  {n} avis OCDS examinés, {sum(1 for r in out if r['id'].startswith('fts-'))} retenus")
    return out


# ----------------------------------------------------------------------------- fusion
def statut_calcule(r, aujourdhui):
    if r.get("cloture") and r["cloture"] < aujourdhui:
        return "clos"
    if r.get("ouverture") and r["ouverture"] > aujourdhui:
        return "a_venir"
    if r.get("cloture") or r.get("ouverture"):
        return "ouvert"
    return r.get("statut") or "a_venir"


def normaliser(r):
    return {k: r.get(k) for k in CHAMPS}


def lire_manuelles(chemin):
    out = []
    if not os.path.exists(chemin):
        return out
    with open(chemin, encoding="utf-8") as f:
        for i, ligne in enumerate(f, 1):
            ligne = ligne.strip()
            if not ligne or ligne.startswith("//"):
                continue
            try:
                out.append(json.loads(ligne))
            except ValueError as e:
                sys.exit(f"saisies_manuelles.jsonl ligne {i} : JSON invalide ({e})")
    return out


# ----------------------------------------------------------------------------- CALENDRIER.md
LACUNES = """## Lacunes et limites

- **Allemagne (BMFTR)** : bmftr.bund.de répond de façon intermittente (délais, erreurs 500) et la Förderdatenbank renvoie un captcha ; seuls l'appel « Transfer und Netzintegration der Quantenkommunikation » (Stichtag 30/11/2026) et, au statut « clos », « Quantum International » ont été vérifiés. Les Stichtage de KMU-innovativ (15/04, 15/10) et des « Wissenschaftliche Vorprojekte » (15/06, 15/12) proviennent de listes secondaires : confiance faible. La directive « Fehlerkorrigiertes Quantencomputing » (BAnz AT 07.04.2026, jusqu'à 20 M€ par projet en module A, selon un moteur de recherche) n'a pas pu être vérifiée.
- **France** : aucun appel à projets spécifiquement quantique ouvert n'a été trouvé sur Bpifrance, l'ANR ni la page de la stratégie nationale (France 2030) au 22/11/2026 ; seul l'appel Eureka Xecs (composants électroniques, générique) est listé. Le nouvel engagement France 2030 d'environ 1 Md€ pour 2026-2030 (communiqué cité par un moteur de recherche) n'est pas encore décliné en appels identifiés.
- **Italie** : le décret MIMIT du 22/07/2026 (Accordi per l'innovazione) réserverait 30 M€ aux technologies quantiques, bio-électronique et radiopharmaceutiques ; le site du MIMIT était injoignable : aucune entrée créée.
- **Espagne** : seul INNTERCONECTA STEP 2026 (CDTI, générique, dates exactes non vérifiées) est listé.
- **Finlande** : le programme Quantum de Business Finland s'est terminé le 30/06/2026 ; les projets quantiques passent désormais par les financements R&D génériques (non listés).
- **Danemark** : le thème « Quantum technology » d'Innovation Fund Denmark passe par Grand Solutions (jusqu'à 90 % pour le quantique) et International collaborations ; aucune date 2027 publiée trouvée.
- **Pays-Bas** : seul l'appel TechBridge UK 2026 est listé ; aucune autre aide RVO/Quantum Delta NL ouverte trouvée.
- **Royaume-Uni** : aucune compétition « Quantum Missions » d'Innovate UK ouverte ou annoncée n'a été trouvée sur l'Innovation Funding Service ; la page NQCC n'affiche aucun financement ouvert (SparQ 2027 = prévision). Find a Tender n'est interrogé qu'à travers son flux OCDS, qui renvoie peu d'avis par fenêtre : la couverture des marchés publics britanniques est partielle ; Contracts Finder ne contient aucun avis « quantum » ouvert.
- **ESA** : esa-star n'est pas joignable ; la liste des opportunités NAVISP est chargée dynamiquement. Seul l'appel permanent NAVISP Élément 2 est listé ; les invitations à soumissionner ESA (ARTES/SAGA, technologies quantiques spatiales) ne sont pas couvertes.
- **EuroHPC JU** : seul l'appel QML-07 est ouvert ; aucun appel quantique 2027 n'est annoncé. La loi européenne sur le quantique (Quantum Act) n'apporte pas de budget propre : risque de creux d'appels après 2027 (fin d'Horizon Europe).
- **États-Unis** : couverture limitée aux sujets listés par SBIR.gov (copies) et à la sollicitation NSF 26-510 ; les BAA DARPA, les appels DOE Office of Science et les AFWERX/AFRL hors SBIR ne sont pas couverts. L'API SBIR.gov renvoie 403 depuis cet environnement.
- **Marchés publics UE (TED)** : la recherche plein texte attrape des faux positifs (marques « Quantum », chantiers de bâtiments « Quantum ») filtrés par CPV et par liste de marques ; d'autres faux positifs ou oublis restent possibles. Les consultations préalables (PMC/PIN) n'ont pas de date limite de dépôt d'offre.
- **Éligibilité** : les groupes de pays sont des points de départ ; chaque topic peut restreindre la participation (art. 22(5) HE, art. 12(5)/(6) DEP) et exclure les entités contrôlées depuis un pays tiers. Le moteur de rapprochement doit signaler, un humain confirmer.
"""


def ecrire_calendrier(recs, chemin, aujourdhui, groupes_note):
    def fmt_eur(x):
        if x is None:
            return "—"
        if x >= 1e6:
            return f"{x / 1e6:.1f} M€".replace(".", ",")
        return f"{x / 1e3:.0f} k€"

    def elig(r):
        return ", ".join(r.get("pays_eligibles") or []) + " ; " + ", ".join(r.get("types_eligibles") or [])

    def cons(r):
        c = r.get("consortium_requis")
        if c is True:
            return "oui" + (f" (≥ {r['taille_min_consortium']})" if r.get("taille_min_consortium") else "")
        if c is False:
            return "non"
        return "?"
    actifs = [r for r in recs if r["statut"] in ("ouvert", "a_venir")]
    dates = sorted([r for r in actifs if r.get("cloture")], key=lambda r: (r["cloture"], r["id"]))
    sans = sorted([r for r in actifs if not r.get("cloture")], key=lambda r: r["id"])
    clos = sorted([r for r in recs if r["statut"] == "clos"], key=lambda r: (r["cloture"] or "", r["id"]))
    L = [f"# Calendrier des appels et marchés publics ouverts aux entreprises du quantique",
         "",
         f"Généré par `construire_opportunites.py` le {aujourdhui} à partir de `opportunites.jsonl` ({len(recs)} enregistrements : "
         f"{sum(r['statut'] == 'ouvert' for r in recs)} ouverts, {sum(r['statut'] == 'a_venir' for r in recs)} à venir, {len(clos)} clos depuis le 1er octobre 2026 conservés comme références de cadence).",
         "Période visée : décembre 2026 à décembre 2027, priorité UE et Royaume-Uni ; les États-Unis figurent en section secondaire (éligibilité réservée aux entreprises américaines).",
         "Confiance : **élevée** = lu sur une page ou une API officielle ; **moyenne** = source officielle mais copie, ou périmètre quantique déduit ; **faible** = source secondaire ou date non confirmée (voir la note de l'enregistrement).",
         "Les groupes de pays (UE27, EEE, HE_ASSOCIES, DEP_ASSOCIES…) sont définis dans `groupes_pays.json`.",
         "",
         "## Opportunités ouvertes et à venir, par date limite",
         "",
         "| Date limite | Financeur | Intitulé | Budget total | Par projet | Éligibles (pays ; types) | Consortium | Statut | Confiance | Lien |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    hors_us = [r for r in dates if r.get("pays_eligibles") != ["US"]]
    us = [r for r in dates if r.get("pays_eligibles") == ["US"]]
    for r in hors_us:
        L.append(f"| {r['cloture']} | {r['financeur']} | {r['intitule'][:110].replace('|', '/')} | {fmt_eur(r.get('budget_total_eur'))} | "
                 f"{fmt_eur(r.get('montant_par_projet_eur'))} | {elig(r)} | {cons(r)} | {r['statut']} | {r['confiance']} | [lien]({r['url']}) |")
    L += ["", "### Sans date limite fixe (guichets permanents, consultations préalables, appels annoncés sans date)", "",
          "| Financeur | Intitulé | Ouverture | Éligibles (pays ; types) | Statut | Confiance | Lien |", "|---|---|---|---|---|---|---|"]
    for r in sans:
        if r.get("pays_eligibles") == ["US"]:
            continue
        L.append(f"| {r['financeur']} | {r['intitule'][:110].replace('|', '/')} | {r.get('ouverture') or '—'} | {elig(r)} | {r['statut']} | {r['confiance']} | [lien]({r['url']}) |")
    L += ["", "### États-Unis (section secondaire — réservé aux petites entreprises américaines)", "",
          "| Date limite | Financeur | Intitulé | Par projet | Statut | Confiance | Lien |", "|---|---|---|---|---|---|---|"]
    for r in us + [x for x in sans if x.get("pays_eligibles") == ["US"]]:
        L.append(f"| {r.get('cloture') or '—'} | {r['financeur']} | {r['intitule'][:110].replace('|', '/')} | {fmt_eur(r.get('montant_par_projet_eur'))} | {r['statut']} | {r['confiance']} | [lien]({r['url']}) |")
    L += ["", "### Références : appels clos depuis le 1er octobre 2026", "",
          "| Date limite | Financeur | Intitulé | Budget total | Lien |", "|---|---|---|---|---|"]
    for r in clos:
        L.append(f"| {r.get('cloture') or '—'} | {r['financeur']} | {r['intitule'][:110].replace('|', '/')} | {fmt_eur(r.get('budget_total_eur'))} | [lien]({r['url']}) |")
    # rythme
    mois = Counter(r["cloture"][:7] for r in dates)
    mois_ue = Counter(r["cloture"][:7] for r in hors_us)
    debut = min([aujourdhui[:7]] + list(mois))
    tous_mois, (y, mo) = [], (int(debut[:4]), int(debut[5:7]))
    while f"{y:04d}-{mo:02d}" <= max(list(mois) + ["2027-12"]):
        tous_mois.append(f"{y:04d}-{mo:02d}")
        y, mo = (y + 1, 1) if mo == 12 else (y, mo + 1)
    L += ["", "## Rythme : dates limites par mois", "",
          "Compte des dates limites des opportunités ouvertes ou à venir (une ligne par date limite ; les dates de lot multiples d'un même appel, comme l'EIC Accelerator, comptent séparément).", "",
          "| Mois | Toutes | Hors États-Unis | Dont thème quantique explicite* | Dont marchés publics |", "|---|---|---|---|---|"]
    for mth in tous_mois:
        spec = sum(1 for r in hors_us if r["cloture"][:7] == mth and FORT.search(r["intitule"] + " " + (r.get("identifiant_appel") or "")))
        mp = sum(1 for r in hors_us if r["cloture"][:7] == mth and r["nature"] == "marche_public")
        L.append(f"| {mth} | {mois.get(mth, 0)} | {mois_ue.get(mth, 0)} | {spec} | {mp} |")
    L += ["", "\\* hors États-Unis, intitulé ou identifiant contenant un terme quantique (quantum, quantique, Quanten, QKD, PQC, post-quantum…) ; les appels génériques ouverts au quantique (EIC Accelerator, STEP, Pathfinder Open, Transition) sont exclus de cette colonne.", "",
          f"Lecture (analyse rédigée le {aujourdhui}, à revoir si les données changent) : les échéances se concentrent fin 2026 – début 2027 (fin des appels britanniques et néerlandais, QML-07, Chips JU au 31 mars 2027, lots EIC), puis en septembre 2027 (gravimétrie spatiale, cryptographie post-quantique du Cluster 3, défi EIC « Quantum Energetics », EIC Transition). "
          "D'avril à août 2027, très peu d'appels quantiques sont publiés à ce jour ; c'est pourtant la période où des appels nationaux (SparQ, Innovate UK, TechBridge) ont été publiés les années précédentes : surveiller. Après 2027, Horizon Europe s'achève et la loi européenne sur le quantique ne prévoit pas de budget propre.", ""]
    L.append(LACUNES)
    L += ["## Méthode", "",
          "- Topics UE : API de recherche SEDIA (POST multipart, clé publique `SEDIA`), tous les topics ouverts/à venir (types 1, 2, 8) et les topics clos depuis le 01/10/2026, filtrés localement sur des termes quantiques (titre, description, mots-clés) ; la décision pour chaque topic examiné est dans `candidats_sedia.tsv`.",
          "- Marchés UE : API TED v3 (`FT~` plein texte multilingue), filtres CPV et marques ; marchés britanniques : Contracts Finder (API de recherche) et Find a Tender (OCDS).",
          "- États-Unis : pages de recherche SBIR.gov et sollicitation NSF 26-510.",
          "- Saisies manuelles (`saisies_manuelles.jsonl`) : Chips JU (Appendix 8 du programme de travail, v13), programme de travail EIC 2027, Innovate UK, UKRI, RVO, NQCC, BMFTR, Bpifrance, CDTI, ESA NAVISP, NSF.",
          f"- {groupes_note}",
          "- Validation : `python3 valider_opportunites.py --aujourdhui " + aujourdhui + "`.", ""]
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("\n".join(L))


# ----------------------------------------------------------------------------- principal
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--aujourdhui", default=dt.date.today().isoformat())
    ap.add_argument("--clos-depuis", default="2026-10-01", help="conserver les appels clos depuis cette date")
    ap.add_argument("--fin", default="2027-12-31", help="ignorer les ouvertures après cette date")
    ap.add_argument("--cache", default=os.path.join(tempfile.gettempdir(), "cantique_opportunites_cache"))
    ap.add_argument("--hors-ligne", action="store_true", help="relire les réponses mises en cache au lieu d'interroger les sources")
    ap.add_argument("--sans-ted", action="store_true")
    ap.add_argument("--sans-sbir", action="store_true")
    ap.add_argument("--sans-uk", action="store_true")
    ap.add_argument("--jours-fts", type=int, default=60)
    ap.add_argument("--ted-depuis", default="2026-06-01", help="date de publication minimale des avis TED")
    a = ap.parse_args()
    cl = Client(a.cache, a.hors_ligne)
    fx = taux_bce(cl)
    recs = collecter_sedia(cl, a.aujourdhui, a.clos_depuis, os.path.join(ICI, "candidats_sedia.tsv"))
    for nom, fn, saut in [("TED", lambda: collecter_ted(cl, a.aujourdhui, fx, a.ted_depuis), a.sans_ted),
                          ("SBIR", lambda: collecter_sbir(cl, a.aujourdhui, fx), a.sans_sbir),
                          ("UK", lambda: collecter_uk(cl, a.aujourdhui, fx, a.jours_fts), a.sans_uk)]:
        if saut:
            continue
        try:
            recs += fn()
        except Exception as e:  # noqa: BLE001
            print(f"  ! {nom} : échec ({e}) — partie ignorée", file=sys.stderr)
    manuelles = lire_manuelles(os.path.join(ICI, "saisies_manuelles.jsonl"))
    par_id = {r["id"]: r for r in recs}
    for m in manuelles:
        if m["id"] in par_id:
            print("  saisie manuelle prioritaire :", m["id"])
        par_id[m["id"]] = m
    final = []
    for r in par_id.values():
        r = normaliser(r)
        r["statut"] = statut_calcule(r, a.aujourdhui)
        if r["statut"] == "clos" and (not r["cloture"] or r["cloture"] < a.clos_depuis):
            continue
        if r["ouverture"] and r["ouverture"] > a.fin:
            continue
        r["date_verification"] = r.get("date_verification") or a.aujourdhui
        final.append(r)
    final.sort(key=lambda r: (r["cloture"] or "9999-99-99", r["id"]))
    with open(os.path.join(ICI, "opportunites.jsonl"), "w", encoding="utf-8") as f:
        for r in final:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    note_fx = (f"Montants convertis au taux de référence BCE du {fx[0]}." if fx[0] else "Taux BCE indisponibles.")
    ecrire_calendrier(final, os.path.join(ICI, "CALENDRIER.md"), a.aujourdhui, note_fx)
    c = Counter(r["statut"] for r in final)
    print(f"\n{len(final)} opportunités écrites dans opportunites.jsonl : " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())))


if __name__ == "__main__":
    main()
