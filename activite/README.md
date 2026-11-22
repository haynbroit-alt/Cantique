# Financements publics pour entreprises quantiques

Activité : aider les entreprises du quantique (startups, PME, fabricants de composants, éditeurs) d'Europe et du Royaume-Uni à décrocher des financements publics et des marchés publics. Les données viennent uniquement de sources publiques ; aucune donnée personnelle n'est collectée.

## Ce qui est prêt (22 novembre 2026)

| Brique | Dossier | Contenu |
|---|---|---|
| Contrat de données | `CONTRAT.md` | Formats partagés : prospect, opportunité, rapprochement |
| Prospects | `prospects/` | 678 entreprises quantiques UE et R-U ayant obtenu 817 M€ de fonds publics depuis 2019 (CORDIS, UKRI), avec la part quantique de leurs projets ; 570 universités et organismes de recherche à part ; précision mesurée 85 % stricte, 98 % large (`RESUME.md`) |
| Opportunités | `opportunites/` | 62 appels et marchés publics vérifiés (36 ouverts, 17 à venir), groupes de pays éligibles, calendrier (`CALENDRIER.md`) |
| Rapprochement | `outils/rapprocher.py` | Croise prospects et appels : score, raisons, réserves, liens ; 10 tests |
| Fiches | `rapprochements/fiches/` | 20 fiches d'opportunité gratuites pour les PME dont le quantique est le cœur de métier, et un tableau interne de toutes les pistes |
| Offre | `offre/` | Offre FR/EN et grille de prix, modèles de livrables, analyse de la concurrence |
| Prospection | `prospection/` | Plan de 12 semaines (30 nov. 2026 – 21 févr. 2027), séquences de messages, actions réservées au fondateur |

## Régénérer les fiches

```
cd activite/outils
python3 rapprocher.py \
  --prospects ../prospects/prospects.jsonl \
  --opportunites ../opportunites/opportunites.jsonl \
  --groupes ../opportunites/groupes_pays.json \
  --aujourdhui AAAA-MM-JJ \
  --sortie ../rapprochements/rapprochements.jsonl \
  --fiches ../rapprochements/fiches --nb-fiches 20 \
  --signature "Nom commercial, Prénom Nom, e-mail"
```

Les données se mettent à jour avec `prospects/construire_prospects.py` et `opportunites/construire_opportunites.py` (voir leurs en-têtes), puis se contrôlent avec `valider_prospects.py` et `valider_opportunites.py`.

## Avant tout envoi

Chaque fiche est une hypothèse du moteur. Avant de l'envoyer : suivre la liste de contrôle de `offre/LIVRABLES/fiche-opportunite.md` (date de clôture revérifiée le jour même, montants, restrictions de pays, longueur), puis appliquer les règles de prospection de `prospection/SEQUENCES.md` (pertinence professionnelle, désinscription simple, pas de suivi d'ouverture). Les envois, les appels et les signatures sont réservés au fondateur : voir `prospection/ACTIONS-HUMAINES.md`.
