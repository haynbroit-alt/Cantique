# Post-quantum cryptography regulatory matrix

Version of 22 November 2026. Texts as they stood on that date.

> **Disclaimer.** This document is not legal advice. It summarises public texts to help an IT manager locate their organisation. Whether a text applies to a specific company, and with what consequences, is a question for a lawyer or the competent authority. Items marked "confidence: low" must not be quoted to a client without checking them first.

## In brief

- **For most private companies outside PCI DSS scope and outside public procurement, there is no binding post-quantum migration deadline today.** The other texts are recommendations, proposals, or obligations aimed at governments.
- The only requirement already enforceable against a broad population of companies is **PCI DSS 4.0.1 requirement 12.3.3**. In force since 31 March 2025, it requires an inventory of cryptographic cipher suites and protocols, reviewed every year. It requires no post-quantum migration.
- In the US, the firm deadlines (2030 for key establishment, 2031 for signatures) bind **federal agencies**. They will reach **federal contractors** if the FAR proposed rule announced by EO 14412 is published and then adopted. That proposal is due around 19 December 2026.
- In Europe and the UK, timelines converge on **2030 for high-risk use cases and 2035 for the rest**. These are recommendations, addressed to Member States in the EU and to large organisations by the NCSC.
- One dated deadline already affects every company with a website, though it is not PQC: the **maximum lifetime of public TLS certificates** falls from 200 days today to 100 days on 15 March 2027, then to 47 days in 2029.

## How to read this document

**Nature** (the text's force for its own target audience, not necessarily for your client):

- *Binding*: a direct obligation for the target audience (law, executive order, mandatory policy, contract).
- *Indirectly binding*: the text does not bind the company itself, but reaches it through a third party (public procurement, FIPS validation, certification authorities).
- *Recommendation*: guidance or roadmap with no mandatory force.
- *Proposal*: announced or pending text, not yet applicable.

**Confidence**:

- *High*: verified in the primary text on 22 November 2026.
- *Medium*: partly verified. The date or core wording is confirmed by an official source, the rest by consistent secondary sources.
- *Low*: not verified in a primary source (aggregator sites or secondary sources only).

**Deadlines**: when a text gives only a year ("by 2031"), the machine-readable file (`regles.json`) uses 31 December of that year. When it gives only a month, it uses the last day of that month. "After 2030" means from 1 January 2031. The identifier in brackets in the "Framework" column points to the matching framework in `regles.json`.

## International and sector-specific

| Framework | Who is affected | Requirement | Deadline | Nature | Source | Confidence |
|---|---|---|---|---|---|---|
| PCI DSS 4.0.1, requirement 12.3.3 [`PCI-DSS-4.0.1`] | Entities that store, process or transmit cardholder data, and their service providers | Cipher suites and protocols in use documented and reviewed at least every 12 months: up-to-date inventory (purpose, where used), monitoring of continued viability, strategy for anticipated vulnerabilities. No PQC deadline, and no "CBOM" requirement in the text | In force since 31 March 2025 | Binding (contractual, via card brands and acquirers) | [PCI SSC blog](https://blog.pcisecuritystandards.org/now-is-the-time-for-organizations-to-adopt-the-future-dated-requirements-of-pci-dss-v4-x); [PCI SSC-hosted document quoting 12.3.3](https://www.pcisecuritystandards.org/day-1_t2_7_pci-dss-v4-0_final/) | Medium: date and core wording confirmed by PCI SSC; monitoring and strategy bullets from secondary sources |
| PCI DSS 4.0.1, requirement 4.2.1.1 [`PCI-DSS-4.0.1`] | Same entities | Inventory of trusted keys and certificates protecting the card number (PAN) in transmission | Since 31 March 2025 | Binding (contractual) | [postquantum.com](https://postquantum.com/security-pqc/pci-dss-v4-quantum-cryptographic-requirements/) | Low: not verified in the standard |
| CA/Browser Forum Baseline Requirements v2.3.1 (ballot SC-081v3) [`CABF-SC-081`] | Public certification authorities; in practice, every holder of public TLS certificates | Maximum public TLS certificate lifetime: 200 days; 100 days; 47 days. Domain validation reuse: 200, 100, then 10 days. Not a PQC requirement | 15 March 2026 (in force); 15 March 2027; 15 March 2029 | Indirectly binding | [Baseline Requirements](https://github.com/cabforum/servercert/blob/main/docs/BR.md); [ballot SC-081v3](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/) | High |
| CA/Browser Forum Baseline Requirements v2.3.1 [`CABF-SC-081`] | Same | Sunset of all remaining SHA-1 use in certificates and revocation lists | 15 September 2026 | Indirectly binding | [Baseline Requirements](https://github.com/cabforum/servercert/blob/main/docs/BR.md) | High |
| G7 Cyber Expert Group, financial-sector roadmap [`G7-CEG-PQC-FINANCE`] | Financial institutions and financial authorities in G7 countries | Six phases (awareness, discovery, risk assessment, migration, testing, validation). Indicative 2035 target, with the most critical systems around 2030-32. The text "does not set guidance or regulatory expectations" | 2035 (indicative) | Recommendation | [G7 CEG (US Treasury)](https://home.treasury.gov/system/files/136/G7-CEG-Quantum-Roadmap.pdf) | High |

## United States

| Framework | Who is affected | Requirement | Deadline | Nature | Source | Confidence |
|---|---|---|---|---|---|---|
| NIST FIPS 203, 204, 205 [`NIST-FIPS-203-204-205`] | Federal agencies; companies through public contracts and FIPS 140-3 validation | Final standards: ML-KEM (key establishment), ML-DSA and SLH-DSA (signatures). ML-KEM is the only approved post-quantum key establishment scheme today | Published 13 August 2024 | Indirectly binding | [CSRC FIPS list](https://csrc.nist.gov/publications/fips) | High |
| NIST FIPS 206 (FN-DSA, derived from Falcon) [`NIST-FIPS-206-PROJET`] | Same, once published | Under development: do not present FN-DSA as approved. HQC, the alternative to ML-KEM, is also still awaiting its FIPS | No official date | Proposal | [NIST IR 8547](https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8547.pdf); [CSRC](https://csrc.nist.gov/publications/fips) | High (status as of 22 Nov 2026) |
| NIST IR 8547, final [`NIST-IR-8547`] | Federal agencies and, through procurement and FIPS 140 validation, their suppliers; does not bind private companies directly | RSA, ECDSA, EdDSA, DH, ECDH and MQV **deprecated after 2030** and **disallowed after 2035** under NIST standards, at every approved key size. ML-KEM-768 is the recommended default. Hybrid schemes can be FIPS 140-validated if one component is approved. SHA-1 disallowed in FIPS-validated modules after 2030. AES and SHA-2/SHA-3 at 128 bits or more remain adequate | After 2030; after 2035 | Indirectly binding | [NIST IR 8547 (27 Oct 2026)](https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8547.pdf) | High |
| Executive Order 14412 (22 June 2026) [`US-EO-14412`] | Federal agencies, excluding National Security Systems. No deadline for critical infrastructure operators | PQC migration lead named within 30 days. High value assets and high impact systems: PQC for key establishment, then for signatures | 22 July 2026; 31 Dec 2030; 31 Dec 2031 | Binding | [EO 14412 (govinfo)](https://www.govinfo.gov/content/pkg/DCPD-202600417/html/DCPD-202600417.htm) | High |
| OMB M-26-15 (24 June 2026) [`US-OMB-M-26-15`] | Federal agencies, excluding National Security Systems | Migration plan within 120 days, describing automated inventory methods and tools (a central CBOM is recommended). TLS 1.3 required. PQC in purchasing for CISA product categories. PQC responsibilities split with FedRAMP cloud providers. Full migration in phase 5 | 22 Oct 2026 (plan); 2 Jan 2030 (TLS 1.3); 2035 | Binding | [OMB M-26-15](https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf) | High |
| FAR proposed rules (EO 14412, sec. 6) [`US-FAR-PQC-PROJET`] | "Covered contractors" of federal agencies, a term the EO does not define | 1) Proposed rule requiring compliance with NIST FIPS, including PQC, **by 31 December 2030**. 2) Proposed rule on vulnerability disclosure, including cryptographic vulnerabilities | Proposals due around 19 Dec 2026 and 19 March 2027 | Proposal (not seen as of 22 Nov 2026) | [EO 14412](https://www.govinfo.gov/content/pkg/DCPD-202600417/html/DCPD-202600417.htm) | High for what the EO orders; final content unknown |
| CISA/NIST minimum elements of a CBOM [`US-CISA-CBOM-PROJET`] | Hardware and software suppliers, public buyers | Public guidance on the minimum content of a cryptographic bill of materials enabling automated assessment | Around 19 March 2027 | Proposal | [EO 14412](https://www.govinfo.gov/content/pkg/DCPD-202600417/html/DCPD-202600417.htm) | High for the deadline; publication not checked |
| CISA PQC product categories (23 Jan 2026) [`US-CISA-PQC-CATEGORIES`] | Buyers at federal civilian agencies; vendors selling to them | PQC "widely available" for cloud PaaS/IaaS, chat and messaging, web browsers and servers, data-at-rest encryption: buy only PQC-capable products in those categories | In effect | Recommendation | [CISA](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards) | High |
| NSA CNSA 2.0 / CNSSP 15 [`NSA-CNSA-2.0`] | National Security Systems (NSS) and their suppliers | New acquisitions CNSA 2.0 compliant unless an exception applies; non-compliant equipment phased out. **Date discrepancy**: atsec puts the CNSA 2.0 mandate in 2028, relying on NIAP Policy Letter 33, which governs product evaluation. These are probably two different tracks | 1 Jan 2027 (2028 per atsec); 31 Dec 2030 | Binding (for NSS) | [postquantum.com](https://postquantum.com/cnsa-2-0/2027-procurement-gate/); [atsec](https://atsec.de/cnsa-compliance-to-be-mandatory-starting-in-2027/) | Low: NSA text unreachable |

## European Union

| Framework | Who is affected | Requirement | Deadline | Nature | Source | Confidence |
|---|---|---|---|---|---|---|
| Coordinated Implementation Roadmap (NIS Cooperation Group, v1.1, published 23 June 2025) [`EU-PQC-ROADMAP`] | Member States. No direct obligation for companies | End-2026: First Steps, initial national roadmaps, planning and pilots. End-2030: high-risk use cases migrated (data needing protection for at least 10 years), quantum-safe upgrades on by default. End-2035: medium-risk use cases migrated, "as many systems as feasible". Hybrid solutions recommended | 31 Dec 2026; 31 Dec 2030; 31 Dec 2035 | Recommendation (follows a Commission recommendation; no binding legal effect on our reading) | [European Commission](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography); [text](https://ec.europa.eu/newsroom/dae/redirection/document/117507) | High |
| Proposed NIS2 amendment, COM(2026) 13 [`EU-NIS2-COM-2026-13`] | Member States (national cybersecurity strategies) | Would require Member States to include PQC migration policies in their national strategies. Only a proposal, in the ITRE committee of the European Parliament, followed by national transposition | Indicative first reading 8 March 2027; no applicable deadline | Proposal | [EP Legislative Observatory](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2026/0012(COD)) | Medium: procedure and content confirmed, article number and exact date not verified |

## United Kingdom

| Framework | Who is affected | Requirement | Deadline | Nature | Source | Confidence |
|---|---|---|---|---|---|---|
| NCSC PQC migration timelines (published 20 March 2025) [`UK-NCSC-PQC`] | Mainly large organisations, critical national infrastructure and bespoke IT. SMEs on commodity IT should migrate through vendor updates; those with custom software follow the same timetable | 2028: goals, full discovery, initial plan. 2031: highest-priority migrations, refined roadmap. 2035: complete migration | 2028; 2031; 2035 | Recommendation | [NCSC](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines) | High |

## France

| Framework | Who is affected | Requirement | Deadline | Nature | Source | Confidence |
|---|---|---|---|---|---|---|
| ANSSI positions on the post-quantum transition [`FR-ANSSI-PQC`] | Government bodies, operators, suppliers of ANSSI-evaluated products (exact scope not verified) | Hybridisation (classical + post-quantum) required, except for hash-based signatures. Timeline aligned on the EU roadmap, which ANSSI publishes | Deployment from 2026, high risk 2030, complete 2035 | Recommendation | [Encryption Consulting (aggregator)](https://www.encryptionconsulting.com/pqc-migration-deadlines-by-country/) | Low: ANSSI site unreachable |

## Germany

| Framework | Who is affected | Requirement | Deadline | Nature | Source | Confidence |
|---|---|---|---|---|---|---|
| BSI TR-02102-1, version 2026-01 (23 Jan 2026) [`DE-BSI-TR-02102-1`] | Mainly developers of new cryptographic systems. Other BSI documents can be binding for certain applications | Classical key agreement on its own recommended only until end-2031; very high protection needs: transition by end-2030. Classical signatures recommended until end-2035. Post-quantum mechanisms (ML-KEM, FrodoKEM, Classic McEliece) to be used in hybrid mode. DSA no longer recommended from 2029 | End-2030; end-2031; end-2035; 2029 (DSA) | Recommendation | [BSI TR-02102-1](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile) | High (medium for DSA 2029) |

The research notes reported a 31 December 2031 "sunset of classical key agreement for regulated use" and a required "ML-KEM + FrodoKEM dual hybrid". The BSI text contains neither. It makes recommendations, and FrodoKEM appears as one post-quantum option, not as a mandatory addition.

## Australia

| Framework | Who is affected | Requirement | Deadline | Nature | Source | Confidence |
|---|---|---|---|---|---|---|
| ASD Information Security Manual [`AU-ASD-ISM-PQC`] | Australian government entities | Refined plan by end-2026, critical systems start migrating by end-2028, classical asymmetric cryptography eliminated from government systems by end-2030; hybrid allowed but not recommended | End-2030 | Binding for government (per the notes) | [Encryption Consulting (aggregator)](https://www.encryptionconsulting.com/pqc-migration-deadlines-by-country/) | Low: ASD site unreachable |

## Canada

| Framework | Who is affected | Requirement | Deadline | Nature | Source | Confidence |
|---|---|---|---|---|---|---|
| Canadian Centre for Cyber Security, ITSM.40.001 (23 June 2025) [`CA-CCCS-ITSM-40-001`] | Federal departments and agencies | Initial departmental plan, then annual reporting; high-priority systems migrated; remaining systems migrated | April 2026; end-2031; end-2035 | Recommendation: a "recommended" roadmap that the Treasury Board Secretariat is to make mandatory | [Canadian Centre for Cyber Security](https://www.cyber.gc.ca/en/guidance/roadmap-migration-post-quantum-cryptography-government-canada-itsm40001) | High |

## What this means for an SME or mid-sized company

1. **If you accept or process card payments**, PCI DSS 12.3.3 already applies. You must keep an inventory of cryptographic cipher suites and protocols, review it at least once a year, track their viability, and document how you will respond to announced weaknesses. Your assessor (QSA) can ask for it now. The workshop's inventory feeds this requirement directly.
2. **If you sell to the US federal government**, directly or as a subcontractor, or provide a FedRAMP cloud service, watch for the FAR proposed rule due around 19 December 2026. As EO 14412 describes it, the rule would require compliance with NIST FIPS, including PQC, by end-2030. The minimum elements of a CBOM are due around March 2027. CISA already tells federal buyers to purchase only PQC-capable products in the categories it rates "widely available".
3. **If you supply a government body or critical operator in Europe or the UK**, expect questionnaires about your post-quantum roadmap. Your customers have to plan: Member States by end-2026, and large UK organisations must finish discovery by 2028. This is an inference from those timelines, not a written obligation aimed at you.
4. **For any website**, automate certificate renewal (for example with ACME). The maximum lifetime drops to 100 days on 15 March 2027 and to 47 days on 15 March 2029. This is not PQC, but it is a firm and close deadline.
5. **A cryptographic inventory is the first step in every one of these texts**: NCSC (discovery by 2028), the EU roadmap, OMB, BSI. They set the same priorities:
   - first, data that must stay confidential for a long time (at least 10 years per the EU), because of "harvest now, decrypt later";
   - key establishment first, then signatures;
   - systems that are hard to update first.
6. **You do not need to build your own cryptography.** The NCSC expects SMEs on commodity IT to receive PQC through vendor updates. Ask your software vendors and hosting providers for their PQC roadmap, and add the question to your procurement.
7. **Target algorithms**: ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205). Hybrid (classical + PQC) is recommended by BSI and the EU roadmap, and required by ANSSI according to an unverified aggregator. FN-DSA (Falcon) and HQC are not yet standardised. AES and SHA-2/SHA-3 at 128 bits of security or more do not need a PQC migration. SHA-1, by contrast, is at end of life: it has been sunset in public certificates since 15 September 2026 and will be disallowed in FIPS modules after 2030.
8. **If you are in scope of NIS2 or DORA**, the EU roadmap notes that these texts already require risk-management measures, including "state-of-the-art" cryptography. They set no PQC deadline. The directives' own text was not re-read for this document.

## What this does not mean

- **There is no general legal obligation to migrate to PQC** for a private SME or mid-sized company today: not in the EU, the UK, France or Germany (where the texts are recommendations), nor in the US outside the federal supply chain.
- **PCI DSS 12.3.3 requires neither a post-quantum migration nor a "CBOM"** in the sense some vendors use. Read literally, a documented inventory, reviewed annually and paired with a strategy, is enough.
- **NIST IR 8547 does not ban RSA or elliptic curves for private companies** in 2030 or 2035. It sets the status of these algorithms within NIST standards. The effect travels through procurement and FIPS 140 validation. A "deprecated" algorithm may still be used during migration, with the risk accepted.
- **The EU roadmap does not bind companies**, and COM(2026) 13 is not law. Even once adopted, it would address Member States.
- **EO 14412 sets no deadline for critical infrastructure operators**: sector agencies are only told to assist them. National Security Systems follow their own track (CNSA 2.0).
- **The G7 roadmap creates no regulatory expectations** for banks or insurers, as it says itself.
- **Shorter certificate lifetimes are not a post-quantum requirement**, and moving to PQC does not remove the need to automate renewal.
- **None of these texts imposes a single switch-over date.** All of them call for a risk-based approach, system by system.

## Items to check before quoting to a client

The following items could not be verified in a primary source on 22 November 2026:

- **NSA CNSA 2.0**: the 2027 date (versus 2028 at atsec) and the end-2030 phase-out. NSA sites refused automated access.
- **ANSSI**: mandatory hybridisation and its exception for hash-based signatures, and the 2026/2030/2035 timeline. The ANSSI site blocks automated access. An aggregator's claim that ANSSI will stop certifying non-quantum-safe products from 2027 is not included here.
- **ASD (Australia)**: the end of classical asymmetric cryptography by 2030. The ASD site refused the connection.
- **PCI DSS**: the monitoring and strategy bullets of 12.3.3, and requirement 4.2.1.1. The licensed standard itself was not consulted.
- **NIS2, COM(2026) 13**: the article number (7(2)(k)), alignment with 2030/2035, and the exact proposal date (14 or 20 January 2026).
- **US texts still due**: publication of the FAR proposed rule (due around 19 December 2026) and of the CBOM minimum elements (due around 19 March 2027). The definition of "covered contractors" is still unknown.
- **Dating and revisions**:
  - G7: the exact publication day (the document says only "January 2026").
  - BSI: the exact day in 2029 when DSA stops being recommended.
  - NCSC: the August 2026 revision of the PDF, which was not read.
  - Canada: publication of the Treasury Board Secretariat instruments.
- **NIS2 (Art. 21) and DORA**: their general cryptography obligations.
- **Out of scope, not covered**: Japan, South Korea, India, UAE, China, Singapore (MAS), DORA technical standards, the Cyber Resilience Act, EO 14306 and OMB M-23-02.
