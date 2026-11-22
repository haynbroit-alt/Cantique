# Quantum software, developer tooling and quantum services layer (state as of Nov. 2026), seen as a business opportunity for a near-zero-capital solo founder

Research note. Every claim is dated and sourced inline. Revenue figures for private companies are mostly press estimates or aggregator figures, not audited accounts, and are flagged as such. Method limit: the web-search budget ran out during the session (the tool refused new searches). Several sub-questions (Kipu Quantum after 2023, BosonQ Psi, Aqarios, Quantum Brilliance software, planqc, Qubit Pharmaceuticals, Pasqal/Qadence, Nvidia CUDA-Q economics, freelance platforms, consulting day rates, Innovate UK/EU grants, DARPA QBI amounts) are therefore listed under Gaps rather than filled from memory.

---

## 1. Who are the main quantum software companies, and what is known about their funding, revenue, headcount and customers? Real commercial revenue versus grants?

### Takeaway
The whole layer runs on venture and government money. Disclosed or estimated revenues are tiny next to the money raised: Classiq makes about $8-9M a year after raising more than $200M; Quantinuum's software cannot be separated from its $30.9M of total 2025 revenue; Horizon Quantum's Q1 2026 revenue was $0. The firms with meaningful revenue earn it next to quantum computing rather than from quantum software: classical AI (Multiverse, SandboxAQ), quantum navigation and sensing (Q-CTRL), control hardware (Quantum Machines), or government programmes (Xanadu via DARPA). The buyers of "pure" software are mostly hardware vendors (IBM, Microsoft, Rigetti, Quantinuum), national labs and corporate R&D pilots.

### Cited Findings

**Algorithm and application-platform software**
- **Classiq (Israel).** $110M Series C in May 2025, billed as "the largest ever for a quantum software company"; total raised then $173M; valuation not disclosed, estimated above $400M — [Globes, May 2025](https://en.globes.co.il/en/article-1001510071); [Nasdaq press release](https://www.nasdaq.com/press-release/classiq-raises-110m-largest-ever-quantum-software-funding-round-2025-05-12).
  - Revenue estimated at **$8-9M per year**, "not company-confirmed"; the company claims it tripled customers and revenue year on year — [Globes](https://en.globes.co.il/en/article-1001510071).
  - Ynet says annual recurring revenue remains "in the low millions, primarily because clients are still in the experimental phase" (as summarised by search results, May 2025) — [Ynet](https://www.ynetnews.com/business/article/sy005l00ewxx).
  - Named customers: BMW, Citi, Deloitte, Rolls-Royce, Mizuho, Toshiba — [Globes](https://en.globes.co.il/en/article-1001510071).
  - In November 2025 a Series C extension of "tens of millions" from AMD Ventures, Qualcomm Ventures, IonQ and others took the round above $200M — [SiliconANGLE, 13 Nov 2025](https://siliconangle.com/2025/11/13/quantum-software-startup-classiq-raises-new-funding-amd-qualcomm/). CB Insights puts 2025 revenue in a $1-10M range — [CB Insights](https://www.cbinsights.com/company/classiq/financials).
- **Phasecraft (UK).** $34M Series B on 2 Sep 2025 (Plural, Playground Global, Novo Holdings); total raised over $50M **including grant funding** — [The Quantum Insider, 2 Sep 2025](https://thequantuminsider.com/2025/09/02/phasecraft-raises-34-million-from-plural-playground-global-and-novo-holdings/); [SiliconANGLE](https://siliconangle.com/2025/09/02/phasecraft-secures-34m-accelerate-practical-quantum-computing-solutions/). No revenue disclosed.
- **Algorithmiq (Finland, now Italy).** €18M round on 11 May 2026 (United Ventures, CDP); total €36M; HQ moved from Helsinki to Milan — [Algorithmiq press release, 11 May 2026](https://algorithmiq.fi/news/algorithmiq-establishes-milan-headquarters-and-raises-18m-to-position-europe-as-the-future-of-quantum-software).
  - The release cites "major commercial agreements with Microsoft, IBM, and Rigetti" in 2025, without terms or values. Its customers are therefore hardware and platform vendors.
  - No reports of layoffs were found.
- **QC Ware (US).** Now centred on **Promethium**, a GPU-accelerated quantum-chemistry SaaS launched in 2023. In other words, its product is classical computing on GPUs — [HPCwire, Apr 2023](https://www.hpcwire.com/2023/04/17/qc-ware-launches-promethium-a-quantum-chemistry-saas-targets-hybrid-world-near-term/); [qcware.com](https://qcware.com).
  - Its August and September 2026 hybrid demonstrations with IBM and IonQ hardware are described as proofs of concept, "not a fully integrated Promethium product capability" — [The Quantum Insider](https://thequantuminsider.com/?p=2391326); [HPCwire](https://www.hpcwire.com/off-the-wire/qc-ware-demonstrates-hybrid-quantum-classical-chemistry-workflow-with-ibm-quantum/).
  - One profile says QC Ware "has been at least two different companies wearing the same name" — [Halo/yespress profile](https://yespress.io/qc-ware-corp).
- **Zapata (US).** See question 2. Relaunched as Zapata Quantum (OTC: ZPTA); $15M financing in April 2026 — [TNW, 23 Apr 2026](https://thenextweb.com/news/zapata-quantum-15m-financing).
- **Horizon Quantum (Singapore).** Listed on Nasdaq (ticker HQ) on 20 Mar 2026 through a SPAC with dMY Squared, raising about $120M gross — [The Quantum Insider, 19 Mar 2026](https://thequantuminsider.com/2026/03/19/horizon-quantum-goes-public-via-spac-raises-120-million/).
  - **Q1 2026 revenue was $0.00 (Q1 2025 also $0)**, against $6.5M of operating expenses and $96.6M of cash — [Quantum Computing Report](https://quantumcomputingreport.com/horizon-quantum-reports-q1-2026-financial-results-nasdaq-debut-and-testbed-expansion/).
- **Terra Quantum (Switzerland/Germany).** Definitive business-combination agreement on 26 May 2026 with Axiom Intelligence Acquisition Corp 1 at a $3.5B equity valuation (from search-result summary; the primary source was not opened). No revenue data found.
- **1QBit (Canada).** CB Insights lists its stage as "Grant | Alive"; last raised $2.49M on 30 May 2024; $37.59M raised in total. No 2025-2026 news found — [CB Insights](https://www.cbinsights.com/company/1qbit-information-technologies).
- **BlueQubit (US/Armenia).** $10M seed in December 2024 led by Nyca Partners — [TechCrunch, 19 Dec 2024](https://techcrunch.com/2024/12/19/bluequbit-raises-10m-to-take-quantum-software-into-real-world-applications); [BlueQubit blog](https://www.bluequbit.io/blog/seed-funding-for-quantum-advantage).
- **Kipu Quantum (Germany).** €10.5M seed in December 2023 — [The Quantum Insider, 19 Dec 2023](https://thequantuminsider.com/2023/12/19/german-quantum-software-company-kipu-quantum-announces-e10-5-million-seed-round/). Its "Iskay Quantum Optimizer" is in IBM's Qiskit Functions catalog — [IBM blog, 11 Feb 2026](https://www.ibm.com/quantum/blog/functions-2026).

**Error suppression, error mitigation and "quantum OS"**
- **Q-CTRL (Australia).**
  - Series B extended to US$113M in October 2024, led by GP Bullhound — [Q-CTRL press release](https://q-ctrl.com/blog/q-ctrl-sets-global-quantum-technology-fundraising-record-increasing-series-b-to-usd-113m-led-by-gp-bullhound).
  - US$290M Series C announced 12 Nov 2026, led by Salesforce Ventures; valuation above US$1B — [eWeek, 19 Nov 2026](https://www.eweek.com/news/q-ctrl-290m-series-c-quantum-software-apac/).
  - The lead investor says "navigation already generates revenue". The split between computing software and navigation/sensing revenue is not disclosed — [eWeek](https://www.eweek.com/news/q-ctrl-290m-series-c-quantum-software-apac/).
  - Fire Opal launched in 2022 with free access for end users, with some features on paid plans — [Q-CTRL blog, Dec 2022](https://q-ctrl.com/blog/q-ctrl-releases-free-access-to-fire-opal-for-end-users-to-improve-quantum-algorithm-performance-by-up-to-1-000x). It is distributed through IBM Qiskit Functions to Premium and Flex customers — [Q-CTRL](https://q-ctrl.com/fire-opal/qiskit-functions).
- **Qedma (Israel).** $26M Series A in July 2025 (Glilot+, with IBM participating); planned headcount growth from about 40 to 50-60 — [TechCrunch, 3 Jul 2025](https://techcrunch.com/2025/07/03/israeli-quantum-startup-qedma-just-raised-26-million-with-ibm-joining-in); [The Quantum Insider](https://thequantuminsider.com/2025/07/04/qedma-raises-26-million-with-participation-from-ibm-to-tackle-quantum-computing-errors/).
  - Its QESEM product is sold through Qiskit Functions and integrated into Quantinuum Nexus — [IBM](https://www.ibm.com/quantum/blog/functions-2026); [search summary of Quantinuum IPO coverage](https://thequantuminsider.com/?p=2391477).
- **Haiqu (US/Ukraine).** $11M seed on 13 Jan 2026 (Primary Venture Partners; Toyota Ventures returning) to launch a "hardware-aware quantum operating system"; about $5.8M raised before this round — [Tech.eu, 13 Jan 2026](https://tech.eu/2026/01/13/quantum-startup-haiqu-raises-11m/); [The Quantum Insider](https://thequantuminsider.com/2026/01/13/haiqu-raises-11-million-in-seed-round/).

**Error correction and control (picks and shovels sold to hardware builders)**
- **Riverlane (UK).** $75M Series C in August 2024, led by Planet First Partners; "nearly 100" employees at the time — [TechCrunch, 5 Aug 2024](https://techcrunch.com/2024/08/05/uks-riverlane-scores-75m-to-correct-quantum-errors); [TNW](https://thenextweb.com/news/riverlane-quantum-computing-error-correction-chip-series-c-75-million-dollars).
  - Revenue is unverified. Aggregators disagree widely: GetLatka gives $20.2M; StartupHub about $3.1M; Dealroom $1-10M — [GetLatka](https://getlatka.com/companies/riverlane.com); [Dealroom](https://dealroom.co/companies/riverlane/).
  - Its latest group accounts (year to 31 Dec 2024) were filed 3 Sep 2025 — [Endole](https://open.endole.co.uk/insight/company/10260255-riverlane-ltd). The revenue line was not retrieved.
- **Quantum Machines (Israel, control systems).** $170M Series C on 25 Feb 2025 led by PSG; $280M raised in total; claims its customers include more than 50% of companies building quantum computers. Revenue not published, estimated in the tens of millions (unconfirmed) — [TechCrunch, 25 Feb 2025](https://techcrunch.com/2025/02/25/quantum-machines-raises-170m-says-its-working-with-more-than-half-of-all-quantum-computing-companies); [Fortune](https://fortune.com/2025/02/25/quantum-machines-computing-startup-170-million-series-c-funding/).

**Platforms and aggregators**
- **Strangeworks (US).** Acquired Quantagonia (Germany; solver orchestration and LLM-based optimisation formulation) on 20 Aug 2025; price not disclosed. The combined company is framed around "applied AI, optimization, and quantum computing", with AI listed first. No revenue or headcount disclosed — [The Quantum Insider, 20 Aug 2025](https://thequantuminsider.com/2025/08/20/strangeworks-acquires-quantagonia-to-create-global-leader-in-applied-ai-optimization-and-quantum-computing/).
- **qBraid (US).**
  - About 20,000 users from more than 400 universities and 100 companies; qBraid-OS used by four (unnamed) quantum hardware companies — [MIT News, Nov 2025](https://news.mit.edu/index%2Ephp/2025/startup-provides-nontechnical-gateway-coding-quantum-computers-1104).
  - Its 2025 funding was a **$300K NSF POSE Phase I grant** (Sep 2025) — [qBraid blog](https://qbraid.com/blog-posts/qbraid-awarded-nsf-grant-to-advance-open-source-quantum-software-ecosystem). CB Insights lists $350K raised in total — [CB Insights](https://www.cbinsights.com/company/qbraid/financials).
  - It monetises through services: "qBraid Pilots" (custom algorithm development) has been sold on AWS Marketplace by private offer since February 2026 — [qBraid](https://www.qbraid.com/blog-posts/qbraid-pilots-aws-marketplace).

**Large players with software lines (hardware-led)**
- **Quantinuum.** IPO on Nasdaq (QNT) in June 2026, raising $1.68-1.7B — [SiliconANGLE, 4 Jun 2026](https://siliconangle.com/2026/06/04/quantum-computer-maker-quantinuum-closes-flat-1-68b-ipo/).
  - FY2025 revenue was $30.9M (+35%), with **RIKEN accounting for 60%** (search-result summary of IPO coverage) — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/quantinuum-ipo-targets-12-7b-162055146.html).
  - Q2 2026 revenue was $8M; GAAP net loss $597M; FY2026 guidance $28-32M. No revenue split by hardware, software and services — [The Quantum Insider, 12 Aug 2026](https://thequantuminsider.com/?p=2391477).
  - The Nexus platform is used by 180 organisations. Guppy (language) and InQuanto (chemistry) are software products, and the IPO filing presents software as a future high-margin line — [The Quantum Insider](https://thequantuminsider.com/?p=2391477).
- **Xanadu (PennyLane).** SPAC listing (XNDU) in late March 2026, raising about $302M against $500M targeted — [The Quantum Insider, 27 Mar 2026](https://thequantuminsider.com/2026/03/27/xanadu-becomes-first-pure-play-photonic-quantum-computing-company-to-go-public/); [The Logic](https://thelogic.co/news/xanadu-public-listing-nasdaq-tsx-quantum/).
  - Q1 2026 revenue was $2.8M, "primarily driven by revenue recognized from DARPA QBI Stage B participation" — [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/xanadu-revenue-climbs-4x-quantum-152853198.html).
  - The CEO said: "revenue is not the main factor to judge us on" — [The Logic](https://thelogic.co/news/xanadu-public-listing-nasdaq-tsx-quantum/).
  - PennyLane has 35,000+ active users and 200,000 monthly downloads, per a third-party write-up. Monetisation of PennyLane is described as still ahead — [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/xanadu-revenue-climbs-4x-quantum-152853198.html).
- **IBM Qiskit Functions.** The catalog holds "nearly a dozen" functions from Kipu, Qedma, Q-CTRL, Qunova and ColibriTD — [IBM, 11 Feb 2026](https://www.ibm.com/quantum/blog/functions-2026). See question 3.

**"Quantum" companies whose revenue is mostly AI**
- **Multiverse Computing (Spain).**
  - €189M (about $215M) Series B in June 2025. Crunchbase reported $170M of equity and **$45M of grants and partnerships** — [TechCrunch, 12 Jun 2025](https://techcrunch.com/2025/06/12/multiverse-computing-raises-215m-for-tech-that-could-radically-slim-ai-costs); [Crunchbase News](https://news.crunchbase.com/venture/quantum-multiverse-computing-startup-raises-funding).
  - $570M Series C announced in July 2026 — [Quantonation, 27 Jul 2026](https://www.quantonation.com/2026/07/27/multiverse-computing-announces-series-c-fundraising-targeting-up-to-570m-e500m-to-power-efficient-ai-from-edge-to-cloud/).
  - Sacra (estimates, not audited): FY2024 revenue €2.8M; **FY2025 €11.1M against a €30M management forecast**; net loss about €24M; about 100 customers; more than 160 staff; ARR about €100M in January 2026. Growth came from CompactifAI (LLM compression) from H2 2025 — [Sacra](https://sacra.com/c/multiverse-computing/).
- **SandboxAQ (US).** Series E brought the round to $450M in April 2025, at a $5.6-5.75B valuation; $95M secondary in July 2025 — [The Quantum Insider, 15 Jul 2025](https://thequantuminsider.com/2025/07/15/sandboxaq-raises-95-million-to-advance-ai-models-that-solve-real-world-problems/); [SecurityWeek](https://www.securityweek.com/sandboxaq-raises-300-million-at-5-3-billion-valuation/).
  - Revenue estimates conflict ($17.8M to $128M) and none is audited — [GetLatka](https://getlatka.com/companies/sandboxaq); [Multiples.vc](https://multiples.vc/private-comps/sandboxaq).
- **Sector-wide figure.** McKinsey's Quantum Technology Monitor 2026 says quantum computing companies generated "more than $1 billion" of revenue in 2025, possibly $4.4B by 2028. Quantum start-up investment reached $12.6B in 2025, 6.3 times 2024. No hardware/software/services split was retrieved — [McKinsey QTM 2026](https://www.mckinsey.com/capabilities/quantumblack/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point) (snippet; full page returned 503).

### Inferences
- Revenue relative to capital raised is extremely low across the pure-software layer:
  - Classiq earns about 4% of its capital raised in annual revenue.
  - Horizon Quantum earns 0%.
  - Xanadu's revenue is mostly DARPA money.
  - Quantinuum's revenue is 60% one national lab.
- Scale is reached by raising capital and selling to hardware vendors, governments and large corporate R&D budgets — channels a zero-capital founder cannot use.
- Commercial revenue that recurs and is not a pilot is concentrated where the customer is a quantum hardware builder (control, error correction, error suppression) or where the product is not quantum at all (Multiverse's LLM compression, Q-CTRL's navigation, QC Ware's GPU chemistry).
- Even the best-funded software firms appear to depend on IBM's ecosystem (Qiskit Functions) or on hardware OEMs for distribution.

### Gaps
- Audited revenue for Classiq, Phasecraft, Algorithmiq, Riverlane (the Companies House PDF was not retrieved), Q-CTRL, Strangeworks, Kipu, BlueQubit and Haiqu.
- No 2024-2026 data found (search budget exhausted) for:
  - Kipu Quantum after its 2023 seed;
  - BosonQ Psi, Aqarios, Quantum Brilliance software, planqc, Qubit Pharmaceuticals;
  - Pasqal/Qadence funding or revenue;
  - Nvidia CUDA-Q ecosystem economics.
- Haiqu: Dealroom lists a $5M Series A in May 2025, which conflicts with the 2026 seed framing; unresolved.

---

## 2. What happened to quantum software companies that failed, shrank, were sold cheaply or pivoted to AI or "quantum-inspired" (2023-2026)? What lessons do founders and investors draw?

### Takeaway
The main failure (Zapata) was caused by a mistimed pivot to AI and a SPAC that brought in no equity. The main exits (Agnostiq/Covalent to DataRobot; Quantagonia to Strangeworks) were sales into AI or optimisation businesses at undisclosed prices. Survivors either moved closer to hardware vendors or drew most of their revenue from AI. The lesson repeated in the coverage: application-layer quantum software has been "ahead of its time" for close to a decade, and funding structures (SPACs, debt tied to the share price) kill companies before the market arrives.

### Cited Findings

**Zapata**
- Zapata AI ceased operations on 9 Oct 2024 after failing to meet the terms of its financial obligations (SEC 8-K) — [The Quantum Insider, 12 Oct 2024](https://thequantuminsider.com/2024/10/12/zapata-computing-holdings-inc-ceases-operations/).
- The trigger was a March 2024 Forward Purchase Agreement with Sandia Investment Management. It let Sandia accelerate a $2.5M payment if the stock traded below $1 for 20 of 30 days, which happened in fall 2024 — [The Quantum Insider, 3 Sep 2025](https://thequantuminsider.com/2025/09/03/viva-zapata-zapata-quantum-reemerges-after-bankruptcy-filing-with-restructuring-and-new-financing/).
- CEO Sumit Kapur (March 2026) said:
  - the company "mispivoted strategically in order to access a SPAC that didn't work";
  - the SPAC was expected to bring $100M of equity but "brought in effectively zero of equity capital", plus "$20-plus millions of liability";
  - Zapata was "a little bit ahead of our time" during a "quantum winter"
  — [The Next Platform, 12 Mar 2026](https://www.nextplatform.com/compute/2026/03/12/four-months-into-its-comeback-zapata-stakes-its-claim-in-quantum-software/5209179).
- The comeback:
  - $3M bridge in senior secured convertible notes (10% interest, conversion at $0.04/share), more than $10M of debt converted to equity, most employees previously terminated; customers cited are BP, BASF and BBVA — [The Quantum Insider, Sep 2025](https://thequantuminsider.com/2025/09/03/viva-zapata-zapata-quantum-reemerges-after-bankruptcy-filing-with-restructuring-and-new-financing/);
  - the restructuring addressed more than $18M of debt, and the IP was kept (60+ patents) — [The Next Platform](https://www.nextplatform.com/compute/2026/03/12/four-months-into-its-comeback-zapata-stakes-its-claim-in-quantum-software/5209179);
  - $15M financing in April 2026 led by Triatomic — [TNW](https://thenextweb.com/news/zapata-quantum-15m-financing).
- Zapata Quantum's VP of strategy says its QIR standardisation work was too early: "people weren't ready to adopt this sort of standardization". Google's Ryan Babbush calls application work an underinvested "classic collective action problem" — [The Next Platform](https://www.nextplatform.com/compute/2026/03/12/four-months-into-its-comeback-zapata-stakes-its-claim-in-quantum-software/5209179).

**Exits into AI and optimisation businesses**
- **Agnostiq/Covalent** was acquired by DataRobot on 10 Feb 2025 (price undisclosed) to support "agentic AI". The announcement does not mention quantum. Covalent had about 140,000 downloads, and Agnostiq had "a few dozen" employees — [The Quantum Insider, 10 Feb 2025](https://thequantuminsider.com/2025/02/10/datarobots-acquisition-of-agnostiq-signals-a-shift-from-quantum-to-ai-orchestration/); [TechTarget](https://techtarget.com/searchenterpriseai/news/366619101/DataRobot-acquires-open-source-and-AI-startup-Agnostiq).
  - The Quantum Insider's reading: quantum start-ups pivot to classical AI or HPC "to generate near-term revenue or because quantum commercialization is slower than expected" — [The Quantum Insider](https://thequantuminsider.com/2025/02/10/datarobots-acquisition-of-agnostiq-signals-a-shift-from-quantum-to-ai-orchestration/).
- **Quantagonia** was absorbed by Strangeworks (August 2025, undisclosed price), and the combined company now leads with AI. Deloitte describes it as an exit for Tensor Ventures — [Deloitte M&A note](https://www.deloitte.com/cz-sk/en/mnaport/articles/clanky-transakce/2025-q3/tensor-ventures-uspesne-vystupuje-z-kvantoveho-start-upu-quantagonia.html); [The Quantum Insider](https://thequantuminsider.com/2025/08/20/strangeworks-acquires-quantagonia-to-create-global-leader-in-applied-ai-optimization-and-quantum-computing/).

**Pivots and stagnation**
- **Multiverse** went from quantum-inspired finance software (Singularity) to LLM compression (CompactifAI). That AI line drives its ARR estimate and its $570M Series C, which was pitched as "efficient AI from edge to cloud" — [Sacra](https://sacra.com/c/multiverse-computing/); [Quantonation](https://www.quantonation.com/2026/07/27/multiverse-computing-announces-series-c-fundraising-targeting-up-to-570m-e500m-to-power-efficient-ai-from-edge-to-cloud/).
- **QC Ware** moved from renting access to other firms' quantum computers to GPU-accelerated quantum chemistry (Promethium) — [yespress profile](https://yespress.io/qc-ware-corp); [HPCwire 2023](https://www.hpcwire.com/2023/04/17/qc-ware-launches-promethium-a-quantum-chemistry-saas-targets-hybrid-world-near-term/).
- **1QBit**, a 2012 "first quantum software company", is classified "Grant | Alive" with a $2.49M grant-type raise in 2024 — [CB Insights](https://www.cbinsights.com/company/1qbit-information-technologies).
- **Nordic Quantum Computing Group** (Norway; hardware) shut down in December 2024, blaming policy, taxes and lack of national support — [The Quantum Insider, 10 Dec 2024](https://thequantuminsider.com/2024/12/10/nordic-quantum-computing-group-shuts-down-citing-government-policies-taxes-lack-of-support/).

**Missed forecasts and SPAC outcomes**
- Multiverse's management had forecast €30M of FY2025 revenue; Sacra estimates the actual at €11.1M — [Sacra](https://sacra.com/c/multiverse-computing/).
- Xanadu's SPAC raised $302M against $500M targeted, after most SPAC holders redeemed — [The Logic](https://thelogic.co/news/xanadu-public-listing-nasdaq-tsx-quantum/).

### Inferences
- A cheap way to fail in this sector: build a horizontal tool (orchestration, an intermediate representation, a workflow engine) before there is a quantum workload large enough to pay for it. Covalent found its buyers in AI, not quantum.
- "Quantum-inspired AI" did not save Zapata. Multiverse's AI line did work, but because it is a good AI product, not because of anything quantum.
- Lesson for a solo founder: if a quantum-adjacent tool gets traction, it will probably be with classical or AI users. The quantum label works as a marketing door-opener, not a revenue base.
- In 2026 the money flows to hardware IPOs and SPACs (Quantinuum, Xanadu, Horizon, Terra). Pure software is repriced as a feature of hardware platforms.

### Gaps
- No systematic list was found of smaller quantum software start-ups that closed quietly in 2025-2026; searches surfaced only Zapata. This probably reflects under-reporting rather than an absence of failures.
- Acquisition prices for Agnostiq and Quantagonia are undisclosed.
- No investor post-mortem with quantified lessons (e.g. VC returns on quantum software) was found.

---

## 3. What do the quantum cloud marketplaces look like for third-party sellers (IBM Qiskit Functions, AWS Braket and AWS Marketplace, Azure Quantum, Nvidia, Strangeworks, qBraid)? Can a tiny vendor list a function or app and get paid?

### Takeaway
None of these marketplaces offers an open, self-serve path for a tiny vendor to list a quantum function and collect usage revenue. IBM's catalog is curated, limited to partners and sold only to Premium and Flex plan customers (IBM even gave free one-year licences in 2026). AWS Marketplace works mainly as a procurement wrapper for services sold by private offer. Azure Quantum hands out credits but has been shrinking its provider list. No marketplace publishes seller revenue or usage figures.

### Cited Findings

**IBM Qiskit Functions Catalog**
- Launched 16 Sep 2024 — [IBM announcement](https://docs.quantum.ibm.com/announcements/product-updates/2024-09-16-introducing-qiskit-functions-catalog).
- By 11 Feb 2026 it held "nearly a dozen functions". Providers: Kipu (Iskay optimizer), Qedma (QESEM), Q-CTRL (Performance Management, Optimization Solver, quantum phase estimation), Qunova (HI-VQE), ColibriTD (QUICK-PDE), plus a hybrid ensemble classifier — [IBM blog, 11 Feb 2026](https://www.ibm.com/quantum/blog/functions-2026). Algorithmiq's tensor-network error mitigation was also listed — [IBM docs](https://docs.quantum.ibm.com/guides/functions).
- Access is limited to Premium and Flex plan users, who can request free trials; "eligible Premium Plan organizations can request a free one-year license until March 31" (2026) — [IBM blog](https://www.ibm.com/quantum/blog/functions-2026).
- The post says nothing about partner compensation, revenue sharing, pricing, or how new providers can join — [IBM blog](https://www.ibm.com/quantum/blog/functions-2026). The documentation says Premium users "procure a license from one of the partners", so the licence is sold partner-to-customer, with no IBM-run billing — [IBM docs](https://eu-de.quantum.cloud.ibm.com/docs/guides/functions).
- The addressable buyers are IBM Premium customers. Premium costs $48/minute with a 5,200-minute annual minimum (about $250K a year); Flex costs $72/minute with a 400-minute annual minimum — [IBM pricing](https://www.ibm.com/quantum/pricing).

**AWS Braket and AWS Marketplace**
- qBraid Pilots (custom algorithm development) is listed by private offer, with price on request. qBraid says the main value is letting customers buy through existing cloud budgets and approved vendors, avoiding new vendor setup — [qBraid, Feb 2026](https://www.qbraid.com/blog-posts/qbraid-pilots-aws-marketplace).
- Other quantum listings include Classiq (integrated with Braket for multi-hardware benchmarking), a Quantuloop simulator suite and Rigetti consulting. D-Wave access moved entirely to AWS Marketplace — [AWS Marketplace listing](https://aws.amazon.com/marketplace/pp/prodview-bodioxhf2ivko); [AWS Quantum blog](https://aws.amazon.com/blogs/quantum-computing/using-d-wave-leap-from-the-aws-marketplace-with-amazon-braket-notebooks-and-braket-sdk) (search summaries).
- AWS describes the Marketplace as a "curated digital catalog of third-party software and professional services" — [HPCwire/AWS](https://hpcwire.com/solution_content/aws/readily-accessible-quantum-computing-solutions-and-professional-services-through-aws-marketplace).

**Azure Quantum**
- First-time users get $500 of credits per participating hardware provider, valid 6 months; the Azure Quantum Credits programme offers up to $10,000 more — [Microsoft Learn pricing](https://learn.microsoft.com/azure/quantum/pricing); [credits FAQ](https://learn.microsoft.com/azure/quantum/credits-faq).
- Quantinuum retired H1-1 on 15 Oct 2025, and the H1 pay-as-you-go plan was removed from Azure Quantum — [Quantinuum product change notice](https://docs.quantinuum.com/systems/pcns/H1%20Product%20Change%20Notification%202025_07_15%20System%20Model%20H1%20Retirement.pdf).
- Toshiba's SQBM+ was added as a quantum-inspired optimisation provider in 2022 — [Azure blog, Jun 2022](https://azure.microsoft.com/en-us/blog/quantum/2022/06/27/toshiba-launches-new-sqbm-quantum-inspired-optimization-provider-on-azure-quantum/).

**Usage share of the platforms (Unitary survey 2026)**
- Active use: IBM Quantum Platform 54.9%, Classiq 22.8%, Amazon Braket 17.9%, qBraid 17.0%, Azure Quantum 9.6% — [Quantum Computing Report, 17 Nov 2026](https://quantumcomputingreport.com/unitary-foundation-releases-2026-quantum-open-source-survey-covering-sdk-adoption-hybrid-hpc-workflows-and-ai-tooling/amp/).

**Aggregators (Strangeworks, qBraid)**
- Both are themselves small companies. qBraid's 2025 funding was a $300K NSF grant — [qBraid](https://qbraid.com/blog-posts/qbraid-awarded-nsf-grant-to-advance-open-source-quantum-software-ecosystem).
- qBraid and Quantum Rings partnered to "expand free access" to simulators and hardware — [The Quantum Insider](https://thequantuminsider.com/?p=2389996). The aggregator business is drifting toward free access, which signals little room for paid third-party apps.

### Inferences
- A tiny vendor can get on AWS Marketplace (for example a services listing sold by private offer) mostly to make procurement easier. That only matters once the vendor has a buyer in hand.
- IBM's catalog is effectively a VC-backed partner club, and IBM has been giving licences away to drive adoption. There is no evidence of meaningful pay-per-use revenue for function authors.
- The "app store for quantum" model is a false good idea for a solo founder in 2026: there are no published usage numbers, buyers are gated behind expensive plans, and the platforms themselves give access for free.

### Gaps
- No published revenue or usage numbers for any third-party seller on Qiskit Functions, AWS Marketplace (quantum category), Azure Quantum or Strangeworks.
- The criteria for joining Qiskit Functions as a provider were not found.
- AWS Marketplace seller fees for quantum listings were not checked.
- Whether Nvidia (CUDA-Q) runs any third-party sales channel was not researched (search budget exhausted).

---

## 4. Which technical pain points are documented as unsolved and commercially relevant in 2025-2026? For each, is there evidence that someone pays for a solution?

### Takeaway
Pain points are well documented by developer surveys and academic work: documentation, price, resource estimation, hybrid HPC integration, verification of AI-generated code, and SDK churn. But evidence of **payment** exists for only a few problems, and in each case the buyers are hardware makers, IBM's Premium customers or governments, and the problems need PhD-level physics: error suppression and mitigation, QEC decoding and control, and benchmarking (government-funded). For benchmarking, decoding and calibration, Nvidia and the open-source community are rapidly releasing free tools. For the problems a non-PhD could tackle (migration, documentation, testing, cost comparison), no paying customer was found.

### Cited Findings

**Error suppression and mitigation — paid, PhD-heavy**
- Sold as Qiskit Functions by Q-CTRL, Qedma and Algorithmiq (see question 3). Qedma raised $26M on it; QESEM is integrated in Quantinuum Nexus — [TechCrunch](https://techcrunch.com/2025/07/03/israeli-quantum-startup-qedma-just-raised-26-million-with-ibm-joining-in).
- Reported scale of use: Mitsubishi Chemical used Q-CTRL up to 52 qubits / 5,000+ two-qubit gates, Qubit Pharmaceuticals up to 123 qubits — [IBM, Feb 2026](https://www.ibm.com/quantum/blog/functions-2026).

**QEC decoders and tooling — paid by hardware builders, now commoditising**
- Riverlane raised $75M in 2024 — [TechCrunch](https://techcrunch.com/2024/08/05/uks-riverlane-scores-75m-to-correct-quantum-errors).
- Unitary survey 2026: 35.2% of respondents use QEC tools. Active-user platforms: Qiskit 51.7%, PennyLane 30.0%, Stim 29.8%, CUDA-Q QEC 20.8%, PyMatching 15.8%, Riverlane Deltakit 13.5%. Among non-users, **22.8% cite cost** and 19.0% missing implementations — [Quantum Computing Report, Nov 2026](https://quantumcomputingreport.com/unitary-foundation-releases-2026-quantum-open-source-survey-covering-sdk-adoption-hybrid-hpc-workflows-and-ai-tooling/amp/).
- Nvidia Ising (14 Apr 2026) is a family of open models for calibration and decoding:
  - decoding pre-decoders combined with PyMatching are claimed 2.25-2.5x faster and 1.11-1.53x more accurate (d=13, p=0.003);
  - weights are on Hugging Face under the NVIDIA Open Model License, and the training framework is Apache 2.0
  — [NVIDIA developer blog](https://developer.nvidia.com/blog/nvidia-ising-introduces-ai-powered-workflows-to-build-fault-tolerant-quantum-systems/).

**Calibration — open agentic tools from Nvidia, hardware access needed**
- Ising Calibration 1 (35B vision-language model) ships with a Quantum Calibration Agent Blueprint. Nvidia claims it beats Gemini 3.1 Pro, Claude Opus 4.6 and GPT-5.4 on its own QCalEval benchmark — [NVIDIA blog](https://developer.nvidia.com/blog/nvidia-ising-introduces-ai-powered-workflows-to-build-fault-tolerant-quantum-systems/).
- IQM and Nvidia demonstrated agentic calibration of a 20-qubit chip (15 Apr 2026). Atom Computing, IonQ, IQM and the Berkeley Lab Advanced Quantum Testbed use Ising Calibration — [Quantum Computing Report](https://quantumcomputingreport.com/iqm-and-nvidia-automate-20-qubit-chip-calibration-via-nvidia-ising-vision-language-models-and-qcaleval-benchmark/).
- A preprint, "Vibe Calibration" (arXiv 2606.22376), reports autonomous bring-up of a 112-qubit processor by a skill-orchestrating language agent — [arXiv](https://arxiv.org/pdf/2606.22376). Only the abstract and title were seen.

**Benchmarking and independent verification of vendor claims — demand exists, payers are governments and vendors**
- Unitary Foundation's open-source Metriq platform publishes cross-vendor results from 10+ quantum computers (arXiv 2603.08680, March 2026). Its single "Metriq Score" is criticised as an oversimplification — [arXiv](https://arxiv.org/abs/2603.08680); [Quantum Zeitgeist](https://quantumzeitgeist.com/unified-platform-delivers-reliable-quantum-computer-performance-assessments/).
- DARPA's QBI pays hardware participants: Xanadu's Q1 2026 revenue came "primarily" from QBI Stage B — [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/xanadu-revenue-climbs-4x-quantum-152853198.html). Zapata cites its own role in DARPA's benchmarking programme (Bench-Q) — [The Quantum Insider](https://thequantuminsider.com/2025/09/03/viva-zapata-zapata-quantum-reemerges-after-bankruptcy-filing-with-restructuring-and-new-financing/).
- BCG and QuEra sell a joint "proof of value" engagement that starts with structured discovery to align "use cases, benchmarks, and success metrics" (Sep 2025) — [BCG](https://www.bcg.com/news-30september2025-accelerate-quantum-value-enterprises-government-innovators).
- qBraid Pilots includes "performance benchmarking against classical baselines" as a paid deliverable — [qBraid](https://www.qbraid.com/blog-posts/qbraid-pilots-aws-marketplace).

**Resource estimation — strong stated need, no payment evidence**
- Unitary survey 2025, open answers (n=102): "resource estimation and planning" 33 mentions; algorithm/circuit optimisation 19; budgeting, pricing and cost estimation 10 — [Unitary Foundation survey 2025](https://unitaryfoundation.github.io/survey-2025).

**Hybrid HPC-quantum orchestration — common use, no standalone business**
- Unitary 2026: 52.9% ran hybrid workflows. Bottlenecks: limited QPU access 54.4%, compute cost 41.8%, constrained GPU/HPC 37.0%, integration friction 25.4%. 36.8% use HPC tools (CUDA 24.1%, Slurm 17.0%) — [Quantum Computing Report, Nov 2026](https://quantumcomputingreport.com/unitary-foundation-releases-2026-quantum-open-source-survey-covering-sdk-adoption-hybrid-hpc-workflows-and-ai-tooling/amp/).
- The leading open-source orchestrator, Covalent, exited to an AI company (see question 2).

**Cost comparison across hardware — weak paid evidence**
- Price was cited by 47.5% of respondents as a barrier to using desired tools (2024 survey) — [Unitary survey 2025 page, 2024 baseline](https://unitaryfoundation.github.io/survey-2025).
- Classiq markets Braket integration for multi-provider benchmarking — [AWS Marketplace listing](https://aws.amazon.com/marketplace/pp/prodview-bodioxhf2ivko).
- Public price points that make comparison possible: IBM PAYG $96/min, Flex $72/min, Premium $48/min, Open Plan up to 10 free minutes per month — [IBM pricing](https://www.ibm.com/quantum/pricing).

**Code migration between SDK versions (Qiskit 1.x to 2.x) — real churn, no payer found**
- Qiskit 2.0 was "the first release since Qiskit SDK v1.0 to contain breaking changes". It removed qiskit.pulse, qobj, BackendV1 and BackendProperties, and changed generate_preset_pass_manager. Qiskit 1.4.x got 6 months of bug fixes and 1 year of security fixes — [IBM Qiskit 2.0 migration guide](https://quantum.cloud.ibm.com/docs/guides/qiskit-2.0); [release notes](https://quantum.cloud.ibm.com/docs/en/api/qiskit/release-notes/2.0).
- IBM itself supplies migration guides, a Code Assistant and MCP servers (see question 5).

**Testing, debugging and verification — active research, no paid market found**
- QTestBench (arXiv 2610.13811, Oct 2026) shows that LLM-written tests can pass solutions whose circuits are wrong — [arXiv](https://arxiv.org/pdf/2610.13811).
- QBugLM (arXiv 2606.07314) benchmarks LLM debugging of quantum programs — [arXiv](https://arxiv.org/html/2606.07314v1).
- Unitary 2026: 42.9% always and 38.7% mostly verify AI outputs. Methods: manual review 78.3%, automated tests 54.2%, formal verification 17.5% — [Quantum Computing Report](https://quantumcomputingreport.com/unitary-foundation-releases-2026-quantum-open-source-survey-covering-sdk-adoption-hybrid-hpc-workflows-and-ai-tooling/amp/).
- Zapata Quantum runs a formal-verification project with the University of Maryland — [The Next Platform](https://www.nextplatform.com/compute/2026/03/12/four-months-into-its-comeback-zapata-stakes-its-claim-in-quantum-software/5209179).

**Documentation — the top barrier, unpaid**
- "Poorly documented" was the most cited barrier (50.8%) in the 2024 survey — [Unitary survey 2025](https://unitaryfoundation.github.io/survey-2025).
- In 2025, documentation and readable source code still outranked chatbots as sources of answers — [The Quantum Insider, 5 Nov 2025](https://thequantuminsider.com/2025/11/05/the-young-and-the-relentless-poll-shows-more-quantum-developers-are-young-independent-and-unpaid/).

### Inferences
- Where money changes hands (error mitigation, decoding, control, calibration, benchmarking for DARPA), the buyers are a few dozen hardware companies, national labs and DARPA. Selling to them requires deep physics expertise, hardware access and credibility. Nvidia and Google-aligned open tools (Stim, PyMatching, Ising) are fast lowering the price of the commodity parts.
- Where a solo non-PhD founder could build with AI agents (Qiskit migration scripts, docs, test harnesses, cost calculators, resource-estimation front-ends), the users are mostly students and researchers. They do not have budgets (see question 7), and IBM or other vendors give the equivalent away to drive platform adoption.
- The most promising "unsolved and somewhat paid" seam is independent classical-baseline benchmarking and verification of quantum PoC claims. Consultancies and qBraid already bill for it as part of PoCs. It is a service, not a product, and it needs strong classical optimisation or simulation skills more than quantum hardware.

### Gaps
- No evidence was found on paid demand for reproducing quantum papers.
- Free resource estimators (Azure Quantum Resource Estimator, Google Qualtran) were not verified this session, so it is unknown whether any commercial resource-estimation product exists.
- No figures were found on DARPA QBI contract sizes per performer.

---

## 5. What is the state of "AI for quantum" (LLM assistants and agents, calibration agents, AI-designed circuits)? Where do general-purpose models still fail, and is there a paid market for specialised tooling, datasets, evaluation suites or MCP servers?

### Takeaway
AI coding assistants are already the default tool of quantum developers. In the 2026 Unitary survey, 77.8% use AI tools for quantum work, and Claude Code is used by 71.6% of AI-assistant users. Frontier general-purpose models now match or beat specialised quantum code models. Measured failures are semantic (wrong physics or logic), not syntax. Benchmarks are themselves unreliable or saturating. Incumbents give the specialised tooling away: IBM's MCP servers and Nvidia's calibration and decoding models are free and open; IBM keeps its Code Assistant for Premium customers. No evidence was found of a paid market for quantum-specific LLM tooling, datasets or MCP servers.

### Cited Findings

**Usage (Unitary survey 2026)**
- AI tools among active users: Claude Code 71.6%, OpenAI Codex 41.8%, Google Gemini 39.4%, Microsoft Copilot 16.6%, Cursor 11.3%.
- 77.8% use AI tools in quantum workflows, mainly for debugging/optimisation (77.0%) and learning SDKs (76.4%).
- Productivity rated 3.1/4, but confidence in code accuracy only 2.5/4 and in conceptual explanations 2.6/4.
- Source for all three points: [Quantum Computing Report, 17 Nov 2026](https://quantumcomputingreport.com/unitary-foundation-releases-2026-quantum-open-source-survey-covering-sdk-adoption-hybrid-hpc-workflows-and-ai-tooling/amp/).

**Benchmarks and where models fail**
- Qiskit HumanEval (June 2024) has more than 100 tasks. The best base model in the original paper, DeepSeek-Coder-33B, scored 39.6% — [arXiv 2406.14712](https://arxiv.org/html/2406.14712v1).
- A 2025 IBM post-training paper reports gpt-oss-20b at 27.15% on Qiskit HumanEval and 15.89% on the hard variant — [arXiv 2508.20907](https://arxiv.org/pdf/2508.20907).
- QuanBench+ (v2, 22 Apr 2026; 12 models), one-shot best Pass@1:
  - Qiskit 59.5% (Gemini-3-Pro), Cirq 54.8%, PennyLane 42.9% (GPT-5.1);
  - with up to five feedback-repair attempts: 83.3%, 76.2% and 66.7%.
  - First-attempt failure modes: wrong answers 46.7%, logic errors 25.0%, missing methods/gates 11.8%, shape mismatches 8.0%, syntax 4.7%.
  - Authors' conclusion: "reliable multi-framework correctness is still out of reach."
  - Source: [arXiv 2604.08570](https://arxiv.org/html/2604.08570).
- An October 2026 audit (arXiv 2610.28678) found:
  - evaluator design alone swings scores, e.g. from 0% to 94.1% on one topic with unchanged outputs;
  - 17 QuanBench tasks fail because of imports owned by the benchmark;
  - Qiskit HumanEval Standard is "near saturation (98.7% pass@1)" while Hard sits at 63.8%;
  - "leaderboard scores alone do not adequately characterize progress"
  — [arXiv 2610.28678](https://arxiv.org/abs/2610.28678).
- A March 2026 re-evaluation reportedly finds that modern general-purpose LLMs with retrieval or execution-feedback agents "consistently outperform" the fine-tuned Granite-based Qiskit baseline — [arXiv 2603.22184](https://arxiv.org/pdf/2603.22184). This comes from a search-result summary; the PDF text could not be parsed.
- Other benchmarks and agents:
  - QCircuitBench, a large-scale algorithm-design benchmark — [arXiv 2410.07961](https://arxiv.org/html/2410.07961v3);
  - QuanBench, 44 tasks — [arXiv 2510.16779](https://arxiv.org/html/2510.16779v1);
  - QAgent, a multi-agent OpenQASM system — [arXiv 2508.20134](https://arxiv.org/html/2508.20134v1).

**Tooling incumbents give away**
- IBM publishes a family of open MCP servers: core Qiskit, IBM Runtime, Code Assistant, Docs, Transpiler, plus a community Gym server; the PyPI bundle `qiskit-mcp-servers` is at 0.7.0 — [IBM docs](https://quantum.cloud.ibm.com/docs/guides/qiskit-mcp-servers); [PyPI](https://pypi.org/project/qiskit-mcp-servers/0.7.0/).
- The **Code Assistant MCP server only works for IBM Quantum Premium Plan users** — [IBM docs](https://quantum.cloud.ibm.com/docs/guides/qiskit-mcp-servers).
- A third-party `mcp-qiskit` package already exists — [PyPI](https://pypi.org/project/mcp-qiskit/0.1.0/).
- Nvidia Ising calibration and decoding models are open-weight (April 2026); see question 4 — [NVIDIA blog](https://developer.nvidia.com/blog/nvidia-ising-introduces-ai-powered-workflows-to-build-fault-tolerant-quantum-systems/).
- Agent and AI features appear inside commercial platforms rather than as standalone products:
  - Zapata Quantum's "Quantum Pilot AI assistant" — [The Next Platform](https://www.nextplatform.com/compute/2026/03/12/four-months-into-its-comeback-zapata-stakes-its-claim-in-quantum-software/5209179);
  - Quantagonia/Strangeworks' LLM-based optimisation-formulation tools — [The Quantum Insider](https://thequantuminsider.com/2025/08/20/strangeworks-acquires-quantagonia-to-create-global-leader-in-applied-ai-optimization-and-quantum-computing/).
- Zapata's team says AI makes a previously DARPA-derived project scalable, something that "was impossible two years ago" — [The Next Platform](https://www.nextplatform.com/compute/2026/03/12/four-months-into-its-comeback-zapata-stakes-its-claim-in-quantum-software/5209179).

### Inferences
- An AI-agent-native solo founder has a real productivity edge for building quantum software. Everyone else has the same edge, though: Claude Code is already the majority tool among quantum developers who use AI.
- Wrapping general LLMs with quantum context (MCP servers, prompts, RAG over Qiskit docs) is a zero-moat activity that IBM does for free.
- A possible but unproven niche: verification and evaluation infrastructure. Failures are semantic, LLM-written tests can be wrong, benchmark harnesses are buggy, and developers say they always verify. Potential buyers are frontier labs (evaluation data), IBM/Nvidia (benchmarks) and grant bodies. No evidence was found that anyone pays a small vendor for a quantum evaluation suite or dataset. Today this is academic work funded by grants.
- AI-for-hardware (calibration, decoding) is being captured by Nvidia, and it needs lab access a zero-capital founder lacks.

### Gaps
- Google DeepMind's AlphaQubit decoder (Nature, 2024) and any AlphaEvolve-type quantum circuit work could not be verified (the Nature page redirected to a login; search budget exhausted).
- Classiq's and Quantinuum's AI assistants were not researched.
- No pricing was found for IBM Qiskit Code Assistant beyond Premium-plan gating.
- No data was found on sales of quantum datasets or evaluation suites to AI labs.

---

## 6. What is the state of "quantum-inspired" and classical-simulation businesses (tensor networks, annealing/Ising solvers, GPU optimisation, Multiverse's model compression)? Real revenue, customers and barriers to entry?

### Takeaway
The quantum-inspired businesses with real money either sit inside giants (Fujitsu's Digital Annealer, Toshiba's SQBM+, with no revenue disclosed) or have become AI companies (Multiverse, whose revenue jump comes from LLM compression). Simulation itself is commoditised: Qiskit Aer, CUDA-Q and GPU simulators are free, and 80% of developers run CPU simulators. Barriers to entry are technically low but commercially high: the true competitors are classical operations-research solvers (Gurobi-class) and the free vendor tools.

### Cited Findings
- **Multiverse.** FY2025 revenue about €11.1M, mostly from the Singularity optimisation platform; CompactifAI contributed only from H2 2025; about 100 customers in 10 industries; ARR about €100M by January 2026 (Sacra estimate) — [Sacra](https://sacra.com/c/multiverse-computing/).
  - Company claims: models compressed by up to 95%, running 4-12x faster with 50-80% lower inference cost — [The Quantum Insider, 12 Jun 2025](https://thequantuminsider.com/2025/06/12/multiverse-computing-raises-215-million-to-scale-technology-that-compresses-llms-by-up-to-95/).
- **Fujitsu Digital Annealer.** Presented as a commercial optimisation service. Toyota Systems uses it for production instructions at its Tsutsumi plant; Toyota applied it to mass-produced ECUs in parallel with conventional methods from May 2025. Quantum-inspired revenue is not broken out of Fujitsu's ¥3.6T group revenue — [Fujitsu PR, 14 Jan 2026](https://global.fujitsu/en-global/pr/news/2026/01/14-01); [Fujitsu DA explainer](https://www.fujitsu.com/global/imagesgig5/Digital_Annealer_Explainer_May2024_New.pdf).
- **Toshiba SQBM+.** Ising solver for up to 100,000 variables, offered on Azure Quantum with "Learn & Develop" and "Performance at scale" plans (2022). No 2025 revenue or customer data found — [Azure blog](https://azure.microsoft.com/en-us/blog/quantum/2022/06/27/toshiba-launches-new-sqbm-quantum-inspired-optimization-provider-on-azure-quantum/).
- **QC Ware Promethium.** GPU-accelerated (classical) quantum-chemistry SaaS, launched 2023 — [HPCwire](https://www.hpcwire.com/2023/04/17/qc-ware-launches-promethium-a-quantum-chemistry-saas-targets-hybrid-world-near-term/).
- **Quantagonia (now Strangeworks).** Its solver-orchestration engine runs several solvers in parallel. Its CEO is a co-founder of Gurobi GmbH, which shows how close quantum-inspired optimisation is to classical operations research — [The Quantum Insider](https://thequantuminsider.com/2025/08/20/strangeworks-acquires-quantagonia-to-create-global-leader-in-applied-ai-optimization-and-quantum-computing/).
- **Simulation usage.** Among hybrid-workflow users (2026), CPU simulators are used by 80.2% and GPU-accelerated simulators by 56.4% — [Quantum Computing Report, Nov 2026](https://quantumcomputingreport.com/unitary-foundation-releases-2026-quantum-open-source-survey-covering-sdk-adoption-hybrid-hpc-workflows-and-ai-tooling/amp/).
  - 2025: Qiskit Aer (free) used by 47.7%; NVIDIA CUDA Quantum by 16.2%, with 25.3% planning to use it — [Unitary survey 2025](https://unitaryfoundation.github.io/survey-2025).
- **Free simulator access.** qBraid and Quantum Rings partnered on free simulator and hardware access — [The Quantum Insider](https://thequantuminsider.com/?p=2389996). BlueQubit raised a $10M seed for GPU-based quantum software — [TechCrunch](https://techcrunch.com/2024/12/19/bluequbit-raises-10m-to-take-quantum-software-into-real-world-applications).

### Inferences
- For a solo founder, quantum-inspired optimisation is really a classical OR/AI consulting business with a quantum label. It can earn money, since manufacturers and logistics firms buy optimisation, but the quantum framing adds credibility risk ("quantum-washing") more than value. The buyer will compare it against Gurobi, CPLEX, OR-Tools and GPU heuristics.
- Tensor-network model compression proved commercial at Multiverse, but only with large-scale engineering, a European grant stack ($45M of grants and partnerships) and enterprise sales. That route is unavailable at zero capital, and Multiverse now competes with quantisation and distillation tooling from the large AI labs (inference, not checked).

### Gaps
- Toshiba and Fujitsu quantum-inspired revenues are not disclosed.
- No data was found on D-Wave's hybrid-solver revenue (likely covered by other researchers).
- No revenue data for BlueQubit, Quantum Rings or Terra Quantum's optimisation products.
- No independent verification of Multiverse's ARR.

---

## 7. What does quantum consulting and PoC work look like commercially (day rates, project sizes, buyers, sellers)? Are freelance quantum developers finding paid work? How large is the developer population, and what does it say it needs or would pay for?

### Takeaway
Enterprise PoC activity is real and growing — about 150 PoCs at 100 enterprises by end-2024 per BCG, and a third of companies studied by McKinsey spending over $10M in 2025. But it is captured by large consultancies (BCG, McKinsey, Deloitte, Accenture), the hardware and software vendors themselves (qBraid Pilots, BCG+QuEra, Rigetti consulting), or government centres. Prices are never published. The developer population is young, academic and price-sensitive. In 2025 nearly 40% of open-source contributors were unpaid; in 2026, 56% had two years or less of experience and fewer than half had quantum as their main paid job. Documentation, price and learning are their top needs. That is a weak base for selling paid developer tools, and there is no evidence of a healthy freelance market.

### Cited Findings

**Enterprise PoC market**
- BCG: by end-2024, 150 PoCs across 100 enterprises, a 50% increase on two years earlier (search-result summary of a BCG/DCD article; the primary page returned 403) — [DCD](https://www.datacenterdynamics.com/en/news/enterprise-quantum-spend-surpassed-combined-academic-and-govt-investments-in-2025-boston-consulting-group-reports/).
- A secondary write-up of McKinsey research says one-third of analysed companies allocated more than $10M to quantum in 2025, mostly on use-case development and integration — [Spinquanta](https://www.spinquanta.com/news-detail/quantum-consulting-services-how-enterprises-unlock-real-world-quantum-use-cases) (secondary source; treat with caution).
- HSBC has worked with the NQCC and Rigetti on fraud detection — [Spinquanta](https://www.spinquanta.com/news-detail/quantum-consulting-services-how-enterprises-unlock-real-world-quantum-use-cases).

**Sellers**
- BCG–QuEra joint offer (30 Sep 2025) — [BCG](https://www.bcg.com/news-30september2025-accelerate-quantum-value-enterprises-government-innovators).
- qBraid Pilots: scoping, algorithm design, benchmarking against classical baselines, roadmap; private-offer pricing (Feb 2026) — [qBraid](https://www.qbraid.com/blog-posts/qbraid-pilots-aws-marketplace).
- Rigetti sells Braket-optimisation consulting on AWS Marketplace (search summary) — [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-ix3tgin5orlx4).
- The Quantum Insider also sells strategy consulting — [TQI consulting](https://thequantuminsider.com/quantum-computing-consulting/strategy-consulting/).
- No published rate card: one provider states fees are set per engagement — [Spinquanta](https://www.spinquanta.com/news-detail/quantum-consulting-services-how-enterprises-unlock-real-world-quantum-use-cases).

**Freelance and wage signals (weak, indirect)**
- ZipRecruiter US average pay: "Qiskit" roles $26.34/h (30 May 2026); "quantum developer" $52.84/h (19 Jun 2026). These are employee wage estimates, not freelance rates — [ZipRecruiter Qiskit](https://www.ziprecruiter.com/Jobs/Qiskit/2); [ZipRecruiter Quantum Developer](https://www.ziprecruiter.com/Jobs/Quantum-Developer).
- Upwork's generic developer rate tiers: $20-40/h entry, $40-70/h intermediate, $70-150+/h expert — [Upwork](https://www.upwork.com/en-gb/hire/software-developers/cost/). Upwork's quantum job listings page returned 403, so actual quantum demand on Upwork was not observed.

**Developer population and needs — Unitary Foundation surveys**
- **2025 survey (fielded Sep-Oct 2025):**
  - 1,400+ respondents — [Unitary survey 2025](https://unitaryfoundation.github.io/survey-2025);
  - 56% work full-time in quantum development, **nearly 40% receive no compensation**, 53.6% are 30 or younger, 11% have no affiliation (up from 7%) — [The Quantum Insider, 5 Nov 2025](https://thequantuminsider.com/2025/11/05/the-young-and-the-relentless-poll-shows-more-quantum-developers-are-young-independent-and-unpaid/);
  - SDK use: Qiskit 69.1%, Qiskit Aer 47.7%, PennyLane 30.8%, Cirq 17.5%, CUDA Quantum 16.2% (25.3% planned);
  - cloud use: IBM 65.5%, Classiq 21.8%, Braket 16.4%, Azure 11.5% — [Unitary survey 2025](https://unitaryfoundation.github.io/survey-2025);
  - 2024 barriers to using desired tools: poorly documented 50.8%, **price 47.5%**, incompatible with stack 35.3%, tool does not exist 33.7% — [Unitary survey 2025](https://unitaryfoundation.github.io/survey-2025);
  - top open-ended requests: structured education, onboarding and mentorship; video learning overtook hackathons — [The Quantum Insider](https://thequantuminsider.com/2025/11/05/the-young-and-the-relentless-poll-shows-more-quantum-developers-are-young-independent-and-unpaid/).
- **2026 survey (published 17 Nov 2026; fielded 10 Sep-29 Oct 2026):**
  - more than 1,800 respondents: researchers 49.4%, software developers 34.2%;
  - **46.6% have quantum as their primary paid job; 56.2% have two years or less of professional quantum experience**;
  - top countries: US 17.7%, India 15.7%, Israel 15.5%, Canada 7.7%, UK 5.1%, Germany 5.0%;
  - Qiskit fell to 56.8% (from 69.1%), PennyLane rose to 34.3%, Classiq Library 21.4%;
  - Python used by 92.5%; 45.3% plan to learn Rust;
  - research priorities: algorithms 54.3%, QEC 44.4%, applications 42.6%
  — [Quantum Computing Report](https://quantumcomputingreport.com/unitary-foundation-releases-2026-quantum-open-source-survey-covering-sdk-adoption-hybrid-hpc-workflows-and-ai-tooling/amp/).

**Other population signals**
- qBraid has about 20,000 users — [MIT News](https://news.mit.edu/index%2Ephp/2025/startup-provides-nontechnical-gateway-coding-quantum-computers-1104).
- PennyLane has 35,000+ active users (third-party write-up) — [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/xanadu-revenue-climbs-4x-quantum-152853198.html).
- Quantinuum Nexus is used by 180 organisations — [The Quantum Insider](https://thequantuminsider.com/?p=2391477).
- Q-CTRL's education product Black Opal Pro costs $9.99/month billed annually or $19.99/month billed monthly — [Q-CTRL](https://www.q-ctrl.com/black-opal/pricing). This is evidence of a small paid B2C learning market with an incumbent.

### Inferences
- The developer population is probably in the tens of thousands of active coders: about 20K on qBraid and about 35K active PennyLane users, with heavy overlap. That is roughly the size of one mid-sized open-source framework community, and it is skewed toward students, academics and unpaid contributors in the US, India and Israel. Developer-tool SaaS needs a large paying base; this one is small, young and price-sensitive (price was a top-2 barrier).
- Consulting money is concentrated at the top (BCG/McKinsey-type firms, vendors, national centres). A solo founder without a PhD or brand would most plausibly reach it as a subcontractor or white-label technical implementer for a consultancy or vendor, or by selling classical-baseline "reality checks". There is no evidence such subcontracting work is plentiful.
- The fastest-growing segment is newcomers (56.2% with two years or less), and learning or mentorship is the most requested need. This suggests that education and on-ramping for classical developers is the most demand-backed niche. It is competitive (IBM, PennyLane, Q-CTRL Black Opal, Classiq's university curricula, all free or cheap) and its willingness to pay is low.

### Gaps
- No published day rates for quantum consulting (BCG, Accenture, Deloitte, Capgemini Quantum Lab, boutiques) were found.
- No observed volume or rates of quantum gigs on Upwork, Malt or Toptal (page blocked; search budget exhausted).
- No practitioner ground truth gathered from Reddit, Hacker News or Stack Exchange.
- No authoritative total count of quantum developers (e.g. across Qiskit, Cirq and CUDA-Q) was found.
- The 2025 percentages for barriers (price, documentation) were not in the page text; only the 2024 baseline was retrieved.

---

## 8. Open-source sustainability and grant programmes: could non-dilutive grants fund a zero-capital start? Typical award sizes and eligibility?

### Takeaway
Yes, but only as a bridge, and the big money depends on location. A solo founder anywhere can get a ~$4K Unitary Foundation microgrant (no affiliation required) plus free or nearly free compute (IBM Open Plan; Azure $500 credits per provider). The meaningful non-dilutive sums are geography-locked:
- **US SBIR/STTR**: up to $305K for Phase I and $1.25M for Phase II, equity-free, roughly 10-20% success, a US small business required;
- **UK NQCC/STFC SparQ proof-of-concept grants**: £60-80K in 2026.

Grants fund the activity but do not prove demand. Several "quantum software" firms (qBraid, 1QBit, Phasecraft, Multiverse) depend partly on grants.

### Cited Findings

**Unitary Foundation microgrants**
- $4,000 each, applications open on a rolling basis; per aggregators, "no organizational affiliation required" and the application is a short form plus a two-minute video — [startupgrantsindia aggregator](https://www.startupgrantsindia.com/unitary-foundation-microgrant); [GrantedAI](https://grantedai.com/grants/unitary-foundation-quantum-tech-grants-unitary-foundation-e35766ff).
- The official page reports more than 140 microgrants across 31+ countries, 420+ citing papers, 40+ new libraries, and "3 new startups" — [Unitary Foundation grants](https://unitary.foundation/grants/).

**NSF SBIR/STTR (solicitation NSF 26-510)**
- Phase I: up to $305K over 6-18 months. Phase II: up to $1.25M. NSF "takes no equity".
- About 180 SBIR Phase I awards a year, and about $210M a year across the programme.
- The PI must be at least 51% employed by the small business; a Project Pitch invitation comes first.
- Deadlines: 27 Jul 2026, 4 Nov 2026, 4 Mar 2027.
- The solicitation does not single out quantum as a topic.
- Source: [NSF 26-510](https://www.nsf.gov/funding/opportunities/small-business-innovation-research-small-business-technology/nsf26-510/solicitation).
- Historical Phase I funding rates are quoted at about 10-20% — [Grantsights guide](https://grantsights.com/blog/nsf-sbir-guide).
- qBraid's 2025 NSF POSE Phase I grant was $300K — [qBraid](https://qbraid.com/blog-posts/qbraid-awarded-nsf-grant-to-advance-open-source-quantum-software-ecosystem).

**UK NQCC / STFC SparQ proof-of-concept calls**
- 2025 call: open 30 Jul-30 Sep 2025, maximum £75K — [NQCC](https://www.nqcc.ac.uk/?p=25216) (search summary).
- 2026 call: up to £60K for a 3-month PoC and £80K for a 6-month PoC+; "business-led projects", including "benchmarking quantum applications and testing algorithms on real hardware"; deadline 19 Aug 2026 — [NQCC](https://www.nqcc.ac.uk/funding/proof-of-concept-call-2025/).
- 13 projects were funded in an earlier round — [HPCwire](https://hpcwire.com/off-the-wire/nqcc-and-stfc-select-13-projects-for-uk-quantum-computing-grants).
- SparQ also offers hardware access via a new "SparQ Access Industry Channel" — [NQCC SparQ](https://www.nqcc.ac.uk/?p=9549).

**Free or cheap compute**
- IBM Open Plan gives up to 10 free minutes per month (28-day window). Since 16 Mar 2026, a promotion adds the equivalent of 180 more minutes over 12 months. Pay-as-you-go costs $96/min, billed per second — [IBM pricing](https://www.ibm.com/quantum/pricing); [IBM Open Plan updates](https://www.ibm.com/quantum/blog/open-plan-updates).
- Azure Quantum gives $500 of credits per hardware provider for 6 months, plus up to $10K via its credits programme — [Microsoft Learn](https://learn.microsoft.com/azure/quantum/pricing).

**Grant dependence of companies in the sector**
- Multiverse's Series B included $45M of grants and partnerships — [Crunchbase News](https://news.crunchbase.com/venture/quantum-multiverse-computing-startup-raises-funding).
- Phasecraft's total raised includes grants — [The Quantum Insider](https://thequantuminsider.com/2025/09/02/phasecraft-raises-34-million-from-plural-playground-global-and-novo-holdings/).
- 1QBit is classified "Grant | Alive" — [CB Insights](https://www.cbinsights.com/company/1qbit-information-technologies).
- Xanadu's revenue comes from DARPA QBI — [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/xanadu-revenue-climbs-4x-quantum-152853198.html).

**Sustainability of open source**
- Nearly 40% of open-source quantum contributors are unpaid (2025) — [The Quantum Insider](https://thequantuminsider.com/2025/11/05/the-young-and-the-relentless-poll-shows-more-quantum-developers-are-young-independent-and-unpaid/).
- In 2025 open-ended feedback, "funding, commercialization, and sustainability" drew only 6 of 88 mentions — [Unitary survey 2025](https://unitaryfoundation.github.io/survey-2025).

### Inferences
- A realistic zero-capital stack is: Unitary microgrant ($4K) + IBM Open Plan / Azure credits + simulators on a laptop or free GPU tiers + AI coding agents. It funds a portfolio project or open-source library, not a company.
- The next step up is an SBIR Phase I ($305K) or a SparQ PoC (£60-80K):
  - US SBIR requires a US small business and a PI at least 51% employed there. Under the SBA policy directive it normally also requires majority US ownership; the NSF page itself does not state this (not verified here).
  - SparQ PoCs require a credible business-led use case, usually with an end-user partner.
- Grant success also drives the observed "pilot economy": grants fund PoCs, PoCs rarely become recurring revenue. For the comparative study, grant-fundable is not the same as a market.

### Gaps
- The following were not researched (search budget exhausted):
  - Innovate UK quantum missions pilots / Quantum Missions programme sizes;
  - EU EIC Accelerator and Pathfinder quantum calls, Digital Europe, Horizon Europe quantum flagship SME eligibility;
  - France 2030 / Bpifrance quantum grants;
  - DARPA QBI contract amounts;
  - AWS Cloud Credit for Research and Braket credits;
  - Quantum Open Source Foundation (QOSF) mentorship and grants;
  - Nvidia Inception.
- The microgrant amount comes from aggregators; the official Unitary page does not state it.

---

## 9. Synthesis (derived from the objective): which niches are realistically open to a solo founder or tiny team with near-zero capital, AI agents and pay-as-you-go cloud or simulators? Where is a PhD a hard prerequisite? Which ideas are false good ideas?

### Takeaway
Weak demand is the binding constraint, not technology. There is no pure quantum-software product niche with evidence of recurring paid demand that a non-PhD solo founder can reach at zero capital in 2026. The defensible openings are thin and service-shaped:
1. classical-baseline "reality check" and benchmarking services sold as part of PoCs, or as white-label work for consultancies and vendors;
2. grant-funded open-source tooling (verification and testing harnesses for quantum code, evaluation-harness hygiene, SDK migration helpers) as a credibility-building springboard;
3. education and on-ramping for the many newcomers, which has low willingness to pay and free incumbents.

Compared with non-software opportunities, this layer should be scored as low demand, high credibility barrier, and fast commoditisation by IBM and Nvidia.

### Cited Findings (evidence base for the assessment, all from sections above)

**Revenue concentration and the pilot economy**
- Classiq ~$8-9M revenue on more than $200M raised — [Globes](https://en.globes.co.il/en/article-1001510071); [SiliconANGLE](https://siliconangle.com/2025/11/13/quantum-software-startup-classiq-raises-new-funding-amd-qualcomm/).
- Horizon Quantum's Q1 2026 revenue was $0 — [QCR](https://quantumcomputingreport.com/horizon-quantum-reports-q1-2026-financial-results-nasdaq-debut-and-testbed-expansion/).
- RIKEN supplied 60% of Quantinuum's 2025 revenue — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/quantinuum-ipo-targets-12-7b-162055146.html).

**Who pays**
- Hardware vendors, through commercial agreements (Algorithmiq with Microsoft, IBM, Rigetti) — [Algorithmiq](https://algorithmiq.fi/news/algorithmiq-establishes-milan-headquarters-and-raises-18m-to-position-europe-as-the-future-of-quantum-software).
- Hardware builders (Quantum Machines' customer base) — [TechCrunch](https://techcrunch.com/2025/02/25/quantum-machines-raises-170m-says-its-working-with-more-than-half-of-all-quantum-computing-companies).
- DARPA (Xanadu) — [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/xanadu-revenue-climbs-4x-quantum-152853198.html).
- IBM Premium customers (Qiskit Functions) — [IBM](https://www.ibm.com/quantum/blog/functions-2026).

**Commoditisation by incumbents**
- IBM's open MCP servers — [IBM](https://quantum.cloud.ibm.com/docs/guides/qiskit-mcp-servers).
- Nvidia's open Ising models — [NVIDIA](https://developer.nvidia.com/blog/nvidia-ising-introduces-ai-powered-workflows-to-build-fault-tolerant-quantum-systems/).
- Free one-year Qiskit Functions licences — [IBM](https://www.ibm.com/quantum/blog/functions-2026).

**Developer base: young, partly unpaid, price-sensitive**
- [The Quantum Insider 2025](https://thequantuminsider.com/2025/11/05/the-young-and-the-relentless-poll-shows-more-quantum-developers-are-young-independent-and-unpaid/); [QCR 2026](https://quantumcomputingreport.com/unitary-foundation-releases-2026-quantum-open-source-survey-covering-sdk-adoption-hybrid-hpc-workflows-and-ai-tooling/amp/); [Unitary 2025](https://unitaryfoundation.github.io/survey-2025).

**Verification is an unmet need**
- QuanBench+ failure modes are semantic — [arXiv 2604.08570](https://arxiv.org/html/2604.08570).
- Benchmark harnesses are unreliable — [arXiv 2610.28678](https://arxiv.org/abs/2610.28678).
- LLM-written tests are unreliable — [arXiv 2610.13811](https://arxiv.org/pdf/2610.13811).
- 81.6% of developers verify AI output always or mostly — [QCR 2026](https://quantumcomputingreport.com/unitary-foundation-releases-2026-quantum-open-source-survey-covering-sdk-adoption-hybrid-hpc-workflows-and-ai-tooling/amp/).

**Benchmarking against classical baselines is billed inside PoCs**
- qBraid Pilots — [qBraid](https://www.qbraid.com/blog-posts/qbraid-pilots-aws-marketplace).
- BCG–QuEra — [BCG](https://www.bcg.com/news-30september2025-accelerate-quantum-value-enterprises-government-innovators).
- NQCC funds "benchmarking quantum applications" PoCs — [NQCC](https://www.nqcc.ac.uk/funding/proof-of-concept-call-2025/).

### Inferences

**Niche-by-niche assessment** (solo founder, about €0 capital, AI agents, pay-as-you-go or simulators)

| Niche | Evidence of paid demand | PhD needed? | Capital or hardware needed? | Commoditisation threat | Verdict |
|---|---|---|---|---|---|
| Error suppression / mitigation functions | Yes (Q-CTRL, Qedma, Algorithmiq via IBM; Quantinuum Nexus) | Yes, hard prerequisite | Hardware access; partner status with IBM | High (IBM giving licences free; VC-funded incumbents) | Closed |
| QEC decoders / calibration agents | Yes, from hardware makers (Riverlane, Quantum Machines) | Yes | Lab or hardware access | Very high (Nvidia Ising open models, Stim/PyMatching) | Closed |
| Qiskit Functions / marketplace "app" | No published seller revenue | Usually | Premium-plan buyers only | High | False good idea |
| Quantum MCP server / AI assistant / skills for Qiskit | No evidence | No | None | Total (IBM ships it free; third-party packages exist) | False good idea as a business; fine as portfolio work |
| Quantum IDE / SDK / multi-cloud aggregator | Weak (qBraid on grants, Strangeworks pivoting to AI, Covalent exited) | No | Low | High | False good idea |
| SDK migration (Qiskit 1.x to 2.x) tooling | None found; users largely unpaid academics | No | None | High (IBM guides plus general LLMs) | Weak; possible micro-service for corporate R&D codebases, unproven |
| Verification and testing harness for (LLM-written) quantum code; eval-harness auditing | Need well documented; payers unclear (labs? IBM? grants) | Helpful but not strictly required (strong software testing plus quantum literacy) | None (simulators) | Medium | Grant-fundable open-source springboard; commercial demand unproven |
| Classical-baseline "reality check" and benchmarking for corporate or investor quantum PoCs | Indirect yes (billed inside PoCs by qBraid and BCG; NQCC funds benchmarking; $12.6B VC in 2025 creates diligence need) | Not strictly; needs strong classical optimisation and simulation skills plus credibility | Low (simulators, free GPU tiers, Open Plan) | Medium (consultancies, vendors) | Most plausible service niche, but credibility and sales are the barrier; fits subcontracting to consultancies or VCs |
| Quantum-inspired optimisation consulting | Yes, but really classical OR demand (Fujitsu/Toyota; Quantagonia/Gurobi lineage) | No | Low | Classical solver vendors | Viable only as an OR/AI business; the quantum label adds risk |
| Education / on-ramp for classical developers (56% newcomers) | Low WTP (Black Opal $10-20/mo; free IBM/PennyLane content) | No | None | High | Low-revenue, content-style niche |
| Grant-funded open-source library (Unitary $4K; NSF SBIR $305K if US; SparQ £60-80K if UK) | Grants, not customers | No for microgrants; credible team for SBIR/SparQ | None | n/a | Feasible bridge, not a business model |

**Where a PhD is a hard prerequisite.** Error mitigation and suppression, QEC decoding, calibration, novel algorithms (Phasecraft- or Algorithmiq-type), and credible enterprise use-case discovery for pharma and chemistry. **Where it is not.** Developer tooling, documentation and education, migration and testing utilities, cloud-cost and benchmarking dashboards, classical baselines for optimisation, and procurement-wrapped services. Those are exactly the areas without proven paying demand.

**False good ideas to flag for the comparative study:**
1. a "Quantum app store", or listing functions on IBM, AWS or Azure for usage revenue;
2. an LLM assistant or MCP server for quantum programming as a SaaS;
3. a cross-SDK or multi-cloud platform (qBraid and Strangeworks already exist, and they are subscale or pivoting);
4. "quantum-inspired AI" branding (Zapata);
5. paid developer tools aimed at students and researchers;
6. assuming that grants or PoCs mean a market. PoCs have grown, but recurring revenue remains in the low millions even for the category leader.

**Honest bottom line for the comparison.** In this layer, a zero-capital founder's realistic best case is a small consulting or service income stream: subcontracted benchmarking, classical-baseline and PoC implementation, possibly bootstrapped by a microgrant and public-hardware time. The founder would compete with venture-funded vendors and big consultancies for a limited pool of corporate R&D budgets. Upside depends on hardware timelines outside the founder's control (utility-scale machines are targeted for 2029-2030 by Xanadu, for example — [Quartr/Analyst Day](https://quartr.com/events/xanadu-quantum-technologies-limited-xndu-analyst-day-2026_FTvjQKcg)). Against non-software opportunities, the layer should rank low on demand certainty.

### Gaps
- Not tested: whether VCs, corporate venture arms or procurement teams actually pay independent experts for quantum due diligence (rates, volume). This is the key hypothesis behind the most plausible niche, and it should be validated by interviews rather than desk research.
- No direct evidence on freelance quantum demand (Upwork, Malt, Toptal), and no consulting day rates.
- Post-quantum cryptography migration services, which may offer far stronger near-term demand, were out of scope for this note and not researched here.
