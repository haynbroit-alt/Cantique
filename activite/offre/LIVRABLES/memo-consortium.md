# Modèle : mémo de recherche de partenaires et de constitution de consortium (service C)

Le mémo porte sur un appel et 1 à 3 rôles à pourvoir, ou plus. Il est livré en 8 jours ouvrés. Prix et conditions : [../OFFRE.md](../OFFRE.md), section 4.4.

---

## 0. Mode d'emploi, réservé à l'usage interne et à retirer du mémo livré

### 0.1 Sources autorisées
Uniquement des données publiques sur des **organisations** :
- **CORDIS :** participants aux projets financés, avec leur rôle et leur contribution. C'est la même source que celle de `prospects.jsonl`, en suivant [CONTRAT.md](../../CONTRAT.md).
- **UKRI Gateway to Research,** pour les organisations britanniques.
- **La recherche de partenaires du portail Funding & Tenders** (profils publiés volontairement par les organisations).
- **Les cartographies d'écosystème publiées** par les grappes d'entreprises, les associations professionnelles et les programmes nationaux.
- **Les sites web des organisations.**

Ce qui est interdit :
- toute donnée sur des personnes (noms, e-mails, profils LinkedIn de salariés) ;
- l'achat de fichiers ;
- le moissonnage (scraping) de plateformes dont les conditions d'utilisation l'interdisent.

### 0.2 Règles d'indépendance
- **Aucune commission ni contrepartie** de la part des organisations citées ([OFFRE.md](../OFFRE.md), section 7.7).
- **Signaler tout lien** entre le fondateur et une organisation citée.
- **Ne pas recommander un concurrent direct du client** sans le signaler comme tel.

### 0.3 Ce que font les agents et ce que fait l'humain
| Tâche | Agents IA | Humain |
|---|---|---|
| Extraire les projets passés proches du topic (mots-clés, codes de topic, programmes) | Oui | Il vérifie la pertinence d'un échantillon |
| Construire la liste longue avec ses preuves | Oui | Il retire les organisations hors sujet |
| Établir la liste courte et sa justification | Proposition | **Il décide et rédige** |
| Identifier les risques (concurrence, PI, géographie) | Pré-signalement | **Il juge** |
| Rédiger les messages d'approche | Squelette | **Il écrit** ; le client envoie |

---

## 1. Modèle à remplir

```markdown
# Mémo de recherche de partenaires

| | |
|---|---|
| Client | {raison sociale}, {pays} |
| Appel | {intitulé} ({identifiant_appel}), clôture {date et heure} |
| Rôle visé du client | {coordinateur / partenaire} |
| Date | {date} |
| Auteur | {Prénom Nom}, {Nom commercial} |
| Usage de l'IA | {Accepté / Refusé}. Journal en annexe. |
| Statut | Confidentiel |

## 1. Résumé
- Rôles à pourvoir : {liste}.
- Recommandation : approcher en priorité {3 organisations}, avant le {date}.
- Principal risque : {…}.

## 2. Exigences de l'appel en matière de consortium
| Exigence | Source (§) | Situation actuelle |
|---|---|---|
| Composition minimale (nombre d'entités, de pays, d'États membres) | | |
| Restrictions de pays (entreprise commune, article 22, paragraphe 5) | | |
| Rôles explicitement attendus : utilisateur final, centre HPC ou entité d'hébergement, ligne pilote, organisme de normalisation | | |
| Équilibre attendu : PME, industrie, recherche ; diversité géographique | | |
| Accès à des infrastructures, par exemple des systèmes quantiques EuroHPC | | |

## 3. Analyse des écarts
| Rôle | Pourquoi l'appel en a besoin | Couvert par | Écart | Priorité |
|---|---|---|---|---|
| {rôle} | {lien avec les résultats attendus ou les critères d'évaluation} | {client / partenaire existant / personne} | {…} | {haute / moyenne / basse} |

## 4. Liste longue (15 à 30 organisations)
| # | Organisation | Pays | Type (PME, grande entreprise, université, recherche) | Rôle possible | Preuve de compétence (projets, produits) | Lien |
|---|---|---|---|---|---|---|

## 5. Liste courte (5 à 8 organisations)
Pour chaque organisation retenue :

### 5.{n} {Organisation} ({pays}, {type})
- **Rôle proposé :** {…}
- **Ce qu'elle apporte au regard des critères d'évaluation :** {Excellence, Impact ou Mise en œuvre}
- **Preuves :** {projets passés et leurs liens}
- **Risques :**
  - concurrence avec le client : {…}
  - questions de PI : {…}
  - éligibilité (pays, entreprise commune) : {…}
  - sollicitations concurrentes probables (même organisation approchée par d'autres consortiums) : {…}
- **Canal d'approche suggéré :** {recherche de partenaires du portail F&T / PCN / réseau EEN / événement / contact existant du client}

## 6. Matrice de complémentarité
| Compétence ou rôle requis | Client | Partenaire existant | {Org 1} | {Org 2} | {Org 3} |
|---|---|---|---|---|---|
| {…} | ● | | ● | | ○ |

● couverture forte · ○ couverture partielle

## 7. Risques pour le consortium
- [ ] Concentration géographique : trop d'entités d'un même pays
- [ ] Dépendance à un seul partenaire pour un rôle critique
- [ ] Partenaire de grande taille qui risque de capter la coordination ou la PI
- [ ] Partenaire déjà engagé dans un consortium concurrent sur le même topic
- [ ] Délai trop court pour obtenir les signatures, les numéros PIC et les lettres
- [ ] Éligibilité au financement non confirmée pour un partenaire (pays associé non membre de l'entreprise commune)

## 8. Plan d'approche (exécuté par le client)
| Semaine | Action | Organisations |
|---|---|---|
| S | Premier message, avec un résumé non confidentiel de 10 lignes | {…} |
| S + 1 | Appel de découverte de 30 minutes | {…} |
| S + 2 | Accord de principe, signature d'un accord de confidentialité, échange des PIC | {…} |
| S + 3 | Atelier de construction (lots, rôles, budget indicatif) | {…} |

### Modèle de premier message (le client l'adapte et l'envoie)
> Objet : {acronyme provisoire} : partenariat pour {identifiant_appel} (clôture {date})
>
> Bonjour,
> {Client} prépare une candidature à {appel} sur {sujet en une ligne}. Votre travail sur {projet public, avec son lien} correspond au rôle de {rôle} que nous cherchons à pourvoir. Nous proposons {ce que le partenaire y gagne : budget indicatif, accès à des résultats, cas d'usage}.
> Seriez-vous disponible pour un appel de 30 minutes d'ici le {date} ? Nous pouvons signer un accord de confidentialité au préalable.
> {Signature}

### Ordre du jour type de la première réunion (30 min)
1. Objectifs de l'appel et résultats attendus (5 min)
2. Idée de projet, non confidentielle (5 min)
3. Rôle proposé et contribution attendue (10 min)
4. Calendrier, ressources, éligibilité (PIC, pays, statut) (5 min)
5. Suite : accord de confidentialité, atelier, date de décision (5 min)

## 9. Pistes pour l'accord de consortium (ne vaut pas avis juridique)
- **Modèle de départ courant :** DESCA, pour les projets Horizon Europe.
- **Points à trancher tôt :**
  - les connaissances antérieures (« background ») apportées par chacun et exclues ;
  - les droits d'accès ;
  - la propriété des résultats ;
  - la gouvernance ;
  - la répartition du budget ;
  - la sortie d'un partenaire.
- **Faire relire par un juriste** avant signature.

## 10. Sources
| Source | Requête ou filtre | Date |
|---|---|---|

## 11. Mentions
- Le mémo cite des organisations à partir de données publiques ; il ne contient aucune donnée personnelle.
- Aucune garantie d'acceptation par les partenaires.
- Je n'ai reçu aucune commission des organisations citées.
- **Mon historique au {date} :** {0} dossier soumis, {0} financé.
- **Usage de l'IA :** voir le journal en annexe. Aucune garantie de résultat.
- Responsabilité plafonnée au prix payé ([OFFRE.md](../OFFRE.md), section 7.8).

## Annexe : journal d'usage de l'IA
| Date | Outil | Tâche | Données transmises | Vérification humaine |
|---|---|---|---|---|
```
