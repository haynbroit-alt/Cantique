# Contrat de données de l'activité « financements publics pour entreprises quantiques »

L'activité aide les entreprises du quantique (startups, PME, fabricants de composants, éditeurs) à décrocher des financements publics et des marchés publics. Trois briques partagent les formats ci-dessous : le fichier de prospects, le calendrier des opportunités et le moteur de rapprochement. Toute modification doit être reportée dans les trois.

Conventions communes :
- Dates au format ISO `AAAA-MM-JJ` ; `null` si inconnue.
- Pays en code ISO 3166-1 alpha-2 (`FR`, `DE`, `GB` pour le Royaume-Uni, `CH`, `NL`…).
- Montants en euros (`_eur`) ; conversion au taux indiqué dans le champ `note` si la source est dans une autre devise.
- Chaque enregistrement porte au moins une URL de source publique et une `date_extraction` ou `date_verification`.
- Aucune donnée personnelle (nom, e-mail, téléphone d'une personne) n'est collectée : uniquement des données d'organisations publiées par des organismes publics.

## Segments technologiques

`calcul`, `capteurs`, `communication`, `composants` (cryogénie, lasers, photonique, électronique de contrôle, matériaux), `logiciel` (logiciel quantique, simulation, algorithmes), `pqc` (cryptographie post-quantique), `transverse` (plusieurs segments), `inconnu`.

## Types d'organisation

`PME` (au sens de la recommandation 2003/361/CE, ou drapeau SME de la source), `grande_entreprise`, `universite`, `recherche` (organisme public de recherche), `autre`.

## Prospect — `activite/prospects/prospects.jsonl`

Une ligne JSON par organisation.

```json
{
  "id": "cordis-999999999",
  "nom": "Exemple Quantum SAS",
  "pays": "FR",
  "ville": "Paris",
  "site_web": "https://… ou null",
  "type_org": "PME",
  "segment": "capteurs",
  "segment_justification": "mots-clés des projets : magnetometer, NV centre",
  "financements_obtenus": [
    {
      "programme": "Horizon Europe | H2020 | EIC | Digital Europe | EuroHPC | Chips JU | UKRI | Innovate UK | autre",
      "projet": "titre du projet",
      "acronyme": "ACRONYME",
      "id_projet": "101234567",
      "debut": "2024-01-01",
      "fin": "2027-12-31",
      "contribution_eur": 512000,
      "role": "coordinateur | participant | beneficiaire_unique",
      "source_url": "https://cordis.europa.eu/project/id/101234567"
    }
  ],
  "total_obtenu_eur": 512000,
  "nb_projets": 1,
  "derniere_activite": "2027-12-31",
  "sources": ["https://cordis.europa.eu/…"],
  "date_extraction": "2026-11-22"
}
```

## Opportunité — `activite/opportunites/opportunites.jsonl`

Une ligne JSON par appel à projets, appel d'offres ou guichet ouvert.

```json
{
  "id": "eurohpc-2026-qml-07",
  "financeur": "EuroHPC JU",
  "programme": "Horizon Europe / Digital Europe / national…",
  "intitule": "…",
  "identifiant_appel": "HORIZON-EUROHPC-JU-2026-QML-07",
  "nature": "subvention | marche_public | pret | fonds_propres | prix | autre",
  "url": "https://…",
  "statut": "ouvert | a_venir | clos",
  "ouverture": "2026-08-01",
  "cloture": "2027-01-28",
  "budget_total_eur": 6000000,
  "montant_par_projet_eur": null,
  "pays_eligibles": ["UE27", "HE_ASSOCIES"],
  "types_eligibles": ["PME", "grande_entreprise", "universite", "recherche"],
  "consortium_requis": true,
  "taille_min_consortium": 3,
  "segments": ["calcul", "logiciel"],
  "trl": "4-6 ou null",
  "taux_financement": "100 % des coûts éligibles (exemple) ou null",
  "mots_cles": ["quantum machine learning"],
  "note": "…",
  "source_url": "https://…",
  "confiance": "elevee | moyenne | faible",
  "date_verification": "2026-11-22"
}
```

`pays_eligibles` contient des codes pays ou des groupes définis dans `activite/opportunites/groupes_pays.json` :

```json
{
  "UE27": ["AT", "BE", "…"],
  "HE_ASSOCIES": ["GB", "CH", "NO", "IS", "…"],
  "DEP_ASSOCIES": ["…"],
  "EEE": ["…"]
}
```

Chaque groupe cite sa source et sa date de vérification dans un champ `_sources`.

## Rapprochement — sortie de `activite/outils/rapprocher.py`

Pour chaque couple (prospect, opportunité) jugé pertinent : score, raisons, réserves (consortium à constituer, éligibilité à confirmer), et lien vers les deux sources. Le moteur ne décide jamais seul de l'éligibilité : il signale, un humain confirme.
