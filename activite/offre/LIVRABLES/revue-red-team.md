# Modèle : revue critique (« red team ») selon les critères officiels d'évaluation (service D)

La revue porte sur un brouillon reçu au moins 12 jours ouvrés avant la clôture. Elle est livrée en 5 jours ouvrés pour 20 pages au plus, en 7 jours ouvrés au-delà. Prix et conditions : [../OFFRE.md](../OFFRE.md), section 4.5.

---

## 0. Mode d'emploi, réservé à l'usage interne et à retirer de la revue livrée

### 0.1 Principe
On lit le dossier comme un évaluateur pressé, qui confronte chaque section aux **critères écrits** de l'appel et aux **résultats attendus** du topic. On note avec l'échelle officielle, puis on classe les corrections selon leur effet probable sur la note. On ne juge pas la validité scientifique : on signale les affirmations non étayées.

### 0.2 Textes de référence à charger pour chaque revue
- Horizon Europe et entreprises communes (EuroHPC JU, Chips JU) :
  - les **annexes générales du programme de travail**, en particulier l'annexe D, qui fixe les critères d'attribution, l'échelle de notation, les seuils et les pondérations ;
  - le **formulaire de candidature** de l'appel (partie B) : limites de pages et structure des sections et des tableaux ;
  - la **page du topic** : périmètre, résultats attendus, conditions propres.
- EIC (Pathfinder, Transition, Accelerator) : le **programme de travail EIC de l'année**, qui définit des critères et des seuils différents de ceux d'Horizon Europe, et le modèle annoté publié par les PCN (Access2EIC).
- Innovate UK : le **brief de la compétition** sur l'Innovation Funding Service, qui fixe les questions, le nombre de mots, la notation et les annexes autorisées.
- La politique de l'organisme financeur sur l'usage de l'IA dans les candidatures.

### 0.3 Rôles
| Tâche | Agents IA | Humain |
|---|---|---|
| Conformité formelle (pages, sections, tableaux, annexes) | Oui | Il vérifie les écarts relevés |
| Cohérence des chiffres (budget, effort, livrables, jalons, rôles) | Oui | Il confirme |
| Repérage des affirmations non sourcées, du vocabulaire générique, des acronymes non définis | Oui | Il juge si c'est pénalisant |
| Mise en regard des résultats attendus avec le texte du dossier | Pré-repérage | **Il évalue** |
| Note par critère, forces et faiblesses | Jamais seul | **Il note et rédige** |
| Les 10 corrections prioritaires | Proposition | **Il décide de l'ordre** |

Le brouillon du client n'est transmis à un outil d'IA qu'avec son accord, par une offre professionnelle qui exclut l'entraînement sur les données. Aucune section brevetable n'est transmise sans consentement spécifique ([OFFRE.md](../OFFRE.md), section 7.5).

### 0.4 Temps cible
- 6 à 8 heures pour 10 pages ;
- 8 à 10 heures pour Innovate UK ;
- 12 à 15 heures pour une partie B de 45 à 50 pages.

---

## 1. Échelles de notation (rappel, à vérifier pour chaque appel)

**Horizon Europe et entreprises communes.** Chaque critère est noté de 0 à 5, par demi-points :

| Note | Signification |
|---|---|
| 0 | Le dossier ne traite pas le critère, ou ne peut pas être évalué faute d'informations |
| 1 | Insuffisant : le critère est mal traité ou présente de graves faiblesses |
| 2 | Passable : le critère est globalement traité, mais avec des faiblesses importantes |
| 3 | Bon : le critère est bien traité, avec plusieurs faiblesses |
| 4 | Très bon : le critère est très bien traité, avec quelques faiblesses |
| 5 | Excellent : tous les aspects du critère sont traités ; faiblesses mineures seulement |

**Seuils et pondérations usuels :**
- 3 sur 5 par critère ;
- 10 sur 15 au total ;
- pour les actions d'innovation (IA), le critère Impact pèse 1,5 dans le classement.

Ces valeurs sont **à confirmer dans l'annexe D et dans le programme de travail de l'appel.** L'EIC applique ses propres seuils et pondérations.

**Innovate UK.** Chaque question notée est évaluée par des évaluateurs indépendants. La question de périmètre (« scope ») est éliminatoire. L'échelle et le nombre de questions figurent dans le brief.

---

## 2. Modèle à remplir

```markdown
# Revue critique : {acronyme} / {identifiant_appel}

| | |
|---|---|
| Client | {raison sociale} |
| Appel | {intitulé} ({identifiant_appel}), {type d'action}, clôture {date et heure} |
| Version relue | {nom du fichier, date, nombre de pages} |
| Textes de référence | {annexe D (version), formulaire (version), page du topic (date)} |
| Date de la revue | {date} |
| Auteur | {Prénom Nom}, {Nom commercial} |
| Usage de l'IA | {Accepté / Refusé}. Journal en annexe. |
| Statut | Confidentiel |

## 1. Synthèse
| Critère | Note estimée | Seuil | Commentaire en une ligne |
|---|---|---|---|
| Excellence | {x}/5 | 3 | |
| Impact | {x}/5 | 3 | |
| Qualité et efficacité de la mise en œuvre | {x}/5 | 3 | |
| **Total** | **{x}/15** | 10 | |

*Note estimée par un relecteur qui n'est pas un évaluateur officiel et qui ne juge pas la validité scientifique. C'est un outil de priorisation, pas une prédiction.*

**Les 3 risques principaux :** {…}

## 2. Rapport d'évaluation simulé, critère par critère
Pour chaque critère, rédiger comme un évaluateur : des forces, puis des faiblesses, chacune rattachée à un sous-critère et à une page.

### 2.1 Excellence
**Forces :** {…}
**Faiblesses :** {…}

### 2.2 Impact
**Forces :** {…}
**Faiblesses :** {…}

### 2.3 Qualité et efficacité de la mise en œuvre
**Forces :** {…}
**Faiblesses :** {…}

## 3. Les 10 corrections prioritaires
| # | Section et page | Problème | Critère touché | Correction proposée | Effort | Effet attendu |
|---|---|---|---|---|---|---|
| 1 | | | | | {h} | {fort / moyen / faible} |

## 4. Conformité et cohérence
(Résultats de la liste de contrôle de la section 3 du présent modèle. Ne lister que les écarts.)

## 5. Ce que cette revue n'a pas évalué
- La validité scientifique et technique des hypothèses, des résultats préliminaires et des performances annoncées.
- {Autres exclusions propres à la mission.}

## 6. Mentions
- **Mon historique au {date} :** {0} dossier soumis, {0} financé ([registre public]({site}/resultats)). Je ne suis pas évaluateur officiel.
- **Aucune garantie de résultat.** Responsabilité plafonnée au prix payé.
- **Usage de l'IA :** {outils, tâches}. Le texte de cette revue a été rédigé par un humain.
- **Rappel :** si vous avez utilisé l'IA pour votre dossier, le programme peut exiger que vous le déclariez (outils et manière). Paragraphe proposé : {…}

## Annexe : journal d'usage de l'IA
| Date | Outil | Tâche | Données transmises | Vérification humaine |
|---|---|---|---|---|
```

---

## 3. Liste de contrôle

### 3.1 Horizon Europe et entreprises communes (RIA, IA) : Excellence
*Sous-critères reformulés d'après l'annexe D ; reprendre le texte exact du programme de travail de l'appel.*

**Objectifs et ambition (section 1.1 du formulaire)**
- [ ] Les objectifs sont clairs, mesurables, réalistes et atteignables dans la durée du projet.
- [ ] Le lien entre les objectifs et le **périmètre du topic** est explicite. Les mots clés du topic sont repris, sans copier-coller.
- [ ] L'état de l'art est décrit, avec des références vérifiables, et le dossier montre en quoi il va au-delà.
- [ ] Le TRL de départ et le TRL d'arrivée sont annoncés et justifiés. Le saut de TRL est plausible dans la durée.
- [ ] Les affirmations de performance (temps de cohérence, fidélités, taux d'erreur, « avantage quantique ») sont comparées à une **référence classique ou à l'état de l'art**, avec leur source.

**Méthodologie (section 1.2)**
- [ ] Les concepts, les modèles et les hypothèses sont exposés, et les hypothèses critiques sont identifiées.
- [ ] L'approche interdisciplinaire est justifiée, quand elle est pertinente.
- [ ] La dimension de genre dans le contenu de la recherche est traitée, ou son absence est justifiée.
- [ ] Les pratiques de science ouverte sont décrites : publications en accès ouvert, partage des données et des logiciels.
- [ ] Un plan de gestion des données (données FAIR) est annoncé.
- [ ] Les solutions de repli aux points techniques risqués sont décrites.
- [ ] L'accès aux infrastructures nécessaires (systèmes quantiques, HPC, salles blanches, lignes pilotes) est démontré, par exemple par une lettre ou un accord.

### 3.2 Horizon Europe et entreprises communes : Impact
**Chemins vers l'impact (section 2.1)**
- [ ] Chaque **résultat attendu** (« expected outcome ») du topic est repris, avec la contribution concrète du projet.
- [ ] Les impacts plus larges de la destination du programme de travail sont reliés au projet.
- [ ] L'ampleur et la portée des impacts sont **chiffrées** (marché, utilisateurs, coûts évités, souveraineté d'approvisionnement), avec les sources et les hypothèses.
- [ ] Les obstacles à l'impact sont identifiés (réglementation, adoption, dépendance au matériel) et des mesures y répondent.

**Mesures pour maximiser l'impact (section 2.2)**
- [ ] Le plan de diffusion, d'exploitation et de communication est distinct par public, avec des indicateurs et un calendrier.
- [ ] La stratégie d'exploitation est précise : qui exploite quoi, comment et quand. La stratégie de PI couvre les brevets, les licences et la liberté d'exploitation.
- [ ] La normalisation est mentionnée si elle est pertinente, par exemple les travaux de normalisation quantique.
- [ ] La section de synthèse (2.3, ou le tableau canevas) est cohérente avec le texte.

### 3.3 Horizon Europe et entreprises communes : Qualité et efficacité de la mise en œuvre
**Plan de travail et ressources (section 3.1 et tableaux)**
- [ ] Les lots de travail ont des objectifs, des tâches, un responsable, des dates de début et de fin.
- [ ] Les livrables sont datés et vérifiables ; leur type et leur niveau de diffusion sont indiqués.
- [ ] Les jalons ont un moyen de vérification.
- [ ] Le **tableau des risques** couvre les risques techniques, de consortium, d'accès au matériel et réglementaires, avec leur probabilité ou leur gravité et des mesures d'atténuation.
- [ ] L'effort en personnes-mois par partenaire et par lot est cohérent avec les tâches et avec le budget.
- [ ] La sous-traitance est justifiée et ne concerne pas des tâches centrales.
- [ ] Les achats et autres coûts sont justifiés lorsque le formulaire l'exige, par exemple quand les achats dépassent 15 % des frais de personnel (seuil à vérifier dans le formulaire).
- [ ] Le Gantt et le PERT sont lisibles et concordent avec les tableaux.

**Capacité des participants et du consortium (section 3.2)**
- [ ] Le rôle de chaque partenaire est indispensable et décrit ; aucun partenaire ne sert seulement à remplir une case.
- [ ] Les compétences sont démontrées par des réalisations vérifiables : projets, produits, publications.
- [ ] Les compétences critiques ne reposent pas sur une seule personne ou un seul partenaire, ou alors ce risque est traité.
- [ ] L'équilibre du consortium est montré (industrie, recherche, utilisateurs finaux, géographie) et justifié au regard du topic.

### 3.4 EIC : grille propre à recopier depuis le programme de travail de l'année
- **Pathfinder :** critères Excellence, Impact et Qualité et efficacité de la mise en œuvre, avec des sous-critères propres à l'EIC : vision à long terme, percée scientifique vers une technologie, nouveauté, caractère « haut risque, haut gain ». Les pondérations et seuils de l'EIC diffèrent d'Horizon Europe : les recopier.
- **Accelerator :** critères Excellence, Impact, et Niveau de risque, mise en œuvre et besoin d'un soutien de l'Union. Hors périmètre pour la rédaction ; une revue est possible si le client rédige lui-même.
- [ ] Le dossier traite explicitement chaque sous-critère du programme de travail EIC de l'année, dans l'ordre.
- [ ] Pour Pathfinder Open 2027, la première étape est fixée au 25 février 2027 ([Innovate UK Business Connect](https://iuk-business-connect.org.uk/quantum/)). Vérifier le format et la limite de pages dans le programme de travail.

### 3.5 Innovate UK : questions standard
*Ensemble standard des compétitions de R&D collaborative. Chaque compétition peut retirer, ajouter ou reformuler des questions, et le nombre de mots varie : suivre le brief.*

| Q | Thème | Points de contrôle |
|---|---|---|
| Périmètre | Adéquation au thème de la compétition (éliminatoire) | Le projet entre dans le périmètre écrit ; les mots clés du brief sont repris |
| 1 | Besoin ou défi | Besoin de l'entreprise, verrou technologique ou opportunité de marché ; pourquoi maintenant ; état de l'art |
| 2 | Approche et innovation | Méthode adaptée au besoin ; caractère innovant comparé aux alternatives ; liberté d'exploitation et PI |
| 3 | Équipe et ressources | Rôles, compétences et expérience ; lacunes et façon de les combler ; équipements ; sous-traitants justifiés |
| 4 | Connaissance du marché | Marchés visés (taille, structure, dynamique), clients, concurrence, chaîne de valeur, sources chiffrées |
| 5 | Résultats et accès au marché | Stratégie commerciale, calendrier, revenus prévus, exploitation et protection de la PI, rôle de chaque partenaire |
| 6 | Impacts plus larges | Effets économiques, sociaux, environnementaux et régionaux ; inclusion |
| 7 | Gestion de projet | Plan, Gantt, jalons, gouvernance, suivi |
| 8 | Risques | Registre des risques techniques, commerciaux, de gestion et réglementaires ; atténuation ; responsables |
| 9 | Additionnalité | Pourquoi un financement public est nécessaire ; ce qui se passe sans lui ; effet sur l'investissement en R&D |
| 10 | Coûts et rapport qualité-prix | Coûts justifiés et cohérents avec le plan ; contribution des partenaires ; rapport qualité-prix pour le contribuable |

- [ ] Le nombre de mots est respecté pour chaque question, et les annexes autorisées sont utilisées à bon escient.
- [ ] Les réponses ne renvoient pas à d'autres questions pour l'information essentielle : chaque question est évaluée seule.
- [ ] Les montants de la partie financière concordent avec les questions 7 et 10.

### 3.6 Contrôles transversaux, quel que soit le programme
**Conformité formelle**
- [ ] Limite de pages, police, marges et format respectés. Les pages excédentaires peuvent être ignorées par les évaluateurs.
- [ ] Toutes les sections et tous les tableaux obligatoires sont présents, numérotés comme dans le formulaire.
- [ ] Les annexes obligatoires sont présentes : lettres, déclarations, auto-évaluations éthique et sécurité.

**Cohérence**
- [ ] Même acronyme, même durée et mêmes montants dans les parties A et B et dans les tableaux.
- [ ] Chaque partenaire cité dans le texte a des tâches, de l'effort et un budget, et inversement.
- [ ] Les livrables et jalons cités dans le texte existent dans les tableaux.

**Lisibilité pour un évaluateur**
- [ ] Les deux premières pages disent ce que fait le projet, pourquoi, avec qui, et ce qui en sortira.
- [ ] Les acronymes sont définis ; les figures sont lisibles en noir et blanc.
- [ ] Il n'y a pas de remplissage, ni de formules génériques interchangeables d'un projet à l'autre.

**Risques liés à l'IA**
- [ ] Le dossier ne contient pas de passages à l'allure générique, typiques d'un texte généré, sans contenu propre au projet. Pour mémoire, le JRC associe un usage intensif de texte généré par LLM à de moins bonnes notes ([JRC146131](https://publications.jrc.ec.europa.eu/repository/handle/JRC146131)).
- [ ] Chaque référence bibliographique existe et dit ce qu'on lui fait dire. Vérifier un échantillon d'au moins 30 %, et toutes les références qui portent un argument clé.
- [ ] La déclaration d'usage de l'IA est présente si le formulaire l'exige : outils utilisés et manière de les utiliser.

**Spécificités du quantique**
- [ ] Les chiffres matériels (nombre de qubits, fidélités, temps de cohérence, sensibilités) sont datés, sourcés et comparés à l'état de l'art.
- [ ] Les applications annoncées tiennent compte du calendrier réaliste du matériel, sans promesse d'utilité à court terme non étayée.
- [ ] Les questions de double usage et de contrôle des exportations sont traitées dans l'auto-évaluation de sécurité. Pour mémoire, des articles quantiques figurent à l'annexe I du règlement 2021/821 depuis la mise à jour du règlement délégué 2025/2003.
- [ ] La dépendance à un fournisseur de matériel ou à un accès cloud est identifiée comme un risque, avec un plan B.
