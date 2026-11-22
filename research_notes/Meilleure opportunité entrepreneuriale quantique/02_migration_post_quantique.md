# Post-quantum cryptography (PQC) migration and crypto-agility, assessed as a zero-capital solo-founder opportunity (state as of 22 Nov 2026)

Scope note: research done 22 Nov 2026. Each claim carries the date of its source. Most market, pricing and survey material comes from vendors or aggregators with commercial interests, and those sources are flagged. The session's shared web-search budget ran out before searches on MSSP white-label, medical devices/FDA, Capgemini Research Institute, DORA/CRA text, SWIFT and MAS. Those topics are listed under Gaps and were not researched.

---

## 1. Which binding or quasi-binding deadlines exist worldwide, and what do they require?

### Takeaway
The deadlines are real and became firmer in 2026: US EO 14412 (June 2026), OMB M-26-15, final NIST IR 8547 (27 Oct 2026), the CNSA 2.0 procurement gate (Jan 2027), the EU roadmap, and the UK NCSC 2028/2031/2035 plan. Almost all of them bind governments, national-security vendors and, through procurement, federal contractors. For ordinary private companies, the main enforceable item today is PCI DSS 12.3.3, which requires a cipher-suite and protocol inventory but no PQC migration. Everything else in the private sector remains guidance, with 2030–2035 horizons.

### Cited Findings
**US: NIST standards**
- In Aug 2024 NIST published FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA). On 11 Mar 2025 it selected HQC as a fifth, backup KEM — [NIST news, Mar 2025](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption)
- HQC: a FIPS is "under development". NIST says it has no current plans to standardize further KEMs beyond HQC (summary of the final IR 8547, 30 Oct 2026) — [CSA Research Note](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ir8547-pqc-transition-20261030-csa-st/). NIST's stated plan was a draft in 2026 and a final standard in 2027. I found no evidence that the HQC draft has been published — [Utimaco summary](https://utimaco.com/news/blog-posts/pqc-news-nist-announces-hqc-fifth-algorithm-be-standardized)
- FIPS 206 (FN-DSA/Falcon): NIST submitted the draft for approval on 28 Aug 2025 ([DigiCert blog, 5 Sep 2025](https://www.digicert.com/blog/quantum-ready-fndsa-nears-draft-approval-from-nist)). NIST's 2025 slides called the draft "basically written, awaiting approval" ([NIST presentation](https://csrc.nist.gov/csrc/media/presentations/2025/fips-206-fn-dsa-%28falcon%29/images-media/fips_206-perlner_2.1.pdf)). I found no confirmation that a final FIPS 206 had been published as of Nov 2026. Vendors expect late 2026 or early 2027 — [Encryption Consulting](https://www.encryptionconsulting.com/education-center/fn-dsa-fips-206/)
- **NIST IR 8547 (final), published 27 Oct 2026:**
  - All approved quantum-vulnerable public-key algorithms (RSA, ECDSA/EdDSA, finite-field and elliptic-curve DH, MQV) are **deprecated after 2030 and disallowed after 2035, at every key size**.
  - The Nov 2024 draft had spared 128-bit-strength parameters such as RSA-3072, P-256 and Ed25519 until 2035. The final text removes that exception.
  - ML-KEM-768 is the recommended default. Ascon (SP 800-232) is added.
  - Hybrid key establishment can be FIPS 140-validated if at least one component is approved.
  - NIST says it is "a high priority for vendors to initiate the integration of PQC support immediately" (HSMs and TPMs especially).
  - IR 8547 does not bind private firms directly. It reaches them through procurement.
  - Source: [CSA Research Note, 30 Oct 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ir8547-pqc-transition-20261030-csa-st/); also [Help Net Security, 28 Oct 2026](https://www.helpnetsecurity.com/2026/10/28/nist-post-quantum-cryptography-migration-roadmap/), [postquantum.com](https://postquantum.com/security-pqc/nist-ir-8547-final/), [NIST PDF](https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8547.pdf)

**US: Executive orders and OMB**
- **EO 14412, "Securing the Nation Against Advanced Cryptographic Attacks"**, signed 22 Jun 2026 and published in the Federal Register on 25 Jun 2026 — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ir8547-pqc-transition-20261030-csa-st/); [Cloudflare, 23 Jun 2026](https://blog.cloudflare.com/post-quantum-eo-2026). Some early commentary misnumbered the order, citing EO 14306 or others — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ir8547-pqc-transition-20261030-csa-st/)
- EO 14412 and OMB M-26-15 milestones ([Pyramid Systems, 26–29 Oct 2026](https://pyramidsystems.com/insights/blog/post-quantum-cryptography-federal-migration)):

  | Date | Milestone | Status at 22 Nov 2026 |
  |---|---|---|
  | 22 Jul 2026 | Each agency names a PQC migration lead | Passed |
  | 24 Jun 2026 | OMB guidance (M-26-15) issued, ahead of its 20 Sep 2026 due date | Done |
  | 22 Oct 2026 | Agency migration plans due to OMB/ONCD | Passed |
  | ~19 Dec 2026 | FAR Council proposed rule requiring covered contractors to comply with PQC-capable FIPS; NIST revises CMVP to speed up PQC module validation; NIST PQC pilot starts | Not yet seen |
  | ~19 Mar 2027 | CISA/NIST minimum elements of a **CBOM** | Not yet due |
  | 2 Jan 2030 | Agencies support TLS 1.3 (first set by EO 14306) | — |
  | 31 Dec 2030 | High-value assets and high-impact systems use PQC key establishment; covered contractors compliant | — |
  | 31 Dec 2031 | Same systems use PQC signatures | — |
  | 2035 | Remaining systems | — |

- M-26-15 phases: discovery 2026–27, pilots 2027–28, key establishment 2028–30, signatures 2031. The inventory has no fixed deadline, but plans must describe inventory methods and tools. "Covered contractors" is not yet defined. Funding depends on appropriations — [Pyramid Systems](https://pyramidsystems.com/insights/blog/post-quantum-cryptography-federal-migration)
- M-26-15 also requires agencies to include PQC in product requirements for CISA-listed categories, and to define PQC responsibilities with FedRAMP providers — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ir8547-pqc-transition-20261030-csa-st/)
- National Security Systems are excluded from EO 14412 and follow a separate classified track. Critical-infrastructure operators have **no hard deadline** — [Cloudflare, 23 Jun 2026](https://blog.cloudflare.com/post-quantum-eo-2026)
- EO 14306 (6 Jun 2025) led CISA to publish PQC product categories on 23 Jan 2026. Once a category is listed as "widely available", agencies should buy only PQC-capable products in it. Sources disagree on which categories are listed (cloud PaaS/IaaS, browsers, endpoint security, networking...) — [CISA bulletin](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/405c246); [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/cisa-post-quantum-cryptography/); [The Quantum Insider, 27 Jan 2026](https://thequantuminsider.com/2026/01/27/cisa-issues-federal-buying-guidance-for-post-quantum-cryptography/)

**US: NSA CNSA 2.0**
- From **1 Jan 2027**, new National Security System acquisitions must be CNSA 2.0 compliant by default (CNSSP 15). Equipment that cannot support CNSA 2.0 must be phased out by 31 Dec 2030 — [postquantum.com "2027 procurement gate"](https://postquantum.com/cnsa-2-0/2027-procurement-gate/). This is contradicted by [atsec](https://atsec.de/cnsa-compliance-to-be-mandatory-starting-in-2027/), which says CNSA 1.0 is mandatory from 2027 and CNSA 2.0 from 1 Jan 2028. The primary text was not checked.

**EU**
- The Coordinated Implementation Roadmap was adopted in June 2025:
  - All Member States should start the transition and have national PQC roadmaps by **end-2026**.
  - High-risk use cases (energy, water, health, finance, transport) should be protected by **end-2030**.
  - Everything should be done by **end-2035**.
  - Sources: [EC policy page](https://digital-strategy.ec.europa.eu/en/policies/post-quantum-cryptography); [ANSSI publication](https://cyber.gouv.fr/en/publications/jointly-led-international-publications/roadmap-for-the-transition-to-pqc/); [ESA/DG CONNECT slides](https://indico.esa.int/event/571/attachments/7210/13622/Ongoing,%20planned%20and%20potential%20future%20activities%20in%20PQC%20at%20DG%20CONNECT.pdf)
- A CEPS task force notes that the roadmap leaves the initiative to Member States and does not bind the Commission — [CEPS, Oct 2025](https://cdn.ceps.eu/2025/10/Task-FORCE-Comments-on-the-NIS-CG-Roadmap-on-PQC-Transition_FINAL.pdf)
- NIS2 amendment COM(2026) 13 (20 Jan 2026; procedure 2026/0012(COD)) proposes a new Art. 7(2)(k). It would require **Member States** to put a PQC transition policy in their national cybersecurity strategies, aligned with 2030/2035. It is a proposal, not law. Adoption is expected late 2026 or more likely 2027, followed by roughly 12 months for transposition. The obligation falls on states, not companies — [postquantum.com](https://postquantum.com/security-pqc/eu-pqc-nis2/); [EP Legislative Observatory](https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1884097); [Mayer Brown, 20 Feb 2026](https://www.mayerbrown.com/en/insights/publications/2026/02/european-commission-proposes-major-cybersecurity-package-to-strengthen-eu-cyber-resilience)
- **France (ANSSI):** deployment from 2026, high-risk by 2030, complete by 2035. Hybrid is mandatory except for hash-based signatures. An aggregator claims France stops certifying non-quantum-safe products from 2027 (unverified) — [Encryption Consulting country guide, 5 Apr 2026](https://www.encryptionconsulting.com/pqc-migration-deadlines-by-country/); [arcqubit aggregator](https://www.arcqubit.ai/blog/pqc-mandates-deadlines)
- **Germany (BSI TR-02102-1, version 2026-01):**
  - Federal deployment from 2026.
  - Critical infrastructure and high-protection systems by 2030.
  - Classical-only key agreement sunsets 31 Dec 2031 for regulated use.
  - The same guide's claim that an "ML-KEM + FrodoKEM dual hybrid" is required looks garbled and should be checked against the BSI text.
  - Source: [Encryption Consulting](https://www.encryptionconsulting.com/pqc-migration-deadlines-by-country/)

**UK**
- NCSC milestones:
  - By **2028**: define goals, complete full discovery and build an initial plan.
  - By **2031**: migrate the highest-priority services.
  - By **2035**: migrate all systems.
  - Sources: [NCSC guidance](https://ncsc.gov.uk/guidance/pqc-migration-timelines); [PDF revised Aug 2026](https://www.ncsc.gov.uk/sites/default/files/2026-08/Timelines-for-migration-to-post-quantum-cryptography.pdf)
- NCSC Assured Cyber Security Consultancy PQC pilot: assured firms reported are Arqit, Avella, Cambridge Consultants, Capgemini, CGI, Frazer-Nash, IBM and PQShield. The pilot runs to March 2027 — [NCSC scheme page](https://www.ncsc.gov.uk/schemes/assured-cyber-security-consultancy/pqc-pilot); [The Stack](https://www.thestack.technology/eight-firms-blessed-by-the-ncsc-for-post-quantum-cryptography-overhauls/)

**Rest of world** (aggregator-sourced, verify against primary texts)
All from [Encryption Consulting, 5 Apr 2026, status as of 24 Jun 2026](https://www.encryptionconsulting.com/pqc-migration-deadlines-by-country/) unless noted:
- **Australia (ASD ISM):** refined plan by end-2026; critical systems begin by end-2028; **classical asymmetric cryptography eliminated from government systems by end-2030**. Binding for government. Hybrid is allowed but not recommended.
- **Canada (CCCS ITSM.40.001, Jun 2025):** federal departments submitted initial plans in Apr 2026 and report annually; high-priority systems by end-2031; all by end-2035. Binding for federal departments.
- **Japan (CRYPTREC):** ML-KEM added to the CRYPTREC list in Apr 2026; national roadmap expected 2027; ~2035 is an estimate. Advisory.
- **South Korea (KPQC):** public-sector rollout mandated from 2026; full-migration date TBD.
- **India (DST/National Quantum Mission task force):** CII sectors complete inventory and pilots by 2027; high-priority CII by 2030; PQC default by 2033. Not clearly binding. The date of the task-force report conflicts: Feb 2026 per Encryption Consulting, May 2026 per [depthgrid](https://www.depthgrid.in/2026/10/post-quantum-cryptography-migration-deadlines.html).
- **UAE:** National Encryption Policy approved 2025; compliance-critical entities must formalise migration plans in 2026.
- **China:** no public deadline. OSCCA algorithms differ from the FIPS ones.

**Finance, payments and the web PKI**
- **G7 Cyber Expert Group** (co-chaired by US Treasury and Bank of England), 12 Jan 2026: a non-binding six-phase financial-sector roadmap. It cites 2035 as a "reasonable target", stresses crypto-agility and third-party dependence, and is explicit that it sets no regulatory expectations — [G7 CEG PDF](https://home.treasury.gov/system/files/136/G7-CEG-Quantum-Roadmap.pdf); [UK gov](https://www.gov.uk/government/publications/advancing-a-coordinated-roadmap-for-the-transition-to-post-quantum-cryptography-in-the-financial-sector); [ABA Banking Journal, Jan 2026](https://bankingjournal.aba.com/2026/01/g7-expert-group-releases-cybersecurity-roadmap-for-post-quantum-cryptography/)
- **PCI DSS 4.0.1 Req. 12.3.3:** became mandatory on 31 Mar 2025. It requires:
  - a documented inventory of cipher suites and protocols in use, with their purpose and where they are used;
  - monitoring of their continued viability;
  - a documented strategy for responding to anticipated cryptographic vulnerabilities;
  - review at least every 12 months.

  It sets **no PQC deadline**. Vendor claims that 12.3.3 "requires a CBOM" are vendor framing, not the standard's wording — [postquantum.com](https://postquantum.com/security-pqc/pci-dss-v4-quantum-cryptographic-requirements/); [Schellman](https://www.schellman.com/blog/pci-compliance/new-cryptographic-pci-dss-v4-requirement); [Encryption Consulting](https://www.encryptionconsulting.com/pci-dss-v4-requirement-on-cbom/)
- **CA/Browser Forum ballot SC-081v3** (passed Apr 2025): maximum public TLS certificate lifetime is 398 days until 15 Mar 2026, then **200 days from 15 Mar 2026** (already in force), **100 days from 15 Mar 2027**, and **47 days from 15 Mar 2029**. Domain-validation reuse falls to 10 days in 2029 — [DigiCert](https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days); [CABF vote thread](https://groups.google.com/a/groups.cabforum.org/g/servercert-wg/c/bvWh5RN6tYI/m/6yPQAxRcCAAJ); [SSL.com](https://ssl.com/article/preparing-for-45-day-ssl-tls-certificates/)

### Inferences
- The forcing functions that bind on dated deadlines fall in four places:
  1. US federal agencies (plans already submitted in Oct 2026).
  2. Vendors to National Security Systems (CNSA 2.0, from Jan 2027 or 2028).
  3. Federal contractors, through a FAR rule that does not yet exist (proposal due around Dec 2026, compliance by end-2030).
  4. Government systems in Australia, Canada and the UK.
- The EU instruments bind Member States, not companies, until NIS2 is amended and transposed, which is realistically 2028 or later.
- For the private-sector mid-market, the only enforceable item today is PCI 12.3.3. It can be met with a cipher-suite and protocol inventory, often a spreadsheet plus TLS scans, so willingness to pay is limited.
- The CA/B certificate-lifetime cut is a stronger, already-dated pain for SMEs (200 days now, 100 days in Mar 2027). That is certificate-lifecycle automation, though, not PQC, and free ACME tooling plus incumbent CLM vendors compete for it.
- The most interesting near-term trigger for software vendors is the CISA CBOM minimum elements (~Mar 2027) combined with the FAR contractor rule. If both land, vendors selling to the US government will need CBOMs. Both texts are still pending, so timing and scope are speculative.

### Gaps
- OMB M-23-02 (Nov 2022, annual agency inventory) was not re-verified, nor was how M-26-15 supersedes or extends it.
- Primary texts were not checked for: CNSSP 15 (2027 vs 2028), ASD ISM, BSI TR-02102-1, the ANSSI 2027 product-certification claim, MAS (Singapore), SWIFT and the Europol Quantum Safe Financial Forum. Search budget was exhausted.
- DORA (RTS on ICT risk management, Delegated Reg. 2024/1774) and Cyber Resilience Act cryptography provisions were not verified in this session. From background knowledge only: DORA's RTS require an encryption/cryptographic-controls policy that follows developments in cryptanalysis, and the CRA requires "state of the art" protection with obligations phasing in 2026–2027. Treat both as unverified.
- The NCSC timelines PDF sits under a "2026-08" path, which suggests a revision in Aug 2026. Its changes were not read.

---

## 2. How big is the PQC / quantum-safe market in 2025–2026, and how much is booked revenue versus forecast?

### Takeaway
Analyst estimates for 2025–2026 range from about $0.4B to $1.6B depending on definition, and forecasts run to $2–30B by 2030–2034. Publicly verifiable revenue of pure-play PQC firms is far smaller: Arqit about $1M in FY2026, SEALSQ $18M in 2025 (mostly secure chips). The largest private player, SandboxAQ, is a diversified AI/quantum firm whose PQC share is not disclosed. Most actual spending is absorbed inside existing PKI, HSM, CLM and consulting budgets.

### Cited Findings
- **MarketsandMarkets:** $0.42B in 2025, $0.60B in 2026, $3.80B by 2031 — [MarketsandMarkets press release](https://www.marketsandmarkets.com/PressReleases/post-quantum-cryptography.asp); [Quantum Zeitgeist](https://quantumzeitgeist.com/nist-post-quantum-3-8-billion/)
- **Other estimates:**
  - IMARC: $470.2M in 2025, $19.17B by 2034 — [IMARC](https://imarcgroup.com/post-quantum-cryptography-market)
  - P&S Intelligence: $1.6B in 2025, $15.9B by 2032 — [P&S](https://www.psmarketresearch.com/market-analysis/post-quantum-cryptography-market-report)
  - Ken Research: $1.38B in 2025 — [Ken Research](https://www.kenresearch.com/industry-reports/global-post-quantum-cryptography-market.md)
  - Roots Analysis: $0.61B in 2026 — [Roots](https://www.rootsanalysis.com/post-quantum-cryptography-market)
  - Technavio: +$3.42B incremental 2025–2030 at 43.4% CAGR — [Technavio](https://www.technavio.com/report/post-quantum-cryptography-market-industry-analysis)
  - A further estimate of $29.95B by 2034 — [MojoAuth relay](https://mojoauth.com/news/post-quantum-cryptography-market-to-reach-usd-2995-bn-by-2034)
- **Arqit (listed, fiscal year to 30 Sep 2026):** preliminary FY2026 revenue about $975k–$1M, against $530k in FY2025. H2 was hurt by the end of revenue recognition on a Middle East contract. Cash about $51M — [The Quantum Insider, 9 Oct 2026](https://thequantuminsider.com/2026/10/09/arqit-preliminary-fiscal-2026-revenue-1-million/)
- **SEALSQ (listed; PQC secure elements and semiconductors):**
  - FY2025 audited revenue $18.3M; 2026 guidance $27–36M — [Finviz/GlobeNewswire](https://finviz.com/news/341397/sealsq-announces-fy-2025-audited-financial-results-reaffirms-q1-2026-expectations-fy-2026-guidance-updates-on-partnerships-and-qs7001-certification-go-to-market-execution)
  - H1 2026 revenue $11.2M (+131%); cash about $486M — [Quantum Computing Report](https://quantumcomputingreport.com/sealsq-reports-h1-2026-financial-results-revenue-surges-131-to-11-2m-486m-cash-balance-and-post-quantum-hardware-progress/?noamp=mobile); [The Quantum Insider, 11 Sep 2026](https://thequantuminsider.com/2026/09/11/sealsq-h1-2026-results-fy2026-guidance/)
- **SandboxAQ revenue (sources conflict):** 2025 revenue $90M per [CB Insights](https://www.cbinsights.com/company/sandbox-aq/financials), against $128M "disclosed with latest round" per [Multiples.vc](https://multiples.vc/private-comps/sandboxaq). Neither is PQC-specific, and SandboxAQ also sells AI simulation models.
- **Keyfactor (PKI/CLM incumbent):** cited 32% year-over-year ARR growth when it announced the InfoSec Global and CipherInsights deals (13 May 2025). Its valuation is about $1.3B after a Sixth Street investment — [The Quantum Insider, 14 May 2025](https://thequantuminsider.com/2025/05/14/keyfactor-acquires-infosec-global-and-cipherinsights-for-quantum-safe-security-expansion/)
- **Survey signals of slow conversion into spend:**
  - DigiCert, Jul 2026 (n=1,001 in US/UK/AU, fielded May 2026): 87% are "planning, testing or implementing" PQC, but **only 7% have deployed** quantum-safe or hybrid cryptography across most certificates, up 2 points in a year. 44% have plans and inventories — [DigiCert press release, 23 Jul 2026](https://www.digicert.com/news/quantum-security-deployment-remains-stuck)
  - Entrust/Ponemon, 27 Jan 2026: 38% are actively preparing for PQC, down from 41%. Budget is cited as a challenge by 39%, up from 31%. The postquantum.com analyst floats a possible "quantum winter" in enthusiasm — [postquantum.com review](https://postquantum.com/security-pqc/entrust-ponemon-pqc-report-2026/)

### Inferences
- Even the lowest analyst figure ($0.4–0.6B for 2026) is spread across HSMs, secure chips, PKI/CLM upgrades, discovery platforms and consulting. The slice for "discovery/CBOM software for the mid-market" is likely tens of millions of dollars, but no source quantifies it.
- The "booked" PQC money visible in public filings is small (Arqit about $1M). Large sums appear in private valuations (SandboxAQ, Keyfactor) and in government contracts with undisclosed values. Forecast CAGRs of 22–49% are vendor and analyst projections that assume regulation converts into spend. The flat-to-declining 2026 survey indicators (Entrust) suggest that conversion is slower than forecast.

### Gaps
- No credible source separates spending on discovery/inventory/CBOM from HSM, PKI or chip spending.
- No Gartner, Forrester or ABI market sizing was retrieved. Gartner's public line remains that asymmetric cryptography is "unsafe by 2029, fully breakable by 2034" — [Gartner article](https://gcom.pdo.aws.gartner.com/en/articles/post-quantum-cryptography); a Gartner analyst quoted by TechRadar says 2030 — [TechRadar](https://www.techradar.com/pro/gartner-the-quantum-threat-is-already-behind-schedule).
- PQShield revenue is not public.

---

## 3. Who are the competitors by segment, with funding, revenue and pricing?

### Takeaway
Discovery, inventory and CBOM is already a consolidated, well-funded segment: SandboxAQ with a Pentagon-wide deal, Keyfactor after buying InfoSec Global and CipherInsights, IBM through Guardium and the CBOMkit it donated to open source, QuSecure, and the CAs (DigiCert, Sectigo) now shipping readiness tools, some of them free. Below them sits a long tail of free open-source scanners and micro-consultancies selling $4–7k fixed-price assessments. In the UK, government-assured advice is limited to eight named firms.

### Cited Findings
**Discovery, inventory and CBOM platforms**
- **SandboxAQ (AQtive Guard):**
  - Five-year agreement with the DoW/DoD CIO to deploy AQtive Guard for automated cryptographic discovery and inventory across the department, with access for other DoW agencies. Value undisclosed; reported 11 Dec 2025 — [Quantum Zeitgeist](https://quantumzeitgeist.com/sandboxaq-post-quantum-cryptography-quantum-security); [S&P Global, Feb 2026](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/2/quantitative-ai-company-s-us-defense-deal-highlights-evolving-cybersecurity-97460811)
  - Funding is unsettled. Securities.io treats a Series E of more than $450M (2025) as the latest independently supportable round — [Securities.io](https://www.securities.io/buy-sandboxaq/). A reported May 2026 Series F of $500M is valued at $9.84B by [DefiLlama](https://defillama.com/pre-ipo/sandbox-aq) and at $13.89B post-money by [a tear sheet](https://siliconvalleyinvestclub.com/it/companies/sandboxaq/tear-sheet.pdf). No primary announcement was found.
- **Keyfactor:**
  - Acquired InfoSec Global (AgileSec Analytics for discovery across code, devices and cloud; AgileSec Agility for remediation) and **CipherInsights** (a passive network sensor formerly owned by Quantum Xchange), announced 13 May 2025. Both integrate with Keyfactor Command for certificate migration — [Keyfactor press release](https://www.keyfactor.com/press-releases/keyfactor-acquires-infosec-global-and-cipherinsights/); [BusinessWire](https://www.businesswire.com/news/home/20250513745017/en)
  - ABI Research describes PKI-sector M&A as vendors expanding into crypto-agility — [ABI Research](https://www.abiresearch.com/market-research/insight/7786231-pki-ecosystem-evolution-modernization-shak)
- **IBM:**
  - Open-sourced CBOMkit in 2024 and donated it to the Linux Foundation's PQCA. Components: Hyperion/sonar-cryptography (a SonarQube plugin for Java, Python and Go source code), Theia (images and directories), a GitHub Action, a viewer and an API — [IBM Research blog](https://researcher.ibm.com/blog/cryptographic-cbom-linux-foundation); [GitHub PQCA/sonar-cryptography](https://github.com/PQCA/sonar-cryptography); [cbomkit-theia](https://github.com/cbomkit/cbomkit-theia)
  - IBM is also an NCSC-assured PQC consultancy (see Q1).
- **QuSecure (QuProtect):**
  - $28M Series A led by Two Bear Capital with Accenture Ventures, Feb 2025; new CEO Rebecca Krauthamer — [The Quantum Insider, 12 Feb 2025](https://thequantuminsider.com/2025/02/12/qusecure-closes-additional-series-a-funding-names-new-ceo/)
  - QuProtect R3 adds encryption visibility, Sep 2025 — [Help Net Security](https://www.helpnetsecurity.com/2025/09/18/qusecure-quprotect-r3-encryption/)
  - AWS Marketplace listing is "Private Offer Only", with no public price — [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-y7wezxxklklp4)
- **Quantum Xchange:** about $23.5M raised (Series A). It sold CipherInsights to Keyfactor in 2025 — [CB Insights](https://www.cbinsights.com/company/quantum-xchange)
- **PQShield (IP cores and libraries rather than discovery):** $37M Series B, Jun 2024, led by Addition — [SecurityWeek](https://www.securityweek.com/post-quantum-cryptography-firm-pqshield-raises-37-million/); [TechCrunch](https://techcrunch.com/2024/06/20/pqshield-secures-37m-more-for-quantum-resistant-cryptography). About $70.5M raised in total — [CB Insights](https://www.cbinsights.com/company/pqshield). No 2026 round found.
- **DigiCert Quantum Central:** asset discovery, remediation prioritisation and migration tracking. Free preview launched Jul 2026 — [IT Brief AU](https://itbrief.com.au/story/digicert-launches-quantum-central-for-post-quantum-readiness); [DigiCert](https://www.digicert.com/quantum-central). DigiCert also runs a free TLS PQC checker — [DigiCert PQC checker](https://www.digicert.com/pqc-checker)
- **Sectigo Quantum Ready (QSPM):** launched 17 Sep 2026 for enterprise cryptographic discovery and dependency mapping, via an early-access programme with no public price — [Sectigo](https://www.sectigo.com/resource-library/sectigo-introduces-sectigo-quantum-ready-qspm); [IT Brief AU](https://itbrief.com.au/story/sectigo-launches-quantum-readiness-tool-for-enterprises)
- **Other AWS Marketplace entrants:**
  - Avahi PQC Readiness Assessment (custom pricing) — [listing](https://aws.amazon.com/marketplace/pp/prodview-3v23v3rwhli54)
  - QuantumGenie/CipherScan (priced per unit; price not shown), Q by Q.security (scoped discovery and CBOM pilot)
  - GaraTrust (Garantir), certificate management at a flat **$99K/year**, the only clear annual price found and a CLM benchmark rather than a discovery one
  - These are summarised from [AWS Marketplace search results](https://aws.amazon.com/marketplace/pp/prodview-bdfqsqxnj232s), and the individual listings were not each verified.
- **Software supply-chain vendors that already emit CBOMs:** OPSWAT MetaDefender — [OPSWAT](https://www.opswat.com/blog/meet-cbom-cryptographic-visibility-arrives-in-metadefender-software-supply-chain-4-2-0); Mondoo — [Mondoo](https://mondoo.com/docs/xgrep/code-scanning/cbom); ReversingLabs Spectra Assure — [ReversingLabs](https://www.reversinglabs.com/blog/what-a-cbom-is); Encryption Consulting "CBOM Secure" — [datasheet](https://www.encryptionconsulting.com/wp-content/downloads/EC_CBOM_Secure_Datasheet.pdf).
- **SEALSQ:** PQC hardware and secure elements (see Q2).

**Open-source and free tools**
- pqcscan (SSH/TLS PQC-algorithm scanner, announced Jul 2025) — [Help Net Security](https://www.helpnetsecurity.com/2025/07/14/pqcscan-open-source-post-quantum-cryptography-scanner/); [oss-security](https://openwall.com/lists/oss-security/2025/07/10/1)
- pqready (Rust) — [docs.rs](https://docs.rs/pqready); tlsferret (sslscan-like, with ML-KEM) — [docs.rs](https://docs.rs/tlsferret)
- QRAMM TLS analyzer — [ecosyste.ms](https://awesome.ecosyste.ms/api/v1/projects/github.com%2Fcsnp%2Fqramm-tls-analyzer)
- Keylens CBOM (Rust) — [GitHub](https://github.com/keylens/cbom); pqcheck (CycloneDX 1.6 CBOM plus SARIF) — [PyPI](https://pypi.org/project/pqcheck/); cbomctl (policy checks on an existing CBOM) — [PyPI](https://pypi.org/project/cbomctl/)
- Free online tests: ImmuniWeb PQC TLS test — [Help Net Security, Sep 2025](https://www.helpnetsecurity.com/2025/09/19/immuniweb-ssl-security-test/); Cloudflare Radar per-domain PQ check — [Cloudflare blog](https://blog.cloudflare.com/post-quantum-visibility/)

**Consulting and micro-consultancies**
- NCSC-assured PQC pilot firms: Arqit, Avella, Cambridge Consultants, Capgemini, CGI, Frazer-Nash, IBM, PQShield — [The Stack](https://www.thestack.technology/eight-firms-blessed-by-the-ncsc-for-post-quantum-cryptography-overhauls/)
- Accenture invested in QuSecure through Accenture Ventures — [The Quantum Insider](https://thequantuminsider.com/2025/02/12/qusecure-closes-additional-series-a-funding-names-new-ceo/)
- Micro-firms and their prices are listed in Q5: PQC Consultancy (INKASEC), PQC NOW (ZincirX), QryptoCyber, Encryption Consulting.

### Inferences
- The enterprise and government discovery segment is effectively closed to a new entrant without a brand. The DoD, the reference buyer, signed a five-year platform deal with SandboxAQ. The PKI incumbents (Keyfactor, DigiCert, Sectigo) bundle discovery into the certificate relationship, and DigiCert gives it away free in preview. IBM made the reference source-code CBOM scanner open source.
- Supply-chain security vendors (OPSWAT, ReversingLabs, Mondoo) already generate CBOMs. That pre-empts "CBOM-as-a-feature" for software vendors.
- Competition at the low end is on price and trust, not technology: many free scanners exist, and at least two micro-firms sell sub-$7k fixed-price assessments.

### Gaps
- No 2025–26 data was gathered on Thales, Entrust (Entrust's newsroom returned 403), Venafi/CyberArk, AppViewX, ISARA, CryptoNext, Qrypt, evolutionQ, Cryptomathic, Post-Quantum (UK), PQStation, or Big Four PQC practices (Deloitte, KPMG, EY, PwC).
- GitHub star counts for CBOMkit, pqcscan and similar projects could not be retrieved, because repository API access was not enabled in this session.
- IBM Guardium Quantum Safe pricing was not found.

---

## 4. Which customer segments are underserved, and is any segment realistically open to a zero-capital solo founder?

### Takeaway
Surveys show a real expertise gap: 38% lack in-house expertise, and only 26% have full crypto-agility. The mid-market, non-English markets and software vendors facing future CBOM or contractor requirements are the least served by enterprise vendors. These segments also have the weakest legal compulsion today and the lowest willingness to pay. The only plausible openings for a zero-capital founder are narrow, service-led niches, and none of them looks like a durable standalone PQC company.

### Cited Findings
- **Entrust/Ponemon (27 Jan 2026; headline n=4,149, though the methods table sums to 2,925):**
  - Lack of in-house expertise rose to 38% from 28%.
  - Budget is a challenge for 39%.
  - 26% cannot change legacy applications.
  - 36% cite "no clear ownership".
  - Only 26% have a fully implemented crypto-agility strategy.
  - 47% have PKI specialists on staff, which implies the rest rely on outside help.
  - Source: [postquantum.com review](https://postquantum.com/security-pqc/entrust-ponemon-pqc-report-2026/); [Entrust newsroom](https://www.entrust.com/company/newsroom/entrust-global-report-finds-cryptographic-visibility-stagnant-as-quantum-threat-nears)
  - Only 32% are compiling a cryptographic inventory or ensuring crypto-agility, down from 38%; 41% name visibility as the top barrier — [Security Boulevard, Feb 2026](https://securityboulevard.com/2026/02/survey-sees-little-post-quantum-computing-encryption-progress/); [Crowdfund Insider, Feb 2026](https://www.crowdfundinsider.com/2026/02/262719-companies-know-post-quantums-coming-but-few-are-preparing-entrust/)
- **DigiCert (Jul 2026):** legacy complexity (25.6%) has replaced standards uncertainty as the top barrier. Only 10–18% self-identify as "leading edge" — [DigiCert](https://www.digicert.com/news/quantum-security-deployment-remains-stuck)
- **Sectigo 2026 (n=500 senior leaders):** 62% have a complete inventory of public TLS certificates, up from 28% in 2025. Only 38% have fully assessed quantum-vulnerable systems, up from 14% — [Sectigo](https://www.sectigo.com/state-of-crypto-agility-report)
- **Axiad (Jul 2026, 315 US organisations with 500+ employees):** 75% claim a continuously updated cryptographic inventory, but 25% say theirs is stale, partial or nonexistent. This illustrates how inconsistent the surveys are — [Webull/PR relay](https://www.webull.com/news/15429629597991936)
- **Federal SaaS and contractors:** M-26-15 requires agencies to define PQC responsibilities with FedRAMP providers and to include PQC in product requirements. The FAR rule will cover "covered contractors", who are not yet defined — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ir8547-pqc-transition-20261030-csa-st/); [Pyramid Systems](https://pyramidsystems.com/insights/blog/post-quantum-cryptography-federal-migration)
- **Critical-infrastructure operators:** no hard US deadline under EO 14412 — [Cloudflare](https://blog.cloudflare.com/post-quantum-eo-2026)
- **Regional maturity:** the postquantum.com reviewer notes that DACH leads regionally in the Entrust data and attributes this, speculatively, to EU privacy regulation — [postquantum.com](https://postquantum.com/security-pqc/entrust-ponemon-pqc-report-2026/)
- **Payment processors and fintechs:** PCI 12.3.3 has been enforced since Mar 2025 but requires only an inventory and strategy, with no PQC migration — [postquantum.com](https://postquantum.com/security-pqc/pci-dss-v4-quantum-cryptographic-requirements/)

### Inferences
Each segment is assessed from a zero-capital, no-brand viewpoint, using the findings above.

- **SMEs and mid-market (general):** underserved, but there is no compulsion before about 2030, and their TLS edge is increasingly PQ by default through CDN and cloud providers (see Q7). Willingness to pay is low and already anchored by free tools and $3.9k–£4.9k offers. The likely result is a lead-generation trickle, not a business. **Weak.**
- **Fintechs and payment processors (PCI 12.3.3):** the only enforced private-sector requirement. QSAs, existing compliance platforms and free scanners can meet it, and it does not require PQC. A product that turns TLS/SSH/code scans plus questionnaires into a 12.3.3 "cipher-suite inventory and response strategy" document is technically trivial with AI agents. It would most likely be a feature that GRC platforms add, not a stand-alone company. **Possible as a micro-product or lead magnet; not defensible.**
- **SaaS vendors answering PQC questions in security questionnaires:** no direct evidence of volume was found (Gap). The best-supported version is SaaS selling to US federal agencies or FedRAMP. Those firms are already in heavyweight compliance stacks and buy from established vendors. **Speculative.**
- **Software vendors needing a CBOM:** the trigger (CISA minimum elements, ~Mar 2027) has not happened yet. Open-source generators (CBOMkit, pqcheck, Keylens) and supply-chain vendors (OPSWAT, ReversingLabs, Mondoo) already exist. The opening would be a "CBOM-in-CI plus attestation" workflow for small ISVs, but incumbents will add the CISA schema quickly. **A timing bet with a short window.**
- **Federal contractors and CMMC suppliers:** the deadline is real but distant (2030), and the rule is not yet proposed. Selling to defence contractors usually requires US presence and credibility. **Hard for a non-US solo founder.**
- **Medical device, IoT and OT manufacturers:** the real work is in hardware, firmware and secure elements (SEALSQ-type firms with hundreds of millions in cash). It needs deep embedded-crypto expertise and long certification cycles. **Not zero-capital friendly.**
- **MSPs and MSSPs (white-label):** structurally plausible, since they own SME relationships and need a cheap repeatable deliverable. No evidence was gathered (search budget exhausted). **Untested hypothesis, worth customer interviews before building.**
- **Non-English markets (France, Germany, Spain, LatAm, Middle East, Asia):**
  - The national roadmaps due by end-2026 under the EU plan, the ANSSI and BSI positions, India's 2027 critical-infrastructure inventory target and the UAE's 2026 plans create local-language demand for guidance and templates.
  - The barrier is trust: national qualification schemes and government-assured lists (the UK pattern of eight assured firms) tend to favour incumbents.
  - **Most credible niche for a bilingual founder** would be localized, regulation-mapped readiness packs and training for ETI/PME (mid-sized and small companies) and their auditors. Even this is likely a modest services business (tens of thousands to low hundreds of thousands of €/year), not a scalable SaaS.

**Overall verdict on Q4:** no segment combines (a) a binding near-term deadline, (b) willingness to pay, (c) an absence of free or bundled alternatives and (d) low trust requirements. The best realistic shape is a **service-led, AI-accelerated readiness and compliance offer** in a non-English market or a PCI/CBOM niche, used as a wedge into broader cybersecurity compliance (NIS2, DORA, PCI). A stand-alone PQC company looks like a "false good idea" for this founder profile.

### Gaps
- No primary evidence on volume of PQC questions in SaaS security questionnaires; no MSSP white-label PQC programme data; no FDA or medical-device PQC expectations; no data on local-language PQC tooling in FR/DE/ES/LatAm/Middle East. Searches were not completed because the budget ran out.

---

## 5. What do buyers actually pay today for an inventory, a readiness assessment or a roadmap, and are there public tender values?

### Takeaway
Public price points cluster as follows: free (scans, single-repo CBOM, CA previews), $3.9k–£4.9k fixed-price small-scope assessments, $12.5k–$27.5k for larger fixed scopes or workshops, and six to seven figures for enterprise programmes. Government tenders for inventory work are appearing in the US, but no award values were found.

### Cited Findings
- **PQC Consultancy ("powered by INKASEC"):**
  - **Free** single-repo source-code CBOM scan.
  - **Tier 1 £4,875 / $6,500**: up to 100 assets, 2–3 weeks, remote, CBOM plus risk classification plus roadmap, with a refund if no actionable finding.
  - **Tier 2 £20,625 / $27,500**: up to 500 assets, including HSM/KMS and TLS/SSH/VPN audit.
  - Tier 3 price on request; training £1,500 (1-hour briefing) to £3,000 (half-day); M&A due diligence from £5,000.
  - Source: [pricing page, accessed 22 Nov 2026](https://pqcconsultancy.com/pricing.html)
- **PQC NOW (operated by ZincirX Inc.):** **$3,900** readiness assessment including an inventory of up to 50 assets, 2–3 weeks; $499 scoping credited; migration help from $499; briefings $990; self-paced courses from $49. No customer evidence shown — [pqcnow.com, accessed 22 Nov 2026](https://pqcnow.com/)
- **QryptoCyber:** fixed-price "Full Simulation" $25,000; workshop $12,500 (up to 20 participants) — [QryptoCyber](https://qryptocyber.com/cryptographic-inventory-simulation/); [QryptoCyber Step Zero](https://qryptocyber.com/no-clue-where-to-start-with-pqc-heres-step-zero-our-new-services-to-kickstart-your-journey/)
- **QNSQY vendor budget template:** inventory and discovery $10–50K for a 100-employee organisation, $100–500K for 1,000 employees, $500K–5M for 10,000+. Explicitly vendor-authored — [QNSQY blog](https://quantumsequrity.com/blog/pqc-migration-budget-planning)
- **Telco programme example:** external consulting "a few hundred thousand to a couple million dollars". The initial inventory is "on the order of a few million" for a large telco (illustrative) — [postquantum.com telco programme](https://postquantum.com/post-quantum/quantum-readiness-telco/)
- **Free self-assessment tools are already available** (browser-based PQC readiness self-assessment) — [postquantum.com](https://postquantum.com/post-quantum/free-pqc-readiness-self-assessment/)
- **CLM benchmark:** GaraTrust certificate management at $99K/year flat on AWS Marketplace — [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-bdfqsqxnj232s) (listing not individually verified)
- **US government demand signals (no values found):**
  - US Navy (NIWC Atlantic) "Zero Trust PQC Roadmap" AOI 26-A006 under CSO N6523626S0001 seeks a continuously updated baseline inventory of all cryptographic algorithms, protocols and modules. Responses were due 8 Jul 2026 — [GovDash](https://discover.govdash.com/solicitations/019f1976-7ca5-73cc-b9e5-15dc2f2a68c1--zero-trust-post-quantum-cryptography-pqc-roadmap-aoi-26-a006-under-rcc-cso-n6523)
  - GSA sources-sought notice "PQC Readiness and Validation Status", responses due 8 Dec 2026 — [GovContractFinder](https://govcontractfinder.com/contracts/post-quantum-cryptography-pqc-readiness-and-validation-statu-sam-opportunity-66d06f12955c485282e56fe41547e408); [GovDash](https://discover.govdash.com/solicitations/01a1b345-de8e-75ff-84c1-76610ca0d79d--post-quantum-cryptography-pqc-readiness-and-validation-status)
  - GSA justification for restricted competition on PQC and federal identity-management support services, contract 47QACB26C0004, dated 24 Sep 2026 (FAR 13.5); no value shown — [SAM.gov](https://sam.gov/workspace/contract/opp/cefe37153fc54c809ca8274983691bb5/view)
- **QVS solo-built scanner:** free scan plus a **$49** premium PDF report (see Q6) — [dev.to](https://dev.to/qvs_quantumvulnerability/i-built-a-quantum-vulnerability-scanner-in-2-weeks-heres-what-i-learned-300b)

### Inferences
- The going rate for an SME or mid-market "readiness assessment plus inventory plus roadmap" is already anchored at roughly $4–7k by remote micro-firms offering refund guarantees. An AI-leveraged solo founder can match that cost structure but cannot undercut it meaningfully, since free alternatives already sit below.
- Large tickets exist only where trust, on-site access and multi-month work are needed: telcos, banks and government.
- Government buying runs through formal vehicles (Navy CSO, GSA). A solo founder could at best subcontract.

### Gaps
- A search snippet reported a UK G-Cloud 15 supplier listing a one-time PQC assessment at £6,000–£28,000 and continuous annual assessment at £35,000–£115,000 (ex-VAT). The supplier and URL were not identified, so the figure is unverified.
- No TED (EU) tender values, no Big Four rate cards, and no SAM.gov award amounts for PQC inventory were found.

---

## 6. What evidence exists of low-capital entrants earning revenue here, and what happened to them?

### Takeaway
Many low-capital entrants have launched since 2025: solo-built scanners, Product Hunt launches, open-source CLIs and remote micro-consultancies. I found **no public evidence that any of them reached meaningful revenue**. The visible exit path is acquisition of a component by an incumbent (CipherInsights to Keyfactor), and even listed pure-plays post tiny revenue (Arqit about $1M in FY2026).

### Cited Findings
- **QVS (Quantum Vulnerability Scanner):**
  - Solo build in about 2 weeks (Python/FastAPI, 46 regex patterns, pyca/cryptography, ReportLab, Stripe, Render).
  - Free scan of URLs, files and code, plus a $49 premium report.
  - The author concedes regex is "not deep cryptographic analysis". No revenue, user or customer figures were reported. Posted Apr 2026.
  - Source: [dev.to](https://dev.to/qvs_quantumvulnerability/i-built-a-quantum-vulnerability-scanner-in-2-weeks-heres-what-i-learned-300b); [Product Hunt](https://www.producthunt.com/products/qvs-quantum-vulnerability-scanner)
- **Other small launches, all without public traction data:**
  - CipherAhead (code scanning, free tier) — [Product Hunt](https://www.producthunt.com/products/cipherahead/makers)
  - CyberReflex (quantum-readiness assessment) — [Product Hunt](https://www.producthunt.com/products/cyberreflex-2)
  - Cerebion Rivet (PQ vulnerability detection) — [Product Hunt](https://www.producthunt.com/p/post-4/cerebion-rivet)
  - PostQuant (open-source TLS and code grading) — [dev.to](https://dev.to/postquant)
  - quantakrypto qScan (npm) — [socket.dev](https://socket.dev/npm/package/@quantakrypto/qscan/overview/0.4.0)
- **Micro-consultancies** with public price lists: PQC Consultancy (INKASEC), PQC NOW (ZincirX), QryptoCyber. None discloses customers or revenue — [PQC Consultancy](https://pqcconsultancy.com/pricing.html); [PQC NOW](https://pqcnow.com/); [QryptoCyber](https://qryptocyber.com/cryptographic-inventory-simulation/)
- **Open-source-led projects:** pqcscan, pqready, tlsferret, QRAMM, Keylens and pqcheck exist as free tools. No associated commercial revenue was found — [Help Net Security](https://www.helpnetsecurity.com/2025/07/14/pqcscan-open-source-post-quantum-cryptography-scanner/); [docs.rs pqready](https://docs.rs/pqready)
- **Exit precedent:** Quantum Xchange (about $23.5M raised) sold its CipherInsights discovery product to Keyfactor (May 2025) — [Keyfactor](https://www.keyfactor.com/press-releases/keyfactor-acquires-infosec-global-and-cipherinsights/); [CB Insights](https://www.cbinsights.com/company/quantum-xchange)
- **Revenue benchmark:** Arqit, a listed quantum-safe pure-play, posted about $1M FY2026 revenue after years of operation — [The Quantum Insider](https://thequantuminsider.com/2026/10/09/arqit-preliminary-fiscal-2026-revenue-1-million/)

### Inferences
- Building a PQC scanner is now a two-week weekend project, which is the clearest sign of commoditisation. The scarce asset is distribution and trust, not code.
- The "free scan, then paid PDF" model has many imitators and no visible traction. This is consistent with buyers who do not yet feel compelled to pay.
- The realistic upside for a small, technically strong discovery tool is to become an acqui-hire or tuck-in for a PKI incumbent. That route needs credibility and enterprise design partners, which a no-brand solo founder lacks.

### Gaps
- No interviews, revenue disclosures or post-mortems from solo PQC founders were found.
- Hacker News and Reddit ground-truth threads were not retrieved (search budget exhausted).

---

## 7. What are the hard barriers?

### Takeaway
The barriers are severe:
- **Trust and assurance gating:** assured-consultancy lists, FIPS/CMVP, government vehicles.
- **Incumbents bundling discovery for free** into PKI/CLM relationships.
- **Cloud and CDN defaults** that already make most web TLS hybrid-PQ, shrinking the "easy" part of the problem.
- **Commoditised open-source scanners.**
- **Weak private-sector compulsion until 2030.**

The hard residual work (signatures, PKI, HSMs, legacy apps, firmware) needs deep expertise and privileged access, not a SaaS front end.

### Cited Findings
- **Cloud and CDN defaults:**
  - Cloudflare has enabled hybrid PQ key agreement on all domains it serves — [Cloudflare Radar](https://radar.cloudflare.com/post-quantum)
  - Client support for PQ rose from under 3% (early 2024) to over 60% (Feb 2026) — [Cloudflare blog](https://blog.cloudflare.com/radar-origin-pq-key-transparency-aspa/); [Cloudflare changelog, 27 Feb 2026](https://developers.cloudflare.com/changelog/post/2026-02-27-radar-pq-key-transparency/)
  - "Over two-thirds of browser traffic to Cloudflare's network is protected with post-quantum encryption" as of Jun 2026 — [Cloudflare, 23 Jun 2026](https://blog.cloudflare.com/post-quantum-eo-2026)
  - Chrome/Edge 131+ and Firefox 132+ support PQ key agreement — [Cloudflare Radar](https://radar.cloudflare.com/post-quantum)
- **Cloudflare advises against waiting for a complete CBOM.** Its guidance is to prioritise by impact and likelihood and turn on PQ encryption now, while signatures, roots and code-signing remain the hard part — [Cloudflare, Jun 2026](https://blog.cloudflare.com/post-quantum-eo-2026)
- **CISA notes that TLS products offer quantum-safe key establishment, but certificates and other elements are "still transitioning"** — [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/cisa-post-quantum-cryptography/)
- **Free bundling by incumbents:** DigiCert Quantum Central is a free preview (Jul 2026) — [IT Brief AU](https://itbrief.com.au/story/digicert-launches-quantum-central-for-post-quantum-readiness). Keyfactor integrates discovery with Command certificate automation — [Keyfactor](https://www.keyfactor.com/press-releases/keyfactor-acquires-infosec-global-and-cipherinsights/). Sectigo bundles Quantum Ready — [Sectigo](https://www.sectigo.com/resource-library/sectigo-introduces-sectigo-quantum-ready-qspm)
- **Trust and assurance gating:**
  - UK NCSC-assured PQC consultancy pilot limited to eight firms, running until March 2027 — [NCSC](https://www.ncsc.gov.uk/schemes/assured-cyber-security-consultancy/pqc-pilot)
  - The DoD reference deal went to SandboxAQ for five years — [Quantum Zeitgeist](https://quantumzeitgeist.com/sandboxaq-post-quantum-cryptography-quantum-security)
  - FIPS 140-3/CMVP validation and the CNSA 2.0 gate apply to product vendors — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ir8547-pqc-transition-20261030-csa-st/); [postquantum.com](https://postquantum.com/cnsa-2-0/2027-procurement-gate/)
- **Expertise and budget barriers on the buyer side:** expertise gap 38% and budget 39% (Entrust 2026) — [postquantum.com](https://postquantum.com/security-pqc/entrust-ponemon-pqc-report-2026/). Legacy complexity is the top barrier (DigiCert 2026) — [DigiCert](https://www.digicert.com/news/quantum-security-deployment-remains-stuck)
- **Weak compulsion:** the G7 roadmap is explicitly non-binding — [G7 CEG](https://home.treasury.gov/system/files/136/G7-CEG-Quantum-Roadmap.pdf). The EU roadmap does not bind the Commission and leaves initiative to Member States — [CEPS](https://cdn.ceps.eu/2025/10/Task-FORCE-Comments-on-the-NIS-CG-Roadmap-on-PQC-Transition_FINAL.pdf). Critical infrastructure has no hard US deadline — [Cloudflare](https://blog.cloudflare.com/post-quantum-eo-2026). PCI sets no PQC deadline — [postquantum.com](https://postquantum.com/security-pqc/pci-dss-v4-quantum-cryptographic-requirements/)
- **Commoditisation:** at least nine free or open-source scanners or online tests exist (Q3), and a solo developer built a usable one in about 2 weeks (Q6).
- **Uncertain timelines:** Gartner gives 2029 ("unsafe") or 2030 depending on the source — [Gartner](https://gcom.pdo.aws.gartner.com/en/articles/post-quantum-cryptography); [TechRadar](https://www.techradar.com/pro/gartner-the-quantum-threat-is-already-behind-schedule). Enthusiasm may already be stalling ("quantum winter" comment) — [postquantum.com](https://postquantum.com/security-pqc/entrust-ponemon-pqc-report-2026/)

### Inferences
- **Problem shrinkage:** the most automatable and externally visible part (public TLS key exchange) is being solved by default for anyone behind Cloudflare, the big clouds or modern browsers. What remains is internal PKI, signatures, code signing, HSM/KMS, mainframe and legacy apps, IoT firmware and vendor dependencies. That work needs privileged internal access, enterprise trust and specialised expertise, which is the opposite of a zero-capital, no-brand founder's strengths.
- **Sales-cycle mismatch:** buyers with money (federal, defence, banks, telcos) buy through vehicles, assured lists and incumbents, with long cycles. Buyers without gatekeepers (SMEs) have no deadline and lots of free options.
- **"False good idea" signals:** heavy marketing noise and forecast CAGRs, combined with flat adoption surveys, free incumbent tools, two-week-buildable scanners, no visible indie revenue, and deadlines (2030/2035) that are years beyond a bootstrapped founder's runway.
- **Counter-signal (honest):** the expertise gap is real and widening (28% to 38% lacking expertise), and the regulatory calendar is now firm. A founder with genuine cryptography or PKI credentials could run a profitable boutique consultancy. The value would come from that expertise, not from the AI tooling.

### Gaps
- AWS, Google Cloud and Microsoft 2025–26 PQC-by-default announcements were not retrieved directly; only Cloudflare data was gathered.
- There is no quantitative evidence of how much incumbent bundling depresses price.

---

## 8. How much of the work can current LLM agents automate, and is there published evidence?

### Takeaway
Detection, inventory formatting, CBOM generation, TLS/SSH scanning, regulation mapping and report drafting are highly automatable. Deterministic scanners plus LLM enrichment already reach 100% recall but only about 72% precision in the one quantitative 2026 study found. Correct remediation, especially code migration, still needs domain fine-tuning and expert review. Automation therefore lowers the cost of entry for everyone, including competitors, and does not create a moat.

### Cited Findings
- **Shaw, arXiv 2604.00560 (1 Apr 2026), "Quantum-Safe Code Auditor":**
  - Method: regex detection of 15 classes of quantum-vulnerable primitives, LLM contextual enrichment of usage and severity, and VQE-based risk scoring.
  - Data: 5,775 findings from 5 open-source libraries (python-rsa, python-ecdsa, python-jose, node-jsonwebtoken, Bouncy Castle). Evaluated on 602 labelled samples.
  - Results: **precision 71.98%, recall 100%, F1 83.71%**. False positives come mainly from algorithm-capability detection code.
  - Single author, small benchmark.
  - Source: [arXiv abs](https://arxiv.org/abs/2604.00560); [arXiv HTML](https://arxiv.org/html/2604.00560)
- **arXiv 2603.07204 (2026), "Detecting Cryptographically Relevant Software Packages with Collaborative LLMs":** LLM ensembles can act as a first-pass filter that reduces manual review. Its ground truth was itself LLM-generated (GPT-4o, Mistral-Large), which weakens the evidence — [arXiv](https://arxiv.org/html/2603.07204)
- **arXiv 2606.07341 (Jun 2026), "Empirical Evaluation of LLMs for Migration of Code Fragments to PQC":** finds domain-specific fine-tuning is essential for reliable RSA/ECDSA-to-PQC rewrites — [arXiv](https://arxiv.org/html/2606.07341v1)
- **arXiv 2606.19474 (Jun 2026):** proposes LLM-as-judge plus static analysis for secure PQC coding. Evaluation is future work — [arXiv](https://arxiv.org/html/2606.19474v1)
- **Deterministic tooling already covers much of the scanning:**
  - CBOMkit-Hyperion (SonarQube plugin) generates CBOMs for Java, Python and Go. Theia covers images and directories — [GitHub PQCA/sonar-cryptography](https://github.com/PQCA/sonar-cryptography); [cbomkit-theia](https://github.com/cbomkit/cbomkit-theia)
  - pqcscan covers TLS/SSH — [Help Net Security](https://www.helpnetsecurity.com/2025/07/14/pqcscan-open-source-post-quantum-cryptography-scanner/)
  - pqcheck emits CycloneDX 1.6 CBOM plus SARIF — [PyPI](https://pypi.org/project/pqcheck/)
- **Practitioner evidence of low build cost:** a 46-regex web scanner with PDF reports and Stripe was built in about 2 weeks — [dev.to](https://dev.to/qvs_quantumvulnerability/i-built-a-quantum-vulnerability-scanner-in-2-weeks-heres-what-i-learned-300b)
- **Vendors already market AI-assisted PQC tooling,** for example SuperQ's "PQC AI" — [The Quantum Insider](https://thequantuminsider.com/?p=2381261). An MCP server for PQC tools (quantakrypto) appears in MCP directories — [Enterprise DNA](https://enterprisedna.co/directories/mcp/quantakrypto-pqc-tools)

### Inferences
Automatability by task, inferred from the evidence above:

| Task | Automatable with current AI agents | Notes |
|---|---|---|
| Code scanning for crypto API usage | High (recall ~100%) | Needs human triage of about 28% false positives |
| CBOM generation (CycloneDX) | High | Already done by open-source tools |
| External TLS/SSH scanning | Very high | Fully commoditised |
| Regulation mapping and policy/roadmap drafting | High | LLMs excel, but accountability and sign-off remain human |
| Internal PKI, HSM/KMS, firmware, legacy discovery | Low | Requires privileged access, agents on hosts, network sensors |
| Remediation and code migration | Low–medium | Fine-tuning plus expert review needed |
| Vendor/supply-chain dependency analysis | Medium | Questionnaire chasing is automatable; answers depend on vendors |

- For a solo founder, AI agents make it realistic to deliver a credible mid-market readiness package (scan, CBOM, risk ranking, regulation map, roadmap) in days instead of weeks, at near-zero marginal cost. The same is true for every competitor, and the incumbents give the scanning away. Margin can therefore come only from trust, local-language and regulatory packaging, and distribution, not from automation itself.

### Gaps
- No published benchmark of autonomous coding or research agents (as opposed to LLM-assisted pipelines) on end-to-end cryptographic inventory of a real enterprise estate was found.
- No vendor disclosed measured labour savings from AI in PQC assessments.
