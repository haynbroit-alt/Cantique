"""Valide regles.json contre SCHEMA.md. Usage : python3 valider_regles.py SCHEMA.md regles.json"""
import json
import re
import sys

schema_path, rules_path = sys.argv[1], sys.argv[2]
schema = open(schema_path, encoding="utf-8").read()

# Family IDs: first backticked cell of each row in the "Familles cryptographiques" table.
section = schema.split("## Familles cryptographiques", 1)[1].split("\n## ", 1)[0]
families = set(re.findall(r"^\| `([^`]+)` \|", section, flags=re.M))
assert len(families) == 23, f"expected 23 families in SCHEMA.md, found {len(families)}"

doc = json.load(open(rules_path, encoding="utf-8"))  # raises if invalid JSON

errors = []
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
NATURES = {"contraignant", "contraignant_indirect", "recommandation", "projet"}
EFFETS = {"deprecie", "interdit", "inventaire_obligatoire", "migration_requise", "recommande", "autre"}
CONF = {"elevee", "moyenne", "faible"}

if not DATE.match(str(doc.get("version", ""))):
    errors.append(f"version is {doc.get('version')!r}")
for k in ("avertissement_fr", "disclaimer_en", "referentiels"):
    if not doc.get(k):
        errors.append(f"missing top-level key {k}")

ref_keys = ["id", "nom", "juridiction", "emetteur", "nature", "public_vise_fr",
            "target_audience_en", "source_url", "date_source", "exigences"]
ex_keys = ["id", "resume_fr", "summary_en", "echeance", "familles", "effet", "source_url", "confiance"]
seen = set()
n_ex = 0
for r in doc["referentiels"]:
    rid = r.get("id")
    for k in ref_keys:
        if k not in r:
            errors.append(f"{rid}: missing {k}")
    if set(r) - set(ref_keys):
        errors.append(f"{rid}: unexpected keys {set(r) - set(ref_keys)}")
    if r.get("nature") not in NATURES:
        errors.append(f"{rid}: bad nature {r.get('nature')}")
    if not str(r.get("source_url", "")).startswith("https://"):
        errors.append(f"{rid}: bad source_url")
    if not DATE.match(str(r.get("date_source"))):
        errors.append(f"{rid}: bad date_source")
    if rid in seen:
        errors.append(f"duplicate id {rid}")
    seen.add(rid)
    if not r.get("exigences"):
        errors.append(f"{rid}: no exigences")
    for e in r.get("exigences", []):
        n_ex += 1
        eid = e.get("id")
        for k in ex_keys:
            if k not in e:
                errors.append(f"{eid}: missing {k}")
        if set(e) - set(ex_keys):
            errors.append(f"{eid}: unexpected keys {set(e) - set(ex_keys)}")
        if eid in seen:
            errors.append(f"duplicate id {eid}")
        seen.add(eid)
        fams = e.get("familles") or []
        if not fams:
            errors.append(f"{eid}: empty familles")
        bad = [f for f in fams if f not in families]
        if bad:
            errors.append(f"{eid}: unknown families {bad}")
        if len(set(fams)) != len(fams):
            errors.append(f"{eid}: duplicate families")
        if not str(e.get("source_url", "")).startswith("https://"):
            errors.append(f"{eid}: missing or non-https source_url")
        if e.get("effet") not in EFFETS:
            errors.append(f"{eid}: bad effet {e.get('effet')}")
        if e.get("confiance") not in CONF:
            errors.append(f"{eid}: bad confiance {e.get('confiance')}")
        ech = e.get("echeance")
        if ech is not None and not DATE.match(str(ech)):
            errors.append(f"{eid}: bad echeance {ech}")
        if e.get("confiance") == "faible" and "non vérifié" not in e.get("resume_fr", "").lower():
            errors.append(f"{eid}: faible but resume_fr does not say 'non vérifié'")
        if e.get("confiance") == "faible" and "not verified" not in e.get("summary_en", "").lower():
            errors.append(f"{eid}: faible but summary_en does not say 'not verified'")
        if not e.get("resume_fr") or not e.get("summary_en"):
            errors.append(f"{eid}: empty summary")

# Schema rule: a whole-inventory requirement (PCI DSS 12.3.3) lists TLS_SUITE and all concerned families.
pci = [e for r in doc["referentiels"] for e in r["exigences"] if e["id"].startswith("PCI-DSS-12.3.3")]
if not pci or "TLS_SUITE" not in pci[0]["familles"] or set(pci[0]["familles"]) != families:
    errors.append("PCI 12.3.3 must list TLS_SUITE and every family")

print(f"families in SCHEMA.md: {len(families)}; referentiels: {len(doc['referentiels'])}; exigences: {n_ex}")
conf = {}
for r in doc["referentiels"]:
    for e in r["exigences"]:
        conf[e["confiance"]] = conf.get(e["confiance"], 0) + 1
print("confiance:", conf)
if errors:
    print("ERRORS:")
    for x in errors:
        print(" -", x)
    sys.exit(1)
print("OK: valid JSON, all family IDs in SCHEMA.md list, every exigence has an https source_url")
