import datetime as dt
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent))

import rapprocher  # noqa: E402

AUJOURDHUI = dt.date(2026, 11, 22)
GROUPES = {"UE27": ["FR", "DE", "NL"], "HE_ASSOCIES": ["GB", "CH"]}


def prospect(**kw):
    base = {
        "id": "cordis-1",
        "nom": "Capteurs Quantiques SAS",
        "pays": "FR",
        "type_org": "PME",
        "segment": "capteurs",
        "segment_justification": "magnetometer NV centre",
        "financements_obtenus": [
            {"programme": "Horizon Europe", "projet": "Diamond magnetometer for medical imaging",
             "acronyme": "DIAMAG", "role": "coordinateur", "contribution_eur": 800000,
             "debut": "2023-01-01", "source_url": "https://cordis.europa.eu/project/id/1"},
            {"programme": "EIC", "projet": "Portable NV sensor", "acronyme": "PNV",
             "role": "participant", "contribution_eur": 200000, "debut": "2024-05-01",
             "source_url": "https://cordis.europa.eu/project/id/2"},
        ],
        "total_obtenu_eur": 1000000,
        "nb_projets": 2,
        "sources": ["https://cordis.europa.eu/project/id/1"],
    }
    base.update(kw)
    return base


def opportunite(**kw):
    base = {
        "id": "opp-1",
        "financeur": "European Commission",
        "programme": "Horizon Europe",
        "intitule": "Quantum sensing for health: magnetometer pilots",
        "statut": "ouvert",
        "cloture": "2027-01-28",
        "pays_eligibles": ["UE27", "HE_ASSOCIES"],
        "types_eligibles": ["PME", "grande_entreprise"],
        "consortium_requis": True,
        "taille_min_consortium": 3,
        "segments": ["capteurs"],
        "mots_cles": ["magnetometer", "medical imaging"],
        "url": "https://ec.europa.eu/topic/1",
        "confiance": "elevee",
    }
    base.update(kw)
    return base


class TestEvaluer(unittest.TestCase):
    def test_bonne_piste(self):
        piste = rapprocher.evaluer(prospect(), opportunite(), GROUPES, AUJOURDHUI)
        self.assertIsNotNone(piste)
        self.assertGreaterEqual(piste["score"], 70)
        self.assertTrue(any("segment" in r for r in piste["raisons"]))
        self.assertTrue(any("coordonné" in r for r in piste["raisons"]))
        self.assertTrue(any("consortium" in r for r in piste["reserves"]))
        self.assertEqual(piste["jours_avant_cloture"], 67)

    def test_pays_non_eligible(self):
        self.assertIsNone(rapprocher.evaluer(prospect(pays="US"), opportunite(), GROUPES, AUJOURDHUI))

    def test_groupe_associe(self):
        self.assertIsNotNone(rapprocher.evaluer(prospect(pays="GB"), opportunite(), GROUPES, AUJOURDHUI))

    def test_groupe_inconnu_donne_reserve(self):
        piste = rapprocher.evaluer(prospect(), opportunite(pays_eligibles=["GROUPE_X"]), GROUPES, AUJOURDHUI)
        self.assertIsNotNone(piste)
        self.assertTrue(any("pays éligibles" in r for r in piste["reserves"]))

    def test_type_non_eligible(self):
        self.assertIsNone(
            rapprocher.evaluer(prospect(type_org="universite"), opportunite(), GROUPES, AUJOURDHUI)
        )

    def test_segment_incompatible(self):
        self.assertIsNone(
            rapprocher.evaluer(prospect(segment="calcul"), opportunite(), GROUPES, AUJOURDHUI)
        )

    def test_appel_clos_ou_passe(self):
        self.assertIsNone(rapprocher.evaluer(prospect(), opportunite(statut="clos"), GROUPES, AUJOURDHUI))
        self.assertIsNone(
            rapprocher.evaluer(prospect(), opportunite(cloture="2026-11-01"), GROUPES, AUJOURDHUI)
        )

    def test_delai_court(self):
        piste = rapprocher.evaluer(prospect(), opportunite(cloture="2026-11-30"), GROUPES, AUJOURDHUI)
        self.assertTrue(any("trop court" in r for r in piste["reserves"]))

    def test_confiance_faible(self):
        piste = rapprocher.evaluer(prospect(), opportunite(confiance="faible"), GROUPES, AUJOURDHUI)
        self.assertTrue(any("non vérifiées" in r for r in piste["reserves"]))


class TestCommande(unittest.TestCase):
    def test_bout_en_bout(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "p.jsonl").write_text(
                "\n".join(json.dumps(x) for x in [prospect(), prospect(id="cordis-2", nom="Calcul SA", segment="calcul")]),
                encoding="utf-8",
            )
            (d / "o.jsonl").write_text(json.dumps(opportunite()) + "\n", encoding="utf-8")
            (d / "g.json").write_text(json.dumps(GROUPES), encoding="utf-8")
            res = subprocess.run(
                [sys.executable, str(ICI.parent / "rapprocher.py"), "--prospects", str(d / "p.jsonl"),
                 "--opportunites", str(d / "o.jsonl"), "--groupes", str(d / "g.json"),
                 "--aujourdhui", "2026-11-22", "--sortie", str(d / "r.jsonl"), "--fiches", str(d / "fiches")],
                capture_output=True, text=True, check=True,
            )
            self.assertIn("1 pistes", res.stdout)
            pistes = [json.loads(l) for l in (d / "r.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(pistes[0]["prospect_id"], "cordis-1")
            fiche = (d / "fiches" / "capteurs-quantiques-sas--opp-1.md").read_text(encoding="utf-8")
            self.assertIn("ni un avis d'éligibilité", fiche)
            self.assertIn("DIAMAG", fiche)
            self.assertIn("https://ec.europa.eu/topic/1", fiche)
            self.assertIn("Consortium : exigé, au moins 3 entités", fiche)
            self.assertIn("répondez « stop »", fiche)
            self.assertLessEqual(len(fiche.split()), 450 + 80)  # une page, marge pour les tableaux
            tableau = (d / "fiches" / "_pistes-par-prospect.md").read_text(encoding="utf-8")
            self.assertIn("Capteurs Quantiques SAS", tableau)


if __name__ == "__main__":
    unittest.main()
