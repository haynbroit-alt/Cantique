# Cantique

Projet consacré aux opportunités commerciales autour des technologies quantiques, constitué le 22 novembre 2026 avec l'assistance d'agents d'IA.

## Contenu

| Dossier | Contenu |
|---|---|
| `activite/` | Activité « financements publics pour entreprises quantiques » : fichier de 678 entreprises quantiques UE et R-U avec leur historique de financement public, calendrier vérifié de 62 appels et marchés publics, moteur de rapprochement, fiches d'opportunité, offre et kit de prospection. Voir `activite/README.md`. |
| `atelier-pqc/` | Cryptographie post-quantique : référentiel réglementaire FR/EN (19 textes, 48 exigences), chaîne d'inventaire (scanner de code, CBOM CycloneDX 1.6, rapport en marque blanche), dossiers de démonstration. |
| `registre-quantique/` | Registre horodaté de 158 affirmations sourcées sur les feuilles de route du calcul quantique et le Q-Day. |
| `reports/`, `research_notes/` | Deux rapports d'étude et douze notes de recherche sourcées. |

## Sources des données et licences

Les compilations de `activite/` reposent sur des données publiques réutilisées sous licence :

- **CORDIS** — © Union européenne, 1994-2026, réutilisé conformément à la décision 2011/833/UE de la
  Commission et sous licence CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Source :
  https://cordis.europa.eu/.
- **UKRI Gateway to Research** — Contains public sector information licensed under the Open Government
  Licence v3.0 (https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). Source :
  https://gtr.ukri.org/.

Les données ont été sélectionnées, agrégées, converties en euros et reclassées ; ni l'Union européenne ni
UKRI ne sont responsables de ces modifications ni n'approuvent ce projet. Les autres sources du calendrier
des opportunités, les contenus de tiers et les dépendances open source (toutes facultatives :
`cryptography`, `cyclonedx-python-lib`, `jsonschema`, `pytest`, `setuptools`) sont détaillés dans
`ATTRIBUTIONS.md`.

Aucun fichier de licence n'accompagne ce dépôt : sauf accord écrit, aucun droit de réutilisation du code,
des documents ou des compilations n'est accordé.
