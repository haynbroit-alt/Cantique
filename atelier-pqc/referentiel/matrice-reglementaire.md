# Matrice réglementaire de la cryptographie post-quantique

Version du 22 novembre 2026. État des textes à cette date.

> **Avertissement.** Ce document n'est pas un avis juridique. Il résume des textes publics pour aider un responsable informatique à situer son organisation. Savoir si un texte s'applique à une entreprise précise, et avec quelles conséquences, relève d'un juriste ou de l'autorité compétente. Les éléments marqués « confiance faible » ne doivent pas être cités à un client sans vérification préalable.

## En bref

- **Pour la plupart des entreprises privées situées hors du périmètre PCI DSS et hors des marchés publics, aucune échéance de migration post-quantique contraignante n'existe aujourd'hui.** Les autres textes sont des recommandations, des projets, ou des obligations qui visent des administrations.
- La seule exigence déjà opposable à une large population d'entreprises est **PCI DSS 4.0.1, exigence 12.3.3**. En vigueur depuis le 31 mars 2025, elle impose un inventaire des suites et protocoles cryptographiques revu chaque année. Elle n'impose aucune migration post-quantique.
- Aux États-Unis, les échéances fermes (2030 pour l'échange de clés, 2031 pour les signatures) s'imposent aux **agences fédérales**. Elles atteindront les **fournisseurs fédéraux** si le projet de règle FAR annoncé par l'EO 14412 est publié puis adopté. Ce projet est attendu vers le 19 décembre 2026.
- En Europe et au Royaume-Uni, les calendriers convergent sur **2030 pour les usages à haut risque et 2035 pour le reste**. Ce sont des recommandations, adressées aux États membres pour l'UE et aux grandes organisations pour le NCSC.
- Une échéance datée touche déjà toute entreprise qui a un site web, sans relever de la PQC : la **durée maximale des certificats TLS publics** passe de 200 jours aujourd'hui à 100 jours le 15 mars 2027, puis à 47 jours en 2029.

## Comment lire ce document

**Nature** (portée du texte pour le public qu'il vise, pas forcément pour votre client) :

- *Contraignant* : obligation directe pour le public visé (loi, décret, politique obligatoire, contrat).
- *Contraignant indirect* : le texte ne lie pas l'entreprise elle-même, mais il s'impose à elle par un tiers (marchés publics, validation FIPS, autorités de certification).
- *Recommandation* : guide ou feuille de route sans force obligatoire.
- *Projet* : texte annoncé ou en cours d'adoption, pas encore applicable.

**Confiance** :

- *Élevée* : vérifié dans le texte primaire le 22 novembre 2026.
- *Moyenne* : partiellement vérifié. La date ou le libellé principal est confirmé par une source officielle, le reste par des sources secondaires concordantes.
- *Faible* : non vérifié dans une source primaire (sites de synthèse ou sources secondaires uniquement).

**Échéances** : quand un texte ne donne qu'une année (« d'ici 2031 »), la version machine (`regles.json`) retient le 31 décembre de cette année. Quand il ne donne qu'un mois, elle retient le dernier jour du mois. « Après 2030 » signifie à compter du 1er janvier 2031. L'identifiant entre crochets dans la colonne « Référentiel » renvoie au référentiel correspondant de `regles.json`.

## International et sectoriel

| Référentiel | Qui est concerné | Exigence | Échéance | Nature | Source | Confiance |
|---|---|---|---|---|---|---|
| PCI DSS 4.0.1, exigence 12.3.3 [`PCI-DSS-4.0.1`] | Entités qui stockent, traitent ou transmettent des données de carte, et leurs prestataires | Suites et protocoles cryptographiques documentés et revus au moins tous les 12 mois : inventaire à jour (usage, emplacement), veille sur leur viabilité, stratégie face aux vulnérabilités attendues. Aucune échéance PQC, aucune exigence de « CBOM » dans le texte | En vigueur depuis le 31 mars 2025 | Contraignant (contrat, via les réseaux de cartes et les acquéreurs) | [PCI SSC, blog](https://blog.pcisecuritystandards.org/now-is-the-time-for-organizations-to-adopt-the-future-dated-requirements-of-pci-dss-v4-x) ; [document hébergé par le PCI SSC citant 12.3.3](https://www.pcisecuritystandards.org/day-1_t2_7_pci-dss-v4-0_final/) | Moyenne : date et libellé principal confirmés par le PCI SSC ; alinéas « veille » et « stratégie » issus de sources secondaires |
| PCI DSS 4.0.1, exigence 4.2.1.1 [`PCI-DSS-4.0.1`] | Mêmes entités | Inventaire des clés et certificats de confiance qui protègent le numéro de carte (PAN) en transmission | Depuis le 31 mars 2025 | Contraignant (contrat) | [postquantum.com](https://postquantum.com/security-pqc/pci-dss-v4-quantum-cryptographic-requirements/) | Faible : non vérifié dans la norme |
| CA/Browser Forum, Baseline Requirements v2.3.1 (scrutin SC-081v3) [`CABF-SC-081`] | Autorités de certification publiques ; en pratique, tout détenteur de certificats TLS publics | Durée maximale d'un certificat TLS public : 200 jours ; 100 jours ; 47 jours. Réutilisation des validations de domaine : 200, 100, puis 10 jours. Ce n'est pas une exigence PQC | 15 mars 2026 (en vigueur) ; 15 mars 2027 ; 15 mars 2029 | Contraignant indirect | [Baseline Requirements](https://github.com/cabforum/servercert/blob/main/docs/BR.md) ; [scrutin SC-081v3](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/) | Élevée |
| CA/Browser Forum, Baseline Requirements v2.3.1 [`CABF-SC-081`] | Idem | Fin de tout usage résiduel de SHA-1 dans les certificats et les listes de révocation | 15 septembre 2026 | Contraignant indirect | [Baseline Requirements](https://github.com/cabforum/servercert/blob/main/docs/BR.md) | Élevée |
| G7 Cyber Expert Group, feuille de route pour le secteur financier [`G7-CEG-PQC-FINANCE`] | Établissements et autorités financières des pays du G7 | Six phases (sensibilisation, découverte, évaluation des risques, migration, tests, validation). Cible indicative 2035, systèmes les plus critiques vers 2030-2032. Le texte « ne fixe ni orientations ni attentes réglementaires » | 2035 (indicatif) | Recommandation | [G7 CEG (US Treasury)](https://home.treasury.gov/system/files/136/G7-CEG-Quantum-Roadmap.pdf) | Élevée |

## États-Unis

| Référentiel | Qui est concerné | Exigence | Échéance | Nature | Source | Confiance |
|---|---|---|---|---|---|---|
| NIST FIPS 203, 204, 205 [`NIST-FIPS-203-204-205`] | Administrations fédérales ; entreprises par les contrats publics et la validation FIPS 140-3 | Normes finales : ML-KEM (échange de clés), ML-DSA et SLH-DSA (signatures). ML-KEM est le seul échange de clés post-quantique approuvé à ce jour | Publiées le 13 août 2024 | Contraignant indirect | [CSRC, liste des FIPS](https://csrc.nist.gov/publications/fips) | Élevée |
| NIST FIPS 206 (FN-DSA, dérivé de Falcon) [`NIST-FIPS-206-PROJET`] | Idem, après publication | En cours d'élaboration : ne pas présenter FN-DSA comme approuvé. HQC, alternative à ML-KEM, attend lui aussi sa FIPS | Aucune date officielle | Projet | [NIST IR 8547](https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8547.pdf) ; [CSRC](https://csrc.nist.gov/publications/fips) | Élevée (statut au 22 nov. 2026) |
| NIST IR 8547 finale [`NIST-IR-8547`] | Administrations fédérales et, par les marchés publics et la validation FIPS 140, leurs fournisseurs ; ne lie pas directement les entreprises privées | RSA, ECDSA, EdDSA, DH, ECDH et MQV **dépréciés après 2030** puis **interdits après 2035** dans les normes du NIST, à toutes les tailles de clé approuvées. ML-KEM-768 recommandé par défaut. Hybride validable FIPS 140 si une composante est approuvée. SHA-1 interdit dans les modules validés FIPS après 2030. AES et SHA-2/SHA-3 d'au moins 128 bits restent adaptés | Après 2030 ; après 2035 | Contraignant indirect | [NIST IR 8547 (27 oct. 2026)](https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8547.pdf) | Élevée |
| Executive Order 14412 (22 juin 2026) [`US-EO-14412`] | Agences fédérales, hors systèmes de sécurité nationale. Aucune échéance pour les opérateurs d'infrastructures critiques | Responsable de migration PQC désigné sous 30 jours. Actifs de grande valeur et systèmes à impact élevé : PQC pour l'échange de clés, puis pour les signatures | 22 juillet 2026 ; 31 déc. 2030 ; 31 déc. 2031 | Contraignant | [EO 14412 (govinfo)](https://www.govinfo.gov/content/pkg/DCPD-202600417/html/DCPD-202600417.htm) | Élevée |
| OMB M-26-15 (24 juin 2026) [`US-OMB-M-26-15`] | Agences fédérales, hors systèmes de sécurité nationale | Plan de migration sous 120 jours, avec méthodes et outils d'inventaire automatisé (CBOM central recommandé). TLS 1.3 obligatoire. PQC dans les achats des catégories CISA. Répartition des responsabilités avec les fournisseurs cloud FedRAMP. Migration complète en phase 5 | 22 oct. 2026 (plan) ; 2 janv. 2030 (TLS 1.3) ; 2035 | Contraignant | [OMB M-26-15](https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf) | Élevée |
| Projets de règles FAR (EO 14412, sec. 6) [`US-FAR-PQC-PROJET`] | « Covered contractors » des agences fédérales, catégorie que l'EO ne définit pas | 1) Projet de règle imposant la conformité aux FIPS du NIST, y compris PQC, **d'ici le 31 décembre 2030**. 2) Projet de règle sur la divulgation des vulnérabilités, y compris cryptographiques | Projets attendus vers le 19 déc. 2026 et le 19 mars 2027 | Projet (non repéré au 22 nov. 2026) | [EO 14412](https://www.govinfo.gov/content/pkg/DCPD-202600417/html/DCPD-202600417.htm) | Élevée pour ce que l'EO ordonne ; contenu final inconnu |
| CISA/NIST, éléments minimaux d'un CBOM [`US-CISA-CBOM-PROJET`] | Fournisseurs de matériel et de logiciels, acheteurs publics | Orientation publique sur le contenu minimal d'un inventaire cryptographique permettant une évaluation automatisée | Vers le 19 mars 2027 | Projet | [EO 14412](https://www.govinfo.gov/content/pkg/DCPD-202600417/html/DCPD-202600417.htm) | Élevée pour l'échéance ; publication non vérifiée |
| CISA, catégories de produits PQC (23 janv. 2026) [`US-CISA-PQC-CATEGORIES`] | Acheteurs des agences fédérales civiles ; éditeurs qui leur vendent | PQC « largement disponible » pour le cloud PaaS/IaaS, la messagerie instantanée, les navigateurs et serveurs web, le chiffrement des données au repos : n'acheter que des produits compatibles PQC dans ces catégories | En vigueur | Recommandation | [CISA](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards) | Élevée |
| NSA CNSA 2.0 / CNSSP 15 [`NSA-CNSA-2.0`] | Systèmes de sécurité nationale (NSS) et leurs fournisseurs | Nouvelles acquisitions conformes CNSA 2.0, sauf exception ; retrait des équipements non compatibles. **Écart de dates** : atsec situe l'obligation CNSA 2.0 en 2028 en s'appuyant sur la NIAP Policy Letter 33, qui vise l'évaluation des produits. Il s'agit probablement de deux circuits différents | 1er janv. 2027 (2028 selon atsec) ; 31 déc. 2030 | Contraignant (pour les NSS) | [postquantum.com](https://postquantum.com/cnsa-2-0/2027-procurement-gate/) ; [atsec](https://atsec.de/cnsa-compliance-to-be-mandatory-starting-in-2027/) | Faible : texte de la NSA inaccessible |

## Union européenne

| Référentiel | Qui est concerné | Exigence | Échéance | Nature | Source | Confiance |
|---|---|---|---|---|---|---|
| Feuille de route coordonnée de mise en œuvre (groupe de coopération NIS, v1.1, publiée le 23 juin 2025) [`EU-PQC-ROADMAP`] | États membres. Aucune obligation directe pour les entreprises | Fin 2026 : premières étapes, feuilles de route nationales initiales, planification et pilotes. Fin 2030 : usages à haut risque migrés (données à protéger au moins 10 ans), mises à jour résistantes au quantique activées par défaut. Fin 2035 : usages à risque moyen migrés, « autant de systèmes que possible ». Solutions hybrides recommandées | 31 déc. 2026 ; 31 déc. 2030 ; 31 déc. 2035 | Recommandation (issue d'une recommandation de la Commission ; pas d'effet juridique contraignant à notre lecture) | [Commission européenne](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography) ; [texte](https://ec.europa.eu/newsroom/dae/redirection/document/117507) | Élevée |
| Proposition de modification de NIS2, COM(2026) 13 [`EU-NIS2-COM-2026-13`] | États membres (stratégies nationales de cybersécurité) | Obligerait les États à inclure des politiques de migration vers la PQC dans leur stratégie nationale. Simple proposition, en commission ITRE au Parlement européen, puis transposition nationale | Première lecture indicative le 8 mars 2027 ; aucune échéance applicable | Projet | [Observatoire législatif du PE](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2026/0012(COD)) | Moyenne : procédure et contenu confirmés, numéro d'article et date exacte non vérifiés |

## Royaume-Uni

| Référentiel | Qui est concerné | Exigence | Échéance | Nature | Source | Confiance |
|---|---|---|---|---|---|---|
| NCSC, calendrier de migration PQC (publié le 20 mars 2025) [`UK-NCSC-PQC`] | D'abord les grandes organisations, les infrastructures nationales critiques et les SI sur mesure. Les PME sur informatique standard devraient migrer via les mises à jour de leurs fournisseurs ; celles qui ont des logiciels spécifiques suivent le même calendrier | 2028 : objectifs, découverte complète, plan initial. 2031 : migrations prioritaires, feuille de route affinée. 2035 : migration complète | 2028 ; 2031 ; 2035 | Recommandation | [NCSC](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines) | Élevée |

## France

| Référentiel | Qui est concerné | Exigence | Échéance | Nature | Source | Confiance |
|---|---|---|---|---|---|---|
| ANSSI, positions sur la transition post-quantique [`FR-ANSSI-PQC`] | Administrations, opérateurs, fournisseurs de produits évalués par l'ANSSI (périmètre exact non vérifié) | Hybridation (classique + post-quantique) exigée, sauf pour les signatures à base de hachage. Calendrier aligné sur la feuille de route européenne, que l'ANSSI diffuse | Déploiement dès 2026, haut risque 2030, complet 2035 | Recommandation | [Encryption Consulting (site de synthèse)](https://www.encryptionconsulting.com/pqc-migration-deadlines-by-country/) | Faible : site de l'ANSSI inaccessible |

## Allemagne

| Référentiel | Qui est concerné | Exigence | Échéance | Nature | Source | Confiance |
|---|---|---|---|---|---|---|
| BSI TR-02102-1, version 2026-01 (23 janv. 2026) [`DE-BSI-TR-02102-1`] | D'abord les développeurs de nouveaux systèmes cryptographiques. D'autres textes du BSI peuvent être contraignants pour certaines applications | Échange de clés classique seul recommandé jusqu'à fin 2031 seulement ; besoins de protection très élevés : transition dès fin 2030. Signatures classiques recommandées jusqu'à fin 2035. Mécanismes post-quantiques (ML-KEM, FrodoKEM, Classic McEliece) à utiliser en mode hybride. DSA n'est plus recommandé à partir de 2029 | Fin 2030 ; fin 2031 ; fin 2035 ; 2029 (DSA) | Recommandation | [BSI TR-02102-1](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile) | Élevée (moyenne pour DSA 2029) |

Les notes de recherche signalaient une « fin de l'échange de clés classique pour les usages réglementés » au 31 décembre 2031 et une exigence de double hybride « ML-KEM + FrodoKEM ». Le texte du BSI ne contient ni l'une ni l'autre : il formule des recommandations, et FrodoKEM y figure comme l'une des options post-quantiques, pas comme un complément obligatoire.

## Australie

| Référentiel | Qui est concerné | Exigence | Échéance | Nature | Source | Confiance |
|---|---|---|---|---|---|---|
| ASD, Information Security Manual [`AU-ASD-ISM-PQC`] | Entités gouvernementales australiennes | Plan affiné fin 2026, début de la migration des systèmes critiques fin 2028, cryptographie asymétrique classique abandonnée dans les systèmes gouvernementaux d'ici fin 2030 ; hybride permis mais non recommandé | Fin 2030 | Contraignant pour le gouvernement (selon les notes) | [Encryption Consulting (site de synthèse)](https://www.encryptionconsulting.com/pqc-migration-deadlines-by-country/) | Faible : site de l'ASD inaccessible |

## Canada

| Référentiel | Qui est concerné | Exigence | Échéance | Nature | Source | Confiance |
|---|---|---|---|---|---|---|
| Centre canadien pour la cybersécurité, ITSM.40.001 (23 juin 2025) [`CA-CCCS-ITSM-40-001`] | Ministères et organismes fédéraux | Plan ministériel initial, puis rapport annuel ; systèmes prioritaires migrés ; systèmes restants migrés | Avril 2026 ; fin 2031 ; fin 2035 | Recommandation : feuille de route dite « recommandée », que le Secrétariat du Conseil du Trésor doit rendre obligatoire | [Centre canadien pour la cybersécurité](https://www.cyber.gc.ca/en/guidance/roadmap-migration-post-quantum-cryptography-government-canada-itsm40001) | Élevée |

## Ce que cela implique pour une PME ou une ETI

1. **Si vous acceptez ou traitez des paiements par carte**, l'exigence PCI DSS 12.3.3 s'applique déjà. Vous devez tenir un inventaire des suites et protocoles cryptographiques, le revoir au moins une fois par an, suivre leur viabilité et documenter votre réponse aux faiblesses annoncées. Votre évaluateur (QSA) peut le demander dès maintenant. L'inventaire produit par l'atelier sert directement à cette exigence.
2. **Si vous vendez à l'administration fédérale américaine**, directement ou comme sous-traitant, ou si vous fournissez un service cloud FedRAMP, surveillez le projet de règle FAR attendu vers le 19 décembre 2026. Tel que l'EO 14412 le décrit, il exigerait la conformité aux FIPS du NIST, y compris PQC, d'ici fin 2030. Les éléments minimaux d'un CBOM sont attendus vers mars 2027. La CISA invite déjà les acheteurs fédéraux à n'acheter que des produits compatibles PQC dans les catégories qu'elle juge « largement disponibles ».
3. **Si vous êtes fournisseur d'une administration ou d'un opérateur critique en Europe ou au Royaume-Uni**, attendez-vous à des questionnaires sur votre feuille de route post-quantique. Vos clients doivent planifier : les États membres d'ici fin 2026, et les grandes organisations britanniques doivent finir leur découverte d'ici 2028. C'est une déduction tirée de ces calendriers, pas une obligation écrite qui vous viserait.
4. **Pour tout site web**, automatisez le renouvellement des certificats (par exemple avec ACME). La durée maximale tombe à 100 jours le 15 mars 2027 et à 47 jours le 15 mars 2029. Ce n'est pas de la PQC, mais c'est une échéance ferme et proche.
5. **L'inventaire cryptographique est la première étape de tous ces textes** : NCSC (découverte d'ici 2028), feuille de route de l'UE, OMB, BSI. Les priorités qu'ils indiquent sont les mêmes :
   - d'abord les données qui doivent rester confidentielles longtemps (au moins 10 ans selon l'UE), à cause du risque « collecter maintenant, déchiffrer plus tard » ;
   - d'abord l'échange de clés, puis les signatures ;
   - d'abord les systèmes difficiles à mettre à jour.
6. **Vous n'avez pas à développer votre propre cryptographie.** Le NCSC prévoit que les PME sur informatique standard recevront la PQC par les mises à jour de leurs fournisseurs. Demandez à vos éditeurs et hébergeurs leur feuille de route PQC, et intégrez la question à vos achats.
7. **Algorithmes cibles** : ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205). L'hybride (classique + PQC) est recommandé par le BSI et la feuille de route de l'UE, et exigé par l'ANSSI selon un site de synthèse non vérifié. FN-DSA (Falcon) et HQC ne sont pas encore normalisés. AES et SHA-2/SHA-3 d'au moins 128 bits de sécurité ne sont pas à migrer pour la PQC. En revanche, SHA-1 est en fin de vie : il disparaît des certificats publics depuis le 15 septembre 2026 et sera interdit dans les modules FIPS après 2030.
8. **Si vous êtes dans le champ de NIS2 ou de DORA**, la feuille de route européenne rappelle que ces textes imposent déjà des mesures de gestion des risques, y compris une cryptographie « à l'état de l'art ». Ils ne fixent pas d'échéance PQC. Le texte des directives n'a pas été relu pour ce document.

## Ce que cela n'implique pas

- **Il n'y a pas d'obligation légale générale de migrer vers la PQC** pour une PME ou une ETI privée aujourd'hui : ni dans l'UE, ni au Royaume-Uni, ni en France ou en Allemagne (où les textes sont des recommandations), ni aux États-Unis hors de la chaîne fédérale.
- **PCI DSS 12.3.3 n'exige ni migration post-quantique ni « CBOM »** au sens où l'emploient certains éditeurs. À la lettre, un inventaire documenté, revu chaque année et assorti d'une stratégie suffit.
- **NIST IR 8547 n'interdit pas RSA ou les courbes elliptiques aux entreprises privées** en 2030 ou 2035. Le texte fixe le statut de ces algorithmes dans les normes du NIST. L'effet passe par les marchés publics et la validation FIPS 140. Un algorithme « déprécié » reste utilisable pendant la migration, en acceptant un risque.
- **La feuille de route européenne n'oblige pas les entreprises**, et la proposition COM(2026) 13 n'est pas une loi. Même adoptée, elle viserait les États membres.
- **L'EO 14412 ne fixe aucune échéance aux opérateurs d'infrastructures critiques** : les agences sectorielles doivent seulement les accompagner. Les systèmes de sécurité nationale suivent leur propre circuit (CNSA 2.0).
- **La feuille de route du G7 ne crée pas d'attentes réglementaires** pour les banques ou assureurs, comme elle le dit elle-même.
- **Le raccourcissement des certificats n'est pas une exigence post-quantique**, et passer à la PQC ne dispense pas de l'automatiser.
- **Aucun de ces textes n'impose une date de bascule unique.** Tous recommandent une démarche fondée sur les risques, système par système.

## Points restant à vérifier avant citation à un client

Les éléments suivants n'ont pas pu être vérifiés dans une source primaire le 22 novembre 2026 :

- **NSA CNSA 2.0** : la date de 2027 (contre 2028 chez atsec) et le retrait fin 2030. Les sites de la NSA ont refusé l'accès automatisé.
- **ANSSI** : l'hybridation obligatoire et son exception pour les signatures à base de hachage, ainsi que le calendrier 2026/2030/2035. Le site de l'ANSSI bloque l'accès automatisé. L'affirmation d'un site de synthèse selon laquelle l'ANSSI cesserait de certifier des produits non résistants au quantique dès 2027 n'est pas reprise ici.
- **ASD (Australie)** : la fin de la cryptographie asymétrique classique d'ici 2030. Le site de l'ASD a refusé la connexion.
- **PCI DSS** : les alinéas « veille » et « stratégie » de 12.3.3, et l'exigence 4.2.1.1. La norme elle-même, diffusée sous licence, n'a pas été consultée.
- **NIS2, COM(2026) 13** : le numéro d'article (7(2)(k)), l'alignement sur 2030/2035 et la date exacte de la proposition (14 ou 20 janvier 2026).
- **États-Unis, textes attendus** : la publication du projet de règle FAR (attendu vers le 19 décembre 2026) et des éléments minimaux du CBOM (attendus vers le 19 mars 2027). La définition des « covered contractors » reste inconnue.
- **Datation et révisions** :
  - G7 : le jour exact de publication (le document indique seulement « janvier 2026 »).
  - BSI : le jour exact de la fin de recommandation de DSA en 2029.
  - NCSC : la révision d'août 2026 du PDF, qui n'a pas été lue.
  - Canada : la publication des instruments du Secrétariat du Conseil du Trésor.
- **NIS2 (art. 21) et DORA** : leurs obligations cryptographiques générales.
- **Hors périmètre, non traités** : Japon, Corée du Sud, Inde, Émirats arabes unis, Chine, Singapour (MAS), normes techniques DORA, Cyber Resilience Act, EO 14306 et OMB M-23-02.
