# Attributions, licences des données et dépendances — ensemble « Cantique »

Relevé fait le **22 novembre 2026** sur les pages officielles citées. Les licences peuvent changer : l'acquéreur
doit revérifier ces pages avant chaque exploitation. Ce document est destiné à servir d'annexes 3 et 4 au
contrat de cession ; il n'est pas un conseil juridique.

**En bref, ce que l'acquéreur devra afficher** dans tout produit, export, API ou publication qui reprend les
données :

> Contient des données issues de CORDIS, © Union européenne, 1994-2026, réutilisées conformément à la
> décision 2011/833/UE de la Commission et sous licence CC BY 4.0
> (https://creativecommons.org/licenses/by/4.0/). Contient des informations du secteur public sous licence
> Open Government Licence v3.0
> (https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), issues de UKRI Gateway to
> Research (https://gtr.ukri.org/). Les données ont été sélectionnées, agrégées, converties et reclassées par
> l'éditeur ; ni l'Union européenne ni UKRI ne sont responsables de ces modifications ni n'approuvent ce
> produit.

> *English:* Contains data from CORDIS, © European Union, 1994-2026, reused under Commission Decision
> 2011/833/EU and the CC BY 4.0 licence (https://creativecommons.org/licenses/by/4.0/). Contains public
> sector information licensed under the Open Government Licence v3.0
> (https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), from UKRI Gateway to Research
> (https://gtr.ukri.org/). The data have been selected, aggregated, converted and reclassified by the
> publisher; neither the European Union nor UKRI is responsible for these changes or endorses this product.

---

## 1. CORDIS (Union européenne)

**Ce qui est utilisé.** Dumps open data CORDIS des projets Horizon Europe et H2020 (fichiers du
2026-11-05, fiche data.europa.eu `cordis-eu-research-projects-under-horizon-europe-2021-2027` et équivalent
H2020), pages projet `https://cordis.europa.eu/project/id/…`, API de recherche CORDIS pour contrôle. Fichiers
concernés : `activite/prospects/prospects.jsonl`, `prospects_recherche.jsonl`, `prospects.csv`,
`echantillon_precision.csv`, `activite/rapprochements/`, `activite/offre/` (exemples).

**Licence relevée.**

- Métadonnées de la fiche data.europa.eu (API `data.europa.eu/api/hub/search/datasets/…`) : licence
  « **European Commission reuse notice** », renvoyant à la décision 2011/833/UE
  (`http://data.europa.eu/eli/dec/2011/833/oj`).
- Avis de droit d'auteur de CORDIS (https://cordis.europa.eu/about/legal), texte relevé :

  > © European Union, 1994-2026
  > The Commission's reuse policy is implemented by Commission Decision 2011/833/EU of 12 December 2011 on the
  > reuse of Commission documents.
  > Unless otherwise noted (e.g. in individual copyright notices), the reuse of the editorial content on this
  > website owned by the EU is authorized under the Creative Commons Attribution 4.0 International (CC BY 4.0)
  > licence. This means that reuse is allowed, provided appropriate credit is given and any changes are
  > indicated.
  > You may be required to clear additional rights if a specific content depicts identifiable private
  > individuals or includes third-party works (drawings, photos, audio, video, etc.). To use or reproduce
  > content that is not owned by the EU, you may need to seek permission directly from the respective
  > rightholders. Software or documents covered by industrial property rights, such as patents, trademarks,
  > registered designs, logos and names, are excluded from the Commission's reuse policy and are not licensed
  > to you.
  > Materials provided by beneficiaries receiving EU funding may only be used according to the terms and
  > conditions applicable to the respective grant.
  > If in doubt, any copyright queries regarding the re-use of CORDIS documents or information, shall be
  > addressed by email to: op-copyright@publications.europa.eu

- Avis juridique de la Commission (https://commission.europa.eu/legal-notice_en), même principe : contenu de
  l'UE sous CC BY 4.0 sauf mention contraire, « reuse is allowed, provided appropriate credit is given and
  changes are indicated ».
- Décision 2011/833/UE, article 6 (conditions générales de réutilisation) : le texte n'a pas pu être relu
  automatiquement (EUR-Lex refuse les accès automatisés). Il prévoit, en substance, l'obligation de
  **mentionner la source**, de **ne pas dénaturer le sens** des documents et l'**absence de responsabilité**
  de la Commission. **À relire sur EUR-Lex** avant signature.
- Licence CC BY 4.0, section 3(a) (https://creativecommons.org/licenses/by/4.0/legalcode.en) : en cas de
  partage, conserver l'identification de l'auteur, la mention du droit d'auteur, la mention de la licence et
  de l'exclusion de garantie, un lien vers la source « to the extent reasonably practicable », **indiquer si
  le contenu a été modifié**, et indiquer la licence avec son texte ou son lien. Ces conditions peuvent être
  remplies « in any reasonable manner », par exemple par un lien vers une page qui les contient. La section 4
  précise qu'en cas de reprise d'une partie substantielle d'une base, la section 3(a) s'applique.

**Mention à afficher.**

- FR : « Contient des données issues de CORDIS, © Union européenne, 1994-2026, réutilisées conformément à la
  décision 2011/833/UE de la Commission et sous licence CC BY 4.0
  (https://creativecommons.org/licenses/by/4.0/). Source : https://cordis.europa.eu/. Données modifiées :
  sélection des projets de technologies quantiques, regroupement par organisation, conversion de devises,
  classement par segment. L'Union européenne n'est pas responsable de ces modifications. »
- EN : "Contains data from CORDIS, © European Union, 1994-2026, reused under Commission Decision 2011/833/EU
  and the CC BY 4.0 licence (https://creativecommons.org/licenses/by/4.0/). Source:
  https://cordis.europa.eu/. Modified data: selection of quantum-technology projects, grouping by
  organisation, currency conversion, classification by segment. The European Union is not responsible for
  these changes."

**Points de vigilance.** Les noms, logos et marques (dont « CORDIS », l'emblème européen) ne sont pas
licenciés : ne pas les utiliser d'une manière qui suggère un partenariat. Les textes rédigés par les
bénéficiaires (résumés de projets) relèvent des conditions de leur subvention : l'ensemble cédé n'en
reprend que les titres et des mots-clés comptés, pas les résumés.

## 2. UKRI Gateway to Research (Royaume-Uni)

**Ce qui est utilisé.** API Gateway to Research (GtR), projets, financements et organisations ; liens
`https://gtr.ukri.org/projects?ref=…`. Les liens vers des personnes ont été supprimés à la lecture et
jamais appelés. Fichiers concernés : les mêmes que pour CORDIS (organisations britanniques).

**Licence relevée.**

- UKRI, *Research Outcomes Collection — Principles of Use* (PDF publié sur ukri.org) :

  > Anyone may search, download and use UKRI Gateway to Research data in line with the Open Government
  > Licence (Open Government Licence (nationalarchives.gov.uk) except where otherwise stated.

- Open Government Licence v3.0 (https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/),
  conditions relevées :

  > You must (where you do any of the above):
  > acknowledge the source of the Information in your product or application by including or linking to any
  > attribution statement specified by the Information Provider(s) and, where possible, provide a link to this
  > licence;
  > If the Information Provider does not provide a specific attribution statement, you must use the following:
  > Contains public sector information licensed under the Open Government Licence v3.0.
  > If you are using Information from several Information Providers and listing multiple attributions is not
  > practical in your product or application, you may include a URI or hyperlink to a resource that contains
  > the required attribution statements.
  > These are important conditions of this licence and if you fail to comply with them the rights granted to
  > you under this licence, or any similar licence granted by the Licensor, will end automatically.

  La licence **ne couvre pas les données personnelles** (« personal data in the Information »), ni les logos,
  ni les autres droits de propriété intellectuelle ; elle **interdit de suggérer un statut officiel** ou un
  soutien du fournisseur (« Non-endorsement ») ; les informations sont fournies « as is ». Elle se déclare
  compatible avec CC BY 4.0 et l'Open Data Commons Attribution License.

- Conditions d'utilisation du site GtR (https://gtr.ukri.org/terms-of-use-for-gtr, « Last updated:
  2 November 2026 »), passages relevés :

  > Except as permitted for academic, personal or other non-commercial purposes, users must not reprint or
  > electronically reproduce from the GTR website any document, graphic or image in whole or in part without
  > the prior written permission of UKRI, or in accordance with the Copyright, Designs and Patents Act 1988.

  > Copyright restrictions — This website is open and free for all to use. We've developed it using open
  > source, open standards and an Open Government Licence (OGL) to enable the code to be reused by third
  > parties.

**Point de vigilance (à signaler à l'acquéreur).** Les principes d'usage placent les **données** de GtR sous
l'OGL v3.0, mais les conditions du **site** restreignent la reproduction commerciale de « documents,
graphiques ou images » sans autorisation. L'ensemble cédé ne reprend que des données factuelles
(organisation, projet, montants, dates, liens). Avant une exploitation commerciale, **demander à UKRI une
confirmation écrite** (formulaire « Contact us » du site GtR) que cette réutilisation relève bien de l'OGL.

**Mention à afficher.**

- EN (texte imposé par défaut par l'OGL, complété) : "Contains public sector information licensed under the
  Open Government Licence v3.0 (https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/),
  from UKRI Gateway to Research (https://gtr.ukri.org/). Amounts converted to euros at the ECB reference rate
  of 20 November 2026; data selected and aggregated by the publisher. UKRI does not endorse this product."
- FR : « Contient des informations du secteur public sous licence Open Government Licence v3.0 (lien
  ci-dessus), issues de UKRI Gateway to Research (https://gtr.ukri.org/). Montants convertis en euros au taux
  de référence de la BCE du 20 novembre 2026 ; données sélectionnées et agrégées par l'éditeur. UKRI
  n'approuve pas ce produit. »

**Autre point.** Le site www.ukri.org (pages d'appels « opportunity ») indique dans ses conditions que la
majorité de son contenu est sous **CC BY-NC-SA 4.0** (usage non commercial). Le calendrier des opportunités
ne reprend de ces pages que des faits (intitulé, dates, montants) et le lien ; ne pas y recopier de texte
descriptif des pages ukri.org.

## 3. Autres sources du calendrier des opportunités

Ces sources alimentent `activite/opportunites/` (intitulés, dates, montants, conditions, liens). Leur statut a
été vérifié seulement en partie ; **à confirmer** avant exploitation commerciale.

| Source | Statut relevé | Mention conseillée |
|---|---|---|
| Portail Funding & Tenders de la Commission (API SEDIA) | Contenu de la Commission : politique de réutilisation (décision 2011/833/UE), CC BY 4.0 sauf mention contraire (avis juridique de la Commission, relevé) | « Source : portail Funding & Tenders, © Union européenne, CC BY 4.0 » |
| TED (ted.europa.eu), avis de marchés UE | Page d'avis juridique non lisible automatiquement ; Office des publications de l'UE | à confirmer ; à défaut « Source : TED, © Union européenne » |
| Find a Tender (Royaume-Uni) | Pied de page relevé : « All content is available under the Open Government Licence v3.0, except where otherwise stated © Crown copyright » ; « Notices are based on TED XML schema. © European Union, https://ted.europa.eu, 1998–2020 » | mention OGL v3.0 (section 2) |
| Contracts Finder (Royaume-Uni) | Non vérifié ; service public britannique, a priori OGL v3.0 | à confirmer |
| SBIR.gov, NSF (États-Unis) | Non vérifié ; les œuvres du gouvernement fédéral américain ne sont en principe pas protégées aux États-Unis (17 U.S.C. § 105) | citer la source et le lien |
| BCE (taux de change, data-api.ecb.europa.eu) | Non vérifié | « Source : BCE » |
| Agences nationales et autres (Chips JU, EIC, Innovate UK, RVO, NQCC, BMFTR, Bpifrance, CDTI, ESA NAVISP) | Saisies manuelles : faits et liens seulement | citer la page officielle de chaque appel |

## 4. Contenus de tiers dans l'ensemble cédé

- **Dossiers de démonstration** (`atelier-pqc/demos/paramiko-3.5.1/`, `atelier-pqc/demos/pyjwt-2.10.1/`) :
  ils contiennent des chemins de fichiers et de **courts extraits d'une ligne** issus des bibliothèques
  libres analysées : **paramiko 3.5.1** (licence **LGPL-2.1**, © ses auteurs) et **PyJWT 2.10.1** (licence
  **MIT**, © ses auteurs). Conserver la mention de ces bibliothèques et de leurs licences avec les dossiers,
  ou retirer les extraits avant toute diffusion publique.
- **Fixtures de test** (`atelier-pqc/outils/tests/fixtures/`) : petits fichiers d'exemple écrits pour les
  tests (code fictif, certificat de test) ; aucune bibliothèque tierce n'y est recopiée.
- **Registre** (`registre-quantique/`) : de courts extraits de sources tierces (presse, entreprises,
  institutions), cités avec leur source, au titre du droit de courte citation (article L122-5 3° a) du Code de
  la propriété intellectuelle). Garder la brièveté des extraits et la mention des sources.
- **Matrice réglementaire** (`atelier-pqc/referentiel/`) : références et courts extraits de textes officiels
  (normes, recommandations, lois), chacun avec son lien. Les textes eux-mêmes restent soumis aux conditions
  de leurs éditeurs.
- **Noms d'organisations et marques** : ils sont cités pour identifier les organisations financées ; ils ne
  sont pas licenciés et ne doivent pas être utilisés pour suggérer un partenariat.

## 5. Dépendances open source

L'ensemble cédé **n'embarque aucun composant open source tiers** : le cœur des outils n'utilise que la
bibliothèque standard de Python. Les dépendances ci-dessous sont **facultatives** et s'installent séparément,
chacune sous sa propre licence. Licences relevées sur PyPI le 22 novembre 2026.

| Paquet | Utilisé par | Rôle | Licence |
|---|---|---|---|
| Python et sa bibliothèque standard (3.11 ou plus récent) | tous les outils | exécution | PSF License (Python Software Foundation License) |
| `cryptography` | `atelier-pqc/outils` (facultatif) | lecture détaillée des certificats X.509 | Apache-2.0 OR BSD-3-Clause |
| `cyclonedx-python-lib[json-validation]` | `atelier-pqc/outils` (facultatif) | validation du CBOM contre le schéma CycloneDX 1.6 | Apache-2.0 (ses dépendances transitives ont leurs propres licences : les inventorier à l'installation, par exemple avec `pip-licenses`) |
| `jsonschema` | `registre-quantique/valider.py` (facultatif) | validation des lignes contre `schema.json` | MIT |
| `pytest` | tests de `atelier-pqc/outils` | tests | MIT |
| `setuptools` | `atelier-pqc/outils/pyproject.toml` | construction du paquet | MIT |
| Schéma CycloneDX 1.6 | `atelier-pqc/outils/pqc_inventaire/cbom.py` (référence par URL, non embarqué) | format du CBOM | spécification CycloneDX (OWASP / Ecma) ; licence à vérifier sur cyclonedx.org |

## 6. Où afficher les mentions

- Dans le dépôt de l'acquéreur : ce fichier, ou un fichier `NOTICE` / `ATTRIBUTIONS.md` à la racine.
- Dans chaque produit, interface, export (CSV, JSON) ou API qui reprend les données : la mention courte en
  tête de ce document, ou un lien vers une page qui la contient (permis par CC BY 4.0 et l'OGL v3.0).
- Dans les documents remis à des clients (fiches, notes) : une ligne « Sources : CORDIS (© UE, CC BY 4.0) ;
  UKRI Gateway to Research (OGL v3.0) ».
