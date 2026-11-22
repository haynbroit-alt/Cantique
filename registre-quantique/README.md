# Registre quantique : affirmations datées sur la route du Q-Day (v0)

Ce dossier tient un **registre public, lisible par machine et horodaté** des affirmations datées sur la route de l'informatique quantique tolérante aux fautes et du Q-Day, c'est-à-dire l'arrivée d'un ordinateur quantique capable de casser la cryptographie à clé publique actuelle (CRQC). Il consigne :

- les feuilles de route des fabricants (qubits physiques et logiques, fidélités, dates promises) ;
- les démonstrations publiées ;
- les étapes du Quantum Benchmarking Initiative (QBI) de la DARPA ;
- les revendications d'avantage quantique et leurs contestations ;
- les estimations de ressources pour casser RSA et les courbes elliptiques ;
- les enquêtes et avis d'experts sur le Q-Day, et les marchés prédictifs ;
- les prix publics d'accès aux processeurs ;
- les projections financières de l'ère des SPAC et les résultats publiés ;
- quelques échéances publiques de migration post-quantique et de protocoles de chaînes de blocs.

Chaque entrée porte sa source, sa date et son statut. **Aucune n'est un verdict maison.**

## Pourquoi ce registre

Plusieurs outils couvrent une partie du sujet, mais aucun ne tient l'historique des promesses et des livraisons (absence constatée lors des recherches, confiance moyenne). Metriq (Unitary Foundation) publie des mesures de performance sur une dizaine de processeurs. Le Quantum Advantage Tracker, convoqué par IBM, recense les revendications d'avantage. Les jugements de la DARPA font autorité mais ne forment pas un suivi public continu. PostQuantum a publié en juillet 2026 un tableau ponctuel des projections de SPAC face aux résultats. Le registre relie ces sources par des identifiants stables et des dates. Chaque mois enregistré est un historique que personne ne pourra reconstituer plus tard avec la même datation.

Premiers usages visés : les développeurs de protocoles et les dépositaires d'actifs numériques, qui cherchent des seuils de déclenchement fondés sur des faits ; le chapitre « horizon de la menace » des dossiers de migration post-quantique ; les analystes, journalistes et investisseurs.

## Ce que le registre n'est pas

- Ce n'est **pas un avis sur la physique**. Le registre ne dit pas si un résultat « tient » une promesse ; il cite ceux qui le disent.
- Ce n'est **pas un classement** des fabricants ni un score composite.
- Ce n'est **pas un conseil en investissement**. Il ne recommande l'achat ni la vente d'aucun titre.

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `affirmations.jsonl` | Les données : une affirmation par ligne, en JSON, encodée en UTF-8. C'est la seule source de vérité. |
| `schema.json` | Le schéma JSON (draft 2020-12) d'une ligne, avec le vocabulaire contrôlé des types, statuts, types de source et métriques. |
| `valider.py` | Le contrôle de cohérence. Il n'utilise que la bibliothèque standard, plus `jsonschema` si le paquet est installé. |
| `generer_vue.py` | Il construit `registre.md` à partir du JSONL, avec la bibliothèque standard seulement. |
| `registre.md` | La vue lisible, générée : par acteur, en ordre chronologique, plus une section Q-Day. On ne la modifie jamais à la main. |

## Méthode : consigner sans trancher

1. **Consigner l'affirmation telle que la source la formule.** L'énoncé est une citation courte ou une paraphrase proche, dans la langue de la source (souvent l'anglais). Les passages entre guillemets (“ ” ou « ») sont des citations exactes quand `verbatim` vaut `true`.
2. **Ne changer un statut que sur la foi d'une source.** Un statut `verifie_tiers`, `contredit`, `en_retard` ou `retire` exige `statut_source_url`, et `valider.py` refuse la ligne sinon. Sont admises : une publication évaluée par les pairs, une annonce de la DARPA ou d'une autre autorité publique, un dépôt réglementaire, une mesure ou une reproduction indépendante, l'attribution d'un prix par un tiers, ou une déclaration ultérieure de l'acteur lui-même.
3. **Enregistrer une contestation comme une entrée à part**, de type `refutation`, liée par `liens` à l'affirmation visée. L'affirmation contestée garde son statut tant qu'aucune source ne la dit réfutée. Une critique d'analyste ne suffit pas à la déclarer « contredite ».
4. **Reprendre les métriques des autres** (Metriq, DARPA, publications évaluées par les pairs) sans les recalculer.
5. **Signaler les conflits d'intérêts connus** dans `conflit_interet` : un fabricant qui estime sa propre feuille de route, un vendeur à découvert, une enquête financée par un fabricant, un grand détenteur de bitcoins qui juge la menace lointaine.
6. **Garder ce qui est incertain plutôt que le taire.** Un fait que la source signale comme non vérifié, contradictoire ou connu seulement par un résumé reste dans le registre avec le statut `inconnu`, et la note explique pourquoi. Une incertitude qui ne porte que sur la date est signalée dans la note, sans changer le statut.
7. **Relire chaque entrée.** Des agents d'IA peuvent préparer les entrées, mais une personne vérifie la source avant chaque commit. L'enquête 2026 de la Unitary Foundation indique que seuls 42,9 % des développeurs quantiques vérifient toujours ce que produit l'IA : la relecture humaine est la condition de la crédibilité.

### Les statuts

| Code | Signification | Preuve exigée |
|---|---|---|
| `promis` | Engagement ou cible future, non échue ou sans information de livraison postérieure. | La source de l'affirmation. |
| `demontre` | L'acteur ou l'auteur a publié ou annoncé le résultat, le chiffre ou la cible, sans vérification indépendante revendiquée. Pour un prix, une enquête, une estimation ou un résultat financier, ce code signifie « publié ou constaté dans la source ». | La source de l'affirmation. |
| `verifie_tiers` | Un tiers indépendant le confirme. | `statut_source_url` obligatoire. |
| `contredit` | Une source tierce ou un dépôt ultérieur rapporte un résultat contraire ou le réfute. | `statut_source_url` obligatoire. |
| `en_retard` | L'échéance est passée et une source constate l'absence de livraison. | `statut_source_url` et `echeance_promise` obligatoires ; l'échéance doit être dépassée à la date de la source du statut. |
| `retire` | L'acteur lui-même a retiré ou remplacé l'affirmation (par exemple une prévision relevée). | `statut_source_url` obligatoire. |
| `inconnu` | Fait non vérifié, contradictoire ou connu par un simple résumé, ou échéance passée sans information. | La note explique l'incertitude. |

Le registre ne passe jamais une promesse en `en_retard` du seul fait que la date est passée. `valider.py` émet un avertissement quand une entrée `promis` a une échéance dépassée : il faut alors chercher une source, et le statut ne change qu'avec elle.

### Les dates

- `date_affirmation` accepte `AAAA`, `AAAA-MM` ou `AAAA-MM-JJ`, selon la précision de la source.
- `precision_date: "au_plus_tard"` signale une source non datée : l'affirmation existait au plus tard à la date indiquée, souvent la date de consultation.
- Pour une page tarifaire, `date_affirmation` est la date d'observation de la page.
- Pour une enquête ou un marché prédictif, `echeance_promise` est l'horizon de la question posée (par exemple « d'ici 2035 »).
- `date_consultation` est la date de consultation de la source. `date_saisie` est la date d'entrée de la ligne dans le registre ; elle ne change pas.

## Format des données

Chaque ligne de `affirmations.jsonl` est un objet JSON. Le schéma complet est dans `schema.json` ; les champs principaux sont résumés ci-dessous.

| Champ | Obligatoire | Contenu |
|---|---|---|
| `id` | oui | Identifiant stable en minuscules (`ibm-starling-2029`). Il ne change jamais. |
| `acteur` | oui | Organisation ou auteur qui fait l'affirmation. |
| `acteurs_associes` | non | Organisations concernées (entreprises retenues par la DARPA, partenaires). |
| `type` | oui | `feuille_de_route`, `demonstration`, `estimation_ressources`, `programme_public`, `prix`, `revendication_avantage`, `refutation`, `financement`, `enquete_experts`, `marche_predictif`, `resultat_financier`. |
| `date_affirmation`, `precision_date` | oui, non | Date de l'affirmation et sa précision. |
| `echeance_promise` | oui | Date cible ou horizon, sinon `null`. |
| `metrique` | oui | Grandeur tirée du vocabulaire contrôlé (`qubits_logiques`, `portes_toffoli`, `taux_erreur_logique`, `prix_minute`, `probabilite_crqc`…). |
| `valeur`, `comparateur`, `valeur_min`, `valeur_max`, `unite` | oui, non, non, non, oui | Valeur (nombre ou chaîne), relation (`<` pour « moins de », `~` pour « environ »), bornes d'une plage, unité. |
| `mesures_complementaires` | non | Autres chiffres de la même affirmation (par exemple les portes Toffoli associées à un nombre de qubits logiques). |
| `enonce`, `verbatim` | oui, non | Citation ou paraphrase proche, dans la langue de la source. |
| `statut`, `statut_source_url`, `statut_date` | oui, selon le statut, non | Statut et source qui le fonde. |
| `source_url`, `source_titre`, `source_type` | oui | Source principale et sa nature (`vendeur`, `revue_a_comite`, `preprint`, `gouvernement`, `depot_reglementaire`, `presse`, `analyste`, `enquete`, `autre`). `vendeur` couvre toute communication de l'acteur lui-même ou de son partenaire commercial. |
| `sources_complementaires` | non | Autres sources rapportant la même affirmation. |
| `conflit_interet` | oui | Conflit d'intérêts connu, sinon `null`. |
| `date_consultation`, `date_saisie` | oui | Dates complètes `AAAA-MM-JJ`. |
| `liens` | oui | Identifiants des entrées liées (liste éventuellement vide). Une réfutation doit pointer vers ce qu'elle conteste. |
| `note` | oui | Précisions et réserves en français, sinon `null`. |

Deux types s'ajoutent à la liste de départ : `marche_predictif`, pour ne pas confondre un marché peu liquide avec une enquête d'experts, et `resultat_financier`, pour mettre les chiffres d'affaires publiés en regard des projections. Le type de source `autre` couvre les marchés prédictifs, Wikipedia et les registres tiers.

## Ajouter une entrée

1. Trouver la source primaire. À défaut, prendre la meilleure source secondaire et le dire dans `note`.
2. Choisir un identifiant de la forme `acteur-sujet-date` (par exemple `quantinuum-helios-erreur-logique-2026-10`), qui ne sera plus jamais modifié.
3. Remplir tous les champs obligatoires. Mettre une seule affirmation par ligne : une feuille de route qui fixe trois échéances donne trois lignes ; les chiffres d'une même affirmation vont dans `mesures_complementaires`.
4. Si la métrique n'existe pas, l'ajouter d'abord dans `schema.json` (liste `$defs.metrique`), puis son libellé dans `METRIQUES` de `generer_vue.py`.
5. Lancer `python3 valider.py`, corriger jusqu'à « Résultat : OK », puis `python3 generer_vue.py`.
6. Faire relire la ligne par une seconde personne, source ouverte, puis faire un commit dont le message cite la source.

## Corriger une entrée ou changer un statut

- **Nouveau fait** (livraison, report, réfutation, prévision relevée) : ajouter une **nouvelle ligne** qui cite sa source et la relier par `liens`. Si cette source justifie un changement de statut de l'affirmation d'origine, mettre à jour `statut`, `statut_source_url` et `statut_date`, et compléter `note` (« statut passé de promis à contredit le AAAA-MM-JJ »).
- **Erreur matérielle** (chiffre mal recopié, URL cassée, mauvaise date) : corriger en place. Le message de commit décrit la correction et cite la source.
- **Entrée sans fondement** (la source ne dit pas ce qui est consigné) : la retirer par un commit explicite qui en donne la raison. Ne jamais réutiliser son identifiant.
- **Demande d'un acteur cité** : elle est acceptée si elle s'appuie sur une source publique, et traitée comme ci-dessus.

## Politique de correction

- Les corrections sont des lignes nouvelles ou des mises à jour de statut qui citent leur source.
- L'historique n'est jamais réécrit en silence : il est celui du dépôt git. Chaque modification passe par un commit qui en donne la raison, et on ne réécrit pas l'historique publié (pas de `git push --force` sur la branche publique).
- Les identifiants sont stables. Une entrée retirée laisse une trace dans l'historique git et son identifiant n'est pas réutilisé.
- Les statuts ne bougent que sur source. Le registre ne qualifie jamais un résultat de lui-même.

## Valider et générer la vue

```sh
python3 valider.py                         # contrôle tout affirmations.jsonl ; code de sortie 1 en cas d'erreur
python3 valider.py --aujourdhui 2026-11-22 # date de référence pour les avertissements d'échéance
python3 valider.py --strict                # les avertissements font aussi échouer
python3 generer_vue.py                     # réécrit registre.md
```

`valider.py` contrôle que :

- chaque ligne est un objet JSON valide ;
- les champs obligatoires sont présents et aucun champ inconnu n'apparaît ;
- les valeurs appartiennent au vocabulaire du schéma ;
- les dates sont des dates ISO réelles, et aucune affirmation n'est postérieure à sa saisie ;
- les identifiants sont uniques et les liens pointent vers des identifiants existants ;
- les URL commencent par `http` ;
- les règles de statut et de réfutation décrites plus haut sont respectées.

Il affiche ensuite un résumé par type, statut, acteur et type de source. Si `jsonschema` est installé, chaque ligne est en plus validée contre `schema.json`.

## Droits

Tous droits réservés par le propriétaire du dépôt. Aucune licence n'est accordée sur les données ni sur le code : la licence de diffusion sera choisie par le propriétaire ou par un éventuel acquéreur.

Les énoncés reprennent de courts extraits de sources tierces, à titre de citation, et chaque source reste soumise à ses propres droits.

## État de la version 0 (22 novembre 2026)

- **158 affirmations**, toutes sourcées par une URL. Par type : 44 feuilles de route, 20 démonstrations, 15 prix, 14 enquêtes ou avis d'experts, 14 programmes publics, 13 financements, 12 estimations de ressources, 12 résultats financiers, 7 réfutations ou contestations, 4 marchés prédictifs et 3 revendications d'avantage.
- Par statut : 87 annoncées ou publiées, 39 promises, 23 inconnues, 5 contredites, 2 retirées ou remplacées, 2 vérifiées par un tiers.
- Le seuil de la version publique est de 150 affirmations sourcées au 31 janvier 2027. Il est atteint en nombre brut. Sans les 23 entrées au statut `inconnu`, il en reste 135 : il en faut **encore 15** pour l'atteindre avec des entrées établies, ou autant d'entrées `inconnu` confirmées sur source primaire.
- La v0 a été constituée à partir de notes de recherche internes datées du 22 novembre 2026. Les sources n'ont pas été rouvertes une à une lors de la saisie, et `date_consultation` reprend la date de ces notes. Les champs `source_titre` reprennent les libellés des notes plutôt que les titres exacts. Plus de la moitié des sources principales sont de la presse spécialisée ou des analystes. Une relecture humaine de chaque ligne, source ouverte, s'impose avant toute publication.
- Lacunes connues : feuille de route datée de Google ; sources primaires de Quantinuum (Apollo), Microsoft (Majorana, 2029) et PsiQuantum (dates de livraison) ; feuilles de route chiffrées de Pasqal, QuEra, Atom Computing et Alice & Bob ; historique entrée par entrée du Quantum Advantage Tracker ; résultats de Metriq ; grille tarifaire complète d'Amazon Braket et d'Azure Quantum.

## Feuille de route (prévue, rien n'est encore réalisé)

| Étape | Contenu | Horizon prévu |
|---|---|---|
| Relecture et compléments | Relire les 158 lignes, source ouverte ; remplacer les libellés par les titres exacts ; résoudre ou confirmer les 23 entrées `inconnu` ; combler les lacunes ci-dessus. | Avant le 31 janv. 2027 |
| Version 0 publique | Publier le registre, cette méthode et la politique de correction, avec au moins 150 affirmations sourcées. | 31 janv. 2027 |
| `llms.txt` | Un fichier `llms.txt`, sur le modèle de DefiLlama, pour que les agents d'IA trouvent et citent les données directement. | Févr. à mai 2027 |
| Export ouvert et API | Des exports datés et versionnés (JSONL, CSV) à chaque version, puis une API de lecture. | Févr. à mai 2027 |
| Serveur MCP | Un serveur MCP qui expose les affirmations, leurs statuts et leurs sources aux assistants de code et aux agents. | Févr. à mai 2027 |
| Lettre mensuelle | Une lettre mensuelle : nouvelles affirmations, changements de statut et leurs sources, échéances du mois. | À partir de févr. 2027 |
| Gouvernance | Un petit comité consultatif de chercheurs (par exemple dans la communauté de la Unitary Foundation) ; proposer à Metriq une articulation plutôt qu'une concurrence. | 2027 |
| Rapport trimestriel | Un rapport trimestriel sur l'état des preuves. | À partir de juin 2027 |
