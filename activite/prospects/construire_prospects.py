#!/usr/bin/env python3
"""Construit la base de prospects « entreprises du quantique déjà financées » (UE + Royaume-Uni).

Sources (données publiques, niveau organisation uniquement — aucune donnée personnelle) :
  * CORDIS, dumps open data « projects » Horizon Europe et H2020 (CSV, publiés sur
    data.europa.eu / cordis.europa.eu/data) : project.csv, organization.csv, topics.csv,
    euroSciVoc.csv. organization.csv fournit le PIC (organisationID), le drapeau SME,
    activityType, le rôle et ecContribution par organisation.
  * UKRI Gateway to Research (GtR) API v2 (Accept: application/vnd.rcuk.gtr.json-v7) :
    recherche plein texte de projets, participantValues (grantOffer par participant
    pour Innovate UK / Horizon Europe Guarantee), /funds/{id} (montant total) et
    /organisations/{id} (adresse : région, pays, ville ; site web).
  * BCE : taux de référence GBP/EUR (data-api.ecb.europa.eu) pour convertir les livres.

Sorties (dans le dossier du script) : prospects.jsonl (entreprises), prospects_recherche.jsonl
(universités, organismes de recherche, autres organismes publics/associatifs), prospects.csv.

Bibliothèque standard uniquement. Les réponses brutes sont mises en cache sous le
répertoire de travail (option --cache, par défaut le scratchpad de la session) ; une
relance réutilise le cache (reprise après interruption). Délai minimal entre deux
requêtes HTTP : 1,1 s (option --delai).

Usage :
  python3 -I construire_prospects.py                 # tout (téléchargement + GtR + construction)
  python3 -I construire_prospects.py --hors-ligne    # reconstruit uniquement depuis le cache
"""
import argparse
import collections
import csv
import datetime
import hashlib
import io
import json
import os
import random
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
CACHE_DEFAUT = os.environ.get(
    "PROSPECTS_CACHE",
    "/tmp/claude-0/-home-user-Cantique/9dc9892d-7fe1-5ee3-bda5-8a634e3d3446/scratchpad",
)
DEBUT_FENETRE = "2019-01-01"
USER_AGENT = "prospects-quantique/1.0 (extraction open data; contact via projet)"

CORDIS_DUMPS = {
    "he": "https://cordis.europa.eu/data/cordis-HORIZONprojects-csv.zip",
    "h2020": "https://cordis.europa.eu/data/cordis-h2020projects-csv.zip",
}
CORDIS_DATASETS = {
    "he": "https://data.europa.eu/data/datasets/cordis-eu-research-projects-under-horizon-europe-2021-2027",
    "h2020": "https://data.europa.eu/data/datasets/cordis-eu-research-projects-under-horizon-2020-framework-programme-2014-2020",
}
GTR_API = "https://gtr.ukri.org/gtr/api"
GTR_ACCEPT = "application/vnd.rcuk.gtr.json-v7"
ECB_URL = "https://data-api.ecb.europa.eu/service/data/EXR/D.GBP.EUR.SP00.A?lastNObservations=5&format=csvdata"

# Requêtes GtR (recherche plein texte ; les guillemets forcent l'expression exacte).
GTR_REQUETES = [
    "quantum", "qubit", "qubits", "QKD", '"atom interferometry"', '"atom interferometer"',
    '"cold atom"', '"cold atoms"', '"optically pumped magnetometer"', '"optically pumped magnetometers"',
    '"nitrogen vacancy"', '"single photon"', '"single-photon"', '"trapped ion"', '"trapped ions"',
    '"dilution refrigerator"', '"atomic clock"', '"optical clock"', "Rydberg", "SNSPD",
    '"superconducting nanowire"', "entanglement", '"post-quantum"',
]

# ---------------------------------------------------------------------------
# Règles de pertinence « technologies quantiques »
# ---------------------------------------------------------------------------

def norm(t):
    t = (t or "").lower()
    t = re.sub(r"[\-‐‑–—_/]", " ", t)
    return re.sub(r"\s+", " ", t)

# Expressions retirées avant comptage (faux positifs classiques : boîtes quantiques pour
# écrans/LED/solaire, rendement quantique, puits quantiques, laser à cascade quantique,
# chimie quantique, physique fondamentale, métaphore « quantum leap »...).
NEG = re.compile(
    r"quantum (dots?|yields?|efficienc(y|ies)|wells?|cascade|chemistry|chemical|mechanical(ly)?|mechanics|"
    r"leaps?|jumps?|field theor(y|ies)|gravity(?! (sensors?|sensing|gradiomet\w*|measurements?|meters?|mapping))|"
    r"chromodynamics|confinement|size|tunnell?ing|biology|hall|many body|phase transitions?|spin liquids?|"
    r"critical\w*|materials?|matter|monte carlo|espresso|defects?|corporation|fluctuations?|statistics|chaos|"
    r"nature|effects?|physics|theory|mechanism|level|fluids?)\b")

STRONG = [
    r"quantum (computing|computers?|computation\w*|processors?|processing units?|processing|hardware|software|"
    r"algorithms?|machine learning|neural networks?|annealing|annealers?|advantage|supremacy|error correct\w*|"
    r"error mitigation|circuits?|gates?|logic|registers?|chips?|programming|compilers?|programs?|cloud|"
    r"optimi[sz]ation|computational advantage)",
    r"\bqubits?\b", r"\bqudits?\b", r"\bqpus?\b",
    r"quantum (enhanced|sensing|sensors?|metrology|magnetomet\w*|gravimet\w*|gradiomet\w*|gyroscopes?|"
    r"accelerometers?|inertial|navigation|imag(ing|es?)|radar|lidar|clocks?|timing|illumination|microscop\w*)",
    r"quantum key distribution", r"\bqkd\b", r"euroqci", r"\bqci\b",
    r"quantum (networks?|networking|internet|repeaters?|memor(y|ies)|communications?|cryptograph\w*|encryption|"
    r"channels?|links?|teleportation|random number\w*|randomness|secure|security|safe|resistant|proof|attacks?|"
    r"threats?|adversar\w*)",
    r"post quantum", r"\bpqc\b", r"\bqrngs?\b",
    r"quantum simulators?",
    r"quantum (technolog\w*|tech|information|flagship)",
    r"quantum (photonic\w*|light|emitters?|transducers?|transduction|frequency conversion|states? of light|optomechanic\w*)",
    r"photonic quantum", r"trapped ions?", r"superconducting (qubits?|quantum)",
    r"atom(ic)? interferomet\w*", r"(ultra ?)?cold atoms?", r"ultracold (molecules?|gas(es)?)",
    r"nitrogen vacancy", r"\bnv (centres?|centers?|diamonds?|magnetomet\w*|based)", r"colou?r cent(er|re)s?",
    r"optically pumped magnetomet\w*", r"\bopm meg\b", r"atomic magnetomet\w*",
    r"dilution (refrigerators?|fridges?|cryostats?|refrigeration)",
    r"squeezed (light|states?|vacuum)", r"entangled (photons?|states?|qubits?|atoms?|photon pairs?)",
    r"quantum entanglement",
    r"\bsnspds?\b", r"superconducting nanowires?", r"single photon (detectors?|sources?|emitters?|guns?)",
    r"(optical|atomic) (lattice )?clocks?",
    r"rydberg (atoms?|atom arrays?|states?|excitations?|sensors?|receivers?|arrays?)",
    r"neutral atom (arrays?|quantum|qubits?|processors?|computers?|computing)",
]
CTX = [
    r"entangle\w*", r"single photons?", r"\bspads?\b", r"rydberg", r"bose einstein", r"majorana", r"ion traps?",
    r"neutral atoms?",
    r"quantum (simulations?|optics|optical|control|limited|states?|coherence|physics|sensitivity|devices?|systems?|"
    r"platforms?|applications?|electronic\w*)",
    r"matter waves?", r"cryogenic\w*", r"cryo cmos", r"magnetomet\w*", r"interferomet\w*", r"superconducting",
    r"decoherence", r"coherence times?", r"quantum dots?", r"photonic integrated", r"\bsquids?\b", r"spin defects?",
    r"lattice based cryptograph\w*", r"homomorphic", r"cryptograph\w*",
]
HW_CTX = re.compile(r"cryogenic|cryo cmos|dilution|superconducting|single photon|entangle|ion trap|neutral atom|"
                    r"rydberg|decoherence|coherence time|spin defect|photonic integrated|magnetomet|squid")
STRONG_RE = [re.compile(p) for p in STRONG]
CTX_RE = [re.compile(p) for p in CTX]
MIXED_TOPIC = re.compile(r"semiconductor or quantum|lawful interception|and solar cells", re.I)
SEUIL = 3.0


def _hits(rxs, t):
    """Occurrences distinctes (les correspondances qui se chevauchent comptent une fois)."""
    spans = []
    for rx in rxs:
        spans.extend((m.start(), m.end(), m.group(0)) for m in rx.finditer(t))
    spans.sort()
    out, fin = [], -1
    for s, e, g in spans:
        if s < fin:  # chevauchement avec l'occurrence précédente
            fin = max(fin, e)
            continue
        out.append(g)
        fin = e
    if "pqc" in out and not re.search(r"crypt|quantum", t):  # PQC = « protein quality control »...
        out = [x for x in out if x != "pqc"]
    return out


def classer(titre, objectif, mots_cles, sujets):
    """Score de pertinence QT. sujets = intitulés de topics d'appel (CORDIS) ou de
    researchTopics/researchSubjects (GtR). Retourne un dict (garder, score, preuves).

    Barème : titre +3 ; topic d'appel quantique +3 ; mots-clés +1 (+2 si au moins deux termes) ;
    résumé +1 par occurrence distincte (plafond 4) ; contexte matériel +1 (sinon contexte +0,5).
    Retenu si score >= 3 ET (titre, topic, >= 2 occurrences dans le résumé, ou >= 2 termes
    en mots-clés avec >= 1 occurrence dans le résumé)."""
    tn = NEG.sub(" ", norm(titre))
    on = NEG.sub(" ", norm(objectif))
    kn = NEG.sub(" ", norm(mots_cles))
    ts, ks, os_ = _hits(STRONG_RE, tn), _hits(STRONG_RE, kn), _hits(STRONG_RE, on)
    top = [s for s in sujets if s and re.search(r"quantum|qkd|\bqci\b", s, re.I)
           and not MIXED_TOPIC.search(s) and NEG.sub(" ", norm(s)).count("quantum") > 0]
    ctx = _hits(CTX_RE, tn + " | " + kn + " | " + on)
    score, parts = 0.0, []
    if ts:
        score += 3; parts.append("titre")
    if top:
        score += 3; parts.append("topic")
    kd = len(set(ks))
    if kd:
        score += 2 if kd >= 2 else 1; parts.append("mots-cles x%d" % kd)
    if os_:
        score += min(len(os_), 4); parts.append("resume x%d" % len(os_))
    hw = sorted(set(c for c in ctx if HW_CTX.search(c)))
    if hw:
        score += 1; parts.append("contexte materiel")
    elif ctx:
        score += 0.5; parts.append("contexte")
    garder = score >= SEUIL and bool(ts or top or len(os_) >= 2 or (kd >= 2 and os_))
    return {"garder": garder, "score": score, "regle": "+".join(parts),
            "termes": sorted(set(ts + ks + os_)), "sujets": top, "texte": tn + " " + kn + " " + on}

# ---------------------------------------------------------------------------
# Segments
# ---------------------------------------------------------------------------
SEGMENTS = {
    "calcul": [r"quantum (computing|computers?|computation\w*|processors?|processing units?|hardware|annealing|"
               r"annealers?|advantage|supremacy|error correct\w*|gates?|chips?|registers?|logic)", r"\bqubits?\b",
               r"\bqpus?\b", r"trapped ions?", r"ion traps?", r"superconducting (qubits?|quantum)",
               r"neutral atom (arrays?|quantum|qubits?|processors?|computers?|computing)", r"quantum simulators?",
               r"\bmajorana\b", r"\bqudits?\b"],
    "capteurs": [r"quantum (enhanced|sensing|sensors?|metrology|magnetomet\w*|gravimet\w*|gradiomet\w*|gyroscopes?|"
                 r"accelerometers?|inertial|navigation|imag(ing|es?)|radar|lidar|clocks?|timing|illumination|"
                 r"microscop\w*)", r"atom(ic)? interferomet\w*", r"nitrogen vacancy",
                 r"\bnv (centres?|centers?|diamonds?|magnetomet\w*|based)", r"optically pumped magnetomet\w*",
                 r"\bopm meg\b", r"atomic magnetomet\w*", r"magnetomet\w*", r"gravimet\w*", r"(optical|atomic) (lattice )?clocks?",
                 r"\bsquids?\b", r"rydberg (sensors?|receivers?)"],
    "communication": [r"quantum key distribution", r"\bqkd\b", r"euroqci", r"\bqci\b",
                      r"quantum (networks?|networking|internet|repeaters?|memor(y|ies)|communications?|"
                      r"cryptograph\w*|encryption|channels?|links?|teleportation|random number\w*|randomness)",
                      r"\bqrngs?\b", r"entanglement distribution", r"entangled photon pairs?"],
    "composants": [r"dilution (refrigerators?|fridges?|cryostats?|refrigeration)", r"cryogenic\w*", r"cryostats?",
                   r"cryo cmos", r"single photon (detectors?|sources?|emitters?|guns?)", r"\bsnspds?\b",
                   r"superconducting nanowires?", r"photonic integrated circuits?", r"\blasers?\b",
                   r"quantum (photonic\w*|light|emitters?|transducers?|transduction|frequency conversion)",
                   r"colou?r cent(er|re)s?", r"isotopically", r"control electronics", r"parametric amplifiers?",
                   r"vapou?r cells?", r"frequency combs?", r"\bwafers?\b", r"packaging"],
    "logiciel": [r"quantum (software|algorithms?|machine learning|neural networks?|programming|compilers?|programs?|"
                 r"cloud|optimi[sz]ation|error mitigation)", r"quantum simulations?", r"tensor networks?",
                 r"hybrid quantum classical", r"variational quantum"],
    "pqc": [r"post quantum", r"\bpqc\b", r"quantum (safe|resistant|proof|attacks?|threats?|adversar\w*)",
            r"lattice based cryptograph\w*", r"crypto ?agility"],
}
SEGMENTS_RE = {s: [re.compile(p) for p in ps] for s, ps in SEGMENTS.items()}


def segments_projet(texte):
    c = {}
    termes = collections.Counter()
    for s, rxs in SEGMENTS_RE.items():
        n = 0
        for rx in rxs:
            for m in rx.finditer(texte):
                n += 1
                termes[m.group(0)] += 1
        if n:
            c[s] = n
    return c, termes


def segment_org(projets):
    """projets : liste de (acronyme_ou_titre, dict segment->hits, Counter termes)."""
    poids = collections.Counter()
    termes = collections.Counter()
    for _, c, t in projets:
        tot = sum(c.values())
        if tot:
            for s, n in c.items():
                poids[s] += n / tot
        termes.update(t)
    if not poids:
        return "inconnu", "aucun mot-clé de segment dans les titres/résumés des projets retenus"
    tot = sum(poids.values())
    parts = sorted(((s, p / tot) for s, p in poids.items()), key=lambda x: -x[1])
    rep = ", ".join("%s %d %%" % (s, round(100 * p)) for s, p in parts)
    top_t = ", ".join("%s (%d)" % (k, v) for k, v in termes.most_common(6))
    if parts[0][1] >= 0.5:
        seg = parts[0][0]
    else:
        seg = "transverse"
    return seg, "mots-clés des projets : %s ; répartition : %s ; %d projet(s) quantique(s)" % (top_t, rep, len(projets))

# ---------------------------------------------------------------------------
# HTTP avec cache et limitation de débit
# ---------------------------------------------------------------------------
class Http:
    def __init__(self, delai, hors_ligne):
        self.delai = delai
        self.hors_ligne = hors_ligne
        self.dernier = 0.0
        self.n_req = 0
        self.echecs = []

    def get(self, url, chemin_cache, accept=None, binaire=False, essais=5):
        if os.path.exists(chemin_cache) and os.path.getsize(chemin_cache) > 0:
            with open(chemin_cache, "rb") as f:
                return f.read()
        if self.hors_ligne:
            return None
        os.makedirs(os.path.dirname(chemin_cache), exist_ok=True)
        attente = 5
        for i in range(essais):
            dt = time.time() - self.dernier
            if dt < self.delai:
                time.sleep(self.delai - dt)
            self.dernier = time.time()
            self.n_req += 1
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **({"Accept": accept} if accept else {})})
            try:
                with urllib.request.urlopen(req, timeout=180) as r:
                    data = r.read()
                tmp = chemin_cache + ".tmp"
                with open(tmp, "wb") as f:
                    f.write(data)
                os.replace(tmp, chemin_cache)
                return data
            except urllib.error.HTTPError as e:
                if e.code in (429, 500, 502, 503, 504) and i < essais - 1:
                    time.sleep(attente); attente *= 2
                    continue
                self.echecs.append((url, "HTTP %s" % e.code))
                return None
            except Exception as e:  # réseau
                if i < essais - 1:
                    time.sleep(attente); attente *= 2
                    continue
                self.echecs.append((url, repr(e)))
                return None
        return None

# ---------------------------------------------------------------------------
# CORDIS
# ---------------------------------------------------------------------------
PAYS_CORDIS = {"UK": "GB", "EL": "GR"}


def lire_csv_zip(zp, nom):
    with zipfile.ZipFile(zp) as z:
        with z.open(nom) as f:
            txt = io.TextIOWrapper(f, encoding="utf-8", newline="")
            return list(csv.DictReader(txt, delimiter=";"))


def montant(x):
    if not x:
        return 0.0
    try:
        return float(x.replace(",", "."))
    except ValueError:
        return 0.0


def programme_cordis(fp, p):
    fs, mc = p["fundingScheme"] or "", (p["masterCall"] or "") + " " + (p["topics"] or "")
    if fp == "he":
        if fs.startswith("HORIZON-EIC"):
            return "EIC"
        if re.search(r"EUROHPC", mc, re.I):
            return "EuroHPC"
        if re.search(r"KDT-JU|JU-CHIPS", mc, re.I):
            return "Chips JU"
        return "Horizon Europe"
    if mc.startswith("H2020-EIC"):
        return "EIC"
    if re.search(r"EuroHPC", mc, re.I):
        return "EuroHPC"
    return "H2020"


def charger_cordis(http, cache, journal):
    projets, orgs = {}, []
    for fp, url in CORDIS_DUMPS.items():
        zp = os.path.join(cache, "opendata", fp, os.path.basename(url))
        if not os.path.exists(zp):
            journal("téléchargement %s" % url)
            http.get(url, zp, binaire=True)
        if not os.path.exists(zp):
            raise SystemExit("dump CORDIS indisponible : %s" % url)
        with zipfile.ZipFile(zp) as z:
            date_dump = max(datetime.datetime(*i.date_time[:3]) for i in z.infolist()).strftime("%Y-%m-%d")
        for r in lire_csv_zip(zp, "project.csv"):
            r["_fp"], r["_sujets"], r["_dump"] = fp, [], date_dump
            projets[(fp, r["id"])] = r
        for r in lire_csv_zip(zp, "topics.csv"):
            k = (fp, r["projectID"])
            if k in projets:
                projets[k]["_sujets"].append(r["title"])
        for r in lire_csv_zip(zp, "organization.csv"):
            r["_fp"] = fp
            orgs.append(r)
        journal("CORDIS %s : dump du %s" % (fp, date_dump))
    return projets, orgs

# ---------------------------------------------------------------------------
# GtR
# ---------------------------------------------------------------------------

def gtr_json(http, cache, chemin, url):
    data = http.get(url, os.path.join(cache, "cache", "gtr", chemin), accept=GTR_ACCEPT)
    if not data:
        return None
    try:
        return json.loads(data)
    except ValueError:
        try:
            os.remove(os.path.join(cache, "cache", "gtr", chemin))
        except OSError:
            pass
        return None


def sans_personnes(p):
    """Retire les liens vers des personnes (données personnelles) avant tout traitement."""
    links = (p.get("links") or {}).get("link") or []
    p["links"] = {"link": [l for l in links if "/persons/" not in (l.get("href") or "")]}
    return p


def recolter_gtr(http, cache, journal):
    projets = {}
    for q in GTR_REQUETES:
        slug = re.sub(r"[^a-z0-9]+", "_", q.lower()).strip("_")
        page, total = 1, None
        while True:
            url = "%s/projects?%s" % (GTR_API, urllib.parse.urlencode({"q": q, "s": 100, "p": page}))
            d = gtr_json(http, cache, "search/%s_p%03d.json" % (slug, page), url)
            if d is None:
                journal("GtR : échec page %d de %r" % (page, q))
                break
            total = d.get("totalPages") or 0
            for p in d.get("project") or []:
                projets.setdefault(p["id"], sans_personnes(p))
            if page >= total:
                break
            page += 1
        journal("GtR %r : %s pages, cumul %d projets" % (q, total, len(projets)))
    return projets


CATEGORIES_INNOVATE_UK = re.compile(r"Collaborative R&D|Feasibility Studies|CR&D Bilateral|Small Business Research "
                                    r"Initiative|Fast Start|Responsive Strategy|Grant for R&D|Smart|Knowledge Transfer|"
                                    r"Investment Accelerator|Loans|Vouchers|GRD|Study", re.I)


def ms_date(ms):
    if ms is None:
        return None
    # Les dates GtR sont des minuits heure de Londres exprimés en UTC (23:00 ou 00:00Z).
    d = datetime.datetime.fromtimestamp(ms / 1000, tz=datetime.timezone.utc) + datetime.timedelta(hours=3)
    return d.strftime("%Y-%m-%d")


PAYS_NOMS = {
    "UNITED KINGDOM": "GB", "UK": "GB", "GREAT BRITAIN": "GB", "ENGLAND": "GB", "SCOTLAND": "GB", "WALES": "GB",
    "NORTHERN IRELAND": "GB", "IRELAND": "IE", "FRANCE": "FR", "GERMANY": "DE", "NETHERLANDS": "NL",
    "THE NETHERLANDS": "NL", "BELGIUM": "BE", "LUXEMBOURG": "LU", "SWITZERLAND": "CH", "AUSTRIA": "AT", "ITALY": "IT",
    "SPAIN": "ES", "PORTUGAL": "PT", "DENMARK": "DK", "SWEDEN": "SE", "NORWAY": "NO", "FINLAND": "FI", "ICELAND": "IS",
    "POLAND": "PL", "CZECH REPUBLIC": "CZ", "CZECHIA": "CZ", "SLOVAKIA": "SK", "HUNGARY": "HU", "SLOVENIA": "SI",
    "CROATIA": "HR", "ROMANIA": "RO", "BULGARIA": "BG", "GREECE": "GR", "CYPRUS": "CY", "MALTA": "MT", "ESTONIA": "EE",
    "LATVIA": "LV", "LITHUANIA": "LT", "SERBIA": "RS", "TURKEY": "TR", "TURKIYE": "TR", "UKRAINE": "UA", "ISRAEL": "IL",
    "UNITED STATES": "US", "UNITED STATES OF AMERICA": "US", "USA": "US", "CANADA": "CA", "AUSTRALIA": "AU",
    "NEW ZEALAND": "NZ", "JAPAN": "JP", "CHINA": "CN", "SOUTH KOREA": "KR", "KOREA, REPUBLIC OF": "KR",
    "KOREA REPUBLIC OF": "KR", "SINGAPORE": "SG", "INDIA": "IN", "TAIWAN": "TW", "HONG KONG": "HK", "BRAZIL": "BR",
    "SOUTH AFRICA": "ZA", "MEXICO": "MX", "CHILE": "CL", "ARGENTINA": "AR", "UNITED ARAB EMIRATES": "AE",
}


def pays_gtr(ad):
    """Pays d'une adresse GtR : champ country (nom anglais) sinon région britannique -> GB."""
    c = (ad.get("country") or "").strip()
    if c:
        if len(c) == 2 and c.isalpha():
            return {"UK": "GB", "EL": "GR"}.get(c.upper(), c.upper())
        return PAYS_NOMS.get(ascii_up(c))
    region = (ad.get("region") or "").strip()
    if region and region not in ("Outside UK", "Unknown"):
        return "GB"
    return None


def taux_bce(http, cache, hors_ligne):
    chemin = os.path.join(cache, "cache", "ecb", "GBP_EUR_derniers.csv")
    data = http.get(ECB_URL, chemin)
    if not data:
        raise SystemExit("taux BCE indisponible")
    rows = list(csv.DictReader(io.StringIO(data.decode("utf-8"))))
    rows = [r for r in rows if r.get("OBS_VALUE")]
    r = max(rows, key=lambda r: r["TIME_PERIOD"])
    return float(r["OBS_VALUE"]), r["TIME_PERIOD"]

# ---------------------------------------------------------------------------
# Typologie et normalisation des noms
# ---------------------------------------------------------------------------
SUFFIXES = r"(LTD|LIMITED|PLC|LLP|LLC|INC|CORP|CORPORATION|CO|COMPANY|GMBH|MBH|AG|SE|SAS|SASU|SARL|SA|SL|SLU|SRL|SPA|" \
           r"BV|NV|AB|OY|OYJ|AS|ASA|APS|A S|KG|UG|SP Z O O|SPOLKA|SRO|S R O|KFT|ZRT|DOO|D O O|AE|IKE|EOOD|OU|UAB|SIA|" \
           r"LDA|EURL|SCA|SCARL|SOCIETA|SOCIEDAD|LIMITADA|HAFTUNGSBESCHRANKT|UK|EUROPE|THE)"
RX_SUFFIXE = re.compile(r"\b%s\b" % SUFFIXES)
RX_SOCIETE = re.compile(r"\b(LTD|LIMITED|PLC|LLP|LLC|INC|GMBH|SAS|SARL|BV|B V|AB|OY|SRL|SPA|SL|NV|AG|SA|APS|ASA)\b")
RX_UNIV = re.compile(r"UNIVERSIT|\bCOLLEGE\b|SCHOOL OF|POLYTECHNIC|INSTITUTE OF TECHNOLOGY|\bUCL\b|ECOLE|HOCHSCHULE")
RX_RECH = re.compile(r"NATIONAL PHYSICAL LABORATORY|NPL MANAGEMENT|SCIENCE AND TECHNOLOGY FACILITIES|\bSTFC\b|"
                     r"RESEARCH COUNCIL|ATOMIC ENERGY AUTHORITY|\bUKAEA\b|NATIONAL QUANTUM COMPUTING CENTRE|"
                     r"DEFENCE SCIENCE AND TECHNOLOGY LAB|\bDSTL\b|MET OFFICE|BRITISH GEOLOGICAL SURVEY|"
                     r"RUTHERFORD APPLETON|DIAMOND LIGHT SOURCE|CATAPULT|FRAUNHOFER|\bINSTITUTE\b|LABORATOR|"
                     r"RESEARCH CENTRE|RESEARCH CENTER|\bTNO\b|\bCNRS\b|\bCEA\b|\bUKRI\b")
RX_AUTRE = re.compile(r"\bNHS\b|COUNCIL\b|\bTRUST\b|DEPARTMENT FOR|MINISTRY|\bGOVERNMENT\b|\bCHARIT|\bFOUNDATION\b|"
                      r"\bASSOCIATION\b|\bSOCIETY\b|ROYAL ACADEMY|NETWORK\b")


def ascii_up(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^A-Za-z0-9]+", " ", s).upper()
    return re.sub(r"\s+", " ", s).strip()


def nom_normalise(s):
    s = ascii_up(s)
    s = RX_SUFFIXE.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()


def type_gtr(nom):
    u = ascii_up(nom)
    if RX_UNIV.search(u):
        return "universite"
    if RX_RECH.search(u):
        return "recherche"
    if RX_SOCIETE.search(u):
        return "entreprise"
    if RX_AUTRE.search(u):
        return "autre"
    return "entreprise"


def type_cordis(activity, sme):
    if activity == "PRC":
        return "PME" if sme == "true" else ("grande_entreprise" if sme == "false" else None)
    if activity == "HES":
        return "universite"
    if activity == "REC":
        return "recherche"
    return "autre"  # PUB, OTH, vide


def url_site(u):
    u = (u or "").strip()
    if not u or " " in u or "." not in u or "@" in u:
        return None
    if not re.match(r"^https?://", u, re.I):
        u = "http://" + u.lstrip("/")
    return u

# ---------------------------------------------------------------------------
# Construction
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", default=CACHE_DEFAUT, help="répertoire de travail (dumps + cache des réponses)")
    ap.add_argument("--sortie", default=ICI)
    ap.add_argument("--delai", type=float, default=1.1, help="secondes minimales entre deux requêtes (>= 0.5)")
    ap.add_argument("--hors-ligne", action="store_true", help="n'utiliser que le cache")
    ap.add_argument("--sans-gtr", action="store_true", help="ignorer GtR")
    ap.add_argument("--date-extraction", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    if a.delai < 0.5:
        raise SystemExit("--delai doit être >= 0.5 s")
    http = Http(a.delai, a.hors_ligne)
    stats = collections.OrderedDict()
    def journal(m):
        print(m, file=sys.stderr, flush=True)

    # ---------------- CORDIS -----------------
    projets, orgs = charger_cordis(http, a.cache, journal)
    stats["cordis_projets_total"] = len(projets)
    pq = {}  # projets quantiques retenus : clé -> info
    n_fenetre = 0
    for k, p in projets.items():
        if p["endDate"] and p["endDate"] < DEBUT_FENETRE:
            continue
        n_fenetre += 1
        c = classer(p["title"], p["objective"], p["keywords"], p["_sujets"])
        if c["garder"]:
            seg, termes = segments_projet(c["texte"])
            pq[k] = {"source": "cordis", "fp": k[0], "id": p["id"], "titre": p["title"], "acronyme": p["acronym"] or None,
                     "debut": p["startDate"] or None, "fin": p["endDate"] or None, "programme": programme_cordis(k[0], p),
                     "schema": p["fundingScheme"], "regle": c["regle"], "score": c["score"], "termes": c["termes"],
                     "seg": seg, "seg_termes": termes, "url": "https://cordis.europa.eu/project/id/%s" % p["id"],
                     "resume": (p["objective"] or "")[:600], "dump": p["_dump"]}
    stats["cordis_projets_fenetre"] = n_fenetre
    stats["cordis_projets_quantiques"] = len(pq)

    # participations financées
    finances = collections.defaultdict(list)  # cle projet -> participations
    ignores = collections.Counter()
    for r in orgs:
        k = (r["_fp"], r["projectID"])
        if k not in pq:
            continue
        ec = montant(r["ecContribution"])
        if ec <= 0:
            ignores[r["role"] or "?"] += 1
            continue
        finances[k].append(r)
    stats["cordis_participations_non_financees_ignorees"] = dict(ignores)

    entites = {}  # id -> entité agrégée

    def entite(eid):
        return entites.setdefault(eid, {"id": eid, "noms": collections.Counter(), "pays": collections.Counter(),
                                        "villes": collections.Counter(), "sites": [], "types": [],
                                        "fin": [], "ids": set(), "type_src": set()})

    for k, parts in finances.items():
        info = pq[k]
        nfin = len(parts)
        for r in parts:
            pic = r["organisationID"]
            e = entite("cordis-%s" % pic)
            e["ids"].add("CORDIS PIC %s" % pic)
            d = info["debut"] or ""
            e["noms"][r["name"].strip()] += 1
            pays = PAYS_CORDIS.get(r["country"], r["country"]) or None
            if pays:
                e["pays"][pays] += 1
            if r["city"]:
                e["villes"][r["city"].strip()] += 1
            if url_site(r["organizationURL"]):
                e["sites"].append((d, url_site(r["organizationURL"])))
            e["types"].append((d, type_cordis(r["activityType"], r["SME"]), r["activityType"], r["SME"]))
            role = r["role"]
            if role == "coordinator":
                role_c = "beneficiaire_unique" if nfin == 1 else "coordinateur"
            else:
                role_c = "participant"
            e["fin"].append({"programme": info["programme"], "projet": info["titre"], "acronyme": info["acronyme"],
                             "id_projet": info["id"], "debut": info["debut"], "fin": info["fin"],
                             "contribution_eur": round(montant(r["ecContribution"]), 2), "role": role_c,
                             "source_url": info["url"], "_cle": ("cordis",) + k,
                             "financeur_source": "Commission européenne — %s (%s)" % (info["schema"], "CORDIS")})

    # ---------------- GtR -----------------
    taux, date_taux = None, None
    gq = {}
    if not a.sans_gtr:
        taux, date_taux = taux_bce(http, a.cache, a.hors_ligne)
        stats["taux_gbp_eur"] = {"gbp_pour_1_eur": taux, "date": date_taux, "source": ECB_URL}
        gp = recolter_gtr(http, a.cache, journal)
        stats["gtr_projets_recoltes"] = len(gp)
        n_fen = 0
        for pid, p in gp.items():
            links = p["links"]["link"]
            funds = [l for l in links if l.get("rel") == "FUND"]
            debut = min((ms_date(l.get("start")) for l in funds if l.get("start")), default=None)
            fin = max((ms_date(l.get("end")) for l in funds if l.get("end")), default=None)
            if fin and fin < DEBUT_FENETRE:
                continue
            n_fen += 1
            sujets = [t.get("text") for t in ((p.get("researchTopics") or {}).get("researchTopic") or [])]
            sujets += [t.get("text") for t in ((p.get("researchSubjects") or {}).get("researchSubject") or [])]
            resume = " ".join(x for x in (p.get("abstractText"), p.get("techAbstractText")) if x)
            c = classer(p.get("title"), resume, "", sujets)
            if not c["garder"]:
                continue
            ref = next((i["value"] for i in ((p.get("identifiers") or {}).get("identifier") or []) if i.get("type") == "RCUK"), None)
            seg, termes = segments_projet(c["texte"])
            lf = p.get("leadFunder") or ""
            gc = p.get("grantCategory") or ""
            # Innovate UK : financeur principal Innovate UK, ou catégories de subventions/contrats
            # d'entreprises gérées par Innovate UK (fonds ISCF, SPF, TMF...). Le reste (EPSRC, STFC,
            # Horizon Europe Guarantee, ISPF, FLF...) est classé « UKRI ».
            if lf == "Innovate UK" or (lf != "Horizon Europe Guarantee" and CATEGORIES_INNOVATE_UK.search(gc)):
                prog = "Innovate UK"
            else:
                prog = "UKRI"
            gq[pid] = {"source": "gtr", "id": ref or pid, "uuid": pid, "titre": p.get("title"), "acronyme": None,
                       "debut": debut, "fin": fin, "programme": prog, "schema": "%s / %s" % (lf, gc),
                       "regle": c["regle"], "score": c["score"], "termes": c["termes"], "seg": seg, "seg_termes": termes,
                       "url": "https://gtr.ukri.org/projects?ref=%s" % urllib.parse.quote(ref or pid),
                       "resume": (p.get("abstractText") or "")[:600], "p": p, "funds": funds}
        stats["gtr_projets_fenetre"] = n_fen
        stats["gtr_projets_quantiques"] = len(gq)

        # montants et organisations
        orgs_a_lire = set()
        for pid, info in gq.items():
            p = info["p"]
            pv = ((p.get("participantValues") or {}).get("participant")) or []
            parts = []
            if pv:
                for x in pv:
                    g = x.get("grantOffer") or 0
                    if g and g > 0:
                        parts.append((x.get("organisationId"), x.get("organisationName"), x.get("role"), g))
            else:
                lead = [l for l in p["links"]["link"] if l.get("rel") == "LEAD_ORG"]
                tot = 0.0
                for l in info["funds"]:
                    fid = l["href"].rstrip("/").split("/")[-1]
                    d = gtr_json(http, a.cache, "funds/%s.json" % fid, "%s/funds/%s" % (GTR_API, fid))
                    if d and (d.get("valuePounds") or {}).get("amount") is not None:
                        tot += float(d["valuePounds"]["amount"])
                if lead and tot > 0:
                    oid = lead[0]["href"].rstrip("/").split("/")[-1]
                    parts.append((oid, None, "LEAD_ORG", tot))
            info["parts"] = parts
            for oid, _, _, _ in parts:
                orgs_a_lire.add(oid)
        gorgs = {}
        for i, oid in enumerate(sorted(orgs_a_lire)):
            d = gtr_json(http, a.cache, "organisations/%s.json" % oid, "%s/organisations/%s" % (GTR_API, oid))
            if d:
                d.pop("links", None)
                gorgs[oid] = d
            if i % 200 == 0:
                journal("GtR organisations : %d/%d" % (i, len(orgs_a_lire)))
        stats["gtr_organisations_lues"] = len(gorgs)
        stats["gtr_organisations_manquantes"] = len(orgs_a_lire - set(gorgs))

        for pid, info in gq.items():
            nfin = len(info["parts"])
            for oid, oname, role, gbp in info["parts"]:
                od = gorgs.get(oid) or {}
                nom = (od.get("name") or oname or "").strip()
                if not nom:
                    continue
                e = entite("gtr-%s" % oid)
                e["ids"].add("GtR org %s" % oid)
                e["noms"][nom] += 1
                addr = ((od.get("addresses") or {}).get("address") or [])
                ad = next((x for x in addr if x.get("type") == "MAIN_ADDRESS"), addr[0] if addr else {})
                pays = pays_gtr(ad)
                if pays:
                    e["pays"][pays] += 1
                if ad.get("city"):
                    e["villes"][ad["city"].strip().title()] += 1
                if url_site(od.get("website")):
                    e["sites"].append((info["debut"] or "", url_site(od.get("website"))))
                e["types"].append((info["debut"] or "", None, "GTR", None))
                e["type_src"].add(type_gtr(nom))
                if role == "LEAD_PARTICIPANT":
                    role_c = "beneficiaire_unique" if nfin == 1 else "coordinateur"
                elif role == "LEAD_ORG":
                    role_c = "beneficiaire_unique"
                else:
                    role_c = "participant"
                pv = ((info["p"].get("participantValues") or {}).get("participant")) or []
                ratio = None
                for x in pv:
                    if x.get("organisationId") == oid and x.get("projectCost"):
                        ratio = (x.get("grantOffer") or 0) / x["projectCost"]
                e["fin"].append({"programme": info["programme"], "projet": info["titre"], "acronyme": None,
                                 "id_projet": info["id"], "debut": info["debut"], "fin": info["fin"],
                                 "contribution_eur": round(gbp / taux, 2), "role": role_c, "source_url": info["url"],
                                 "_cle": ("gtr", pid), "_gbp": gbp, "_ratio": ratio, "_categorie": info["schema"],
                                 "financeur_source": "UKRI — %s (GtR)" % info["schema"]})

    # ---------------- Typage des entités -----------------
    for e in entites.values():
        noms = e["noms"].most_common()
        e["nom"] = noms[0][0]
        tc = sorted([t for t in e["types"] if t[2] != "GTR"], key=lambda t: t[0])
        if tc:
            # type CORDIS : participation la plus récente avec un drapeau exploitable
            act = [t for t in tc if t[1]]
            last = act[-1] if act else tc[-1]
            t = last[1]
            if t is None:  # PRC sans drapeau SME
                t, src = "grande_entreprise", "CORDIS activityType=PRC, drapeau SME absent (classé grande_entreprise par défaut)"
            else:
                src = "CORDIS activityType=%s, SME=%s (participation la plus récente)" % (last[2], last[3])
            # activityType vide dans la source : forme sociale commerciale -> entreprise (drapeau SME)
            if last[2] == "" and RX_SOCIETE.search(ascii_up(e["nom"])) and not RX_UNIV.search(ascii_up(e["nom"])):
                t = "PME" if last[3] == "true" else "grande_entreprise"
                src = "CORDIS activityType vide, forme sociale commerciale dans le nom, SME=%s" % (last[3] or "absent")
            # entreprise de recherche privée déclarée REC + SME
            if last[2] in ("REC", "OTH") and last[3] == "true" and RX_SOCIETE.search(ascii_up(e["nom"])) \
                    and not RX_UNIV.search(ascii_up(e["nom"])) and not re.search(r"FRAUNHOFER|STIFTUNG|FOUNDATION|ASSOCIA|VEREIN|FUNDA", ascii_up(e["nom"])):
                t, src = "PME", "CORDIS activityType=%s mais drapeau SME=true et forme sociale commerciale dans le nom" % last[2]
            e["type_org"], e["type_src"] = t, src
        else:
            tg = next(iter(e["type_src"]))
            if tg == "entreprise":
                ratios = [f["_ratio"] for f in e["fin"] if f.get("_ratio") is not None and
                          re.search(r"Collaborative R&D|Feasibility|CR&D Bilateral|Smart|Grant for R&D", f["_categorie"])]
                if any(r > 0.55 for r in ratios):
                    e["type_org"] = "PME"
                    e["type_src"] = "inféré : taux d'aide Innovate UK > 55 % sur au moins une subvention (plafond 50 % pour une grande entreprise)"
                else:
                    e["type_org"] = "PME"
                    e["type_src"] = "taille non publiée par GtR : classé PME par défaut, à vérifier"
            else:
                e["type_org"], e["type_src"] = tg, "GtR : type déduit du nom de l'organisation"

    # ---------------- Fusion CORDIS <-> GtR (nom normalisé + pays, exact) -----------------
    def cle_fusion(e):
        pays = e["pays"].most_common(1)[0][0] if e["pays"] else None
        return (nom_normalise(e["nom"]), pays)
    index = collections.defaultdict(list)
    for eid, e in entites.items():
        index[cle_fusion(e)].append(eid)
    fusions = 0
    for (nn, pays), eids in index.items():
        if len(eids) < 2 or not nn or not pays:
            continue
        gtrs = [x for x in eids if x.startswith("gtr-")]
        cords = [x for x in eids if x.startswith("cordis-")]
        if not gtrs:
            continue  # on ne fusionne pas deux PIC CORDIS distincts
        cible = cords[0] if len(cords) == 1 else (None if cords else gtrs[0])
        if cible is None:
            continue  # ambigu : plusieurs PIC CORDIS pour le même nom
        for x in eids:
            if x == cible or x.startswith("cordis-"):
                continue
            src, dst = entites.pop(x), entites[cible]
            dst["noms"].update(src["noms"]); dst["pays"].update(src["pays"]); dst["villes"].update(src["villes"])
            dst["sites"] += src["sites"]; dst["fin"] += src["fin"]; dst["ids"] |= src["ids"]
            if cible.startswith("gtr-") and dst["type_org"] == "PME" and "défaut" in dst["type_src"] and "inféré" in src["type_src"]:
                dst["type_src"] = src["type_src"]
            fusions += 1
    stats["fusions_nom_pays"] = fusions

    # ---------------- Écriture -----------------
    date_x = a.date_extraction
    sorties = {"prospects": [], "recherche": []}
    for eid, e in entites.items():
        fins = sorted(e["fin"], key=lambda f: (f["debut"] or "", f["id_projet"]))
        # dédoublonnage : une même entité listée plusieurs fois dans un même projet (ex. participant
        # + tiers lié) -> une seule ligne, montants additionnés, rôle le plus élevé conservé.
        rang = {"coordinateur": 0, "beneficiaire_unique": 1, "participant": 2}
        vus = collections.OrderedDict()
        for f in fins:
            prev = vus.get(f["_cle"])
            if prev is None:
                vus[f["_cle"]] = dict(f)
                continue
            prev["contribution_eur"] = round(prev["contribution_eur"] + f["contribution_eur"], 2)
            if rang[f["role"]] < rang[prev["role"]]:
                prev["role"] = f["role"]
        fins = list(vus.values())
        total = round(sum(f["contribution_eur"] for f in fins), 2)
        fins_pub = [{k: v for k, v in f.items() if not k.startswith("_")} for f in fins]
        dates = [f["fin"] or f["debut"] for f in fins if (f["fin"] or f["debut"])]
        segp = []
        for f in fins:
            info = pq.get(f["_cle"][1:]) if f["_cle"][0] == "cordis" else gq.get(f["_cle"][1])
            if info:
                segp.append((info["acronyme"] or info["titre"], info["seg"], info["seg_termes"]))
        seg, just = segment_org(segp)
        site = sorted(e["sites"])[-1][1] if e["sites"] else None
        sources = sorted(set(f["source_url"] for f in fins))
        pays = e["pays"].most_common(1)[0][0] if e["pays"] else None
        ville = e["villes"].most_common(1)[0][0] if e["villes"] else None
        notes = ["Type : %s." % e["type_src"]]
        if any(f["_cle"][0] == "gtr" for f in fins):
            notes.append("Montants GtR convertis de GBP en EUR au taux de référence BCE du %s : 1 EUR = %s GBP "
                         "(montant EUR = montant GBP / %s)." % (date_taux, taux, taux))
        if any(f["_cle"][0] == "cordis" for f in fins):
            notes.append("Montants CORDIS = ecContribution par organisation (dumps open data CORDIS du %s)."
                         % ", ".join(sorted(set(pq[f["_cle"][1:]]["dump"] for f in fins if f["_cle"][0] == "cordis"))))
        if len(e["noms"]) > 1:
            notes.append("Autres libellés : %s." % "; ".join(n for n, _ in e["noms"].most_common()[1:4]))
        rec = collections.OrderedDict([
            ("id", eid), ("nom", e["nom"]), ("pays", pays), ("ville", ville), ("site_web", site),
            ("type_org", e["type_org"]), ("segment", seg), ("segment_justification", just),
            ("financements_obtenus", fins_pub), ("total_obtenu_eur", total), ("nb_projets", len(fins_pub)),
            ("derniere_activite", max(dates) if dates else None), ("sources", sources),
            ("date_extraction", date_x), ("a_coordonne", any(f["role"] in ("coordinateur", "beneficiaire_unique") for f in fins_pub)),
            ("identifiants_sources", sorted(e["ids"])), ("note", " ".join(notes)),
        ])
        if e["type_org"] in ("PME", "grande_entreprise"):
            sorties["prospects"].append(rec)
        else:
            sorties["recherche"].append(rec)
    for k in sorties:
        sorties[k].sort(key=lambda r: (-r["total_obtenu_eur"], r["nom"]))
    with open(os.path.join(a.sortie, "prospects.jsonl"), "w", encoding="utf-8") as f:
        for r in sorties["prospects"]:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(os.path.join(a.sortie, "prospects_recherche.jsonl"), "w", encoding="utf-8") as f:
        for r in sorties["recherche"]:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(os.path.join(a.sortie, "prospects.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["nom", "pays", "ville", "type_org", "segment", "nb_projets", "total_obtenu_eur", "derniere_activite",
                    "a_coordonne", "programmes", "site_web", "lien_source_principal"])
        for r in sorties["prospects"]:
            fins = r["financements_obtenus"]
            princ = max(fins, key=lambda x: x["contribution_eur"])["source_url"] if fins else None
            progs = " | ".join(sorted(set(x["programme"] for x in fins)))
            w.writerow([r["nom"], r["pays"], r["ville"], r["type_org"], r["segment"], r["nb_projets"],
                        "%.2f" % r["total_obtenu_eur"], r["derniere_activite"], "oui" if r["a_coordonne"] else "non",
                        progs, r["site_web"] or "", princ])

    # ---------------- Échantillons pour la mesure de précision -----------------
    tous = [("cordis",) + k for k in pq] + [("gtr", k) for k in gq]
    avec_entreprise = set()
    for r in sorties["prospects"]:
        for f in r["financements_obtenus"]:
            avec_entreprise.add(f["source_url"])
    rnd = random.Random(20261122)
    ech = rnd.sample(sorted(tous), 30)
    rnd2 = random.Random(20261123)
    tous_e = sorted(k for k in tous if (pq.get(k[1:]) if k[0] == "cordis" else gq.get(k[1]))["url"] in avec_entreprise)
    ech2 = rnd2.sample(tous_e, min(30, len(tous_e)))
    chemin_ech = os.path.join(a.cache, "echantillon_precision_a_verifier.csv")
    with open(chemin_ech, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["echantillon", "source", "id_projet", "programme", "regle", "titre", "url", "termes", "resume_debut"])
        for nom_e, liste in (("A_tous_projets", ech), ("B_projets_avec_entreprise", ech2)):
            for k in liste:
                info = pq[k[1:]] if k[0] == "cordis" else gq[k[1]]
                w.writerow([nom_e, info["source"], info["id"], info["programme"], info["regle"], info["titre"],
                            info["url"], "; ".join(info["termes"][:8]), info["resume"].replace("\n", " ")])

    # ---------------- Statistiques -----------------
    def compte(lst, f):
        return dict(collections.Counter(f(r) for r in lst).most_common())
    P, R = sorties["prospects"], sorties["recherche"]
    stats["prospects"] = len(P)
    stats["recherche"] = len(R)
    stats["prospects_par_pays"] = compte(P, lambda r: r["pays"])
    stats["prospects_par_segment"] = compte(P, lambda r: r["segment"])
    stats["prospects_par_type"] = compte(P, lambda r: r["type_org"])
    stats["recherche_par_type"] = compte(R, lambda r: r["type_org"])
    stats["recherche_par_pays_top15"] = dict(list(compte(R, lambda r: r["pays"]).items())[:15])
    progc = collections.Counter()
    for r in P:
        for pr in set(f["programme"] for f in r["financements_obtenus"]):
            progc[pr] += 1
    stats["prospects_par_programme_nb_entreprises"] = dict(progc.most_common())
    progm = collections.Counter()
    for r in P:
        for f in r["financements_obtenus"]:
            progm[f["programme"]] += f["contribution_eur"]
    stats["prospects_montant_par_programme_eur"] = {k: round(v) for k, v in progm.most_common()}
    stats["prospects_total_eur"] = round(sum(r["total_obtenu_eur"] for r in P))
    stats["prospects_ayant_coordonne_ou_seul_beneficiaire"] = sum(1 for r in P if r["a_coordonne"])
    stats["prospects_ayant_coordonne_projet_collaboratif"] = sum(
        1 for r in P if any(f["role"] == "coordinateur" for f in r["financements_obtenus"]))
    stats["prospects_beneficiaire_unique"] = sum(
        1 for r in P if any(f["role"] == "beneficiaire_unique" for f in r["financements_obtenus"]))
    stats["prospects_avec_site_web"] = sum(1 for r in P if r["site_web"])
    stats["prospects_multi_sources"] = sum(1 for r in P if len(set(i.split()[0] for i in r["identifiants_sources"])) > 1)
    stats["prospects_type_par_defaut"] = sum(1 for r in P if "défaut" in r["note"])
    stats["projets_cordis_par_programme"] = compte(list(pq.values()), lambda i: i["programme"])
    stats["projets_gtr_par_programme"] = compte(list(gq.values()), lambda i: i["programme"])
    stats["projets_gtr_par_financeur"] = compte(list(gq.values()), lambda i: i["schema"].split(" / ")[0])
    stats["top30"] = [(r["nom"], r["pays"], r["type_org"], r["segment"], r["nb_projets"], r["total_obtenu_eur"],
                       r["a_coordonne"]) for r in P[:30]]
    stats["http_requetes"] = http.n_req
    stats["http_echecs"] = http.echecs[:50]
    stats["http_echecs_nb"] = len(http.echecs)
    with open(os.path.join(a.cache, "statistiques_prospects.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in stats.items() if k not in ("top30", "http_echecs")}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
