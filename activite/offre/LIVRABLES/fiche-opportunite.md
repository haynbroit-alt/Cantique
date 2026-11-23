# Modèle : fiche opportunité (service A, gratuit)

La fiche opportunité est le produit d'appel de l'offre. Elle tient sur une page et montre qu'un appel ouvert correspond peut-être à ce que l'entreprise a déjà financé. Elle ne vaut pas avis d'éligibilité. Elle sert d'amorce aux séquences de prospection ([../../prospection/SEQUENCES.md](../../prospection/SEQUENCES.md)).

---

## 0. Mode d'emploi, réservé à l'usage interne et à retirer de la fiche envoyée

### 0.1 Données d'entrée
Les données d'entrée suivent [activite/CONTRAT.md](../../CONTRAT.md) :
- l'enregistrement du prospect dans `activite/prospects/prospects.jsonl` : `nom`, `pays`, `type_org`, `segment`, `segment_justification`, `financements_obtenus[]` et `sources` ;
- l'enregistrement de l'opportunité dans `activite/opportunites/opportunites.jsonl` : `identifiant_appel`, `cloture`, `pays_eligibles`, `types_eligibles`, `consortium_requis`, `segments`, `trl`, `source_url`, `confiance` et `date_verification` ;
- la sortie de `activite/outils/rapprocher.py` : score, raisons, réserves et liens. Le moteur ne décide jamais seul de l'éligibilité : il signale, un humain confirme.

### 0.2 Règles de production
1. **Une page au maximum**, soit 350 à 450 mots.
2. **Uniquement des données publiques sur l'organisation.** Aucune donnée personnelle : aucun nom de salarié, aucun e-mail nominatif.
3. **Une source par fait,** sous forme de lien vers la page publique : fiche CORDIS, Gateway to Research, page officielle de l'appel.
4. **Pas d'envoi sans vérification du jour.** Le jour de l'envoi, il faut vérifier la date et l'heure de clôture sur la page officielle du topic, et pas seulement dans `opportunites.jsonl`. Si `confiance` vaut `faible`, la fiche n'est pas envoyée.
5. **Pas de spéculation sur des informations non publiques.** On écrit « d'après vos projets publics », jamais « vous travaillez sur ».
6. **Aucune promesse.** Pas de « vous êtes éligible », mais « points à vérifier ».
7. **Un humain relit et valide chaque fiche** à l'aide de la liste de contrôle ci-dessous. Ce temps est compté dans les métriques du plan.

### 0.3 Liste de contrôle avant envoi
- [ ] Le nom de l'entreprise, son pays et son segment correspondent à sa page publique.
- [ ] Chaque financement cité ouvre bien la bonne fiche publique, et le montant indiqué est la contribution de l'entreprise, pas le budget total du projet.
- [ ] La date et l'heure de clôture ont été revérifiées aujourd'hui sur la page officielle, fuseau horaire compris.
- [ ] L'appel est toujours ouvert ou à venir. Il n'est ni suspendu ni annulé.
- [ ] Les restrictions éventuelles de pays ont été lues, par exemple pour une entreprise britannique visant un appel d'une entreprise commune.
- [ ] La fiche donne au moins un point à vérifier ; elle n'est jamais rassurante sans réserve.
- [ ] Le lien vers le PCN, le réseau EEN ou le service d'assistance de l'appel est présent.
- [ ] Les mentions de pied de page sont présentes : données publiques, absence de garantie, IA déclarée, historique réel et désinscription.
- [ ] La fiche ne compte pas plus de 450 mots.
- [ ] Il n'y a pas de doublon : cette entreprise n'a pas déjà reçu de fiche pour cet appel, et elle ne figure pas dans la liste d'opposition.

---

## 1. Modèle à remplir

```markdown
# Fiche opportunité : {nom} × {identifiant_appel}

*Fiche gratuite, établie le {date} à partir de données publiques uniquement. Ce n'est ni un avis d'éligibilité, ni une recommandation de candidater.*

## Ce que disent les sources publiques sur vos financements
| Programme | Projet (acronyme) | Période | Contribution à {nom} | Rôle | Source |
|---|---|---|---|---|---|
| {programme} | {acronyme} | {debut} → {fin} | {contribution_eur} € | {role} | [fiche publique]({source_url}) |

Segment retenu : **{segment}**. Justification : {segment_justification}.

## L'appel
- **{intitule}** ({identifiant_appel}), {financeur}, {programme}.
- **Clôture : {cloture}**, à {heure} ({fuseau}). Vérifiée le {date_verification} sur la [page officielle]({url}).
- Nature : {nature}. Type d'action : {type_action ou « à vérifier »}. Budget : {budget_total_eur} €. Montant indicatif par projet : {montant_par_projet_eur ou « non publié »}.
- Consortium : {consortium_requis → « exigé, au moins N entités » / « non exigé »}. Pays éligibles : {pays_eligibles}.

## Pourquoi cet appel pourrait vous concerner
1. {raison 1, reliée à un fait public, par exemple « votre projet {acronyme} portait sur {mots-clés} ; l'appel vise {résultat attendu} »}
2. {raison 2}
3. {raison 3, facultative}

## À vérifier avant d'y consacrer du temps
- {réserve 1, par exemple « type d'action et taux de financement non confirmés sur la page du topic »}
- {réserve 2, par exemple « éligibilité des entités britanniques à cet appel d'entreprise commune »}
- {réserve 3, par exemple « consortium à constituer en moins de N semaines »}

## Effort et calendrier indicatifs
Il reste **{N} semaines** avant la clôture. Un dossier de ce type demande en général {fourchette} personnes-jours côté candidat. {Phrase de réalisme : « faisable seulement si un consortium existe déjà » ou « délai confortable »}.

## Aide gratuite
Le Point de contact national de votre pays ({lien PCN}), le réseau Enterprise Europe Network ({lien EEN}) et le service d'assistance de l'appel ({lien}) répondent gratuitement.

## Pour aller plus loin
Si vous le souhaitez, une **note d'éligibilité et d'adéquation** tranche en 5 jours ouvrés : go, go sous conditions ou no-go, avec les justifications. Elle coûte 490 € HT (245 € pour les 5 premiers clients) et elle est remboursée si je la livre en retard.

---
*{Nom commercial}, {Prénom Nom}, {e-mail}. Fiche préparée avec des outils d'IA sur des sources publiques, puis vérifiée et rédigée par un humain. Elle peut contenir des erreurs ; aucune garantie de résultat. Mon historique : 0 dossier accompagné à ce jour ([registre public]({site}/resultats)). Pour ne plus recevoir de fiches : répondez « stop ».*
```

---

## 2. Exemple rempli (entreprise fictive, appel réel)

L'entreprise « Exemple Quantum SAS » est fictive ; elle reprend l'exemple de [CONTRAT.md](../../CONTRAT.md). L'appel QML-07 est réel. Les informations qui ne sont pas confirmées sont marquées « à vérifier ».

> # Fiche opportunité : Exemple Quantum SAS × HORIZON-JU-EUROHPC-2026-QML-07
>
> *Fiche gratuite, établie le 7 décembre 2026 à partir de données publiques uniquement. Ce n'est ni un avis d'éligibilité, ni une recommandation de candidater.*
>
> **Ce que disent les sources publiques sur vos financements**
>
> | Programme | Projet | Période | Contribution | Rôle | Source |
> |---|---|---|---|---|---|
> | Horizon Europe | EXEMPLE (fictif) | 2024-01 → 2027-12 | 512 000 € | participant | fiche CORDIS (fictive) |
>
> Segment retenu : **logiciel**. Justification : les mots-clés des projets publics portent sur des algorithmes variationnels et sur la simulation.
>
> **L'appel**
> - **Quantum Machine Learning** (HORIZON-JU-EUROHPC-2026-QML-07-01), EuroHPC JU, Horizon Europe.
> - **Clôture : 28 janvier 2027 à 17 h (heure de Bruxelles)**, appel en une seule étape, ouvert depuis le 2 juin 2026 ([EuroHPC](https://www.eurohpc-ju.europa.eu/quantum-machine-learning_en) ; [qt.eu](https://qt.eu/funding-opportunities)). À revérifier le jour de l'envoi sur la [page du topic](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-JU-EUROHPC-2026-QML-07-01).
> - Budget annoncé : environ 6 M€ ([note 07](../../../research_notes/Meilleure%20opportunité%20entrepreneuriale%20quantique/07_verification_radar_financements.md)). Type d'action, montant par projet et composition du consortium : **à vérifier** sur la page du topic.
>
> **Pourquoi cet appel pourrait vous concerner**
> 1. L'appel vise des méthodes d'apprentissage automatique quantiques, inspirées du quantique ou hybrides, avec des bancs d'essai de performance et des stratégies tenant compte du bruit. Vos projets publics portent sur des algorithmes variationnels.
> 2. L'appel demande des démonstrations couplant processeurs quantiques et systèmes HPC classiques. Un éditeur logiciel peut y tenir le rôle d'intégrateur des méthodes.
>
> **À vérifier avant d'y consacrer du temps**
> - Le type d'action et le taux de financement applicable à une entreprise.
> - La composition exigée du consortium et l'accès aux systèmes quantiques EuroHPC.
> - Il reste 7 semaines : c'est réaliste seulement si vous faites déjà partie d'un consortium en formation.
>
> **Effort et calendrier indicatifs**
> Il reste environ 7 semaines. Une contribution de partenaire demande plusieurs dizaines de personnes-jours ; coordonner le dossier en demande nettement plus. À ce stade, une relecture critique du brouillon est plus utile qu'une rédaction.
>
> **Aide gratuite**
> PCN « numérique » français, réseau EEN, service d'assistance du portail Funding & Tenders.
>
> **Pour aller plus loin**
> Une note d'éligibilité en 5 jours ouvrés coûte 490 € HT (245 € pour les 5 premiers clients) et elle est remboursée si je la livre en retard.
>
> *[Nom commercial], [Prénom Nom]. Fiche préparée avec des outils d'IA, vérifiée et rédigée par un humain. Elle peut contenir des erreurs ; aucune garantie. Mon historique : 0 dossier accompagné à ce jour. Pour ne plus recevoir de fiches : répondez « stop ».*
