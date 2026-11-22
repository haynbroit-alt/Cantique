# Adversarial check: the "quantum funding radar" (AI-run funding/tender alerts plus fixed-fee proposal support for quantum companies and labs)

Method note: research ran on 22 Nov 2026 with a limited search budget. Web searches and page fetches were used, plus one direct test of the EU Funding & Tenders (SEDIA) search API with curl (results below, reproducible). Each claim carries its source URL. Figures from vendor marketing pages or blogs are flagged as low-confidence. Several of the requested names were not checked individually; they are listed under Gaps. Today is 22 Nov 2026, so any deadline earlier than that has passed.

## 1. Competitors: does anyone already sell quantum-specific funding/tender intelligence or quantum-specific grant writing?

### Takeaway
The earlier claim that there is "no quantum-specialised grant consultancy or tender feed" is **refuted for the feed** and **partly refuted for the consultancy**.

On the feed side, quantum funding feeds and alerts already exist, and most are free:
- **BW&CO**: a free quantum and photonics database with email alerts, plus paid SBIR proposal services.
- **The Quantum Insider (TQI)**: its paid platform advertises real-time public procurement and funding feeds.
- **Science|Business**: a paid newswire that runs recurring quantum "Funding Radar" lists.
- **Public bodies**: qt.eu, NQCC, quantum.gov and Innovate UK Business Connect all list quantum calls for free.
- **EUACC.ai**: a free AI connector to EU funding programmes, with a weekly briefing.
- **Official portals**: the EU portal, UK Find a Grant and Grants.gov all offer free saved-search alerts.

On the consultancy side, I found no quantum-only grant consultancy in Europe. But generalist firms already market to quantum companies and name quantum wins: GrantUp, Zaz Ventures, PNO UK, GrantTree, and SetSquared's subsidised quantum grant writer.

### Cited Findings

**Quantum-specific feeds and trackers (the "radar" half)**
- **BW&CO Consulting (Houston, TX)** runs a funding database page titled "Quantum & Photonics":
  - Each listing gives a deadline, award size and fit notes, across DoD, DOE, NSF and NIST.
  - The page states "Anyone can search and read the listings" (it is free).
  - It also states "Join 6,732 others who get free funding alerts". This subscriber count covers BW&CO's alerts across all categories, not quantum only.
  - Fetched 22 Nov 2026 — [BW&CO Quantum & Photonics](https://www.bwcoconsulting.com/funding/quantum-photonics)
  - Example quantum topic page: "Integrated Multicomponent Module for Quantum Sensors – SBIR Topic OSW26BZ04-DV007" — [BW&CO topic page](https://www.bwcoconsulting.com/fod/osw26bz04-dv007)
- **BW&CO also sells proposals.** Its pricing pages give:
  - SBIR Phase I: **$13,000 flat**, or **$10,000 + 5% success fee**.
  - SBIR Phase II: **$18,000 flat**, or **$14,000 + 5%**.
  - Multiple proposals: from **$6,000/month + 5%**.
  - Review: from **$1,000 + 1%**. Compliance: from **$4,000 + 3%**.
  - Sources: [BW&CO pricing](https://www.bwcoconsulting.com/new-blog); [single proposal](https://www.bwcoconsulting.com/services/single-proposal); [multiple proposals](https://www.bwcoconsulting.com/services/multiple-proposals) (via search snippets).
  - Its self-ranking article (Mar 2026) describes BW&CO as using "AI-driven analysis of agency behavior". It lists US competitors BBCetc, Dawnbreaker, Eva Garland and REOFTech; none is described as quantum-specialised and no prices are given — [BW&CO best SBIR firms 2026](https://www.bwcoconsulting.com/blog/best-sbir-consulting-firms-2026)
  - In short, BW&CO already combines an AI-assisted free funding feed, a quantum category and paid proposal writing, in the US market. That is the proposed business model.
- **The Quantum Insider (TQI) Intelligence Platform** (paid; page modified 26 Oct 2026):
  - It advertises "Real-time public procurement and funding feeds, tracked in one place".
  - Its FAQ says "A government layer tracks national programs, public funding, and procurement opportunities".
  - It counts 180+ government agencies, 2,100+ companies, 1,000+ research groups and 700+ universities.
  - It claims "More than 200 enterprise and government clients" and 60,000+ daily briefing subscribers.
  - Pricing is by quote, based on seat count and subscription type; academic subscriptions are priced separately.
  - Sources: [TQI Intelligence Platform](https://thequantuminsider.com/tqi-intelligence-platform/); [TQI platform](https://thequantuminsider.com/platform/)
  - TQI also publishes a "Global Government Quantum Funding Dataset": 657 programme lines for 2016–2030, $40.9B confirmed against $160.6B announced, as of Q3 2026 (search summary). This tracks programmes, not open calls — [TQI government funding dataset](https://thequantuminsider.com/government-quantum-funding/)
- **Science|Business Funding Newswire** (paid, weekly):
  - It includes "Funding Radar: Your weekly selection of essential calls".
  - It has run recurring quantum-only roundups, for example "this week's seven most interesting calls for proposals in quantum technologies", and lists covering the EU, UK, US, Japan, India, Canada, Singapore, Korea and the Nordics (one roundup dated late April 2025).
  - It offers a 2-week free trial and SME rates on request. Prices could not be retrieved (HTTP 403).
  - Sources: [S|B subscriptions](https://sciencebusiness.net/funding-newswire-subscriptions); [S|B quantum roundup](https://sciencebusiness.net/news/funding-radar-weeks-seven-most-interesting-calls-proposals-quantum-technologies); [S|B quantum roundup 2](https://sciencebusiness.net/news/r-d-funding/quantum-computing/weeks-round-quantum-related-calls-2)
- **Free official quantum call lists:**
  - **qt.eu (EU Quantum Flagship), "Open and Forthcoming Calls"**, sorted by deadline. On 22 Nov 2026 it listed EuroHPC QML-07 (deadline 28 Jan 2027), Chips JU QUANTUM-1 and QUANTUM-2 (31 Mar 2027) and CL4 Space Gravimetry (2 Sep 2027) — [qt.eu funding opportunities](https://qt.eu/funding-opportunities)
  - **NQCC (UK) funding opportunities page** — [NQCC](https://www.nqcc.ac.uk/funding-opportunities)
  - **quantum.gov "R&D funding opp" category (US).** Its first page shows only one post in 2026: NSF NQNI, up to $100M, posted 28 Feb 2026 — [quantum.gov](https://www.quantum.gov/category/rd-funding-opp)
  - **Innovate UK Business Connect quantum page and mailing list.** On 22 Nov 2026 it listed the UK–Netherlands quantum co-innovation competition (opens 3 Nov 2026, closes 9 Feb 2027, up to £1.5M), EIC Pathfinder 2027 (with ring-fenced quantum challenge funding), and Chips JU 2026 — [IUKBC quantum](https://iuk-business-connect.org.uk/quantum/)
  - **EuroAgenda** science funding calls page — [EuroAgenda](https://euagenda.eu/funding-calls/science)
- **AI-native free substitute: EUACC.ai** (guide published 1 Mar 2026). It offers:
  - An "AI Connector (MCP)" that links Claude, ChatGPT or Grok to its EU programme records, source documents and grant-writing methods.
  - A weekly funding briefing, with a free account.
  - Coverage of EIC Accelerator, Pathfinder and Transition, Horizon Clusters 4–6 and Chips JU.
  - It does not list quantum as a sector.
  - Source: [EUACC AI grant writing guide](https://www.euacc.ai/guides/ai-grant-writing)
- **Free portal alerts:**
  - The EU Funding & Tenders Portal saved searches can trigger automatic notifications. The documentation found covers calls for tenders explicitly — [F&T wiki: Saved searches](https://wikis.ec.europa.eu/display/FTPortal/Saved+searches); [F&T wiki: Notifications](https://wikis.ec.europa.eu/display/FTPortal/Notifications)
  - UK Find a Grant offers email notifications — [Find a grant](https://www.find-government-grants.service.gov.uk:443/notifications/check-email)
  - Grants.gov offers saved-search subscriptions — [Grants.gov](https://grants.gov/help/connect/subscribe-to-saved-searches)
- **Other public trackers** (they track funding money, not open calls):
  - ECIPE Quantum Tracker — [ECIPE](https://ecipe.org/quantum-tracker/)
  - QPF policy tracker covering 96 jurisdictions — [QPF](https://qpf.org/policy-tracker/)
  - Entangled Future investment tracker — [Entangled Future](https://entangledfuture.com/investment/)
  - QuantumRoundup — [QuantumRoundup](https://quantumroundup.com/)

**Grant writing with explicit quantum positioning (the "proposal support" half)**
- **GrantUp (UK)** has a "Quantum Technologies" sector page. It says applications are "written by PhD-level specialists who have won these awards themselves". It targets Innovate UK Quantum CR&D, EIC Pathfinder, ESA quantum calls and EPSRC. It names no quantum clients and gives no fees; it claims "£190m+ won" overall — [GrantUp quantum](https://grantup.co.uk/sectors/quantum)
- **Zaz Ventures** (Brussels, London, Stans, Singapore) is a deep-tech capital advisory firm working on a "no-win-no-pay" basis. Its success stories include **QuantrolOx, €10.6M, EIC Accelerator**, and MiraEx (€2.5M, Swiss SERI Accelerator), under a "Semiconductors, Chips & Quantum" category — [Zaz Ventures](https://www.zazventures.com/)
- **PNO Consultants UK** publishes pages on the UK Quantum Missions pilot (quantum computing and networks) and on quantum consortium funding rules, with a "How PNO can support you" section — [PNO Quantum Missions pilot](https://pnoconsultants.com/uk/?p=7349); [PNO UK quantum rules](https://pnoconsultants.com/uk/?p=7127)
- **GrantTree (UK)** appeared in search results as offering grant-writing experts and eligibility checks for quantum applications. The page itself returned 404, so this is unverified — [GrantTree (search result)](https://granttree.co.uk/?p=15439)
- **SetSquared's quantum technology programme** offered funded (subsidised) support, including "support from an experienced professional grant writer" and a pre-submission review. The listing is from 2023 and its current status was not checked — [SetSquared quantum](https://www.setsquared.co.uk/programme/quantum-technology/)
- **QURECA** offers business development, business intelligence, training and research support. I found no grant-writing service — [QURECA research support](https://www.qureca.com/?p=19549)
- **Quantum Delta NL** runs investment and support programmes (QDNL Participations €15M fund; Infinity spin-out support; LightSpeed). I found no grant-application service — [TQI on QDNL fund](https://thequantuminsider.com/2023/03/02/e15-million-fund-launches-to-accelerate-netherlands-early-stage-quantum-technology-startups/); [Silicon Canals](https://siliconcanals.com/quantum-delta-nl-helps-startups/)
- **QuIC** has 140–210+ members. I found no description of grant or member funding-alert services — [qt.eu QuIC](https://qt.eu/ecosystem/industry/quic); [EuroHPC on QuIC](https://eurohpc-ju.europa.eu/press-release/quic-joins-eurohpc-ju)
- **Generic AI grant tools:**
  - **Granter.ai** (Lisbon) raised €1.6M (about €2M total). It matches companies to EU and public funding and auto-drafts applications. Pricing is unclear (waitlist, custom pricing) — [Tech Insider](https://tech-insider.org/granter-1-6m-euro-ai-public-funding-platform-europe-expansion-2026/); [Portugal Global](https://www.portugalglobal.pt/en/news/portuguese-ai-startup-generates-applications-for-eu-funding/)
  - **Grantbot.pl** starts at €49/month for 3 applications — [Capterra](https://www.capterra.com/p/10047180/Grantbot-pl/)
  - **Instrumentl** (US, mostly nonprofits): about $299/month billed annually for Discover, $499 for Pre-Award with AI drafting, $999 for Full Lifecycle (third-party summaries, 2026) — [AI Tools Bakery](https://aitoolsbakery.com/blog/instrumentl-pricing/); [Capterra](https://www.capterra.com/p/233384/Instrumentl/pricing/)
- **Official free help competes with paid consultants.** The EIC Board (28 Feb 2025) says "success in EIC calls is achievable without them". It points applicants to free National Contact Points, technology transfer offices and EIC coaching, and warns about "exclusivity clauses, IP rights, and the nature of success fees" — [EIC Board observations](https://eic.ec.europa.eu/news/eic-board-observations-use-consultants-eic-applications-2025-02-28_en)
- **The EIC consultants' Code of Conduct** requires consultants to disclose their success rate (approved vs submitted applications) and to make success-fee pricing transparent before taking an assignment (search summary of the Code) — [EIC Board CoC](https://eic.ec.europa.eu/system/files/2023-08/EIC_Board_CoC_versionforcomments_31072023_0.pdf)

### Inferences
- **The radar half is not a gap.**
  - In the US, BW&CO already gives away a quantum and photonics feed to build a list of thousands, then sells $10–18k proposals.
  - In Europe, the Quantum Flagship (qt.eu) curates open quantum calls for free.
  - TQI, the dominant quantum media and data brand, already bundles procurement and funding feeds into an enterprise platform with 200+ clients.
  - A newcomer's alert product would compete with free official lists and with features inside incumbents' bundles.
- **The proposal-support half is a partial gap.** No firm calls itself "the quantum grant consultancy" in Europe. But GrantUp, Zaz and PNO already put quantum on their sites and in their references. A no-brand entrant with no track record would face the EIC Code of Conduct obligation to disclose a success rate of zero.
- **"AI-run" is not a differentiator.** BW&CO markets AI-driven analysis, EUACC.ai gives away an AI connector to EU programme documents, and Granter.ai raised money to auto-draft EU applications.

### Gaps
Not checked individually (search budget):
- GQI / Quantum Computing Report funding modules.
- QED-C member services (funding alerts for members?).
- Munich Quantum Valley; Bpifrance, Le Lab Quantique and France Quantum alerts.
- UKQuantum/techUK member alerts; EuroQCS info days; the Quantum NCP network specifically.
- Zabala, Evalueserve, Ayming, Leyton, Alcimed, Inno-Fund, EU-Startups/Eurofunding, Kaila, Grantify, Fundingbox, Euro Funding Advisory, Up2Europe, Getfund, Spinverse, PeakFunding, Fundinghouse.
- Larta, Foresight, SBIR Advisors; GrantForward, Grantable, Grantboost, Fundsprout, Openfund.
- A search combining Spinverse, Zabala and Fundinghouse with "quantum" returned nothing. That is **not** evidence that they lack quantum work.

Not retrieved:
- Science|Business and TQI prices.
- BW&CO's list of quantum clients (if any).

## 2. Demand and willingness to pay: do quantum SMEs, spinouts and labs pay for grant or tender help?

### Takeaway
Paying for proposal writing is an established habit in deep tech. US SBIR proposals sell for about $10–18k plus around 5%, EU firms often charge success fees in the 2–5% range, and blog estimates for an EIC proposal run €5–30k. I found **no direct evidence of quantum companies paying for alerts**, and no quantum-specific testimonials beyond a few consultancy case studies (QuantrolOx via Zaz). Grants matter to quantum firms: Innovate UK supplied 91% of UK high-growth quantum firms' grant funding in 2022. But the public share of quantum start-up capital collapsed in 2025 as private money surged. Odds of winning are low and falling as AI-assisted applications flood funders, which weakens any success-fee model.

### Cited Findings
- **US proposal-writing prices:** BW&CO charges $13k flat (Phase I) or $10k + 5%; Phase II $18k flat or $14k + 5%; retainer from $6k/month + 5% — [BW&CO pricing](https://www.bwcoconsulting.com/new-blog)
- **EU price signals (low confidence; vendor or blog sources):**
  - A founder guide gives "€5K–€30K for professional proposal writing support" for the EIC (search summary) — [search result on EIC costs](https://www.openaeuropeancompany.com/blog/eu-startup-funding-guide/)
  - One EIC-ecosystem vendor charges a monthly rate plus a 5% success fee and calls it "standard". Another charges 2% on grant or equity (search summary) — [EIC consultant search results](https://eic.ec.europa.eu/eic-funding-opportunities/bas_en)
  - Zaz Ventures works on a pure "no-win-no-pay" basis — [Zaz](https://www.zazventures.com/)
  - A grant-writing guide notes there are no official reference rates; fees are hourly, daily, per proposal, retainer or success-based — [Grantbite (search summary)](https://www.grantbite.com/en/blog/grant-writing-services)
- **Who pays, and from what budget:** Under Horizon Europe the grant generally cannot reimburse proposal writing, so the fee comes from the applicant's own funds, often shared across consortium partners (search summary of university grants-office guidance) — [Unibas grants office](https://www.unibas.ch/en/University/Administration-Services/Vice-President-for-Research/Grants-Office/Grants-Office-News/Grants-Office-Newsletter-Archive/Grants-Office-Newsletter-2021-03/Consultants.html)
- **Subsidised consulting for EIC beneficiaries:** EIC Business Acceleration Services cover "up to EUR 60,000 to cover up to 50% of service costs" from vetted EIC Partners (2026 listing, search summary) — [EIC BAS](https://eic.ec.europa.eu/eic-funding-opportunities/bas_en)
- **Odds:**
  - EIC Accelerator March 2025 cut: 1,211 submissions (a record) and 71 winners, of which 4 were quantum SMEs — [TQI](https://thequantuminsider.com/2025/03/19/eic-chooses-nine-quantum-tech-start-ups-in-latest-funding-round/)
  - Quantum Dice was "one of only 40 deep-tech start-ups" chosen from about 1,000 applicants (Dec 2025) — [TQI](https://thequantuminsider.com/2025/12/09/quantum-dice-eic-grant/)
  - Overall EIC Accelerator success rate is about 5.9% (low-confidence blog figure) — [search result](https://www.openaeuropeancompany.com/blog/eu-startup-funding-guide/)
  - An applicant may not reapply after 3 unsuccessful submissions of the same proposal — [EIC FAQ](https://eic.ec.europa.eu/eic-frequently-asked-questions/faqs-eic-accelerator_en)
- **Quantum grant sizes:**
  - SemiQon: up to €17.5M (EIC) — [TQI](https://thequantuminsider.com/2024/07/24/quantum-transistors-awarded-up-to-e17-5-million-by-european-innovation-council/)
  - Groove Quantum: €10M EIC package, of which €2.5M is grant — [DCD](https://www.datacenterdynamics.com/en/news/groove-quantum-receives-10m-in-eic-funding-for-germanium-quantum-technology-development/)
  - QuantrolOx: €10.6M (EIC Accelerator, via Zaz) — [Zaz](https://www.zazventures.com/)
  - Phasecraft: $4.5M ARPA-E contract (2026) — [Entangled Future](https://entangledfuture.com/investment/)
  - In the 2024 EIC Accelerator round, 87% of beneficiaries received blended grant-plus-equity finance — [TQI](https://thequantuminsider.com/2024/09/23/eic-accelerator-2024-quantum-technology-start-ups-secure-grants-and-equity-funding-for-innovative-solutions)
- **UK grant dependence:**
  - Beauhurst: high-growth UK quantum firms received £24.8M of grants in 2022, 91.1% of it from Innovate UK (53 grants, £22.6M), against £98.9M of equity — [Beauhurst summary](https://www.beauhurst.com/blog/a-summary-of-the-uks-high-growth-quantum-technology-companies)
  - techUK: of 562 companies in its Quantum Economy group, 157 raised £311M in Innovate UK grants — [techUK](https://www.techuk.org/resource/collaboration-and-communities-fuel-quantum-s-funding.html)
- **Public share is falling:** McKinsey QTM 2026 reports quantum start-up investment of $12.6B in 2025, with the public-source share falling from about one-third in 2024 to 3% in 2025 (cited in earlier notes) — [McKinsey QTM 2026](https://www.mckinsey.com/capabilities/quantumblack/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point)
- **Applications are flooding in, and AI is suspected:**
  - EIC Transition proposals: 257 (2023), 413 (2024), 611 (2025).
  - The first EIC Advanced Innovation Challenges call drew 709 proposals; Science|Business reports that only 2.8% will be funded.
  - Sources: [Science|Business](https://sciencebusiness.net/news/european-innovation-council/applications-flood-first-eic-advanced-innovation-challenge-call); [EIC news 9 Mar 2026](https://eic.ec.europa.eu/news/high-interest-first-eic-advanced-innovation-challenges-call-2026-03-09_en); [Unibas commentary 11 Nov 2025](https://wwz.unibas.ch/en/news/details-2598/christian-rutzer-horizon-europe-applications-are-skyrocketing-is-ai-to-blame-11112025/); [THE](https://timeshighereducation.com/news/research-funders-flooded-ai-assisted-applications)
- **Founder statements on grant burden:** a targeted search found none. The closest material is an IBM Quantum course module on grant writing for quantum projects — [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning/courses/designing-and-leading-quantum-projects/grant-writing)

### Inferences
- **Proposal support has real willingness to pay**, at a few thousand to tens of thousands per proposal. But buyers choose writers on track record and references, which a no-brand founder lacks.
- **Alerts have weak willingness to pay**: the same information is free from qt.eu, IUKBC, NQCC, the official portals, BW&CO and EUACC.
- **Success fees are slow and low-probability cash.** With EIC odds of roughly 3–6% and a growing pile of competing applications, a portfolio needs many paid submissions before one success fee lands. The time from submission to signed grant was not verified in this session (see Gaps).
- **Grant money is shrinking as a share of what top quantum start-ups raise.** That reduces the founders' relative incentive to buy grant help, though absolute public budgets remain large (see Q4).

### Gaps
- Grant histories and the non-dilutive share for Pasqal, IQM, Alice & Bob, Quandela, planqc, Oxford Ionics, Riverlane, Phasecraft and Q-CTRL were not checked.
- No survey was found of quantum SMEs' spend on consultants, or of their use of consultants.
- No public prices were found for PNO, Zabala, GrantUp or similar EU firms.
- No quantum founder quotes on grant-writing burden were found.
- EIC and Horizon Europe time-to-grant was not verified.

## 3. Customer count and reach

### Takeaway
The buyer pool is small. QED-C counts **556 pure-play quantum companies worldwide** at end-2025, of which **173 are in the EU and 164 in the US**. UK counts range from **110** (government annex) to **771** (NPL/Beauhurst broad mapping). On this basis the EU+UK pure-play pool is in the low hundreds (roughly 300–400 by QED-C-style definitions). Broader "quantum-engaged" counts (7,418 organisations worldwide) and TQI's 2,100+ companies include large firms and adjacent players that rarely buy grant help from a newcomer. Contacts are easy to reach through public ecosystem maps, but so they are for every competitor.

### Cited Findings
- **QED-C (2026 report on 2025):** 556 pure-play quantum companies and 7,418 quantum-engaged organisations worldwide; EU 173 pure-plays, US 164; pure-play workforce about 16,500 — [TQI on QED-C 2026](https://thequantuminsider.com/2026/04/14/global-quantum-computing-market-to-double-by-2028-reaching-3-billion-in-revenue-qed-c-state-of-the-global-quantum-industry-2026-report-finds/) (EU/US split taken from earlier notes, 06_modeles_sans_capital_et_echecs.md, which cite the same source)
- **TQI:** 2,100+ companies, 1,000+ research groups, 700+ universities, 180+ government agencies tracked — [TQI platform](https://thequantuminsider.com/platform/)
- **EPO:** 935 active companies of quantum-technology origin across 72 countries (different method) — [EPO executive summary](https://link.epo.org/web/publications/studies/en-mapping-the-global-quantum-ecosystem-executive-summary.pdf)
- **UK counts:**
  - NPL ecosystem mapping: 771 companies (broad definition) — [Beauhurst NPL report](https://www.beauhurst.com/research/npl-quantum-ecosystem-mapping-report/)
  - National Quantum Strategy annex: about 110 companies, roughly 11% of the world's total — [UK gov annex](https://assets.publishing.service.gov.uk/media/6572db4433b7f20012b720b7/national-quantum-strategy-additional-evidence-annex.pdf)
  - UKRI (6 Nov 2026): 74 spinouts from the coordinated quantum programme — [UKRI](https://www.ukri.org/news/how-the-uk-built-a-quantum-technology-nation/)
  - UK quantum equity raised to date: £1.73bn; H1 2026: £587M across 23 deals — [Beauhurst Top 50, Oct 2026](https://beauhurst.com/blog/top-quantum-companies-uk/)
- **Europe-wide counts:** 542 companies and 293 start-ups in one mapping study (date unclear) — [Springer Nature community post](https://communities.springernature.com/posts/the-landscape-of-the-quantum-start-up-ecosystem). Sifted/Dealroom found 147+ start-ups in 2023 — [Sifted](https://sifted.eu/articles/europe-quantum-startups-mapped)
- **Membership bodies** (all have public or semi-public member lists usable for outreach):
  - QuIC: 140–210+ members — [qt.eu QuIC](https://qt.eu/ecosystem/industry/quic)
  - techUK Quantum Economy group: 562 companies — [techUK](https://www.techuk.org/resource/collaboration-and-communities-fuel-quantum-s-funding.html)
- **Who already reaches this audience:** TQI daily briefing has 60,000+ subscribers — [TQI platform](https://thequantuminsider.com/platform/); BW&CO alert list has 6,732 subscribers (all categories) — [BW&CO](https://www.bwcoconsulting.com/funding/quantum-photonics)

### Inferences
- **Sizing illustration** (assumption-driven, not sourced data):
  - With about 350 EU+UK pure-plays, 5% conversion at €150/month gives about 17 subscribers, or about €31k/year.
  - Even 15% conversion gives about €95k/year.
  - Adding labs and university groups mainly adds buyers who already have institutional funding databases and grants offices (see Q6).
- **The cash-poor, grant-dependent subset** (sensing, communications, components and enabling-hardware SMEs) is exactly the subset least able to pay €10k+ proposal fees upfront. That pushes the business toward success fees and their cash-flow risk.
- Reach is not a moat. TQI's list is about 9 times BW&CO's and many times what a newcomer could build in a year.

### Gaps
- There is no reliable 2026 census of EU+UK pure-plays. The QED-C UK figure was not retrieved.
- No count of quantum SMEs that actually applied to EU or UK grants in 2025–2026 was found.
- No breakdown of cash-poor versus VC-backed firms was found.

## 4. Funding volumes and cadence, 2026–2027

### Takeaway
Quantum-specific public calls are **lumpy and infrequent** at EU level.

- **SEDIA API count:** a direct query of the EU Funding & Tenders API finds about 12–15 quantum-titled EU topics with deadlines each year (2024: 12; 2025: 15; 2026: 12, including 3 cancelled; 2027: 4 so far). This undercounts topics without "quantum" in the title.
- **Quantum calls moved to EuroHPC JU:** in 2026 the EU moved quantum calls into EuroHPC JU (Council Regulation 2026/150). EuroHPC launched about €19M of quantum calls in June 2026 and €119M in August 2026; the August deadlines passed on 17 Nov 2026.
- **Currently open EU quantum calls:** only a handful as of 22 Nov 2026 (QML-07 €6M, 28 Jan 2027; Chips JU quantum calls to 31 Mar 2027; CL4 Space Gravimetry €29M, 2 Sep 2027; CL3 PQC topics, 15 Sep 2027; EIC Pathfinder 2027 quantum challenge, 29 Sep 2027).
- **The Quantum Act** will carry **no dedicated budget**. Money is deferred to the 2028–2034 MFF, which creates uncertainty after 2027.
- **US SBIR/STTR** was frozen for six months (30 Sep 2025 to 13 Apr 2026) and is now reauthorised to 2031.
- **Volume:** the flow is real (hundreds of millions per year across the EU, UK and US) but arrives in a few dozen quantum-relevant opportunities per year per region. That suits a per-opportunity service better than a monthly subscription.

### Cited Findings
- **Direct SEDIA API test (22 Nov 2026).** Endpoint: `POST https://api.tech.ec.europa.eu/search-api/prod/rest/search?apiKey=SEDIA&text=quantum`, with types 1/2/8.
  - 486 hits overall; 76 unique topics with "quantum", "QKD" or "qubit" in the title.
  - Quantum-titled topics by deadline year: 2024: 12; 2025: 15; 2026: 12; 2027: 4.
  - Open or forthcoming quantum-titled topics found: HORIZON-JU-EUROHPC-2026-QML-07-01 (28 Jan 2027), HORIZON-CL4-2027-SPACE-03-71 (2 Sep 2027), HORIZON-CL3-2027-02-CS-ECCC-03 and -04 (PQC and hybrid quantum primitives, 15 Sep 2027).
  - EuroHPC platform calls without "quantum" in the title (trapped-ion, superconducting, neutral-atom) are not counted.
  - Source: [EU Funding & Tenders search API (tested)](https://api.tech.ec.europa.eu/search-api/prod/rest/search?apiKey=SEDIA&text=quantum)
- **Horizon Europe WP 2026–2027:** published 11 Dec 2025, €14bn overall — [EEAS](https://www.eeas.europa.eu/delegations/united-kingdom/horizon-europe-makes-%E2%82%AC14-billion-available-researchers-eu-and-associated-countries_en)
  - Quantum topics in CL4 2026 had a preliminary deadline of 15 Apr 2026: the inertial-navigation sensors Grand Challenge, Standards (CSA) and Large-Scale Photonic QC (RIA). Space Gravimetry (€29M) is in 2027 — [qt.eu, 17 Dec 2025](https://qt.eu/news/2025/2025-17-12_New_EU_Quantum_Flagship_calls_published)
  - On 14 Apr 2026 those three CL4 topics were **suspended** because Council Regulation (EU) 2026/150 (16 Jan 2026) "enlarged the mandate" of EuroHPC JU to quantum — [qt.eu, 14 Apr 2026](https://qt.eu/news/2026/2026-04-14_Three_quantum_calls_suspended_under_Horizon_Europe)
- **EuroHPC JU quantum calls 2026:**
  - **June 2026:** 4 calls, about €19M. Includes QML-07 (€6M, deadline 28 Jan 2027) and PQC-06 photonic platform (€10M; deadline given as 19 or 26 Jan 2027 by different sources). The API shows STAND-05, NGC-04 and PQC-06 with deadlines on 30 Sep 2026, so sources conflict — [EuroHPC 2 Jun 2026](https://www.eurohpc-ju.europa.eu/four-new-eurohpc-ju-calls-boost-quantum-innovation-and-standardisation-europe-2026-06-02_en); [EuroHPC QML](https://www.eurohpc-ju.europa.eu/quantum-machine-learning_en)
  - **13 Aug 2026:** 6 calls, all with deadline 17 Nov 2026. Trapped-Ion €20M, Superconducting €20M, Neutral-Atom €20M, Next-Gen QKD €24M, Quantum Testing Infrastructure €20M, Experimental Pilot Lines €15M; total about €119M — [EuroHPC 14 Aug 2026](https://www.eurohpc-ju.europa.eu/six-new-quantum-calls-launched-eurohpc-joint-undertaking-2026-08-14_en); [TQI](https://thequantuminsider.com/2026/08/24/eurohpc-119m-funding-calls-quantum-technologies/)
  - **Quantum Grand Challenge QGC-02:** deadline 29 Jan 2026 — [CORDIS](https://cordis.europa.eu/programme/id/HORIZON_HORIZON-JU-EUROHPC-2026-QGC-02-01)
- **Chips JU 2026 quantum calls:** QUANTUM-1 (design) about €30M and QUANTUM-2 (enabling technologies) about €20M; one source gives €30M for QUANTUM-2. Dates conflict:
  - Norway, Malta and Denmark listings give July–September 2026.
  - qt.eu and IUKBC give a 1 Dec 2026 opening and a 31 Mar 2027 deadline.
  - Chips JU opened 16 calls worth over €300M on 8 Jul 2026.
  - Sources: [Chips JU calls](https://www.chips-ju.europa.eu/Open-and-Upcoming-Calls); [Forskningsrådet](https://www.forskningsradet.no/en/call-for-proposals/International-joint-calls/chips-eu-calls-within-technologies-2026/); [IUKBC Chips JU](https://iuk-business-connect.org.uk/opportunities/horizon-europe-chips-joint-undertaking-2026/); [qt.eu](https://qt.eu/funding-opportunities)
- **EIC 2026:**
  - About €1.4B overall. Pathfinder Challenges €96M (deadline 28 Oct 2026). Pathfinder Open €166M. Accelerator Challenges €220M (€20–50M per challenge) — [EIC 2026 WP](https://eic.ec.europa.eu/eic-2026-work-programme_en); [EIC Pathfinder Challenges 2026](https://eic.ec.europa.eu/eic-funding-opportunities/eic-pathfinder/eic-pathfinder-challenges-2026_en)
  - EIC Pathfinder 2027: Open stage-1 deadline 25 Feb 2027; Challenges 29 Sep 2027, "ring-fenced challenge funding for quantum, AI and materials" — [IUKBC quantum](https://iuk-business-connect.org.uk/quantum/)
  - 2025 Pathfinder Open: €140M to 44 projects, including quantum projects — [Quantum Zeitgeist](https://quantumzeitgeist.com/european-innovation-council-140m-to-44-projects-2/)
- **EU Quantum Act:** "The act is not about budget" (DG CNECT, 3 Sep 2026). The Nov 2026 draft sets no overall allocation; money is to come from the Horizon Europe successor and the European Competitiveness Fund, with implementation largely via EuroHPC — [The Next Web, 7 Sep 2026](https://thenextweb.com/news/eu-quantum-act-no-budget-consolidation); [TQI, 10 Nov 2026](https://thequantuminsider.com/2026/11/10/draft-eu-quantum-act-would-favor-european-suppliers-set-computing-and-security-targets/); [Clubic](https://www.clubic.com/actualite-628480-quantum-act-europeen-la-commission-veut-de-la-consolidation-mais-pas-de-budget-dedie.html)
- **UK (Innovate UK) quantum competitions 2026:**
  - Quantum-enabled sensing/PNT supply chains: up to £32.8M (registration to 8 Jul 2026).
  - Quantum technologies: up to £3M (deadline 15 Apr 2026).
  - UK–Germany co-innovation: £750k–£1M per UK grant.
  - DeepTech Catalyst Quantum: up to £50k.
  - Growth Catalyst quantum: at least £100M grant pot with investor matching (date unconfirmed).
  - UK–Netherlands co-innovation: up to £1.5M, closes 9 Feb 2027.
  - Sources: [IUKBC search results](https://iuk-business-connect.org.uk/?p=132212); [IUKBC UK-Germany](https://iuk-business-connect.org.uk/opportunities/uk-germany-collaborative-innovation-for-quantum-technologies-2026/); [IUKBC DeepTech Catalyst](https://iuk-business-connect.org.uk/?p=134298); [Quantum Zeitgeist on Growth Catalyst](https://quantumzeitgeist.com/innovate-uk-grant-funding-seed-funding/); [IUKBC quantum](https://iuk-business-connect.org.uk/quantum/)
  - The earlier Commercialising Quantum Technologies challenge ran 2018–2025 with £174M — [UKRI](https://www.ukri.org/what-we-do/our-main-funds-and-areas-of-support/browse-our-areas-of-investment-and-support/commercialising-quantum-technologies-challenge)
- **Germany (BMFTR):** the "KMU-innovativ: Photonik und Quantentechnologien" programme has twice-yearly sketch deadlines (15 Apr and 15 Oct; a 15 Apr 2026 deadline is listed by a regional database). A quantum supply-chain call had a 30 Sep 2026 deadline (university list) — [gesundheitsindustrie-bw](https://www.gesundheitsindustrie-bw.de/datenbank/foerderungen/kmu-innovativ-photonik-und-quantentechnologien/sendPdf/687085); [Uni Saarland](https://www.uni-saarland.de/en/dezernat/f/ausschreibungen/foerderer/bmbf.html)
- **Other European and international calls:** a Xecs (Eureka cluster) call on quantum technologies 2026 has a deadline of 26 Nov 2026 — [fundsforNGOs](https://www2.fundsforngos.org/innovation/xecs-call-on-quantum-technologies-2026/). Canada NSERC Alliance Quantum grants pay $100k–$650k per year for up to 2 years — [NSERC](https://nserc-crsng.canada.ca/en/funding-opportunity/alliance-quantum-grants-call-proposals-advancing-development-and-adoption)
- **US:**
  - SBIR/STTR authorisation lapsed 30 Sep 2025. Agencies could not issue new solicitations. It was reauthorised on 13 Apr 2026 through 30 Sep 2031 (P.L. 119-83) after a six-month lapse — [CRS IN12705](https://www.everycrsreport.com/reports/IN12705.html); [Crowell](https://www.crowell.com/en/insights/client-alerts/sbirsttr-programs-reauthorized-after-six-month-lapse); [AIP](https://www.aip.org/fyi/congress-passes-small-business-research-reauthorization)
  - NQI Reauthorization Act (S.3597) passed Senate Commerce on 14 Apr 2026; H.R. 8462 was reported in April 2026; final passage not confirmed.
  - FY2026 requests: NSF QIS flat at $231M; DOE Office of Science QIS $328M.
  - DOE "Quantum Genesis" was announced in June 2026 without stated funding.
  - Sources: [Nextgov](https://www.nextgov.com/emerging-tech/2026/01/sens-young-cantwell-introduce-national-quantum-initiative-reauthorization/410550); [House Science markup](https://science.house.gov/2026/4/full-committee-markup-of-the-national-quantum-intiative-reauthorization-act); [AIP on Quantum Genesis](https://www.aip.org/fyi/doe-launches-quantum-genesis-initiative); [USC landscape 2025](https://www.sc.edu/about/offices_and_divisions/provost/docs/emerging-technology-series-quantum-information-science-landscape-2025.pdf)
  - DOE awarded $7.3M for quantum research in high-energy physics (Aug 2026) — [TQI](https://thequantuminsider.com/2026/08/26/doe-awards-7-3m-quantum-research-high-energy-physics/)

### Inferences
- **Monthly alert volume is thin.** For a typical EU quantum SME, the EU-level stream amounts to perhaps 1–3 relevant new topics a month, clustered around work-programme releases. Adding national and UK calls helps but they are country-locked: UK competitions need UK-registered firms, and BMFTR calls need German applicants.
- **Each opportunity is high-stakes** (€6–30M EU topics, £1–3M UK grants, $0.3–2M SBIR). That favours selling per-opportunity eligibility checks, partner matching and proposal work, not a monthly subscription.
- **Structural risks to 2027–2028:**
  - The EU quantum funding channel has just moved institutions (to EuroHPC JU), which creates confusion. That is a short-term argument for a radar, but EuroHPC and qt.eu publish the calls themselves.
  - Horizon Europe ends in 2027, the Quantum Act brings no new money, and the 2028–2034 MFF is unresolved. There is a plausible call gap in 2028.
  - The US just showed a six-month SBIR freeze can happen.

### Gaps
- Exact Chips JU 2026 quantum dates (conflicting).
- France 2030 / Bpifrance / ANR quantum calls; Netherlands NWO and RVO; Spain, Italy, Finland, Denmark national calls.
- Japan (Moonshot, NEDO), Korea, India NQM, Australia, the Gulf.
- DARPA QBI (mostly selected-performer stages, not open calls to SMEs), AFRL quantum topics, and FY2027 US numbers.
- Total EU quantum budget per year (only partial sums here).

## 5. AI-agent feasibility and data access

### Takeaway
Technically this is **easy**, which is the problem: the barrier to entry is near zero.
- The EU SEDIA search API works anonymously with the public key "SEDIA" (tested 22 Nov 2026, HTTP 200, JSON).
- Simpler.Grants.gov has a documented API (key required), and SBIR.gov exposes a solicitations API.
- UK Find a Tender and Contracts Finder publish OCDS data under the Open Government Licence v3.
- Rules on AI in EU proposals permit use, require disclosure and full applicant responsibility, and forbid evaluators from penalising AI use as such.
- The JRC's Horizon Europe study (Mar 2026) found that **proposals relying extensively on LLM text score lower and are funded less often**, even though partial assistance shows little effect.

### Cited Findings
- **EU F&T / SEDIA search API.** A direct POST to `https://api.tech.ec.europa.eu/search-api/prod/rest/search?apiKey=SEDIA` returned HTTP 200 and about 957 KB of JSON. Metadata includes identifier, title, deadlineDate and status (31094501 forthcoming, 31094502 open). Status flags are noisy: some "open" items have deadlines in 2023–2024. Tested 22 Nov 2026 — [SEDIA API](https://api.tech.ec.europa.eu/search-api/prod/rest/search?apiKey=SEDIA&text=quantum)
  - Third-party scrapers use the same endpoint, and Apify actors sell EU F&T monitoring — [Apify EU F&T scraper](https://apify.com/studio-amba/eu-funding-tenders-scraper); [Apify EU tenders monitor](https://apify.com/gabriel_cr/eu-tenders.md)
  - Reuse terms: one actor claims reuse under Commission Decision 2011/833/EU, which allows commercial reuse with attribution. This is unverified against an official F&T notice.
  - TED has an official, anonymous search API for procurement notices — [TED developers' corner](https://ted.europa.eu/en/simap/developers-corner-for-reusers)
- **US:**
  - Simpler.Grants.gov: `POST /v1/opportunities/search` with an `X-API-Key` header; maximum 10,000 results per search; an extracts endpoint is available — [Simpler.Grants.gov wiki](https://wiki.simpler.grants.gov/product/api/search-opportunities); [developer page](https://simpler.grants.gov/developer)
  - Legacy Grants.gov APIs: some need a key obtained through the help desk — [Grants.gov API guide](https://grants.gov/api/api-guide)
  - SBIR.gov solicitations API filters by keyword, agency and status; sorting is not supported — [SBIR.gov API](https://www.sbir.gov/api/solicitation)
  - DoD SBIR topics sit under the DoW BAA — [DARPA SBIR topics](https://www.darpa.mil/work-with-us/communities/small-business/sbir-sttr-topics)
- **UK:** Find a Tender notice data is "available under the Open Government Licence", with OCDS JSON API packages. The official REST API docs mention organisation API keys, and a third party says the OCDS endpoints need none, so this conflicts. Contracts Finder offers OCDS and CSV plus a daily archive on data.gov.uk — [Find a Tender developer docs](https://www.find-tender.service.gov.uk/Developer/Documentation); [gov.uk open contracting](https://www.gov.uk/government/publications/open-contracting); [OCP registry](https://data.open-contracting.org/en/publication/41)
- **EU rules on AI in proposals:**
  - Applicants may use generative AI but must disclose which tools were used and how, and "are fully responsible for the content … including parts produced by the AI tool".
  - Evaluators must not delegate evaluation to AI, and AI use "cannot be considered … as a reason to penalise a proposal".
  - Source: Commission standard expert briefing v13.0, Dec 2025 — [Leuphana copy of briefing slides](https://www.leuphana.de/fileadmin/user_upload/forschung/Files/transparenz/standard-briefing-slides-for-experts_he_en.pdf); [SwissCore](https://www.swisscore.org/?p=7895)
  - The European Ombudsman has opened an inquiry into AI use by external evaluators — [EO](https://eno.ombudsman.europa.eu/home/news/maincontent/eo-ombudswoman-opens-inquiry-con.html)
  - The Dutch NCP (RVO) advises: treat GenAI tools as non-private; "Do not use GenAI tools on an idea that you would like to patent later"; check for plagiarism and state AI use; failure to follow programme AI rules can make a proposal ineligible (page checked 5 Aug 2025) — [RVO](https://english.rvo.nl/topics/horizon-europe/how-use-ai-grant-proposal-writing)
- **JRC Working Paper 02/2026** (Santoleri, Rentocchini, Lelli, 18 Mar 2026), covering the universe of firm applications to Horizon Europe:
  - "around 40% of proposal abstracts exhibiting LLM-modified content by the end of 2024".
  - "proposals that rely extensively on LLM-generated text are associated with lower evaluation scores and funding probabilities".
  - Repeated-submission analysis shows no causal worsening from LLM-assisted writing.
  - Source: [JRC146131](https://publications.jrc.ec.europa.eu/repository/handle/JRC146131)

### Inferences
- **Monitoring and matching can be automated quickly by anyone.** That is why BW&CO, TQI, EUACC.ai, Granter.ai and Apify scrapers already exist. There is no data moat.
- **Value sits in judgement**: eligibility nuance, consortium construction, evaluator-grade writing. That is where AI is weakest without domain review, and where the JRC evidence penalises heavy LLM text.
- **Confidentiality and patent-disclosure concerns** (RVO) force a careful data-handling policy. Quantum founders' IP sensitivity adds sales friction for an AI-first provider with no brand.

### Gaps
- No official F&T portal terms of use or API terms were retrieved.
- SAM.gov opportunities API terms, UKRI Gateway to Research API and Innovate UK IFS machine-readability were not checked.
- No benchmark of LLM accuracy on eligibility screening was found.
- No 2026 EIC-specific data on AI-written submissions was found.

## 6. Failure modes, and whether the idea should be eliminated

### Takeaway
**The standalone "radar" subscription should be eliminated.**
- The niche is already served for free by the Quantum Flagship, Innovate UK Business Connect, NQCC, quantum.gov, BW&CO, EUACC.ai and the official portals' alerts.
- Incumbents bundle it: TQI with 200+ clients and 60k+ subscribers; Science|Business.
- The data is open via public APIs, so there is no moat.
- Call cadence is thin (about 12–15 quantum-titled EU topics a year).
- The buyer pool is a few hundred EU+UK pure-plays.

**Proposal support survives only as a heavily caveated service business.** Willingness to pay is real ($10–18k per SBIR proposal; €5–30k EIC, low confidence; 2–5% success fees). But without a track record the founder faces:
- trust barriers (EIC code: disclose success rate);
- low and falling odds (EIC about 3–6%, applications rising sharply);
- success-fee cash-flow lag;
- deadline liability;
- reputational risk from AI-heavy drafting.

At best the radar is a free lead magnet for a review or eligibility-check service. It is not the business.

### Cited Findings
- **Free substitutes** — see Q1: [qt.eu](https://qt.eu/funding-opportunities); [IUKBC quantum](https://iuk-business-connect.org.uk/quantum/); [NQCC](https://www.nqcc.ac.uk/funding-opportunities); [quantum.gov](https://www.quantum.gov/category/rd-funding-opp); [BW&CO free alerts](https://www.bwcoconsulting.com/funding/quantum-photonics); [EUACC.ai](https://www.euacc.ai/guides/ai-grant-writing); [F&T saved searches](https://wikis.ec.europa.eu/display/FTPortal/Saved+searches); [UK Find a grant notifications](https://www.find-government-grants.service.gov.uk:443/notifications/check-email); [Grants.gov saved searches](https://grants.gov/help/connect/subscribe-to-saved-searches)
- **Free human help:** NCPs "will not write your proposal, but may advise on inconsistencies, gaps and weak points". The Access2EIC annotated EIC template was published by NCPs — [EU guide on consultants (search summary)](https://webgate.ec.europa.eu/circabc-ewpp/d/d/workspace/SpacesStore/bc719794-c86e-49ce-887e-1ed5a070bc2e/download); [Business Finland Access2EIC template](https://www.businessfinland.fi/49f089/globalassets/finnish-customers/horizon-europe/access2eic_eic-accelerator-annotated-template_2024-2-1.pdf). The EIC Board says success "is achievable without" consultants — [EIC Board](https://eic.ec.europa.eu/news/eic-board-observations-use-consultants-eic-applications-2025-02-28_en)
- **Universities already pay for funding databases.** Research Professional (Ex Libris/Clarivate), Pivot and SPIN/SMARTS alert services are in institutional use, as shown by university guides from Newcastle (AU), SDU, Jena and NYIT — [Newcastle RP guide](https://www.newcastle.edu.au/__data/assets/pdf_file/0004/355612/UON-Research-Professional-User-Guide-4-Saving-Searches.pdf); [SDU RP guide](https://www.sdu.dk/-/media/files/om_sdu/centre/tekinnovation/samarbejde/rp_guide.pdf); [Pivot funding alerts](https://knowledge.exlibrisgroup.com/Pivot/Knowledge_Articles/Navigating_the_Home_Page/010Pivot_Researcher_Home_Page%3A_Funding_Alerts)
- **Incumbent bundling:** TQI "Real-time public procurement and funding feeds" sits inside a seat-priced platform with 200+ enterprise and government clients — [TQI platform](https://thequantuminsider.com/platform/)
- **Odds and competition:** EIC Accelerator March 2025 had 1,211 submissions, 71 winners, 4 quantum — [TQI](https://thequantuminsider.com/2025/03/19/eic-chooses-nine-quantum-tech-start-ups-in-latest-funding-round/). EIC Transition submissions went 257 → 413 → 611 (2023–2025). The first EIC Advanced Innovation Challenges call had a 2.8% expected success rate — [Science|Business](https://sciencebusiness.net/news/european-innovation-council/applications-flood-first-eic-advanced-innovation-challenge-call)
- **AI-drafting quality risk:** extensive LLM text is associated with lower scores and funding probability — [JRC146131](https://publications.jrc.ec.europa.eu/repository/handle/JRC146131). Applicants are fully responsible for AI-produced content and must disclose it — [RVO](https://english.rvo.nl/topics/horizon-europe/how-use-ai-grant-proposal-writing)
- **Policy and cadence shocks:**
  - Three CL4 quantum calls were suspended mid-cycle in April 2026 — [qt.eu](https://qt.eu/news/2026/2026-04-14_Three_quantum_calls_suspended_under_Horizon_Europe)
  - US SBIR was frozen for six months in 2025–2026 — [CRS](https://www.everycrsreport.com/reports/IN12705.html)
  - The Quantum Act has no dedicated budget — [The Next Web](https://thenextweb.com/news/eu-quantum-act-no-budget-consolidation)
- **Success-fee and contract risk:** the EIC warns about "the nature of success fees" and exclusivity and IP clauses, and its Code of Conduct requires success-rate disclosure and transparent success-fee pricing — [EIC Board](https://eic.ec.europa.eu/news/eic-board-observations-use-consultants-eic-applications-2025-02-28_en); [EIC CoC](https://eic.ec.europa.eu/system/files/2023-08/EIC_Board_CoC_versionforcomments_31072023_0.pdf)
- **Low-ticket SaaS comparables:** Grantbot.pl €49/month — [Capterra](https://www.capterra.com/p/10047180/Grantbot-pl/); Instrumentl about $299/month (third party) — [AI Tools Bakery](https://aitoolsbakery.com/blog/instrumentl-pricing/). Earlier notes found that QCR charged only about $100/year per person before being folded into GQI — see 06_modeles_sans_capital_et_echecs.md.

### Inferences
- **Failure modes, ranked:**
  1. **Commoditised information.** Alerts are free and API-accessible, so conversion to paid will be near zero unless bundled with human judgement.
  2. **Small TAM.** A few hundred EU+UK pure-plays caps subscription revenue at tens of thousands of euros a year even at optimistic conversion (Q3 illustration).
  3. **Trust gap.** No brand, no physics PhD and no win record is a poor fit for clients who hire on track record and references, and the EIC code requires disclosing a success rate.
  4. **Success-fee economics.** With 3–6% odds and month-long evaluation cycles, a pure success-fee model starves a zero-capital founder. Upfront fees are needed, which cash-poor SMEs resist.
  5. **Liability.** A missed deadline or an eligibility error on a €10M call is a serious professional-indemnity exposure.
  6. **AI-drafting penalty.** Heavy AI text correlates with lower scores (JRC), and disclosure is mandatory, which undercuts an "AI-operated writing" pitch.
  7. **Institutional churn.** The EuroHPC transfer, the Quantum Act with no money and the post-2027 MFF uncertainty mean the call landscape can change mid-year.
  8. **Universities** have grants offices and institutional databases (Research Professional, Pivot), and buy slowly.
- **What partly survives:** a narrow, human-reviewed eligibility-and-partner-matching service for non-UK EU quantum SMEs facing the new EuroHPC/Chips JU calls and consortium requirements (for example UK–NL and UK–DE co-innovation partner needs).
  - Sold per opportunity (for example a few hundred to a low-thousands-euro eligibility and fit memo).
  - Possibly as a white-label subcontractor to established consultancies (PNO, GrantUp, Zaz) that already have quantum clients.
  - This is a service job, not a scalable AI business, and it still needs credibility the founder lacks.
- **Verdict for this founder profile** (zero capital, no quantum brand, no PhD): **eliminate the radar as a primary business.** Keep it only as a free content and lead-generation asset if another quantum business is chosen. The earlier pass's "fastest-to-revenue" ranking rested on an unverified competitive gap, and this pass refutes that premise.

### Gaps
- No data on free-to-paid conversion for B2B funding newsletters.
- No professional-indemnity insurance cost for grant consultancies.
- No EIC or Horizon time-to-grant figures retrieved.
- No interviews or posts from quantum founders on willingness to pay for alerts versus writing.
- Science|Business and TQI subscription prices not retrieved.
- Non-EU/UK/US regions (Canada beyond NSERC, Australia, India NQM, Japan, Korea, the Gulf) not assessed.
