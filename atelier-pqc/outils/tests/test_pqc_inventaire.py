"""Tests de la v0 : scanner, extraction de paramètres, masquage, contexte, CBOM, rapport."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pqc_inventaire import pem  # noqa: E402
from pqc_inventaire.cbom import construire_cbom, valider_cbom  # noqa: E402
from pqc_inventaire.cli import main  # noqa: E402
from pqc_inventaire.familles import FAMILLES, resoudre  # noqa: E402
from pqc_inventaire.rapport import generer_rapport  # noqa: E402
from pqc_inventaire.scanner import charger_constats, classer_contexte, scanner  # noqa: E402

FIXTURES = Path(__file__).parent / "fixtures"
CODE = FIXTURES / "code"
REGLES = FIXTURES / "regles_fixture.json"
CHAMPS = {"famille", "classe", "detail", "fichier", "ligne", "extrait", "langage", "regle", "confiance", "contexte"}


@pytest.fixture(scope="module")
def doc():
    return scanner(CODE)


def trouver(doc, fichier, famille, ligne=None):
    return [c for c in doc["constats"] if c["fichier"] == fichier and c["famille"] == famille
            and (ligne is None or c["ligne"] == ligne)]


def test_format_du_contrat(doc):
    assert doc["constats"]
    for c in doc["constats"]:
        assert CHAMPS <= set(c)
        assert c["famille"] in FAMILLES and c["classe"] == FAMILLES[c["famille"]]
        assert c["confiance"] in ("elevee", "moyenne", "faible")
        assert c["contexte"] in ("production", "test", "exemple", "documentation")


@pytest.mark.parametrize("fichier,famille,ligne,algorithme", [
    ("python/app.py", "RSA", 13, "RSA-3072"),          # taille via constante de module
    ("python/app.py", "ECDSA", 14, "EC-P-384"),        # courbe via ec.SECP384R1()
    ("python/app.py", "MD5", 21, "MD5"),
    ("python/app.py", "RSA", 25, "RS256"),             # PyJWT
    ("python/app.py", "TLS_LEGACY", 30, "TLS 1.1"),    # ssl.TLSVersion
    ("java/Crypto.java", "RSA", 8, "RSA-2048"),        # initialize(2048) ligne suivante
    ("java/Crypto.java", "ECDSA", 12, "EC-P-256"),     # ECGenParameterSpec
    ("java/Crypto.java", "SHA1", 11, "SHA-1"),
    ("java/Crypto.java", "3DES", 14, "3DES"),          # Bouncy Castle
    ("go/main.go", "RSA", 14, "RSA-4096"),
    ("go/main.go", "ECDSA", 15, "ECDSA-P-256"),
    ("go/main.go", "ML-KEM", 16, "ML-KEM-768"),
    ("go/main.go", "HYBRID_KEM", 20, "X25519MLKEM768"),
    ("go/main.go", "TLS_LEGACY", 19, "TLS 1.0"),
    ("js/app.js", "RSA", 4, "RSA-2048"),               # modulusLength ligne suivante
    ("js/app.js", "3DES", 8, "3DES"),
    ("js/app.js", "ECDSA", 9, "ES256"),                # jsonwebtoken
    ("c/legacy.c", "RSA", 6, "RSA-1024"),
    ("c/legacy.c", "ECDSA", 9, "EC-P-256"),
    ("c/legacy.c", "MD5", 8, "MD5"),
    ("config/nginx.conf", "HYBRID_KEM", 5, "X25519MLKEM768"),
    ("pem/serveur.crt", "RSA", 1, "RSA-2048"),         # certificat X.509
])
def test_vrais_positifs_et_parametres(doc, fichier, famille, ligne, algorithme):
    trouves = trouver(doc, fichier, famille, ligne)
    assert trouves, f"{famille} attendu en {fichier}:{ligne}"
    assert algorithme in {c["parametres"]["algorithme"] for c in trouves}


def test_pas_de_faux_positifs_evidents(doc):
    # docstring, commentaire Python, « RSA » dans un texte, identifiants contenant « rsa »
    assert not trouver(doc, "python/app.py", "RSA", 12)
    assert not trouver(doc, "python/app.py", "RSA", 16)
    assert not trouver(doc, "python/app.py", "RSA", 34)
    assert not trouver(doc, "js/app.js", "RSA", 10)
    assert not trouver(doc, "java/Crypto.java", "RSA", 15)
    # la ligne commentée « # ssl_protocols SSLv3; » d'une configuration est ignorée
    assert not [c for c in doc["constats"] if c["fichier"] == "config/nginx.conf" and c["ligne"] == 6]
    # « !RC4 » est une exclusion, pas une activation
    assert not trouver(doc, "config/nginx.conf", "RC4")
    # TLS 1.0 et 1.1 sur la même ligne restent deux constats distincts
    assert len(trouver(doc, "config/nginx.conf", "TLS_LEGACY", 3)) == 2


def test_contexte(doc):
    assert classer_contexte("src/app.py") == "production"
    assert classer_contexte("tests/test_x.py") == "test"
    assert classer_contexte("pkg/handler_test.go") == "test"
    assert classer_contexte("src/test/java/FooTest.java") == "test"
    assert classer_contexte("web/app.spec.ts") == "test"
    assert classer_contexte("examples/demo.py") == "exemple"
    assert classer_contexte("docs/guide/conf.py") == "documentation"
    assert trouver(doc, "tests/test_crypto.py", "MD5")[0]["contexte"] == "test"
    assert trouver(doc, "examples/demo.py", "DES")[0]["contexte"] == "exemple"


def test_resolution_noms():
    assert resoudre("SHA1withRSA")[1].famille == "SHA1"
    assert resoudre("AES_256/GCM/NoPadding")[0].nom == "AES-256-GCM"
    assert resoudre("aesthetic") == [] and resoudre("rsa_key") == []
    assert resoudre("Kyber768")[0].famille == "ML-KEM"


def _cle_rsa_pem(chemin: Path, chiffree: bool = False) -> str:
    serialization = pytest.importorskip("cryptography.hazmat.primitives.serialization")
    from cryptography.hazmat.primitives.asymmetric import rsa
    k = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    chiffrement = serialization.BestAvailableEncryption(b"x") if chiffree else serialization.NoEncryption()
    texte = k.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.TraditionalOpenSSL,
                            chiffrement).decode()
    chemin.write_text("# cle de test generee par les tests\nCLE = '''\n" + texte + "'''\n")
    return texte


def test_cle_privee_masquee(tmp_path):
    texte = _cle_rsa_pem(tmp_path / "config.py")
    corps = [li for li in texte.splitlines() if li and not li.startswith("-----")]
    d = scanner(tmp_path)
    sortie = json.dumps(d)
    assert all(li not in sortie for li in corps), "le contenu de la clé privée ne doit jamais apparaître"
    (c,) = [c for c in d["constats"] if c["regle"] == "pem-cle-privee"]
    assert c["famille"] == "RSA" and c["parametres"]["taille_cle"] == 2048
    assert c["extrait"] == "-----BEGIN RSA PRIVATE KEY----- [contenu masqué]"
    assert "cle_privee" in c["parametres"]["notes"]


def test_cle_chiffree_a_verifier(tmp_path):
    _cle_rsa_pem(tmp_path / "k.pem", chiffree=True)
    d = scanner(tmp_path)
    # PEM « Proc-Type: ENCRYPTED » : l'en-tête suffit à établir RSA, la taille reste inconnue
    (c,) = d["constats"]
    assert c["famille"] == "RSA" and "taille_cle" not in c["parametres"]


def test_masquage_generique():
    assert "[masqué]" in pem.masquer('key = "' + "A" * 50 + '"')
    assert "[masqué]" in pem.masquer("secret = 0x" + "ab" * 20)


def test_certificat_sans_cryptography():
    der = __import__("base64").b64decode("".join(
        (CODE / "pem/serveur.crt").read_text().splitlines()[1:-1]))
    infos = pem.analyser_certificat(der, utiliser_cryptography=False)
    assert infos["analyseur"] == "der-stdlib"
    assert infos["cle"].famille == "RSA" and infos["cle"].taille == 2048
    assert infos["signature"] == "SHA256withRSA" and infos["not_after"].startswith("2027-01-01")


def test_certificat_illisible_a_verifier(tmp_path):
    (tmp_path / "x.pem").write_text("-----BEGIN CERTIFICATE-----\nAAAA\n-----END CERTIFICATE-----\n")
    d = scanner(tmp_path)
    assert not d["constats"]
    assert d["a_verifier"][0]["famille"] is None and d["a_verifier"][0]["confiance"] == "faible"


def test_dossiers_vendor(tmp_path):
    (tmp_path / "node_modules").mkdir()
    (tmp_path / "node_modules" / "x.js").write_text("crypto.createHash('md5')\n")
    assert not scanner(tmp_path)["constats"]
    assert scanner(tmp_path, inclure_vendor=True)["constats"]


def test_sortie_deterministe(doc):
    assert json.dumps(scanner(CODE)) == json.dumps(doc)


def test_cbom(doc):
    cbom = construire_cbom(doc["constats"], doc["a_verifier"], nom="fixtures", horodatage="2026-11-22T00:00:00Z")
    assert cbom["specVersion"] == "1.6"
    refs = {c["bom-ref"]: c for c in cbom["components"]}
    rsa = refs["crypto/algorithm/rsa-2048"]
    props = rsa["cryptoProperties"]["algorithmProperties"]
    assert props["nistQuantumSecurityLevel"] == 0 and props["parameterSetIdentifier"] == "2048"
    assert {o["location"] for o in rsa["evidence"]["occurrences"]} >= {"java/Crypto.java", "js/app.js"}
    assert refs["crypto/algorithm/ml-kem-768"]["cryptoProperties"]["algorithmProperties"]["nistQuantumSecurityLevel"] == 3
    assert any(c["cryptoProperties"]["assetType"] == "certificate" for c in cbom["components"])
    assert any(c["cryptoProperties"]["assetType"] == "protocol" for c in cbom["components"])
    assert construire_cbom(doc["constats"], doc["a_verifier"], horodatage="x")["serialNumber"] == \
        construire_cbom(doc["constats"], doc["a_verifier"], horodatage="y")["serialNumber"]


def test_cbom_valide_schema(doc):
    cbom = construire_cbom(doc["constats"], doc["a_verifier"], nom="fixtures", horodatage="2026-11-22T00:00:00Z")
    erreurs = valider_cbom(cbom)
    if erreurs is None:
        pytest.skip("cyclonedx-python-lib non installé")
    assert erreurs == []
    cbom["components"][0]["cryptoProperties"]["assetType"] = "pas-un-type"
    assert valider_cbom(cbom), "le validateur doit rejeter un document invalide"


def _rapport(doc, **kw):
    regles = json.loads(REGLES.read_text(encoding="utf-8"))
    d = dict(doc, _source="constats.json")
    return generer_rapport([d], doc["constats"], doc["a_verifier"], regles, "Client Test", date="2026-11-22",
                           regles_chemin="regles_fixture.json", **kw)


def test_rapport_fr(doc):
    r = _rapport(doc)
    for titre in ("## 1. Synthèse", "## 2. Inventaire", "## 3. Correspondance réglementaire",
                  "## 4. Feuille de route", "## 5. Limites de l'analyse", "## 6. Liste de contrôle du relecteur"):
        assert titre in r
    assert "<https://exemple.invalid/test-pq#2030>" in r and "<https://exemple.invalid/test-inv#1>" in r
    assert "| AES | Aucune exigence du référentiel ne vise cette famille. |" in r
    assert "Exigence fictive : interdiction en 2035." in r
    assert "Atelier PQC" in r
    assert "TEST-PQ-DEPRECIATION-2030" in r.split("### Horizon 2")[1].split("### Horizon 3")[0]
    assert "TEST-PQ-INTERDICTION-2035" in r.split("### Horizon 3")[1]


def test_rapport_marque_blanche_en(doc):
    r = _rapport(doc, langue="en", marque="Partenaire SAS")
    assert "| Prepared by | Partenaire SAS |" in r
    assert "atelier" not in r.lower() and "pqc-inventaire" not in r
    assert "## 5. Limits of the analysis" in r and "Fictitious requirement: disallowed in 2035." in r
    assert "Synthèse" not in r


def test_cli_bout_en_bout(tmp_path):
    constats, cbom, rapport = tmp_path / "c.json", tmp_path / "cbom.json", tmp_path / "r.md"
    assert main(["scan-code", str(CODE), "-o", str(constats)]) == 0
    assert main(["cbom", str(constats), "-o", str(cbom), "--date", "2026-11-22T00:00:00Z"]) == 0
    assert main(["rapport", str(constats), "--regles", str(REGLES), "--client", "X", "--date", "2026-11-22",
                 "-o", str(rapport)]) == 0
    docs, c, _ = charger_constats([str(constats)])
    assert c and json.loads(cbom.read_text())["bomFormat"] == "CycloneDX"
    assert rapport.read_text().startswith("# Préparation post-quantique")
