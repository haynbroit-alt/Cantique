# Modèle : note d'éligibilité et d'adéquation (service B)

La note porte sur un appel et une entité candidate, plus 5 partenaires vérifiés au maximum. Elle fait 4 à 6 pages et elle est livrée en 5 jours ouvrés. Prix et conditions : [../OFFRE.md](../OFFRE.md), section 4.3.

---

## 0. Mode d'emploi, réservé à l'usage interne et à retirer de la note livrée

### 0.1 Ordre de priorité des sources
On ne s'appuie jamais sur une source secondaire pour trancher une condition d'éligibilité. Les sources se consultent dans cet ordre :
1. **La page du topic et les documents de l'appel** sur le portail Funding & Tenders, avec leur version et leur date.
2. **Le programme de travail concerné et ses annexes générales** (Horizon Europe : annexes A à G).
3. **Pour une entreprise commune** (EuroHPC JU, Chips JU) : son programme de travail et ses règles propres, qui peuvent s'écarter des règles standard d'Horizon Europe.
4. **Le règlement Horizon Europe** (UE) 2021/695 et la convention de subvention annotée (AGA).
5. **La FAQ de l'appel, le service d'assistance ou le PCN.** Toute réponse de leur part est citée avec sa date.
6. **Pour le Royaume-Uni :** le brief de la compétition sur l'Innovation Funding Service, et ses documents d'orientation.

### 0.2 Ce que les agents pré-remplissent, et ce que l'humain tranche
| Élément | Agents IA | Humain |
|---|---|---|
| Extraction des conditions du texte officiel, avec citation et référence | Oui | Il vérifie chaque citation dans le document source |
| Situation du client sur chaque condition | Seulement à partir des pièces fournies par le client | Il interprète et pose les questions manquantes |
| Statut ✔ / ✖ / ? | Proposition | **Il décide** |
| Score d'adéquation | Pré-score à partir de la sortie de `rapprocher.py` | **Il fixe le score et rédige la justification** |
| Décision go / no-go | Jamais | **Il décide et signe** |

### 0.3 Temps cible
4 heures de travail humain au plus. Au-delà de 6 heures en moyenne, le prix ne tient plus ([../../prospection/PLAN-12-SEMAINES.md](../../prospection/PLAN-12-SEMAINES.md), critères qualité).

---

## 1. Modèle à remplir

```markdown
# Note d'éligibilité et d'adéquation

| | |
|---|---|
| Client | {raison sociale}, {pays}, {PIC si connu} |
| Appel | {intitulé} ({identifiant_appel}) |
| Financeur / programme | {financeur} / {programme} |
| Clôture | {date}, {heure}, {fuseau} |
| Documents consultés | {liste avec version et date} (détail en section 9) |
| Date de la note | {date} |
| Auteur | {Prénom Nom}, {Nom commercial} |
| Usage de l'IA | {Accepté / Refusé par le client}. Journal en annexe. |
| Statut | Confidentiel, réservé au client |

## 1. Résumé
- **Décision : {GO / GO SOUS CONDITIONS / NO-GO}**
- **Score d'adéquation : {xx}/100**
- **Conditions ou motifs principaux :**
  1. {…}
  2. {…}
  3. {…}
- **Effort estimé :** {N} personnes-jours côté candidat. Démarrage au plus tard le {date}.
- **Point bloquant à lever d'abord :** {…}

## 2. L'appel en bref
| Élément | Valeur | Référence |
|---|---|---|
| Type d'action | {RIA / IA / CSA / EIC / compétition Innovate UK / autre} | {§ du document} |
| Budget de l'appel / montant indicatif par projet | {…} | |
| Taux de financement applicable au client | {…} | |
| Durée attendue du projet | {…} | |
| Niveau de maturité technologique (TRL) attendu | {…} | |
| Procédure | {une étape / deux étapes / enregistrement préalable} | |
| Résultats attendus (« expected outcomes ») | {résumé en 2 ou 3 lignes ; les citer exactement en annexe} | |

## 3. Liste de contrôle d'éligibilité et de recevabilité
Légende du statut : ✔ conforme · ✖ non conforme (rédhibitoire si marqué R) · ? à confirmer · n.a. non applicable.

| # | Condition | Exigence (citation et référence) | Situation du client (fait et pièce) | Statut | Action |
|---|---|---|---|---|---|
| **3.1 Recevabilité** | | | | | |
| 1 | Soumission par le portail officiel avant la date et l'heure fixées | | | | |
| 2 | Formulaire complet : partie A (administrative) et partie B (technique) | | | | |
| 3 | Limite de pages de la partie B (souvent 45 pages pour RIA et IA ; à vérifier dans le formulaire de l'appel) | | | | |
| 4 | Annexes obligatoires : tableaux, lettres, déclarations éthiques ou de sécurité | | | | |
| **3.2 Éligibilité des entités** | | | | | |
| 5 | Personnalité juridique ; numéro PIC ; validation de l'entité et désignation d'un LEAR | | | | |
| 6 | Pays d'établissement : État membre, pays associé à Horizon Europe ou pays tiers | | | | |
| 7 | **Entreprise commune (EuroHPC, Chips JU) :** les entités des pays associés qui ne sont pas membres de l'entreprise commune sont-elles éligibles au financement ? Ne pas supposer que l'association du Royaume-Uni à Horizon Europe suffit | | | | |
| 8 | **Restrictions de participation au titre de l'article 22, paragraphe 5, du règlement Horizon Europe** (actifs stratégiques, autonomie, sécurité) : participation limitée à certains pays, évaluation du contrôle et de la propriété, garanties exigées | | | | |
| 9 | Entités affiliées ; contrôle par des entités de pays tiers (cap table et pactes) | | | | |
| **3.3 Composition du consortium** | | | | | |
| 10 | Composition minimale : condition standard RIA et IA (au moins 3 entités indépendantes de 3 pays différents, États membres ou pays associés, dont au moins une d'un État membre) ou condition propre au topic | | | | |
| 11 | Candidature mono-bénéficiaire autorisée ou non ; exigences sur le rôle du coordinateur | | | | |
| 12 | Rôles exigés ou attendus : utilisateur final, centre HPC, ligne pilote, organisme de recherche | | | | |
| **3.4 Statut de PME (recommandation 2003/361/CE)** | | | | | |
| 13 | Effectifs inférieurs à 250 ; chiffre d'affaires ≤ 50 M€ **ou** total du bilan ≤ 43 M€ | | | | |
| 14 | Autonomie : entreprises partenaires ou liées (participations de 25 % ou plus ; exceptions pour certains investisseurs) ; consolidation des seuils | | | | |
| 15 | Conséquence pour l'appel : statut exigé, taux majoré ou quota de PME | | | | |
| **3.5 Capacités** | | | | | |
| 16 | Capacité financière : contrôle du coordinateur (seuil usuel de 500 000 € de contribution demandée, à vérifier) ; comptes des derniers exercices | | | | |
| 17 | Capacité opérationnelle : CV, publications ou produits, infrastructures, accès aux systèmes quantiques | | | | |
| **3.6 Financement** | | | | | |
| 18 | Taux de financement : RIA 100 % ; IA 70 % pour les entités à but lucratif ; CSA 100 %. Coûts indirects forfaitaires de 25 %. À confirmer dans le programme de travail | | | | |
| 19 | **Chips JU :** l'appel combine-t-il un financement de l'UE et un financement national des États participants, avec des conditions nationales supplémentaires ? | | | | |
| 20 | Cofinancement à apporter, besoin de trésorerie, coûts non éligibles (préparation du dossier, honoraires de succès) | | | | |
| **3.7 Périmètre et maturité** | | | | | |
| 21 | Adéquation au périmètre (« scope ») et aux résultats attendus | | | | |
| 22 | TRL de départ et d'arrivée cohérents avec l'appel | | | | |
| **3.8 Éthique, sécurité, double usage, exportations** | | | | | |
| 23 | Auto-évaluation éthique (données personnelles, IA, environnement) | | | | |
| 24 | Exigence d'applications civiles ; examen de sécurité ; informations classifiées | | | | |
| 25 | Contrôle des exportations : biens à double usage (annexe I du règlement 2021/821, mise à jour par le règlement délégué 2025/2003), règles américaines (EAR) pour les composants | | | | |
| **3.9 Plan d'égalité entre les femmes et les hommes** | | | | | |
| 26 | Plan exigé des organismes publics, des organismes de recherche et des établissements d'enseignement supérieur des États membres et pays associés, pas des entreprises privées. Vérifier pour chaque partenaire | | | | |
| **3.10 Spécificités britanniques (Innovate UK), si l'appel est britannique** | | | | | |
| 27 | Entreprise immatriculée au Royaume-Uni ; taille ; rôle de chef de projet ; règles de collaboration propres à la compétition | | | | |
| 28 | Taux de financement selon la taille et la catégorie de recherche, à vérifier dans le brief (taux usuels : recherche industrielle jusqu'à 70 % pour une petite entreprise ; développement expérimental jusqu'à 45 %) | | | | |
| 29 | Règles de contrôle des subventions (Subsidy Control Act 2022) ; capacité à apporter le cofinancement | | | | |
| 30 | Échéance d'enregistrement préalable, si elle existe ; fourchettes de coûts et de durée du projet | | | | |
| **3.11 Cumul et resoumission** | | | | | |
| 31 | Pas de double financement des mêmes coûts ; limite de resoumission (EIC Accelerator : pas de nouvelle candidature après 3 refus de la même proposition) | | | | |

## 4. Score d'adéquation
Chaque critère est noté de 0 à 5 puis multiplié par son poids. La somme des poids vaut 20, le maximum est donc 100.

| Critère | Poids | Note (0–5) | Points | Justification (faits et sources) |
|---|---|---|---|---|
| Adéquation thématique au périmètre et aux résultats attendus | 5 | | | |
| Maturité (TRL) et type d'action | 3 | | | |
| Capacité à monter le dossier dans le délai (équipe disponible, semaines restantes) | 4 | | | |
| Consortium (existant, à compléter ou non requis) | 3 | | | |
| Capacité de cofinancement et trésorerie | 2 | | | |
| Valeur stratégique, comparée aux autres appels possibles dans les 12 mois | 3 | | | |
| **Total** | **20** | | **/100** | |

Lecture du score :
- **70 ou plus : GO.**
- **De 50 à 69 : GO SOUS CONDITIONS,** à lever avant une date fixée.
- **Moins de 50 : NO-GO.**
- **Une seule condition marquée ✖ R en section 3 donne NO-GO,** quel que soit le score.

*Le score mesure l'adéquation, pas une probabilité de succès. Pour mémoire, taux de succès historique du programme : {taux, source}.*

## 5. Signaux d'alerte
Cocher, puis commenter chaque case cochée :
- [ ] Délai inférieur à 6 semaines et consortium inexistant
- [ ] Doute sur l'éligibilité du pays ou de l'entité (entreprise commune, article 22, paragraphe 5)
- [ ] Statut de PME incertain : investisseur industriel à 25 % ou plus, groupe
- [ ] Projet hors du cœur des résultats attendus : adaptation forcée d'un projet existant
- [ ] Affirmations de performance (par exemple un « avantage quantique ») sans comparaison avec une référence classique
- [ ] Cofinancement ou trésorerie insuffisants pour le taux applicable
- [ ] Concurrent direct probablement candidat sur le même topic avec un consortium plus fort
- [ ] Données techniques soumises au contrôle des exportations nécessaires au dossier
- [ ] Dossier déjà refusé : vérifier la limite de resoumission et les commentaires du rapport d'évaluation précédent
- [ ] Appel récemment transféré, suspendu ou modifié (par exemple le transfert des appels quantiques vers EuroHPC en 2026)
- [ ] Charge interne incompatible avec d'autres échéances : levée de fonds, livraison client

## 6. Décision
**{GO / GO SOUS CONDITIONS / NO-GO}**

- Conditions à lever, avec une date limite pour chacune : {…}
- Ce qui ferait changer la décision : {…}
- Solution de repli, si NO-GO : {autre appel et sa date de clôture, pour mémoire}

## 7. Effort et rétroplanning
| Échéance | Jalon | Responsable |
|---|---|---|
| J − {60} | Décision de candidater ; validation du consortium | Client |
| J − {45} | Plan détaillé de la partie B ; répartition des sections | Client et partenaires |
| J − {30} | Premier brouillon complet ; budget v1 | Client |
| J − {20} | Revue critique (service D, facultative) | {Nom commercial} |
| J − {10} | Version quasi finale ; signatures, déclarations, lettres | Client |
| J − 2 | **Soumission** : ne pas attendre le dernier jour | Client |

Effort estimé, en personnes-jours :

| Rôle | Charge |
|---|---|
| Scientifiques | {…} |
| Direction et gestion | {…} |
| Finance | {…} |
| Partenaires | {…} |
| Appui externe | {…} |

## 8. Contrôle coût-bénéfice
- Contribution demandée par le client : **{A} €**.
- Taux de succès historique de référence : **{p} %** (source : {…}). Ce taux n'est pas une prédiction pour ce dossier.
- Valeur espérée brute : A × p = **{A·p} €**.
- Coût de la candidature : {personnes-jours} × {coût journalier interne} + honoraires externes = **{C} €**.
- Bénéfices non financiers : partenariats, visibilité, résultats d'évaluation réutilisables, à décrire.
- **Conclusion :**
  - {« La candidature a un sens économique »}
  - ou {« Le coût dépasse la valeur espérée ; je le signale par écrit, comme le demande le code de conduite de l'EIC. Candidater reste votre décision. »}

## 9. Sources consultées
| Document | Version ou date | URL | Consulté le |
|---|---|---|---|
| Page du topic | | | |
| Documents de l'appel | | | |
| Programme de travail et annexes générales | | | |
| FAQ ou réponse du service d'assistance / du PCN | | | |

## 10. Aide gratuite disponible
- Point de contact national : {lien}.
- Enterprise Europe Network : {lien}.
- Service d'assistance de l'appel : {lien}.
- URL officielle de l'appel : {lien}. Vous pouvez candidater directement, sans intermédiaire.

## 11. Mentions
- **Usage de l'IA :** {outils} ont servi à {extraction des conditions, pré-remplissage}. Aucune donnée non publique n'a été transmise à un outil tiers sans votre accord. Le journal détaillé figure en annexe.
- **Mon historique au {date} :** {0} dossier soumis, {0} financé ([registre public]({site}/resultats)).
- **Aucune garantie de résultat.** Cette note donne une interprétation des textes à la date indiquée. En cas de doute, la lecture de l'agence de financement prévaut : faites confirmer les points marqués « ? » par le service d'assistance ou par le PCN.
- **Responsabilité** plafonnée au prix payé ([OFFRE.md](../OFFRE.md), section 7.8). Document confidentiel.

## Annexe : journal d'usage de l'IA
| Date | Outil (offre et conditions) | Tâche | Données transmises | Vérification humaine |
|---|---|---|---|---|
```
