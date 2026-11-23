# Prospects : organisations du quantique déjà financées (UE + Royaume-Uni)

Extraction du 2026-11-22. Données publiques au niveau organisation uniquement (aucun nom, e-mail ni téléphone de personne), conformes à `activite/CONTRAT.md` (`valider_prospects.py` : 0 erreur).

## 1. En bref

- **678 entreprises** dans `prospects.jsonl` (461 PME, 217 grandes entreprises), issues de 33 pays. Elles ont obtenu **817,4 M EUR** de financements publics sur des projets quantiques actifs ou terminés depuis le 2019-01-01. Cela représente 1 480 participations financées dans 623 projets.
- **570 universités, organismes de recherche et autres organismes** dans `prospects_recherche.jsonl` (337 universités, 153 organismes de recherche, 80 « autre »). Ce sont des partenaires de consortium, pas des acheteurs.
- **223 entreprises ont porté au moins un projet** : 117 ont coordonné un projet collaboratif et 147 ont été seules bénéficiaires (EIC Accelerator, Innovate UK mono-entreprise…). Une entreprise peut être dans les deux cas.
- **366 entreprises ont au moins un projet encore en cours** (date de fin ≥ 2026-11-22).
- **Part du quantique** (`part_quantique` = projets quantiques / tous projets financés depuis 2019) : **375 entreprises ≥ 0,5**, dont 244 n'ont que des projets quantiques. C'est le cœur de cible « quantique natif ». **97 entreprises ont `profil_consultant_ue = true`** : sociétés de gestion de projets UE, conseil, fondations, mais aussi grands groupes très présents dans les programmes UE (voir § 3.9 et § 5).
- **Précision mesurée à la main** sur deux échantillons aléatoires de 30 projets retenus :
  - stricte (« le projet est un projet de technologie quantique ») : 80 % sur l'ensemble des projets, 90 % sur les projets comptant une entreprise ;
  - large (y compris les projets où le quantique est une composante secondaire) : 97 % et 100 %.
  - Détail au § 4.
- **Pas de données américaines** : SBIR.gov renvoyait HTTP 403 depuis ce conteneur. Ce point est un constat du coordinateur, que je n'ai pas retesté. **Pas de données Digital Europe** (EuroQCI) ni de programmes nationaux (voir § 7).

## 2. Fichiers

| Fichier | Contenu |
|---|---|
| `prospects.jsonl` | Une entreprise par ligne (types `PME`, `grande_entreprise`), triée par total obtenu décroissant. |
| `prospects_recherche.jsonl` | Universités (`universite`), organismes publics de recherche (`recherche`) et autres organismes (`autre` : agences de financement, collectivités, associations, clusters). |
| `prospects.csv` | Vue à plat des entreprises : nom, pays, ville, type_org, segment, nb_projets, total_obtenu_eur, derniere_activite, a_coordonne (oui = coordinateur ou seul bénéficiaire d'au moins un projet), programmes, site_web, lien_source_principal (projet le mieux doté), puis nb_projets_total, part_quantique, profil_consultant_ue (oui/non). |
| `construire_prospects.py` | Script d'extraction reproductible. Bibliothèque standard uniquement. Cache des réponses brutes hors dépôt, ≥ 1,1 s entre requêtes, reprise sur cache, option `--hors-ligne`. |
| `valider_prospects.py` | Contrôle de chaque ligne contre le contrat (champs, vocabulaires, dates ISO, codes pays ISO 3166-1, URLs de sources, absence de données personnelles, cohérence des totaux, fenêtre temporelle, CSV). |
| `echantillon_precision.csv` | Les 60 projets tirés au sort et mon verdict manuel (oui / limite / non) avec sa justification. |

Champs ajoutés au contrat, tous au niveau organisation :
- `nb_projets_total`, `part_quantique`, `profil_consultant_ue` : champs optionnels désormais dans l'exemple de `CONTRAT.md`, renseignés pour les entreprises seulement (§ 3.9) ;
- `a_coordonne` (booléen) ;
- `identifiants_sources` (PIC CORDIS, identifiant d'organisation GtR) ;
- `note` (origine du type d'organisation, taux de change, date des dumps, autres libellés) ;
- `financeur_source` dans chaque financement (schéma CORDIS ou financeur et catégorie GtR).

## 3. Sources et méthode

### 3.1 Sources

| Source | Accès | Volume |
|---|---|---|
| **CORDIS – Horizon Europe** (dont EIC, Chips JU/KDT, EuroHPC) | Dump open data `cordis-HORIZONprojects-csv.zip`, fichiers du 2026-11-05 (fiche data.europa.eu `cordis-eu-research-projects-under-horizon-europe-2021-2027`) | 24 419 projets, 151 382 lignes organisation |
| **CORDIS – H2020** | Dump `cordis-h2020projects-csv.zip`, fichiers du 2026-11-05 | 35 389 projets, 179 063 lignes organisation |
| **UKRI Gateway to Research** | API v2 (`Accept: application/vnd.rcuk.gtr.json-v7`) : `/projects?q=…`, `/funds/{id}`, `/organisations/{id}`, `/organisations/{id}/projects` | 23 requêtes plein texte, 6 657 projets distincts récoltés ; 2 295 appels (108 pages de recherche, 1 630 funds, 329 organisations, 228 pages de projets par organisation pour `nb_projets_total`), 0 échec après relances. Le service a renvoyé des 503 temporaires lors de mes premiers essais manuels ; le script relance avec attente croissante. |
| **BCE** | `data-api.ecb.europa.eu`, série EXR.D.GBP.EUR.SP00.A | Taux de référence du **2026-11-20 : 1 EUR = 0,83735 GBP** |

**Pourquoi les dumps plutôt que l'API de recherche CORDIS.** Les dumps contiennent *tous* les projets, sans aucune limite de pagination. Leur `organization.csv` donne directement :
- le PIC (`organisationID`) ;
- le drapeau `SME` et l'`activityType` (PRC, HES, REC, PUB, OTH) ;
- le rôle et l'`ecContribution` de chaque organisation ;
- la ville, le pays et l'URL du site.

L'API de recherche (`/search/en?q=…&format=json`) a servi de contrôle de cohérence. La requête `contenttype='project' AND frameworkProgramme='HORIZON' AND ('quantum')` renvoie 1 597 projets, et 1 819 pour `'H2020'`. Les dumps contiennent 1 498 et 1 494 projets avec « quantum » dans le titre, le résumé ou les mots-clés. L'écart vient du fait que l'API cherche aussi dans les rapports et résultats. Les dumps ne sont pas lacunaires.

**GtR.** Requêtes plein texte : `quantum`, `qubit`, `qubits`, `QKD`, `"atom interferometry"`, `"atom interferometer"`, `"cold atom(s)"`, `"optically pumped magnetometer(s)"`, `"nitrogen vacancy"`, `"single photon"`, `"single-photon"`, `"trapped ion(s)"`, `"dilution refrigerator"`, `"atomic clock"`, `"optical clock"`, `Rydberg`, `SNSPD`, `"superconducting nanowire"`, `entanglement`, `"post-quantum"`. Les résultats (100 par page, toutes les pages) sont ensuite passés au même filtre de pertinence que CORDIS. Les liens vers des personnes (`/persons/`) sont supprimés à la lecture et ne sont jamais appelés.

### 3.2 Fenêtre temporelle

Seuls les projets dont la date de fin est ≥ 2019-01-01 sont gardés (ou sans date de fin). Pour GtR, c'est la fin du « fund ».
- CORDIS : 52 001 projets dans la fenêtre.
- GtR : 5 115 projets dans la fenêtre.

### 3.3 Règles de pertinence « technologies quantiques »

Le filtre porte sur le titre, le résumé, les mots-clés (CORDIS) et l'intitulé du topic d'appel (CORDIS) ou des research topics (GtR). Le texte est mis en minuscules et les tirets sont remplacés par des espaces.

**1. Exclusions retirées avant comptage.** Ce sont les faux positifs connus :
- `quantum dot(s)` : écrans, LED, solaire, imagerie biologique ;
- `quantum yield`, `quantum efficiency`, `quantum well`, `quantum cascade` (lasers QCL de spectroscopie) ;
- `quantum chemistry/chemical`, `quantum mechanics/mechanical` ;
- `quantum leap/jump` (métaphores) ;
- physique fondamentale : `quantum field theory`, `quantum gravity` (sauf « quantum gravity sensor/gradiometer »), `quantum chromodynamics`, `quantum confinement/size/tunnelling`, `quantum biology`, `quantum Hall`, `quantum many-body`, `quantum phase transition`, `quantum spin liquid`, `quantum critical…`, `quantum material(s)/matter`, `quantum fluids` ;
- outils de calcul classiques : `quantum Monte Carlo`, `Quantum ESPRESSO`…

Une boîte quantique utilisée comme qubit ou comme source de photons uniques reste détectée par les autres termes.

**2. Termes forts.**

| Segment | Termes |
|---|---|
| Calcul | quantum computing/computer/computation/processor/hardware/annealing/advantage/error correction/circuit/gate/chip, qubit, qudit, QPU, trapped ion, superconducting qubit, neutral-atom array/qubit/processor, quantum simulator |
| Capteurs, métrologie, temps | quantum sensing/sensor/metrology/magnetometer/gravimeter/gradiometer/gyroscope/accelerometer/inertial/navigation/imaging/radar/lidar/clock/timing/enhanced, atom interferometry, cold/ultracold atoms, nitrogen-vacancy, NV centre/diamond, colour centre, optically pumped magnetometer, OPM-MEG, atomic magnetometer, optical/atomic clock, Rydberg atoms/sensors |
| Communication | quantum key distribution, QKD, EuroQCI, quantum network/internet/repeater/memory/communication/cryptography/teleportation/random number, QRNG, entangled photons/states, squeezed light |
| Composants | dilution refrigerator, SNSPD, superconducting nanowire, single-photon detector/source/emitter, quantum photonics/light/emitter/transducer |
| Logiciel | quantum software/algorithm/machine learning/programming/compiler/cloud/optimisation/error mitigation |
| PQC | post-quantum, quantum-safe/-resistant/-proof/-secure, quantum attack/threat, PQC (compté seulement si « crypt… » ou « quantum » figure dans le texte : sinon c'est « protein quality control ») |
| Transverse | quantum technology, quantum information, Quantum Flagship |

**3. Termes de contexte.** Ils comptent peu et ne suffisent jamais seuls : entanglement, single photon(s), SPAD, Rydberg, Bose-Einstein, Majorana, ion trap, neutral atoms, quantum simulation/optics/control/states/devices/systems, cryogenic, cryo-CMOS, magnetometer, interferometer, superconducting, decoherence, coherence time, photonic integrated, SQUID, spin defects, cryptography.

**4. Barème.**

| Preuve | Points |
|---|---|
| Terme fort dans le titre | +3 |
| Topic d'appel dont l'intitulé est quantique | +3 |
| Mots-clés | +1, ou +2 si au moins deux termes forts distincts |
| Résumé | +1 par occurrence distincte, plafonné à 4 (des correspondances qui se chevauchent comptent une fois) |
| Contexte matériel (cryogénie, supraconducteur, photon unique, intrication, ions/atomes, décohérence, photonique intégrée, magnétomètre, SQUID) | +1 |
| Autre contexte | +0,5 |

Trois topics mixtes ne donnent pas de points : « semiconductor or quantum technology components », « lawful interception… quantum », « chip-scale atomic clocks and solar cells ».

Un projet est retenu si **score ≥ 3** **et** si l'une de ces conditions est remplie :
- terme fort dans le titre ;
- topic quantique ;
- au moins 2 occurrences fortes dans le résumé ;
- au moins 2 termes forts en mots-clés et au moins 1 occurrence dans le résumé.

Une phrase isolée du type « résistant aux futurs ordinateurs quantiques » dans un projet de cybersécurité généraliste n'est donc pas retenue.

**Projets retenus.**
- CORDIS : **1 045 projets**. Par programme : Horizon Europe 623 (dont EIC 92, Chips JU 8, EuroHPC 4) et H2020 422 (dont EIC 10, EuroHPC 1). Par preuve : 517 retenus sur le titre, 47 sur le topic, 481 sur le résumé ou les mots-clés.
- GtR : **1 973 projets**. Par programme : 1 633 « UKRI » (EPSRC 1 329, STFC 70, SPF, FLF, Horizon Europe Guarantee 30…) et 340 « Innovate UK » (Innovate UK, ISCF, SPF, TMF pour les catégories de subventions d'entreprises).

### 3.4 Participations retenues (« a obtenu un financement »)

- **CORDIS.** Seules les lignes avec `ecContribution` > 0 sont gardées, quel que soit le rôle (coordinator, participant, thirdParty). Les lignes non financées sont écartées : 425 associated partners, 130 third parties, 67 participants, 49 partners (H2020), 2 coordinateurs, 1 international partner.
- **GtR, Innovate UK et Horizon Europe Guarantee.** Chaque participant de `participantValues` avec `grantOffer` > 0 est retenu.
- **GtR, subventions des conseils de recherche (EPSRC, STFC…).** Le montant total des « funds » est attribué à l'organisation porteuse (`LEAD_ORG`). Les project partners et collaborators sont exclus, puisqu'ils ne reçoivent pas d'argent.

**Rôles.**
- `coordinateur` : coordinator CORDIS ou `LEAD_PARTICIPANT` GtR, dans un projet à plusieurs bénéficiaires.
- `beneficiaire_unique` : seul bénéficiaire financé, ou porteur d'une subvention de conseil de recherche.
- `participant` : tous les autres cas.

### 3.5 Type d'organisation

**CORDIS.** Le type vient de la participation la plus récente :
- `PRC` + `SME=true` → `PME` ;
- `PRC` + `SME=false` → `grande_entreprise` ;
- `HES` → `universite` ;
- `REC` → `recherche` ;
- `PUB` et `OTH` → `autre`.

Exceptions documentées dans `note` :
- `REC`/`OTH` avec `SME=true` et une forme sociale commerciale (GmbH, Ltd…) → `PME` (3 cas) ;
- `activityType` vide avec une forme sociale commerciale → entreprise (1 cas) ;
- NPL Management Ltd (laboratoire national de métrologie britannique, codé PRC) et les Catapults → `recherche`.

**GtR.** GtR ne publie ni la nature ni la taille des organisations.
- La nature (université, laboratoire public, Catapult, entreprise, autre) est déduite du nom.
- La taille est **inférée** du taux d'aide Innovate UK (`grantOffer` / `projectCost`) sur les subventions R&D, hors contrats SBRI et projets UE. Une grande entreprise est plafonnée à 50 % en recherche industrielle et en faisabilité.
  - Majorité des taux > 55 % → `PME` : 140 entreprises.
  - Majorité des taux entre 40 et 50 % → `grande_entreprise` : 38 entreprises, signalées « à vérifier ».
  - Taux non concluants → `PME` **par défaut** : 20 entreprises, signalées « à vérifier ».

  C'est une déduction. Exemples d'erreurs probables : Capgemini UK et QuEra Computing UK sont classées PME par défaut ; Kelvin Nanotechnology est inférée grande entreprise.
- Pays : 16 entreprises GtR sans pays ni région dans GtR sont mises en `GB`. Les financements UKRI sont réservés aux organisations établies au Royaume-Uni. Ce cas est signalé dans `note`.

### 3.6 Segment

Pour chaque projet, je compte les termes de segment (tableau du § 3.3, élargi à cryogenic, laser, photonic integrated circuit, frequency comb… pour les composants, et tensor networks pour le logiciel). Chaque projet pèse 1 dans le profil de l'organisation.
- Si le premier segment pèse ≥ 50 %, c'est le segment de l'organisation.
- Sinon, le segment est `transverse`.
- Sans aucun terme, le segment est `inconnu` (8 entreprises).

`segment_justification` donne les termes les plus fréquents, la répartition en pourcentage et le nombre de projets.

### 3.7 Agrégation, dédoublonnage, fusion

1. Je dédoublonne par PIC CORDIS (H2020 et Horizon Europe confondus) et par identifiant d'organisation GtR. Si une même entité apparaît plusieurs fois dans un même projet, ses montants sont additionnés et je garde le rôle le plus élevé.
2. Je fusionne ensuite de façon **conservatrice**, uniquement si le nom normalisé (majuscules, accents et ponctuation retirés, formes sociales LTD/GMBH/SAS/BV… retirées) **et** le pays sont strictement égaux. La fusion n'est faite qu'entre CORDIS et GtR, ou entre deux identifiants GtR. Elle n'a jamais lieu entre deux PIC CORDIS distincts, ni s'il y a ambiguïté.
3. Résultat : 82 fusions, dont **13 entreprises présentes dans les deux sources** (Riverlane, Toshiba Europe, Quantum Motion, Duality Quantum Photonics, M Squared Lasers, Phasecraft, Quantum Dice, PQShield, Element Six, Hitachi Europe…). Au total, 467 entreprises viennent de CORDIS seul et 198 de GtR seul.
4. `site_web` n'est rempli que si la source le fournit : `organizationURL` CORDIS, le champ GtR étant toujours vide. Il est renseigné pour 108 entreprises, aucun domaine n'est deviné.

### 3.8 Montants

- **CORDIS** : `ecContribution` par organisation, c'est-à-dire la contribution UE maximale signée, pas les paiements effectifs.
- **GtR** : `grantOffer` par participant, ou montant total du fund pour les subventions de conseils de recherche. Converti en euros par montant GBP / 0,83735 (taux BCE du 2026-11-20, rappelé dans `note`).

### 3.9 Part du quantique et profil « consultant UE » (entreprises)

**`nb_projets_total`.** Nombre de **tous** les projets financés de l'entreprise dans la même fenêtre (fin ≥ 2019-01-01), quel que soit le thème. Il est calculé avec les mêmes critères de financement que `nb_projets` :
- **CORDIS** : tous les projets H2020 et Horizon Europe des dumps où l'un des PIC rattachés à l'entité a `ecContribution` > 0 ;
- **GtR** : tous les projets de `/organisations/{id}/projects` (un appel par page de 100, 228 appels) où l'entreprise a `grantOffer` > 0, ou est porteuse d'une subvention de conseil de recherche.

Les deux comptes sont additionnés et figurent dans `note` (« Projets financés depuis 2019-01-01, tous thèmes : n CORDIS, m GtR »). Les projets quantiques sont inclus par construction : `nb_projets_total` ≥ `nb_projets`.

**`part_quantique`** = `nb_projets` / `nb_projets_total`, arrondi à 2 décimales. Il vaut null si la liste GtR n'a pas pu être lue ; cela n'arrive pour aucune entreprise ici.

**`profil_consultant_ue` = true** dans l'un ou l'autre de ces cas :
1. l'entreprise compte **au moins 15 projets CORDIS financés** (tous thèmes, depuis 2019) **et** `part_quantique` < 0,20 ;
2. son nom (majuscules, sans accents) contient un marqueur de gestion de projets, de conseil ou de fondation : `CONSULT`, `BERATUNG`, `PLANUNGSGESELLSCHAFT`, `FOUNDATION`, `STIFTUNG`, `FONDAZIONE`, `FUNDACI`, `FUNDACAO`, `EURESCOM`.

Le seuil de 15 ne compte que les projets UE (CORDIS), pas les subventions GtR.

**Limites.**
- Le dénominateur ne couvre que les identifiants rattachés à l'entité. Une société britannique vue seulement dans GtR, mais aussi présente en H2020 sous un PIC non fusionné, a une part surestimée. L'inverse vaut pour une société CORDIS dont les subventions Innovate UK n'ont pas été fusionnées.
- Les programmes hors H2020 et Horizon Europe (Digital Europe, programmes nationaux…) ne sont pas comptés.
- Le compte des projets quantiques hérite de la précision du filtre (§ 4).
- La règle 1 attrape aussi les **grands groupes industriels très présents dans les programmes UE** (Thales, Airbus, Infineon, IBM Research, Telefónica I+D, EDF…) : 59 des 97 entreprises signalées sont des grandes entreprises. Pour isoler les sociétés de montage de projets UE et de conseil, il faut croiser avec `type_org = PME` (38 entreprises).

## 4. Précision mesurée (contrôle manuel)

Le script tire deux échantillons (graines fixes 20261122 et 20261123) :
- **A** : 30 projets parmi les 3 018 retenus (24 GtR, 6 CORDIS) ;
- **B** : 30 projets parmi ceux qui comptent au moins une entreprise financée (16 CORDIS, 14 GtR), c'est-à-dire ceux qui alimentent `prospects.jsonl`.

J'ai lu le titre et le résumé de chaque projet. Verdict « oui » : le projet développe ou applique une technologie quantique (calcul, capteurs, temps, communication, PQC, composants, logiciel) ou vise explicitement cette finalité. Verdict « limite » : le quantique n'est qu'une composante ou une motivation secondaire. Verdict « non » : faux positif.

| Échantillon | oui | limite | non | Précision stricte (IC 95 % Wilson) | Précision large |
|---|---|---|---|---|---|
| A : tous projets | 24 | 5 | 1 | **80 %** (63–90 %) | 97 % (83–99 %) |
| B : projets avec entreprise | 27 | 3 | 0 | **90 %** (74–97 %) | 100 % (89–100 %) |
| A + B | 51 | 8 | 1 | 85 % (74–92 %) | 98 % (91–100 %) |

**Le faux positif.** Un équipement d'épitaxie généraliste dont le résumé cite le quantique parmi plusieurs débouchés.

**Les cas limites :**
- une machine d'Ising optique ;
- de la théorie des catégories avec des applications aux circuits quantiques ;
- de la chimie ultrafroide ;
- de la théorie des nombres motivée par la PQC ;
- un microscope à gaz quantique de molécules ;
- des liaisons optiques inter-satellites mentionnant la QKD ;
- de l'optimisation « quantum-inspired » ;
- de la logique nano-mécanique pour l'électronique cryogénique.

L'imprécision vient surtout des projets académiques dont le quantique est la motivation, pas l'objet. Elle est plus faible sur les projets d'entreprises.

**Rappel non mesuré.** Je n'ai pas mesuré le rappel. Les faux négatifs connus sont des projets d'entreprise qui ne citent le quantique qu'une fois, par exemple un SME-1 H2020 de refroidissement sans cryogène « pour l'informatique quantique ».

## 5. Résultats : entreprises (`prospects.jsonl`)

### Par pays

| Pays | Entreprises | Total obtenu (EUR) |
|---|---|---|
| GB | 220 | 289 551 509 |
| DE | 99 | 107 686 498 |
| FR | 69 | 104 562 199 |
| IT | 45 | 30 019 470 |
| ES | 35 | 35 623 907 |
| NL | 31 | 89 265 552 |
| GR | 22 | 11 965 032 |
| AT | 18 | 23 300 360 |
| CH | 15 | 23 827 478 |
| FI | 14 | 19 659 650 |
| DK | 14 | 24 290 678 |
| SE | 11 | 4 494 123 |
| PL | 10 | 8 305 872 |
| PT | 8 | 5 306 889 |
| CY | 8 | 3 283 538 |
| BE | 8 | 2 617 157 |
| IL | 7 | 13 056 778 |
| IE | 5 | 6 734 863 |
| CZ | 5 | 2 695 833 |
| BG, EE, LU, TR | 4 chacun | 1 487 375 / 834 311 / 1 156 050 / 1 242 295 |
| LT, RO | 3 chacun | 920 600 / 979 462 |
| LV, SI, MT, RS | 2 chacun | 802 500 / 714 796 / 800 000 / 757 125 |
| KR, HR, NO, HU | 1 chacun | 749 750 / 350 000 / 343 350 / 41 360 |

**Pays les plus représentés.** Le Royaume-Uni (220 entreprises, 289,6 M EUR) domine parce que GtR couvre en détail les programmes nationaux d'Innovate UK. Les données de l'UE ne couvrent, elles, que les programmes européens. Viennent ensuite l'Allemagne (99 ; 107,7 M), la France (69 ; 104,6 M), l'Italie (45), l'Espagne (35) et les Pays-Bas (31, mais 89,3 M : forte concentration EIC et Chips JU).

### Par segment et par type

| Segment | Entreprises | Total (EUR) |
|---|---|---|
| calcul | 202 | 311 922 313 |
| communication | 102 | 117 073 751 |
| capteurs | 98 | 83 938 833 |
| transverse | 84 | 213 801 753 |
| composants | 75 | 40 785 431 |
| pqc | 74 | 29 096 456 |
| logiciel | 35 | 15 147 858 |
| inconnu | 8 | 5 659 966 |

| Type | Entreprises | Total (EUR) |
|---|---|---|
| PME | 461 | 606 777 307 |
| grande_entreprise | 217 | 210 649 054 |

### Par programme

Une entreprise est comptée dans chaque programme où elle a obtenu au moins un financement.

| Programme | Entreprises | Participations | Montant (EUR) |
|---|---|---|---|
| Horizon Europe (hors EIC, Chips JU, EuroHPC) | 310 | 453 | 224 945 980 |
| Innovate UK | 210 | 573 | 264 234 011 |
| H2020 (hors EIC, EuroHPC) | 134 | 221 | 85 929 436 |
| EIC (H2020 EIC pilot + Horizon Europe) | 89 | 118 | 173 795 743 |
| Chips JU (dont KDT JU) | 86 | 98 | 57 518 770 |
| EuroHPC | 11 | 11 | 2 835 459 |
| UKRI (Horizon Europe Guarantee, EPSRC…) | 6 | 6 | 8 166 962 |

### Taille et coordination

**Répartition par total obtenu :**

| Total obtenu | Entreprises |
|---|---|
| < 100 k EUR | 106 |
| 100 k – 500 k EUR | 298 |
| 500 k – 2 M EUR | 165 |
| 2 – 5 M EUR | 71 |
| ≥ 5 M EUR | 38 |

**Récurrence.** 444 entreprises n'ont qu'un seul projet quantique ; 136 en ont au moins trois.

**Coordination.**
- 117 entreprises ont coordonné au moins un projet collaboratif, soit 212 coordinations.
- 147 ont été seules bénéficiaires d'au moins un projet, soit 216 projets.
- Au total, 223 entreprises ont `a_coordonne = true`.

### Top 30 par financement public obtenu

| # | Entreprise | Pays | Type | Segment | Projets quantiques / total | Part quantique | Total (EUR) | A porté | Programmes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | COLDQUANTA UK LIMITED | GB | PME | transverse | 19 / 21 | 0.90 | 22 715 976 | coordination | Innovate UK |
| 2 | RIVERLANE LTD | GB | PME | calcul | 24 / 24 | 1.00 | 16 106 733 | coordination | Horizon Europe / Innovate UK / UKRI |
| 3 | OXFORD IONICS LIMITED | GB | PME | calcul | 13 / 13 | 1.00 | 16 104 530 | coordination | Innovate UK |
| 4 | RIGETTI UK LIMITED | GB | PME | calcul | 12 / 12 | 1.00 | 12 449 667 | coordination | Innovate UK |
| 5 | IBM RESEARCH GMBH † | CH | grande_entreprise | transverse | 14 / 82 | 0.17 | 12 331 182 | seul bénéficiaire | EIC / H2020 / Horizon Europe |
| 6 | ORCA COMPUTING LTD. | GB | PME | calcul | 14 / 19 | 0.74 | 12 264 632 | coordination | Innovate UK |
| 7 | TOSHIBA EUROPE LIMITED | GB | grande_entreprise | communication | 17 / 31 | 0.55 | 11 949 961 | coordination | H2020 / Horizon Europe / Innovate UK |
| 8 | THALES † | FR | grande_entreprise | transverse | 20 / 145 | 0.14 | 11 365 712 | coordination | Chips JU / EIC / EuroHPC / H2020 / Horizon Europe |
| 9 | QUANTUM MOTION TECHNOLOGIES LTD | GB | PME | calcul | 12 / 14 | 0.86 | 10 950 825 | coordination | H2020 / Innovate UK |
| 10 | Delft Networks B.V. | NL | PME | communication | 3 / 3 | 1.00 | 10 785 111 | seul bénéficiaire | Chips JU / EIC / Horizon Europe |
| 11 | EXAIL | FR | grande_entreprise | capteurs | 14 / 22 | 0.64 | 10 363 556 | coordination | H2020 / Horizon Europe |
| 12 | ALPINE QUANTUM TECHNOLOGIES GMBH | AT | PME | calcul | 9 / 9 | 1.00 | 10 086 238 | seul bénéficiaire | Chips JU / EIC / Horizon Europe |
| 13 | QUOBLY | FR | PME | calcul | 5 / 5 | 1.00 | 10 057 300 | seul bénéficiaire | Chips JU / EIC / Horizon Europe |
| 14 | SINGLE QUANTUM BV | NL | PME | transverse | 17 / 19 | 0.89 | 9 849 574 | coordination | Chips JU / EIC / H2020 / Horizon Europe |
| 15 | TOPTICA PHOTONICS SE | DE | PME | transverse | 13 / 14 | 0.93 | 9 714 725 | non | H2020 / Horizon Europe |
| 16 | KIUTRA GMBH | DE | PME | calcul | 5 / 6 | 0.83 | 9 276 728 | seul bénéficiaire | EIC / H2020 / Horizon Europe |
| 17 | QBLOX BV | NL | PME | calcul | 7 / 7 | 1.00 | 9 156 826 | seul bénéficiaire | Chips JU / EIC / Horizon Europe |
| 18 | WELINQ SAS | FR | PME | communication | 5 / 5 | 1.00 | 9 031 812 | seul bénéficiaire | Chips JU / EIC / Horizon Europe |
| 19 | PASQAL | FR | PME | calcul | 7 / 7 | 1.00 | 8 877 845 | coordination | Chips JU / EIC / Horizon Europe |
| 20 | SEEQC UK | GB | PME | calcul | 10 / 10 | 1.00 | 8 731 258 | coordination | Innovate UK |
| 21 | QUANTWARE B.V. | NL | PME | calcul | 6 / 6 | 1.00 | 7 875 088 | seul bénéficiaire | Chips JU / EIC / Horizon Europe |
| 22 | QUERA COMPUTING UK LIMITED | GB | PME (par défaut) | calcul | 1 / 1 | 1.00 | 7 826 823 | seul bénéficiaire | Innovate UK |
| 23 | KETS QUANTUM SECURITY LTD | GB | PME | communication | 13 / 13 | 1.00 | 7 724 487 | coordination | Innovate UK / UKRI |
| 24 | SEMIQON TECHNOLOGIES OY | FI | PME | calcul | 6 / 6 | 1.00 | 7 598 049 | coordination | Chips JU / EIC / Horizon Europe |
| 25 | INFINEON TECHNOLOGIES AUSTRIA AG † | AT | grande_entreprise | transverse | 7 / 79 | 0.09 | 7 394 063 | coordination | Chips JU / EIC / H2020 / Horizon Europe |
| 26 | CPI TMD TECHNOLOGIES LIMITED | GB | grande_entreprise (inféré) | transverse | 9 / 14 | 0.64 | 7 220 777 | coordination | Innovate UK |
| 27 | SPARROW QUANTUM ApS | DK | PME | transverse | 4 / 4 | 1.00 | 7 061 992 | seul bénéficiaire | Chips JU / EIC / Horizon Europe |
| 28 | NU QUANTUM LTD | GB | PME | transverse | 11 / 12 | 0.92 | 7 055 985 | coordination | Innovate UK |
| 29 | BULL SAS † | FR | grande_entreprise | calcul | 9 / 47 | 0.19 | 6 300 049 | coordination | EuroHPC / H2020 / Horizon Europe |
| 30 | AIRBUS DEFENCE AND SPACE GMBH † | DE | grande_entreprise | capteurs | 3 / 69 | 0.04 | 6 036 269 | non | Horizon Europe |

† = `profil_consultant_ue`. Ici, ce sont tous de grands groupes très présents dans les programmes UE (règle 1 du § 3.9).

### Part du quantique dans l'activité financée

| part_quantique | Entreprises | dont PME | dont grandes | Total obtenu (EUR) |
|---|---|---|---|---|
| 1,00 (tous les projets financés sont quantiques) | 244 | 194 | 50 | 344 836 588 |
| [0,75 ; 1[ | 25 | 21 | 4 | 126 328 490 |
| [0,50 ; 0,75[ | 106 | 69 | 37 | 119 731 704 |
| [0,20 ; 0,50[ | 122 | 86 | 36 | 79 774 065 |
| [0,05 ; 0,20[ | 135 | 74 | 61 | 118 625 581 |
| < 0,05 | 46 | 17 | 29 | 28 129 934 |
| **Total** | **678** | **461** | **217** | **817 426 362** |

La médiane est de 0,50 et la moyenne de 0,55. **375 entreprises ont une part ≥ 0,5** (284 PME, 91 grandes) : elles totalisent 590,9 M EUR. Le dénominateur médian n'est que de 4 projets ; une part de 1,00 sur 1 projet (ex. SOFTJAM, Demcon Focal) est donc peu informative, et il vaut mieux la lire avec `nb_projets_total`.

Exemples « quantique natif » (part ≥ 0,5, non signalés consultant), par financement décroissant :

| Entreprise | Pays | Type | Segment | Projets quantiques / total | Part |
|---|---|---|---|---|---|
| COLDQUANTA UK LIMITED | GB | PME | transverse | 19 / 21 | 0.90 |
| RIVERLANE LTD | GB | PME | calcul | 24 / 24 | 1.00 |
| OXFORD IONICS LIMITED | GB | PME | calcul | 13 / 13 | 1.00 |
| RIGETTI UK LIMITED | GB | PME | calcul | 12 / 12 | 1.00 |
| ORCA COMPUTING LTD. | GB | PME | calcul | 14 / 19 | 0.74 |
| TOSHIBA EUROPE LIMITED | GB | grande_entreprise | communication | 17 / 31 | 0.55 |
| QUANTUM MOTION TECHNOLOGIES LTD | GB | PME | calcul | 12 / 14 | 0.86 |
| Delft Networks B.V. | NL | PME | communication | 3 / 3 | 1.00 |
| EXAIL | FR | grande_entreprise | capteurs | 14 / 22 | 0.64 |
| ALPINE QUANTUM TECHNOLOGIES GMBH | AT | PME | calcul | 9 / 9 | 1.00 |

**97 entreprises ont `profil_consultant_ue = true`.**
- 91 via la règle 1 (≥ 15 projets CORDIS et part < 0,20), 11 via le nom, 5 cumulant les deux.
- Par type : 59 grandes entreprises et 38 PME, totalisant 115,2 M EUR.
- Les grandes entreprises signalées sont surtout des groupes industriels : EDF (2 projets quantiques sur 156 financés), AVL, Thales (20/145), Bosch Car Multimedia, Indra, Leonardo, Telefónica I+D, Infineon, Airbus, IBM Research (14/82), Bull (9/47)…
- Parmi les 38 PME signalées, les profils de montage et de gestion de projets UE et de conseil ressortent nettement. Exemples :

| Entreprise | Pays | Projets quantiques / total | Part | Déclencheur |
|---|---|---|---|---|
| EURICE EUROPEAN RESEARCH AND PROJECT OFFICE GMBH | DE | 5 / 100 | 0.05 | ≥ 15 projets UE et part < 0,20 |
| UBITECH LIMITED | CY | 3 / 64 | 0.05 | ≥ 15 projets UE et part < 0,20 |
| WINGS ICT SOLUTIONS TECHNOLOGIES PLIROFORIKIS KAI EPIKOINONION ANONYMI ETAIREIA | GR | 2 / 71 | 0.03 | ≥ 15 projets UE et part < 0,20 |
| TECHNIKON FORSCHUNGS- UND PLANUNGSGESELLSCHAFT MBH | AT | 2 / 31 | 0.06 | ≥ 15 projets UE et part < 0,20 + nom |
| AMIRES SRO | CZ | 2 / 45 | 0.04 | ≥ 15 projets UE et part < 0,20 |
| ECLIPSE FOUNDATION EUROPE GMBH | DE | 2 / 36 | 0.06 | ≥ 15 projets UE et part < 0,20 + nom |
| INTELLIGENTSIA CONSULTANTS SARL | LU | 2 / 15 | 0.13 | ≥ 15 projets UE et part < 0,20 + nom |
| DAY ONE SOCIETA A RESPONSABILITA LIMITATA | IT | 2 / 63 | 0.03 | ≥ 15 projets UE et part < 0,20 |
| TIMELEX | BE | 1 / 64 | 0.02 | ≥ 15 projets UE et part < 0,20 |
| SUITE5 DATA INTELLIGENCE SOLUTIONS LIMITED | CY | 1 / 68 | 0.01 | ≥ 15 projets UE et part < 0,20 |
| INCITES CONSULTING SA | LU | 1 / 24 | 0.04 | ≥ 15 projets UE et part < 0,20 + nom |
| DEEP BLUE SRL | IT | 1 / 109 | 0.01 | ≥ 15 projets UE et part < 0,20 |

Exemples cités par le coordinateur :
- Technikon, Ubitech, Eclipse Foundation Europe et Eurescom sont signalés.
- Zortenet ne l'est pas (2 projets quantiques sur 6, part 0,33).
- Capgemini UK (1/5, part 0,20, vue seulement dans GtR) et Capgemini Deutschland (1/1) ne le sont pas non plus : peu de projets financés rattachés à ces entités.

Pour une prospection centrée sur les « quantiques natifs », filtrer `part_quantique ≥ 0,5` et `profil_consultant_ue = false` donne 371 entreprises.

## 6. Organisations de recherche et autres (`prospects_recherche.jsonl`)

570 organisations, 3,13 Md EUR au total, en grande partie des subventions EPSRC aux universités britanniques. Le fichier compte 337 universités, 153 organismes de recherche et 80 « autre ». Par pays : GB 83, DE 79, IT 57, FR 51, ES 40, PL 22, GR 22, AT 19, NL 18, CZ 17.

Les cinq premiers par montant :

| Organisation | Projets | Total |
|---|---|---|
| University of Oxford | 70 | 196,2 M EUR |
| University of Glasgow | 72 | 146,4 M EUR |
| University of Birmingham | 59 | 136,9 M EUR |
| CNRS | 113 | 115,1 M EUR |
| TU Delft | 57 | 76,5 M EUR |

Le type « autre » regroupe des agences nationales de financement (ANR, DFG, BMFTR, Vetenskapsrådet…). Elles sont bénéficiaires CORDIS des ERA-NET Cofund QuantERA, mais ne sont pas des partenaires de consortium.

## 7. Lacunes connues et biais

**Ce que la base ne voit pas.**
- **Entreprises sans financement UE ou UK** : celles qui n'ont jamais obtenu de financement H2020, Horizon Europe, EIC, Innovate UK ou UKRI n'apparaissent pas, même si elles sont actives en quantique. La liste mesure autant la *propension à candidater* que l'activité quantique.
- **Programmes nationaux et régionaux.** Non couverts :
  - France : Bpifrance (i-Nov, PIA/France 2030, Stratégie nationale quantique), ANR ;
  - Allemagne : BMFTR (ex-BMBF), DLR ;
  - Pays-Bas : NWO, Quantum Delta NL ;
  - autres : Business Finland, régions, FEDER, ESA, Fonds européen de la défense.
  
  Les cofinancements QuantERA sont attribués dans CORDIS aux agences nationales, pas aux équipes lauréates.
- **Digital Europe** : EuroQCI nationaux (FranceQCI, NostrumQCI…) et autres projets DIGITAL ne figurent pas dans ces dumps CORDIS. La valeur `Digital Europe` du vocabulaire n'est donc jamais utilisée.
- **États-Unis** : SBIR.gov renvoyait 403 ; aucune donnée US.
- **Royaume-Uni en Horizon Europe 2021-2023** : les entités britanniques étaient « associated partners » sans contribution UE. Elles sont exclues côté CORDIS et n'apparaissent que via « Horizon Europe Guarantee » dans GtR, si le résumé passe le filtre.

**Biais de classement.**
- **Taille des entreprises GtR** : inférée ou par défaut pour 198 entreprises (§ 3.5). Les filiales britanniques de groupes étrangers et les grands groupes vus uniquement dans GtR peuvent être mal classés. Le drapeau SME de CORDIS est autodéclaré et validé, mais parfois périmé : une startup qui a grandi, ou au contraire Duality Quantum Photonics marquée `SME=false`.
- **Segment = thème des projets, pas métier de l'entreprise** : un fournisseur de cryogénie ou d'électronique de contrôle engagé dans des projets d'ordinateur quantique est classé `calcul`, comme Qblox ou Kiutra. Les projets « Quantum Internet Alliance » et les lignes pilotes Chips JU tirent de nombreuses entreprises vers `communication` ou `transverse`.

**Limites des données.**
- **Ville** : absente pour 198 entreprises GtR seules (GtR ne publie que région et code postal) ; les libellés CORDIS sont gardés tels quels (souvent en majuscules).
- **Montants** : contribution maximale signée et non paiements. Conversion GBP au taux unique du 2026-11-20 plutôt qu'au taux de chaque année. Les contrats SBRI (marchés publics de R&D précommerciale, à 100 %) sont comptés comme des financements Innovate UK.
- **Doublons résiduels** : je n'ai pas fusionné les noms qui diffèrent au-delà des formes sociales. Exemple : « Quantum Motion » (GtR) et « QUANTUM MOTION TECHNOLOGIES LTD ». Même chose pour deux PIC CORDIS de même nom (1 cas d'entreprise, Telefónica I+D).
- **Données personnelles** : je n'ai collecté aucune donnée personnelle. Quelques raisons sociales contiennent toutefois un nom de fondateur, par exemple « Robert Harrison Consulting GmbH ». Ce sont des noms d'entités juridiques publiés par la Commission.
- **Rappel non mesuré** ; la précision est estimée sur 60 projets seulement (intervalles au § 4).

## 8. Sources suivantes suggérées

1. **Digital Europe** (EuroQCI, infrastructures quantiques) : projets et bénéficiaires via le Funding & Tenders Portal (API de recherche SEDIA) ou les jeux « DIGITAL » de data.europa.eu, s'ils sont publiés.
2. **France** :
   - lauréats Bpifrance / France 2030 publiés sur data.gouv.fr ;
   - « Horizon Europe – Winning projects and participations » de data.enseignementsup-recherche.gouv.fr (déjà visible sur data.europa.eu), utile pour recouper les participants français ;
   - ANR (projets financés, open data).
3. **Allemagne** : Förderkatalog fédéral (foerderportal.bund.de), qui couvre les projets BMFTR « Quantentechnologien » avec bénéficiaire et montant.
4. **Pays-Bas, Finlande, Danemark** : Quantum Delta NL, Business Finland, Innovationsfonden (listes de lauréats).
5. **ESA** (ARTES, programmes de communication quantique) et **EDF/FED** (projets de défense quantique).
6. **Marchés publics** : TED (Tenders Electronic Daily) pour les attributaires de marchés « quantum », Contracts Finder et Find a Tender pour le Royaume-Uni. C'est le volet « marchés publics » du positionnement.
7. **Taille d'entreprise UK** : Companies House (comptes et effectifs) pour remplacer l'inférence par taux d'aide.
8. **États-Unis** (si besoin) : SBIR.gov depuis un autre réseau, ou USAspending.gov.

## 9. Reproduire

```bash
cd activite/prospects
python3 -I construire_prospects.py --cache <répertoire de travail hors dépôt>   # télécharge, interroge GtR, construit (~1 h la première fois)
python3 -I construire_prospects.py --cache <même répertoire> --hors-ligne       # reconstruit depuis le cache (~40 s)
python3 -I valider_prospects.py                                                  # 0 erreur attendue
```

Le premier lancement :
- télécharge les deux dumps CORDIS (38 et 55 Mo) dans `<cache>/opendata/` ;
- met en cache les réponses GtR dans `<cache>/cache/gtr/` et le taux BCE dans `<cache>/cache/ecb/` ;
- écrit l'échantillon à vérifier dans `<cache>/echantillon_precision_a_verifier.csv` et les statistiques dans `<cache>/statistiques_prospects.json`.

`--date-extraction AAAA-MM-JJ` fixe la date d'extraction.

Le validateur accepte les trois champs optionnels (`nb_projets_total` entier ≥ `nb_projets`, `part_quantique` entre 0 et 1 égal à `nb_projets / nb_projets_total`, `profil_consultant_ue` booléen, null admis) et le CSV à 12 ou 15 colonnes.

Il émet aussi des avertissements non bloquants :
- 242 villes manquantes ;
- 2 libellés « ressemblant à un nom de personne » vérifiés à la main : STANDARD CHARTERED BANK et COMPACT CRYOGENICS, deux entreprises.
