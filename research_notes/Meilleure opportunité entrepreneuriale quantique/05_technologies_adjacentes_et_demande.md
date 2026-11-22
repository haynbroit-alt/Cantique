# Adjacent quantum technologies (sensing, communication, quantum-inspired/hybrid optimisation) and end-user industry demand, as sources of capital-light business opportunities (state as of November 2026)

Research note written 22 Nov 2026. Scope: non-computing quantum technologies and real end-user spend, judged from the position of a founder with about zero capital, no hardware and existing AI tools and agents. Every figure is dated. "Vendor-reported" means the only source is the company or its press release.

Method caveats:
- The session's web-search budget ran out before I could check some named vendors: QuSpin, Element Six, Quantum Diamond Technologies, SBQuantum, Aquark, Delta g, Nomad Atomics, QZabre, Qant, KETS, Quantum Bridge, Qunnect, Aliro and QuintessenceLabs. The same applies to several named enterprises (Moderna, Roche, Boehringer, BASF details, Crédit Agricole, E.ON, EDF, TotalEnergies, SoftBank) and to insurance and defence-procurement mandates. These are listed under Gaps rather than filled in from memory.
- Several documents were read in full and are the core quantitative sources:
  - McKinsey Quantum Technology Monitor 2026 (April 2026, data to March 2026)
  - QED-C "State of the Global Quantum Industry 2026: Quantum Sensing Market Forecast" (April 2026)
  - BCG "Quantum Is Getting Real" (4 June 2026)

---

## Q1. Quantum sensing: actual 2025-2026 market, which products sell, who buys, and whether a role exists that needs no hardware capital

### Takeaway
Quantum sensing is the most commercially mature non-computing segment. It is still small and run by governments, mostly defence. Estimates for 2025 range from about $470M (QED-C, bottom-up from a vendor survey) to $2.8–3.1B (McKinsey, broad product-family definition that includes atomic clocks). Products that actually sell are atomic clocks and timing, magnetometers (including OPM-MEG for research), absolute quantum gravimeters (counted in tens of units), and government-funded quantum navigation prototypes.
- Software is the first-ranked offering for only 6% of sensing companies.
- Reselling is almost non-existent (2% for hardware, 0% for software as first-ranked activity).
- More than a third of sensing companies had no sales at all in 2025.
- For a zero-capital founder, the only plausible entries are narrow software/data or business-development services sold to the vendors themselves, or to defence/geoscience integrators. Defence clearances and medical-device rules close most of the attractive end markets.

### Cited Findings
**Market size and growth (dated, conflicting definitions)**
- McKinsey QTM 2026 (April 2026):
  - Quantum sensing market: $2.8–3.1B (2025), $4.0–5.0B (2030), $7.1–10.1B (2035).
  - Magnetometers "lead the expansion". The 2035 optimistic mix is about 35% magnetometers, about 25% inertial/gravimetric and about 25% atomic clocks.
  - Growth rationales given:
    - brain imaging, mineral exploration and predictive maintenance (magnetometers);
    - GPS-denied navigation and subsea exploration, "defense-led" (inertial/gravimetric);
    - telecom, GPS and financial-network timing (clocks);
    - semiconductor inspection and medical diagnostics (imaging/spectroscopy).
  - [McKinsey QTM 2026 PDF](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf); [landing page](https://www.mckinsey.com/capabilities/quantumblack/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point)
- McKinsey QTM 2025 (June 2025) gave quantum sensing as $7–10B by 2035 and $18–31B by 2040 — [McKinsey QTM 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-year-of-quantum-from-concept-to-reality-in-2025)
- QED-C/SRI (April 2026), based on 58 respondents from 47 sensing companies:
  - Global sensing market about $470M in 2025, $625M in 2026, $831M in 2027 and $1,106M in 2028 (about 32% a year).
  - Defence alone is projected at 35% of 2028 revenue. Government overall (defence plus civil) is 47%.
  - The commercial share rises from 25% (2025) to 34% (2028).
  - QED-C notes that "higher-end projections are not well supported by individual company revenue expectations."
  - [QED-C 2026 QS forecast](https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/)
- An earlier SRI/QED-C figure put 2024 quantum sensing revenue at about $375M — [SRI](https://sri.com/?p=95861). This comes from a search snippet; the underlying page was not read.
- **Conflict:** McKinsey ($2.8–3.1B, 2025) and QED-C ($470M, 2025) differ by a factor of about 6. McKinsey's 2025 breakdown already shows about $1.0–1.3B for atomic clocks alone, which suggests it counts conventional atomic-clock and SQUID product lines that QED-C's survey of "quantum sensing companies" does not capture. Treat about $0.5B as the "new quantum-sensing startup" market and about $3B as the broad incumbent-plus-startup market. Both sources: [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf); [QED-C 2026](https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/)

**What the market looks like from the supply side (QED-C, April 2026)**
- 36% of respondents had no quantum-sensing sales in 2025. Among the rest, 11% had under $500k. Only 4% had $25–50M and none had more than $50M — [QED-C 2026](https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/)
- Primary (first-ranked) activity by share of companies:

  | Activity | Share |
  |---|---|
  | Direct hardware sales | 43% |
  | Component/subassembly supply | 20% |
  | Integration services | 20% |
  | Direct software sales | 6% |
  | Reseller of hardware | 2% |
  | Reseller of software | 0% |

  Across top-three choices, software and integration services are each 16%, hardware reselling 7% and software reselling 3% — [QED-C 2026](https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/)
- Funding sources:
  - 69% get government R&D funding, which averages 56% of their financial input.
  - Commercial end-user payments are reported by only 31%.
  - Venture capital is reported by 14%.
  - [QED-C 2026](https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/)
- Revenue mix by application in 2025 (average share among sellers):

  | Application | Average share |
  |---|---|
  | Atomic clocks | 26% |
  | Magnetometers | 21% |
  | Quantum imaging (lidar/radar/low-SNR) | 18% |
  | Photon detectors | 17% |
  | Inertial sensors | 12% |
  | Gravimeters | 10% |

  Aerospace is the top commercial sector (39% first-choice), ahead of computer/electronic/optical products (15%) and cybersecurity (13%). Finance, oil and gas, pharma and energy are each at 0–2% first-choice — [QED-C 2026](https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/)
- Only 31% of companies say their primary sensing technology was commercially available in 2025. They expect 58% by 2028 — [QED-C 2026](https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/)

**Timing, clocks and PNT (the strongest-selling cluster)**
- Infleqtion (NYSE: INFQ, listed via SPAC):
  - 2025 revenue $32.5M. 2026 guidance about $40M.
  - Revenue mix about two-thirds sensing, one-third computing.
  - About 60% of 2025 revenue came from US government contracts. These included an $11M APFIT contract for Tiqker optical clocks and a $20M NASA gravity-sensing contract.
  - Its Safran partnership integrates Tiqker with Safran White Rabbit/SecureSync timing (available April 2026).
  - Sources: [The Quantum Insider, 9 Apr 2026](https://thequantuminsider.com/2026/04/09/infleqtion-announces-2026-revenue-guidance-of-40-million/); [Yahoo Finance Q4 call](https://finance.yahoo.com/markets/stocks/articles/infleqtion-q4-earnings-call-highlights-154339983.html)
  - Aggregator figures for net loss and cash conflict with the earnings-call figures, so prefer the filings.
- Q-CTRL "Ironstone Opal" (software-defined quantum navigation):
  - Two DARPA Robust Quantum Sensors (RoQS) awards worth A$38M (about US$24.4M) in total, announced 27 Aug 2025, with Lockheed Martin as subcontractor on one.
  - Q-CTRL claims "up to 111x" better accuracy than conventional inertial navigation without GPS. This is a vendor claim.
  - It has had a DIU prototype contract with Lockheed for a quantum-enabled INS (2025).
  - Sources: [Q-CTRL press release](https://q-ctrl.com/blog/darpa-selects-q-ctrl-to-develop-next-generation-quantum-sensors-for-navigation-on-advanced-defense-platforms); [Quantum Zeitgeist](https://quantumzeitgeist.com/darpa-awards-q-ctrl-24-4-m-to-build-quantum-navigation-sensors-for-defence/); [GPS World](https://www.gpsworld.com/q-ctrl-lockheed-to-develop-quantum-navigation-for-darpa/)
- SandboxAQ AQNav (magnetic anomaly navigation; the product is software plus AI on magnetometer data):
  - US Air Force SBIR Phase 2B "Tactical Funding Increase" extending a Jan 2023 Direct-to-Phase-II SBIR. Award amount not disclosed in sources.
  - More than 200 flight hours and more than 40 sorties on 4 aircraft types.
  - Joined DIU's Transition of Quantum Sensing (TQS) programme in Nov 2025.
  - Sources: [GPS World](https://www.gpsworld.com/us-air-force-and-sandboxaq-address-gps-jamming-and-spoofing/); [Defense One, Nov 2025](https://www.defenseone.com/technology/2025/11/pentagon-expands-partnership-quantum-sensing-startup/409597/)
  - Defense One quotes an official saying MagNav "isn't going to be a perfect replacement for GPS."
- SandboxAQ and Acubed (Airbus) flew more than 150 hours across routes between 200 US airports to test MagNav against commercial navigation requirements (July 2025) — [The Quantum Insider](https://thequantuminsider.com/2025/07/16/sandboxaq-and-acubed-achieve-progress-in-magnetic-navigation/)
- DIU TQS programme:
  - Field tests of about a dozen quantum sensing systems, with 18 vendors announced by March 2025, including Lockheed Martin, Northrop Grumman, Honeywell, Leidos and Anduril.
  - Honeywell holds two DoD contracts: CRUISE (quantum inertial navigation with Vector Atomic) and QUEST (magnetometer navigation).
  - A DIU MagNav flight test (Honeywell system on an Embraer 170, reported Sept 2026) ran 4h23 GPS-free with an 89% position-accuracy gain over traditional backup navigation.
  - Sources: [Breaking Defense, Mar 2025](https://breakingdefense.com/2025/03/diu-to-start-field-testing-quantum-sensors-in-tough-conditions); [DIU](https://www.diu.mil/latest/dius-transition-of-quantum-sensing-tqs-field-testing-to-begin-across-five); [ASDNews, Jul 2025](https://www.asdnews.com/news/defense/2025/07/17/honeywell-awarded-us-government-contracts-develop-quantum-sensorbased-navigation-systems); [Leeham News, 9 Sep 2026](https://leehamnews.com/2026/09/09/honeywell-tests-magnetic-navigation-in-gps-free-flight/); [ExecutiveGov](https://www.executivegov.com/articles/diu-magnav-quantum-system-flight-test)
- The US "Department of War" announced an initiative of up to about $200M for ISR via quantum sensing (June 2026). Separate from TQS — [The Quantum Insider, 24 Jun 2026](https://thequantuminsider.com/2026/06/24/department-of-war-announces-initiative-to-revolutionize-isr-via-quantum-sensing/)
- MagNav depends on magnetic anomaly maps:
  - Commercial tests used the public North American Magnetic Anomaly Map, with supplements from survey-industry and defence maps.
  - Creating maps is "often time- and resource-intensive".
  - Platform magnetic noise can be 100–1000x larger than the target anomalies.
  - Sources: [arXiv 2504.08167](https://arxiv.org/abs/2504.08167); [Airbus, Mar 2026](https://www.airbus.com/en/newsroom/stories/2026-03-quantum-navigation-the-magnetic-secret-for-precisely-determining-aircraft-location)
- No source found confirming airline certification or routine airline use of MagNav as of late 2026 (search result review).

**Gravimetry (geophysics, volcanology, civil engineering, defence)**
- Exail (ex-Muquans):
  - "More than 20 units" of its Absolute Quantum Gravimeter deployed worldwide (Dec 2025).
  - Three AQGs delivered to INVOLCAN, Canary Islands, for volcano monitoring (Dec 2025).
  - Two gravimeters sold to a European research institute in Q3 2025.
  - The French Navy received a serial-produced quantum gravimeter for seabed mapping (2024).
  - Group revenue was €479M in 2025, with no breakdown for gravimeters.
  - Sources: [Exail news](https://www.exail.com/news/three-exail-absolute-quantum-gravimeters-delivered-to-tenerife-for-advanced-volcano-monitoring); [optics.org](https://optics.org/news/exail-quantum-gravimeters-delivered-to-tenerife-for-volcano-monitoring); [Exail Q3 2025 release](https://live.euronext.com/en/products/equities/company-news/2025-10-22-activity-3rd-quarter-2025-revenue-growth-18); [Defense News, Jun 2024](https://defensenews.com/global/europe/2024/06/25/armed-with-quantum-sensors-france-eyes-leaps-in-electronic-warfare/)
- EU public tenders exist for "gravimètre quantique absolu", for example a French award on 8 Oct 2025 and a CNRS award on 19 Dec 2025 — [TED notice 239416-2026](https://ted.europa.eu/en/notice/239416-2026/pdf); [TED notice 236489-2026](https://ted.europa.eu/en/notice/236489-2026/pdf)

**Medical magnetometry (OPM-MEG, MCG)**
- Cerca Magnetics (OPM-MEG, UK):
  - 19 systems sold to neuroscience centres in 12 countries, with more than 100% annual sales growth over three years.
  - Buyers are research centres rather than routine clinical hospitals.
  - A £3.8M Series A (April 2026) is meant to move it "into clinical applications" with UK/US approvals pending.
  - Sources: [The Quantum Insider](https://thequantuminsider.com/?p=2387185); [Pulse 2.0](https://pulse2.com/cerca-magnetics-3-8-million-series-a-raised-to-advance-opm-meg-brain-imaging-technology-toward-clinical-deployment/)
- SandboxAQ CardiAQ / AQMed (magnetocardiography):
  - Still "an investigational device… not yet cleared or approved by the FDA" per the company's own 2026 materials.
  - More than 200 patients scanned across three hospitals.
  - A Mayo Clinic study of about 150 patients ran 2024–2025.
  - Sources: [SandboxAQ AQMed](https://www.sandboxaq.com/solutions/aqmed); [Fierce Healthcare](https://www.fiercehealthcare.com/ai-and-machine-learning/mayo-clinic-taps-startup-sandboxaq-study-new-tech-quantum-sensing-and-ai)

**NV-diamond, semiconductor inspection, gas imaging**
- Quantum Diamonds announced a €152M investment in a production-scale quantum-diamond chip-inspection facility in Munich (2025). McKinsey cites it as moving sensing "from pilots to industrial scale" — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
- QLM Technology (Bristol spin-out):
  - Single-photon lidar gas-imaging camera for methane leak detection, backed by BP and National Grid among others.
  - A licensed product was trialled at Repsol Sinopec's Flotta terminal (via SLB). No 2025–2026 customer or revenue data found.
  - Sources: [QuantIC case study](https://quantic.ac.uk/technologies/climatechange/headline_818013_en.html); [SLB case study](https://slb.com/resource-library/case-study-with-navigation/sees/sees-lidar-repsol-cs)

### Inferences
- The buyer is overwhelmingly a government or defence prime. Commercial buyers are research labs, observatories and volcanology institutes, buying a few units at a time through public tenders. A solo founder without clearances cannot sell into the largest pocket (defence PNT). Selling to the second pocket (research institutes) needs a hardware product they do not have.
- Two features suggest software can win in sensing:
  - The most interesting "software-only" precedent is SandboxAQ AQNav: it runs on commercial magnetometers plus AI denoising plus anomaly maps.
  - Q-CTRL's value-add is likewise software-defined robustness.
  - Both are heavily funded firms with DoD relationships, not solo operators. The software-plus-data layer is real but is being captured by well-capitalised players with defence access.
- Reselling or distributing quantum sensors is structurally marginal: 2% of companies rank it first, unit volumes are in the tens, and customers need application support and export-control handling. It is a "false good idea" for a zero-capital founder unless tied to one vendor and one under-served region.
- The plausible capital-light niches are:
  1. Business-development and tender-monitoring services sold to the 47-ish sensing vendors, since 36% have no sales and need commercial customers.
  2. Application-specific data analysis on top of public datasets (magnetic anomaly maps, gravimetry time series), sold to geoscience or civil-engineering clients. This needs geophysics credentials.
  3. Grant and SBIR writing for sensing startups, whose funding is 56% government R&D on average.
  None of these is evidenced by a named solo business in the sources.

### Gaps
- No unit or revenue data found for QuSpin (OPM hardware), Element Six, Qnami, QZabre, Bosch Quantum Sensing, SBQuantum, Aquark, Delta g, Nomad Atomics, Qant or Quantum Diamond Technologies (search budget exhausted).
- No public contract value for SandboxAQ's AFWERX TACFI or DIU TQS agreements.
- No evidence found of independent "quantum sensing software/data" boutiques earning revenue, or of commercial airlines paying for MagNav.
- No reliable figure for how much of McKinsey's $2.8–3.1B is legacy atomic-clock revenue (e.g. Microchip, Safran) versus new-entrant revenue.

---

## Q2. Quantum communication (QKD, QRNG, quantum networks): market state, regulator positions, buyers, capital-light niches

### Takeaway
Quantum communication is about a $1.3–1.6B market (2025, McKinsey), driven by state programmes: EuroQCI, China, India, Korea, Japan. Western security agencies (NSA, UK NCSC, ANSSI, BSI, Dutch NLNCSA, Swedish NCSA) explicitly prefer post-quantum cryptography and treat QKD as a niche. No regulator mandates QKD. Buyers are governments, state telecom operators and a few banks running trials. QRNG is the only piece that is commoditised and API-accessible, and it is already offered free or bundled (Cisco Outshift free API; Quantum Dice in Thales HSMs). There is no evidenced capital-light niche in QKD for an uncleared solo founder. QRNG reselling or entropy auditing exists but is thin and commoditised.

### Cited Findings
**Market size**
- McKinsey QTM 2026 (April 2026):
  - Quantum communication market $1.3–1.6B (2025), $3.5–4.6B (2030), $11–15B (2035).
  - QKD is "currently not favored because of regulation, high costs, deployment complexity… and incumbent IP protection."
  - QKD is "recognized as a valuable longer-term and high-assurance complement; however, it is not presently mandated or explicitly scheduled."
  - [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
- McKinsey QTM 2025 put QComm at about $1.2B in 2024 — [McKinsey QTM 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-year-of-quantum-from-concept-to-reality-in-2025)
- Commercial market-research estimates for QKD alone diverge widely, from about $0.6B to about $2.5B for 2025, depending on scope. Low methodological quality. Which figure belongs to which firm was not verified — [MarketsandMarkets](https://marketsandmarkets.com/Market-Reports/quantum-key-distribution-qkd-market-80654677.html); [Credence Research](https://www.credenceresearch.com/report/quantum-key-distribution-market)

**Regulator positions (decisive for demand)**
- Joint position paper by ANSSI (France), BSI (Germany), NLNCSA (Netherlands) and Swedish NCSA, January 2024. QKD:
  - "currently has significant functional limitations and is only suitable for niche use cases";
  - security maturity insufficient;
  - needs dedicated hardware;
  - distance-limited over fibre;
  - "very expensive" (BSI);
  - still depends on classical authentication.
  - PQC should be prioritised.
  - Sources: [ANSSI](https://cyber.gouv.fr/en/publications/jointly-led-international-publications/position-paper-on-quantum-key-distribution/); [BSI](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Crypto/Quantum_Positionspapier.html); [AIVD full text](https://aivd.nl/binaries/aivd_nl/documenten/publicaties/2024/01/26/position-paper-on-quantum-key-distribution/Position+Paper+over+Quantum+Key+Distribution.pdf)
- NSA does not recommend QKD for national security systems and favours PQC as more cost-effective and deployable. UK NCSC does not endorse QKD for government or military use and recommends PQC. Both are reported in secondary or academic sources; the agencies' own pages were not fetched in this session — [IACR ePrint 2025/173](https://eprint.iacr.org/2025/173.pdf); [Laser Focus World](https://laserfocusworld.com/quantum/article/55265521/quantum-problem-and-solution-for-the-next-decade-of-data-security)
- NATO's first quantum strategy urges coordinated PQC adoption "as the essential near term" and "exploration of QKD" — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)

**Deployments and buyers (governments and telcos dominate)**
- EU, Eagle-1:
  - ESA/SES QKD satellite (SITAEL platform, Tesat payload). Earlier slated for "late 2026" on Vega C.
  - An ESA page now says launch is "slated for February 2027".
  - The Commission and ESA are specifying a first-generation EuroQCI constellation building on Eagle-1.
  - Sources: [ESA Eagle-1](https://www.esa.int/Applications/Connectivity_and_Secure_Communications/EAGLE-1); [ESA connectivity page](https://connectivity.esa.int/?p=24469); [EC EuroQCI](https://digital-strategy.ec.europa.eu/en/policies/european-quantum-communication-infrastructure-euroqci); [Tesat paper](https://arxiv.org/html/2505.20838v1)
- China, China Telecom:
  - Reports more than 6.8M quantum-communication subscribers in more than 40 cities (March 2026), with quantum communication its main quantum revenue driver. Independent verification is lacking.
  - Supplier QuantumCTek separately reports more than 6M users of its quantum secure voice/messaging service, so do not add the two figures.
  - May 2025: a hybrid QKD+PQC system with a 1,000 km Beijing–Hefei call, rolling out in 16 cities. Its "Quantum Secret" platform is used by "hundreds" of government agencies and SOEs.
  - Sources: [The Quantum Insider, Mar 2026](https://thequantuminsider.com/2026/03/27/china-telecom-latest-report-flags-quantum-as-a-key-growth-driver-but-scale-remains-uncertain/); [The Quantum Insider, May 2025](https://thequantuminsider.com/2025/05/20/china-telecom-launches-hybrid-quantum-safe-encryption-system-completes-1000-kilometer-secure-call/)
- India:
  - QNu Labs (backed by the National Quantum Mission) demonstrated a 500 km QKD network over existing fibre with Army Corps of Signals access in Rajasthan (Nov 2025).
  - A 1,000 km network was reported in April 2026.
  - NQM budget is ₹6,003 crore over 8 years.
  - Sources: [DST](https://dst.gov.in/startup-supported-dst-under-nqm-demonstrates-500-km-quantum-safe-network); [India Science & Technology](https://www.indiascienceandtechnology.gov.in/stihighlights/national-quantum-mission-advances-1000-km-secure-communication-network); [Drishti IAS](https://www.drishtiias.com/daily-updates/daily-news-analysis/india-demonstrates-500-km-quantum-key-distribution-network)
- Japan uses a hybrid approach: PQC by 2035 plus QKD for point-to-point high-security links, including a planned 600 km intercity network and a SoftBank–Toshiba QKD integration. South Korea plans a 100 km regional quantum network and runs its own PQC standardisation (KPQC) — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
- 2025 milestones McKinsey cites include:
  - ID Quantique's terrestrial intercontinental QKD in Istanbul;
  - Toshiba's coherent QComm over national telecom infrastructure;
  - SpeQtral/Thales Alenia Space satellite-ground entanglement;
  - IonQ (incl. Capella) plans for space-based QKD;
  - Quantum Computing Inc.'s "quantum secure networking" launch at ECOC 2025.
  - [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
- Toshiba (UK):
  - New UK government supply-chain contract (6 Nov 2026), value undisclosed, with BT and Colt, to validate long-distance multi-user network subsystems over 18 months.
  - HSBC joined the BT/Toshiba London commercial quantum-secure metro network in July 2023.
  - Toshiba's 2026 financial-services deck also lists an HSBC trial of quantum protection for AI FX trading and a Wells Fargo QKD proof of concept (Sept 2024).
  - No 2025–2026 bank QKD production contract was found.
  - Sources: [TechRepublic, Nov 2026](https://techrepublic.com/article/news-toshiba-uk-quantum-network-contract-bt-colt-emea/); [Toshiba/HSBC](https://asia.toshiba.com/highlights/english/hsbc-becomes-first-bank-to-join-the-uks-pioneering-commercial-quantum-secure-metro-network/); [Toshiba FS deck 2026](https://asia.toshiba.com/wp-content/uploads/2026/03/Toshiba-Quantum-Technology-for-Financial-services-sector-.pdf)
- ID Quantique is reported to have been acquired by IonQ in 2025. The acquisition filing was not checked in this session — [The Quantum Insider company list](https://thequantuminsider.com/2021/01/11/25-companies-building-the-quantum-cryptography-communications-markets/)

**QRNG / entropy-as-a-service (the only API-native piece)**
- Quantum Dice:
  - "Quantum Entropy-as-a-Service" (QEaaS) with a self-certifying protocol (DISC).
  - Integrated with Thales Luna 7 HSMs as an external entropy source (launched Feb 2025).
  - Presented at MWC 2025 via GSMA Foundry.
  - Sources: [The Quantum Insider, Feb 2025](https://thequantuminsider.com/2025/02/12/quantum-dice-and-thales-offer-qrng-backed-hardware-security-module-for-real-time-security-verification/); [GSMA Foundry](https://www.gsma.com/get-involved/gsma-foundry/gsma_resources/ramy-aboushelbaya-ceo-founder-of-quantum-dice-at-mwc-barcelona-2025/)
- Quside Entropy Core: an on-premises appliance with a REST API (10,000 req/s for 32-byte requests) and NIST SP800-90B certification for its entropy source — [Quside](https://quside.com/product/entropy-core/); [The Quantum Insider tag](https://thequantuminsider.com/tag/quside/)
- Cisco Outshift offers a free QRNG API with an account and API key — [Cisco Outshift](https://outshift.cisco.com/blog/outshift-qrng-api-accessible)
- Fortanix ingests QRNG entropy from Qrypt and Quantum Dice — [Fortanix](https://www.fortanix.com/resources/solution-briefs/independent-quantum-entropy)
- Managed QRNG services are listed on AWS Marketplace (Quantum B msQRNG; Qrypt) — [AWS Marketplace](https://aws.amazon.com/marketplace/pp/B09SFWPDRJ)
- Fraunhofer IPMS launched a rack QRNG plus an online Entropy-as-a-Service platform (June 2026) — [The Quantum Insider, Jun 2026](https://thequantuminsider.com/2026/06/22/fraunhofer-ipms-unveils-quantum-random-number-generator-to-deliver-true-randomness/)
- No market-size figure for QRNG or entropy-as-a-service was found.

### Inferences
- With agencies against QKD, PQC as the mandated path everywhere, and QKD deployed as sovereign state infrastructure (EuroQCI, China, India), QKD integration work goes to telecom operators, defence primes and national champions with security clearances. A zero-capital solo founder has no realistic way in.
- QRNG is already a commodity API (free from Cisco) or a bundled HSM feature. Reselling entropy is close to a non-business. A narrow possibility is "entropy assurance" consulting: helping regulated firms document randomness sources in PQC and crypto-agility programmes (SP800-90B, HSM configuration). That is really a cybersecurity/PQC service. It belongs to the parallel cybersecurity track of the broader study, not to quantum communication.
- Quantum-network simulation software (e.g. for EuroQCI planning) would sell to a few dozen national labs and telcos. It needs deep optics and protocol expertise, and it competes with academic open-source tools and vendor tools. No paid evidence was found.

### Gaps
- Revenue figures for Toshiba QKD, IonQ/IDQ, QuintessenceLabs, Quantum Bridge, KETS, Qunnect and Aliro were not found.
- The NSA and NCSC QKD pages were not fetched directly; positions come from secondary sources.
- EuroQCI national-segment tender values per member state were not found.
- Korea (SK Telecom/SK Broadband) QKD network scale was not found in this session.

---

## Q3. End-user spend: which enterprises disclose quantum budgets, teams, production use or measurable results in 2025–2026, and what surveys say

### Takeaway
Enterprise spend is real but small and concentrated:
- BCG estimates enterprise quantum-computing spend at about $550M in 2025, more than half of total QC spend for the first time.
- McKinsey finds about 33% of 162 analysed customers have QC budgets of at least $10M. The average use-case-development budget is about $6M, and about 19% of QC budgets go to "consultation".
- Survey data from vendor-sponsored studies show 89% hands-on activity but only 13% with any production and 3% at scale.

Named results are mostly pilots or research papers: JPMorgan certified randomness, the HSBC bond-fill prediction (whose authors call the 34% gain unexplained), AstraZeneca–IonQ, BMW–Airbus challenges. Genuine production cases are few and narrow. The ones found are D-Wave hybrid optimisation at Ford Otosan and NTT DOCOMO.

### Cited Findings
**Aggregate spend and budgets**
- BCG (4 June 2026), studying more than 200 large companies plus a biennial survey:
  - Enterprise QC spend about $550M in 2025, more than academia and government combined for the first time.
  - More than 60% of surveyed enterprises spend more than $1M a year, up 11 points since 2022.
  - Software and algorithm share of spend rose from 21% to 40% (2022 to 2024).
  - 100 enterprises ran about 150 proofs of concept by end-2024, 50% more than two years earlier.
  - 92% of top finance/insurance firms, 56% of top healthcare/biopharma and 52% of industrials have begun investing.
  - BCG warns of a "value gap": "concrete applications… remain scarce."
  - [BCG PDF](https://web-assets.bcg.com/pdf-src/prod-live/ceos-need-to-shape-where-quantum-creates-value.pdf); [BCG page](https://www.bcg.com/publications/2026/ceos-need-to-shape-where-quantum-creates-value)
- McKinsey QTM 2026 (customer study conducted in 2025, n=162 customers analysed):
  - Yearly QC budget distribution: 48% under $5M, 19% $5–10M, 26% $10–50M, 7% over $50M (largest $200M).
  - Budget use: 44% use-case development, 19% consultation, 37% other.
  - Average use-case-development budget about $6M; willingness to pay for use cases about $13M.
  - Pain points: immature hardware and software, unclear use cases, talent gap, limited executive buy-in.
  - More than 300 QT customers globally.
  - [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
  - McKinsey's sample is of companies it "analysed", likely skewed to active players.
- McKinsey estimates QC company revenue at $1.1–1.4B (2025), rising to $3.2–4.4B (2028), about 47% a year. Total "QC market" in 2025 is about $15B including investments and big-tech internal funding. Value-chain shares (2025):

  | Segment | Share |
  |---|---|
  | Components | 15–20% |
  | Hardware + operating system | 25–30% |
  | Cloud provisioning | 20–25% |
  | Application software | 20–25% |
  | Technical + consulting services | 8–13% |

  [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)

**Surveys (note sponsor bias)**
- IQM-linked "State of Quantum 2026" (IQM is a hardware vendor, June 2026): 89% of organisations report hands-on activity; 13% report any production deployment, 10% limited production, 3% at scale — [Nasdaq press release](https://www.nasdaq.com/press-release/new-industry-study-finds-quantum-computing-has-entered-capability-era-early-movers)
- QuEra readiness survey (QuEra is a hardware vendor, 291 respondents, 2026):
  - 46% expect flat budgets, 44% increases, 10% decreases.
  - The top budget driver is government mandates and grants, ahead of competitive pressure or successful pilots.
  - [Intelligent CIO](https://www.intelligentcio.com/north-america/?p=53171)
- D-Wave/Censuswide UK survey (D-Wave sponsored, June 2026): 26% say their organisation is "actively adopting"; 39% are piloting — [The Quantum Insider, 3 Jun 2026](https://thequantuminsider.com/2026/06/03/uk-enterprises-quantum-computing-survey/)
- Gartner (4 Aug 2026) predicts no enterprise AI workload at scale will run on quantum hardware through 2028. It says vendors' "quantum AI" claims usually mean hybrid or quantum-inspired techniques, and that classical methods already deliver similar optimisation benefits — [Gartner](https://gartner.com/en/newsroom/press-releases/2026-08-04-gartner-predicts-enterprise-ai-workloads-at-scale-will-not-run-on-quantum-hardware-through-2028)

**Named enterprise disclosures, 2025–2026 (pilot versus production)**
- **JPMorganChase**: Global Technology Applied Research (led by Marco Pistoia) ran certified randomness expansion on Quantinuum H2-56 and certified 71,313 bits (Nature, March 2025). Pistoia says the next step is "to find applications" — this is research. No team budget disclosed — [JPMorganChase](https://www.jpmorganchase.com/about/technology/news/certified-randomness); [Bloomberg, 26 Mar 2025](https://www.bloomberg.com/news/articles/2025-03-26/jpmorgan-says-quantum-experiment-generated-truly-random-numbers)
- **HSBC + IBM** (25 Sept 2025):
  - Claimed "up to 34%" improvement in predicting fill probability for European corporate bond RFQs using IBM Heron, on more than a year of intraday data.
  - The researchers call the gain's magnitude "puzzling and not fully explained"; it needs validation and may not generalise.
  - This is a trial, not production.
  - [HSBC](https://www.hsbc.com/news-and-views/news/media-releases/2025/hsbc-demonstrates-worlds-first-known-quantum-enabled-algorithmic-trading-with-ibm); [The Quantum Insider deeper look](https://thequantuminsider.com/2025/09/28/bond-trading-quantum-bond-trading-a-deeper-look-at-hsbc-and-ibms-bond-trading-study/)
- **AstraZeneca + IonQ + AWS + NVIDIA**: end-to-end hybrid workflow for simulating a drug-synthesis reaction (June 2025) — research/demonstration — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf); [BCG](https://web-assets.bcg.com/pdf-src/prod-live/ceos-need-to-shape-where-quantum-creates-value.pdf)
- **BMW**:
  - Expert team for nearly a decade; formal strategy in 2020; open Quantum Computing Challenge with AWS, then Airbus (2024).
  - Collaborations with Quantinuum, NVIDIA, Classiq and BCG on battery design, system engineering and pricing optimisation.
  - BCG calls BMW an "outlier".
  - [BCG](https://web-assets.bcg.com/pdf-src/prod-live/ceos-need-to-shape-where-quantum-creates-value.pdf)
- **Airbus + BMW + Quantinuum** modelling fuel-cell efficiency — research — [BCG](https://web-assets.bcg.com/pdf-src/prod-live/ceos-need-to-shape-where-quantum-creates-value.pdf)
- **Aramco + Pasqal**:
  - 200-qubit neutral-atom computer installed in Aramco's Dhahran data centre (Nov 2025), with a regional QCaaS platform and training for Saudi engineers.
  - Background: MoU 2022, Aramco's Wa'ed Ventures invested in Pasqal (Jan 2023), agreement 2024.
  - [Aramco](https://www.aramco.com/en/news-media/news/2025/aramco-and-pasqal-make-history-with-saudi-arabias-first-quantum-computer); [HPCwire](https://www.hpcwire.com/off-the-wire/pasqal-and-aramco-launch-qcaas-platform-for-saudi-quantum-computer/)
- **Ford Otosan** (D-Wave hybrid solver via Leap), in production (March 2025): Ford Transit body-shop vehicle sequencing; scheduling time for 1,000 vehicles cut from 30 min to under 5 min. Vendor-reported — [D-Wave press release](https://www.dwavequantum.com/company/newsroom/press-release/in-production-ford-otosan-deploys-vehicle-manufacturing-application-built-with-d-wave-technology/)
- **NTT DOCOMO** (D-Wave), second production application (Q3 2026): tracking-area grouping, with a 65.3% cut in peak location-registration signals and a 7% cut in paging over 333 base stations, about 5 minutes optimisation — [The Quantum Insider, 10 Nov 2026](https://thequantuminsider.com/2026/11/10/d-wave-revenue-rises-21-as-customer-deployments-expand-and-chips-agreement-advances/)
- **BASF** (D-Wave hybrid application for manufacturing workflows) and **North Wales Police** (vehicle-deployment proof of technology), cited in D-Wave Q3 2025 — [Quantum Computing Report](https://quantumcomputingreport.com/d-wave-reports-on-its-q3-2025-financial-results-revenue-doubles-year-over-year-cash-reserves-at-record-high/)
- **Multiverse Computing** (quantum-inspired tensor networks) claims more than 100 customers, including Iberdrola, Bosch, Bank of Canada, Allianz, BBVA, Telefónica and PwC — [Sacra](https://sacra.com/c/multiverse-computing/)
- **BBVA** is a participant in D-Wave's gate-model simulator beta (Oct 2026) — [The Quantum Insider, 10 Nov 2026](https://thequantuminsider.com/2026/11/10/d-wave-revenue-rises-21-as-customer-deployments-expand-and-chips-agreement-advances/)

**Use cases with credible near-term value versus none**
- McKinsey and BCG place the earliest value in chemistry and materials simulation, which needs about 100–200 logical qubits (BCG 2030 baseline about $2.5B market). Optimisation and QML value depends on algorithmic breakthroughs (BCG optimistic scenario about $5B by 2030) — [BCG](https://web-assets.bcg.com/pdf-src/prod-live/ceos-need-to-shape-where-quantum-creates-value.pdf)
- BCG recommends that centres of excellence pursue near-term value "potentially with quantum-inspired algorithms, such as tensor networks running on today's CPUs and GPUs" — [BCG](https://web-assets.bcg.com/pdf-src/prod-live/ceos-need-to-shape-where-quantum-creates-value.pdf)

### Inferences
- The demand pool a small advisory player could address is the "consultation" slice of enterprise QC budgets. Using McKinsey's 19% against BCG's about $550M enterprise spend gives roughly $100M a year globally in 2025. This is an inference combining two different sources and definitions. It is mostly captured by McKinsey, BCG, Accenture, Deloitte, Capgemini, IBM Consulting, and the vendors' own professional services.
- The buyers are about 100–300 large firms, mostly global banks, pharma, automotive/aero and energy majors. They already have internal teams or strategic consultancies, so a solo founder's addressable share is tiny unless they bring rare domain-specific depth (e.g. ex-quant, ex-process chemist).
- The survey signal "budgets flat for 46%, driven by government grants" suggests demand is not accelerating organically. A founder's timing should not assume a 2027 boom.

### Gaps
- No 2025–2026 public budget or team-size disclosures were found for JPMorgan, Goldman, HSBC, BBVA, Crédit Agricole, Moderna, Roche, Boehringer, BASF, BMW, Airbus, VW, DHL, EDF, E.ON, TotalEnergies, NTT or SoftBank (search budget exhausted).
- Capgemini, Deloitte, EY, SAS and Economist Impact surveys were not retrieved.
- No satisfaction or pilot-to-production conversion rate from an independent (non-vendor) survey was found.

---

## Q4. D-Wave and annealing/quantum-inspired optimisation in production: real economics, and whether small integrators make money on Leap or quantum-inspired solvers

### Takeaway
D-Wave is the clearest "production" story, and its whole-company revenue is tiny: $3.7M in Q3 2025 and $4.5M in Q3 2026. It has more than 100 revenue customers, including about two dozen Forbes Global 2000 firms. It is growing low-margin professional services, so the vendor itself competes with integrators. Gross margin fell from 71.4% to 52.9% as services rose. Production deployments are narrow scheduling and telecom-network optimisation (Ford Otosan, NTT DOCOMO). Quantum-inspired solvers (Fujitsu Digital Annealer, Toshiba SQBM+) show reference trials, mostly in Japan. No source found shows a small independent integrator earning meaningful revenue on Leap or on quantum-inspired solvers. Resellers that appear are defence-connected (Davidson Technologies).

### Cited Findings
- D-Wave Q3 2025 (quarter to 30 Sep 2025):
  - Revenue $3.7M (+100% y/y), split $1.8M systems (Jülich upgrade), $1.4M QCaaS, $0.5M professional services.
  - Gross margin 71.4%. Bookings $2.4M, plus more than $12M after the quarter.
  - "In excess of 100 revenue generating customers including nearly two dozen Forbes Global 2000" over the trailing four quarters.
  - Net loss $140M (mostly non-cash warrant charges).
  - Sources: [Business Wire](https://www.businesswire.com/news/home/20251106696544/en); [Quantum Computing Report](https://quantumcomputingreport.com/d-wave-reports-on-its-q3-2025-financial-results-revenue-doubles-year-over-year-cash-reserves-at-record-high/); [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/01/22/d-wave-qbts-q3-2025-earnings-call-transcript/)
- D-Wave Q3 2026 (reported 10 Nov 2026):
  - Revenue $4.5M (+21% y/y); nine-month revenue $10.4M (versus $21.8M).
  - Professional services +$1.5M y/y; QCaaS +$0.8M; systems −$1.5M.
  - Gross margin 52.9% (from 71.4%) "partly because lower-margin professional services made up more of revenue."
  - Remaining performance obligations $38.3M; cash $503.4M; operating expenses $55.9M a quarter.
  - Up to $100M CHIPS Act agreement with Commerce.
  - Advantage2 system installed in Como, Italy, half the capacity financed by Swiss Quantum Technology (€10M over 5 years).
  - No resellers or consultancies mentioned.
  - Sources: [The Quantum Insider, 10 Nov 2026](https://thequantuminsider.com/2026/11/10/d-wave-revenue-rises-21-as-customer-deployments-expand-and-chips-agreement-advances/); [Morningstar/Business Wire](https://morningstar.com/news/business-wire/20261110935432/d-wave-reports-third-quarter-2026-results)
- Production references (vendor-reported):
  - Ford Otosan: 30 min to under 5 min for 1,000-vehicle sequencing; extension to paint shops and assembly planned — [D-Wave](https://www.dwavequantum.com/company/newsroom/press-release/in-production-ford-otosan-deploys-vehicle-manufacturing-application-built-with-d-wave-technology/)
  - Pattison Food Group: workforce-scheduling time fell to 15 h/week, an "80% increase in efficiency" — [D-Wave optimization guide](https://dwavesys.com/media/5d0gxhqk/d-wave-optimization-guide-v3.pdf)
  - NTT DOCOMO: second production application in Q3 2026 — [The Quantum Insider](https://thequantuminsider.com/2026/11/10/d-wave-revenue-rises-21-as-customer-deployments-expand-and-chips-agreement-advances/)
- Channel structure:
  - Davidson Technologies (Huntsville, defence) has been a multi-year reseller since Aug 2022 and hosts an Advantage2 system for US government missions — [HPCwire](https://www.hpcwire.com/off-the-wire/d-wave-and-davidson-technologies-enter-multi-year-reseller-agreement/); [Quantum Computing Report](https://quantumcomputingreport.com/d-wave-reports-on-its-q3-2025-financial-results-revenue-doubles-year-over-year-cash-reserves-at-record-high/)
  - Zapata AI announced an expanded partnership to build generative AI on Leap (July 2024) — [Business Wire](https://businesswire.com/news/home/20240708685316/en/Zapata-AI-D-Wave-Quantum-Announce-Expanded-Partnership). Zapata AI is believed to have ceased operations in late 2024; this was not verified in this session and should be checked, because it would be a direct "false good idea" precedent for a software layer built on annealers.
  - D-Wave runs its own "Leap Quantum LaunchPad" onboarding with "expert project support", i.e. the vendor gives away pre-sales consulting — [D-Wave](https://dwavequantum.com/)
- Fujitsu Digital Annealer: customers listed in manufacturing, finance, pharma, mobility/logistics and government. References include Toyota Systems (production-instruction system at Tsutsumi plant), Kutxabank, Bayer and NYK; SAP has benchmarked it. Offered as cloud and on-premises. The list is from 2024 — [Fujitsu DA explainer, May 2024](https://www.fujitsu.com/global/imagesgig5/Digital_Annealer_Explainer_May2024_New.pdf); [Fujitsu UK](https://www.fujitsu.com/uk/imagesgig5/Quantum-Inspired-Computing.pdf)
- Toshiba SQBM+:
  - Version 2.2 supports up to 1 billion variables (June 2026), targeting finance, drug discovery and logistics.
  - Past references are validations: high-frequency trading, drug discovery, and TOPPAN Digital warehouse picking (2024).
  - Available on Azure Quantum.
  - Sources: [AFPBB (Toshiba release, Japanese)](https://www.afpbb.com/articles/fp/3641170); [Azure blog, 2022](https://azure.microsoft.com/en-us/blog/quantum/2022/06/27/toshiba-launches-new-sqbm-quantum-inspired-optimization-provider-on-azure-quantum/)
- BQP (IBM Ventures-backed) sells the BQPhy quantum-inspired engineering/logistics solver on HPC/GPU. Only the optimisation solver is in commercial use, and its quantum-advantage claims are not demonstrated on hardware — [TechRepublic](https://techrepublic.com/article/news-ibm-ventures-bqp-quantum-inspired-computing/)

### Inferences
- The production economics are small. D-Wave's entire QCaaS line is about $1.4–2.2M a quarter globally. Integrator margin on top of that, for a third party, would be tiny. And D-Wave is actively expanding its own professional services, which pushed its gross margin down, so it is competing with would-be integrators.
- The documented production wins (car sequencing, workforce scheduling, telecom tracking areas) are classical operations-research problems. Gurobi, OR-Tools or GPU heuristics could plausibly address them; no independent benchmark versus Gurobi was found in this session. So a small firm's real value is OR modelling expertise, not quantum access. The "quantum" layer adds vendor-credit marketing value but little technical moat.
- Fujitsu and Toshiba sell through their own large SI arms, so there is no visible channel for small integrators outside Japan.

### Gaps
- No independent benchmark (e.g. versus Gurobi or CPLEX) for the Ford Otosan or NTT DOCOMO problems was found.
- No data on D-Wave partner-programme revenue shares, or on Quantagonia, Kipu Quantum, Jij or Staque revenues (searches returned nothing relevant).
- The contract value of the "Fortune 100 $10M two-year QCaaS" deal and its date were not verified (title only) — [Barchart](https://www.barchart.com/story/news/37251495/d-wave-announces-10-million-two-year-enterprise-qcaas-agreement-with-fortune-100-company)

---

## Q5. "Quantum-enabled but classical-today" products sold by small firms; is the "quantum" label an asset or a liability with enterprise buyers in 2026?

### Takeaway
The strongest commercial evidence of a "quantum-inspired, classical-today" product is Multiverse Computing. It pivoted from quantum finance tools to tensor-network compression of AI models (CompactifAI): about €11M recognised revenue in 2025 and about €100M ARR claimed by January 2026 (Sacra estimates), with $570M raised in its Series C. It succeeded by selling an AI-cost-reduction outcome, not "quantum". In 2026 analysts (Gartner) explicitly warn that "quantum AI" claims usually mean classical or hybrid techniques. So the label helps get meetings with innovation teams and grant bodies, but it is a liability with procurement and operational buyers unless the product shows classical ROI on its own.

### Cited Findings
- Multiverse Computing:
  - FY2025 recognised revenue about €11.1M (Sacra estimate), from about €2.8M in 2024. CB Insights instead lists $1.4M for 2024, so the base is disputed.
  - About €100M ARR in January 2026 (Sacra), explained by late-2025 enterprise and OEM contracts.
  - Company claims annualised revenue grew more than 10x since its June 2025 Series B and Q1 2026 sales were 96x y/y.
  - €189M Series B (June 2025); $570M Series C at a $1.7B pre-money valuation.
  - Sources: [Sacra](https://sacra.com/c/multiverse-computing/); [CB Insights](https://www.cbinsights.com/company/multiverse-computing/financials); [HPCwire, Jun 2025](https://www.hpcwire.com/aiwire/2025/06/12/multiverse-computing-closes-e189m-series-b-to-scale-compactifai-deployment/); [IT Brief](https://itbrief.co.uk/story/multiverse-computing-raises-usd-570-million-in-series-c)
- Gartner (4 Aug 2026): "quantum AI" vendor claims usually mean hybrid or quantum-inspired techniques; classical methods already deliver similar optimisation benefits; no enterprise AI workload at scale on quantum hardware through 2028 — [Gartner](https://gartner.com/en/newsroom/press-releases/2026-08-04-gartner-predicts-enterprise-ai-workloads-at-scale-will-not-run-on-quantum-hardware-through-2028)
- BQP: only its classical optimisation solver is in commercial use; claims of quantum advantage should not be read as hardware-demonstrated — [TechRepublic](https://techrepublic.com/article/news-ibm-ventures-bqp-quantum-inspired-computing/)
- Deloitte frames quantum-inspired methods as near-term "milestones" in a quantum programme, not a replacement — [Deloitte Insights](https://www.deloitte.com/us/en/insights/topics/technology-management/quantum-computing-readiness.html)
- BCG recommends tensor-network, quantum-inspired methods on CPUs/GPUs for near-term value inside a COE — [BCG](https://web-assets.bcg.com/pdf-src/prod-live/ceos-need-to-shape-where-quantum-creates-value.pdf)
- Vendor-friendly promotional content (e.g. Qutwo "10–80x speedup") cites no clear primary source — [byteiota](https://byteiota.com/qutwo-builds-quantum-infrastructure-before-quantum-works/). This illustrates the hype risk.

### Inferences
- The label "quantum" is mainly an asset in three settings:
  1. Corporate innovation/CTO-office budgets, which still exist: 56% of large companies invest per BCG.
  2. Public grant and sovereign programme funding.
  3. Fundraising.
- It is a liability when selling to operations or procurement, who will benchmark against Gurobi, GPUs or plain ML, and where Gartner now primes skepticism.
- For a zero-capital founder using AI agents, the defensible version of "quantum-ready optimisation" is to sell classical or GPU-accelerated optimisation outcomes, with optional QPU or annealer back-ends as an R&D option. "Quantum" becomes a secondary story, not the value proposition.
- Multiverse's success came from riding the AI-inference-cost wave with large capital ($215M plus $570M). A solo founder cannot replicate model-compression R&D at that scale. Smaller tensor-network consulting for AI cost reduction would compete with open-source quantisation and pruning tools.

### Gaps
- No revenue data for Quantagonia, Kipu Quantum, Classiq, Qubit Pharmaceuticals, Terra Quantum or small "quantum-ready" optimisation SaaS firms.
- No buyer-side survey on how "quantum" branding affects enterprise purchasing.

---

## Q6. Sector-specific compliance or readiness mandates that create forced demand outside pure cybersecurity

### Takeaway
The only quantum-related mandates with real timelines are post-quantum cryptography migrations. Examples include US federal 2030, EU high-risk by 2030 and full by 2035, UK NCSC high-risk by 2031 and full by 2035, G7 financial sector 2030–32 for critical systems with 2035 as the outer horizon, and Japan/Korea 2035. They are cybersecurity mandates and largely non-binding for the private sector:
- The G7 roadmap states it "does not establish regulatory expectations".
- Italy's agency confirms the June 2026 G7 statement sets no statutory deadline.

No mandate was found that forces purchases of quantum sensing, QKD or quantum computing. Defence quantum-PNT programmes (DIU TQS, DARPA RoQS, the DoW ISR initiative) create procurement demand but only for cleared defence suppliers. Insurance/actuarial and ESG mandates on quantum were not found.

### Cited Findings
- Europol Quantum Safe Financial Forum "call to action" (Feb 2025): urges financial institutions to prioritise transition to quantum-safe cryptography, citing "store now decrypt later" — [Europol](https://europol.europa.eu/media-press/newsroom/news/call-for-action-urgent-plan-needed-to-transition-to-post-quantum-cryptography-together)
- A follow-up Europol/FS-ISAC risk-prioritisation report is reported for January 2026. The date was not verified at the source — [PostQuantum.com](https://postquantum.com/security-pqc/europol-pqc-financial-services/)
- G7 Cyber Expert Group (January 2026):
  - Coordinated PQC roadmap for the financial sector in six phases.
  - Explicitly "does not establish regulatory expectations".
  - 2035 is cited as the completion target.
  - Sources: [US Treasury PDF](https://home.treasury.gov/system/files/136/G7-CEG-Quantum-Roadmap.pdf); [gov.uk](https://www.gov.uk/government/publications/advancing-a-coordinated-roadmap-for-the-transition-to-post-quantum-cryptography-in-the-financial-sector); [Orrick](https://infobytes.orrick.com/2026-01-29/g7-cyber-expert-group-releases-roadmap-for-post-quantum-cryptography-transition-in-financial-services/)
- A G7 "Key considerations for financial sector participants" note followed (May 2026) — [Banque de France PDF](https://www.banque-france.fr/system/files/2026-05/G7_Key_Considerations_for_Financial_Sector%20Participants_May_2026.pdf)
- Banca d'Italia (June 2026): Italy's agency (ACN) signed the G7 joint migration statement; it gives guidance "but does not establish a separate Italian statutory migration deadline" — [Banca d'Italia](https://www.bancaditalia.it/media/notizia/the-g7-cyber-expert-group-publishes-the-roadmap-for-the-transition-of-the-financial-sector-to-post-quantum-cryptography/17.G7CybersecurityWorkingGroup%20JointMigrationStatement(June2026)Italy'sNationalCybersecurityAgency,ACN,isasignatorytothisjointpublication.Itprovidescommonpreparationguidance,butdoesnotestablishaseparateItalianstatutorymigrationdeadline./)
- ANSSI, chairing the G7 Cybersecurity Working Group under France's 2026 presidency, led a "Preparing for the post-quantum era: a call to action" with G7 agencies, supported by the EU Commission and ENISA — [ANSSI](https://cyber.gouv.fr/en/publications/jointly-led-international-publications/preparing-for-the-post-quantum-era-a-call-to-action/)
- Government PQC timelines collected by McKinsey (April 2026):
  - US federal full adoption by 2030 (CISA/NSA product-category lists).
  - EU high-risk use cases (water, energy, healthcare, finance, transport) by 2030, full by 2035.
  - UK NCSC high-risk by 2031, complete by 2035.
  - Japan government by 2035.
  - South Korea 2035 with pilots through 2028.
  - China a sovereign track.
  - [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
- India's DST published a post-quantum migration task-force report (4 Feb 2026). Only the title was seen — [DST PDF](https://dst.gov.in/sites/default/files/Report_TaskForce_PQMigration_4Feb26%20%28v1%29.pdf)
- QuEra's survey finds government mandates and grants are the top driver of enterprise quantum budgets — [Intelligent CIO](https://www.intelligentcio.com/north-america/?p=53171)
- Defence demand signals (procurement, not civilian mandates): DIU TQS (18 vendors), DARPA RoQS (Q-CTRL A$38M), DoW quantum-sensing ISR initiative (up to about $200M, June 2026) — [Breaking Defense](https://breakingdefense.com/2025/03/diu-to-start-field-testing-quantum-sensors-in-tough-conditions); [Q-CTRL](https://q-ctrl.com/blog/darpa-selects-q-ctrl-to-develop-next-generation-quantum-sensors-for-navigation-on-advanced-defense-platforms); [The Quantum Insider](https://thequantuminsider.com/2026/06/24/department-of-war-announces-initiative-to-revolutionize-isr-via-quantum-sensing/)
- McKinsey QTM 2026 includes an energy/ICT section citing ICT-sector electricity data (Malmodin et al., 2024). No mandate is attached — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)

### Inferences
- "Forced demand" in quantum exists only on the PQC side, and is only quasi-forced: regulators set expectations and dates, but the G7 roadmap is not binding. Paid demand will come from supervisory pressure, audit findings and DORA-style operational-resilience reviews, not from quantum-specific law. That sits squarely in the cybersecurity track of the wider study.
- Outside cybersecurity, the nearest thing to a mandate is GNSS-resilience pressure in aviation, maritime and critical timing. That is driven by jamming and spoofing, not quantum, and procurement goes to established avionics and timing primes (Honeywell, Safran, Infleqtion). A small player could at most sell "PNT-resilience assessments", which need aviation or maritime credentials. No paid evidence for such quantum-specific assessments was found.

### Gaps
- Not found (search budget exhausted):
  - actuarial or insurance treatment of quantum risk (e.g. Lloyd's, EIOPA, NAIC);
  - telecom-operator requirements (e.g. GSMA PQTN obligations);
  - specific UK MoD, NATO or EU aviation (EASA) quantum-PNT procurement requirements;
  - ESG or energy rules on quantum data centres.
- Whether the ECB, FCA, MAS or SEC have issued binding PQC expectations beyond the G7 guidance was not verified.

---

## Q7. Emerging-market and regional angles: paid demand for ecosystem-building, local distribution, training or programme design?

### Takeaway
About $55B in national public quantum funding had been announced cumulatively by 2025 (McKinsey). Outside the US, EU, China, Japan, India and Korea the sums are small:
- Qatar $150M
- Israel about $0.7B
- Singapore about $0.4B
- Brazil about $17M
- Philippines about $17M
- Thailand about $6M
- South Africa about $3M

Gulf demand exists but comes bundled with hardware vendor deals. Aramco–Pasqal included training and QCaaS; WEF produced a Saudi "quantum economy blueprint". Established intermediaries (The Quantum Insider with ITU, the big consultancies, vendors) sell national-strategy work, priced case by case. No public tenders for ecosystem-building services in Africa, Latin America or the Gulf were found.

### Cited Findings
- McKinsey QTM 2026 map of announced national investments (to 2025, "estimated and directional"):

  | Region | Announced (approx.) |
  |---|---|
  | China | $15.3B |
  | Japan | $9.2B |
  | US | $6.0B |
  | South Korea | $2.4B |
  | France | $2.2B |
  | India | $1.7B |
  | Netherlands | $1B |
  | Spain | $1B |
  | Australia | $0.8B |
  | Israel | $0.7B |
  | Singapore | $0.4B |
  | Taiwan | $0.3B |
  | Qatar | $150M |
  | New Zealand | $37M |
  | Brazil | $17M |
  | Philippines | $17.2M |
  | Thailand | $6M |
  | South Africa | $3M |

  The map also shows entries of about $5.2B and about $1.5B whose country labels could not be recovered from the PDF text extraction (probably large European countries, not verified). Total about $55B. Saudi Arabia's $6.4B (2022) future-tech investment is excluded for lack of a quantum breakdown, as are Qatar QIA's and Bpifrance's investment in Alice & Bob — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
- OECD: as of Nov 2025, 18 OECD countries plus the EU have national quantum strategies — [OECD, Dec 2025](https://www.oecd.org/en/publications/2025/12/an-overview-of-national-strategies-and-policies-for-quantum-technologies_33a0b249.html)
- Chile released a draft National Quantum Technologies Strategy 2025–2035 for consultation (2025), per search-result summary. The primary government page was not fetched — [OECD overview](https://www.oecd.org/en/publications/an-overview-of-national-strategies-and-policies-for-quantum-technologies_5e55e7ab-en.html)
- Saudi Arabia: WEF "Quantum Economy Blueprint" supports building a national ecosystem — [WEF](https://www.weforum.org/stories/emerging-technologies/quantum-economy-blueprint-saudi-arabia/). Aramco–Pasqal includes training programmes and joint research for Saudi engineers plus a QCaaS platform — [Aramco](https://www.aramco.com/en/news-media/news/2025/aramco-and-pasqal-make-history-with-saudi-arabias-first-quantum-computer); [HPCwire](https://www.hpcwire.com/off-the-wire/pasqal-and-aramco-launch-qcaas-platform-for-saudi-quantum-computer/)
- QED-C sensing survey: 0% of the 47 respondent sensing companies are headquartered in Latin America or the Middle East/Africa — [QED-C 2026](https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/)
- The IYQ activity map shows North America and Europe "largely outnumber" Latin America, Africa and Asia in activities. Quantum activity is underway in G-77 states from Brazil to South Africa — [IViR "Quantum Computing and the G-77"](https://www.ivir.nl/publicaties/download/Quantum-Computing-and-the-G-77.pdf)
- Intermediaries already selling:
  - The Quantum Insider sells national quantum strategy consulting, with pricing "scoped individually" — [TQI](https://thequantuminsider.com/quantum-computing-consulting/national-quantum-strategy/)
  - With ITU it launched a "Quantum World Tour" ecosystem series — [TQI/ITU](https://thequantuminsider.com/?p=2379504)
  - Avasant offers quantum strategy advisory — [Avasant](https://avasant.com/what-we-do/advisory-for-quantum-computing/)
  - Qureca offers business intelligence, training and tech scans — [TQI consulting guide](https://thequantuminsider.com/guides/quantum-computing-consulting-firms/)
- India's National Quantum Mission (₹6,003 crore over 8 years) funds domestic startups (e.g. QNu Labs) rather than foreign intermediaries — [DST](https://dst.gov.in/startup-supported-dst-under-nqm-demonstrates-500-km-quantum-safe-network); [Drishti IAS](https://www.drishtiias.com/daily-updates/daily-news-analysis/india-demonstrates-500-km-quantum-key-distribution-network)
- Helium supply risk (Qatar is a major helium exporter) is an emerging-market and geopolitical angle. India's IDSA published a "helium shock" brief on its quantum ambitions — [IDSA](https://idsa.in/publisher/issuebrief/a-helium-shock-to-indias-quantum-technology-ambitions)

### Inferences
- Paid demand for programme design and ecosystem services in emerging markets is real but:
  1. concentrated in the Gulf and a few Asian states with money;
  2. procured through tenders or relationships favouring big consultancies, multilaterals (WEF, ITU, World Bank) or vendors who bundle training into hardware deals;
  3. tiny in Africa and Latin America (Brazil about $17M, South Africa about $3M in total announced public funding).
- A solo founder could plausibly sell low-ticket training and curriculum content, or act as a local representative or lead-generator for a European vendor in a region the vendor cannot staff. Time to revenue is long (6–18 months is typical for government procurement; this is an inference, not sourced). Credibility, local presence and references are prerequisites.
- AI agents help with producing tailored strategy documents and market scans. They do not solve the relationship and procurement barriers.

### Gaps
- No tender values were found for national quantum strategy or ecosystem consulting (ChileCompra, Saudi Etimad, the World Bank and other development banks were not searched).
- No data on UAE (TII) or Qatar (QC2) programme procurement.
- Eastern Europe and Southeast Asia (Thailand, Malaysia, Vietnam) programmes were not examined.

---

## Q8. Quantum infrastructure siting and operations: demand from data centres, HPC centres and colocation providers; advisory or brokerage roles?

### Takeaway
Colocation of quantum computers is a real but low-volume activity:
- Equinix hosts OQC (Tokyo), Alice & Bob, Quantinuum and Diraq (Sydney).
- Digital Realty markets quantum-AI hosting.
- HPC centres (EuroHPC, Jülich, RIKEN) host on-premises systems.
- Aramco hosts Pasqal in Dhahran.
- D-Wave systems sit at Davidson and in Como.

Requirements are specific but manageable by data-centre engineers: about 15–20 kW per QPU and cooling system, helium compressors, seismic isolation and oxygen-depletion detection. The Open Compute Project published integration guidance in May 2026. Deal counts are in the dozens a year, and vendors and operators handle siting directly, so independent brokerage or advisory has no evidenced paid demand. Helium-3 scarcity is a strategic issue but is not accessible to a zero-capital broker.

### Cited Findings
- Equinix:
  - Hosts OQC's system in TY11 Tokyo (target go-live autumn 2023).
  - Lists Alice & Bob, OQC and Quantinuum as quantum hosting customers (Jan 2026).
  - In the Diraq Sydney deployment, Equinix owns power, cooling, security, connectivity and facility operations; Diraq owns the quantum system.
  - Sources: [Data Center Frontier](https://www.datacenterfrontier.com/colocation/article/33001720/equinix-will-host-a-quantum-computer-in-its-tokyo-colocation-center); [Equinix blog, 27 Jan 2026](https://blog.equinix.com/blog/2026/01/27/what-does-enterprise-ready-quantum-computing-look-like/)
- Facility requirements:
  - Each QPU plus cooling needs about 15–20 kW, mostly six 9 kW water-cooled helium compressors.
  - Oxygen detectors are needed for leaks or boil-off.
  - Seismic requirements were a challenge in Tokyo.
  - [DCD analysis](https://datacenterdynamics.com/en/analysis/when-data-centers-meet-quantum-computers)
- Digital Realty lists specialised cooling, vibration isolation, EM shielding, dedicated power circuits and environmental controls as typical needs — [Digital Realty](https://www.digitalrealty.com/about/projects/quantum-ai)
- The Open Compute Project published a white paper on integrating quantum processors into data-centre infrastructure (May 2026) — [OCP blog](https://www.opencompute.org/blog/what-will-it-take-to-deploy-a-quantum-computer-within-a-data-center)
- A DCD opinion piece argues colos and wholesalers should start courting quantum customers, which implies demand is still nascent — [DCD opinion](https://datacenterdynamics.com/en/opinions/its-time-for-colos-and-wholesalers-to-start-looking-at-quantum-computing-customers)
- The Quantum Insider ran "From Lab to Live: practical realities of deploying quantum computing at data-centre scale" (19 Nov 2026) — [The Quantum Insider](https://thequantuminsider.com/2026/11/19/from-lab-to-live-inside-the-practical-realities-of-deploying-quantum-computing-at-data-center-scale/)
- McKinsey (April 2026): vendors are moving quantum hardware closer to HPC clusters (IBM Quantum System Two, RIKEN–Fujitsu, IQM inside EuroHPC sites). Cloud platforms (AWS Braket Hybrid Jobs, Azure Quantum) "reduce the need for dedicated on-site infrastructure." Quantum is "an accelerator, not a stand-alone system" — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
- Helium-3 and cryogenics:
  - Terrestrial helium-3 output is about 22,000–30,000 litres a year (2025 Lowy Institute synthesis cited by PostQuantum), shared with medical imaging, neutron detection and fusion.
  - Interlune cites about $20M/kg.
  - A large dilution fridge holds about 40 litres of He-3 (about $100k).
  - Fridges cost about $0.7–1M (small) to $5–10M (largest), with 6–12-month lead times.
  - These are estimates from a vendor-oriented guide — [PostQuantum](https://postquantum.com/quantum-systems-integration/helium-3-quantum-computing/)
- Chinese mass production of dilution refrigerators could tighten He-3 (Jan 2026 report) — [pulse.bot](https://www.pulse.bot/quantum/news/china-reports-mass-production-of-dilution-refrigerators-is-a-global-he-3-shortfall-coming-4d16ccf7-cbac-4d4a-ade7-6da311d75787)
- Supply-chain chokepoints in quantum are covered in [War on the Rocks, Oct 2025](https://warontherocks.com/2025/10/the-supply-chain-chokepoints-in-quantum/)
- McKinsey flags specialised lasers and optics as the largest supply-chain bottleneck risk, alongside RF control and cryogenics/vacuum — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
- On Qatari helium and the 2026 US–Iran conflict, former OQC CEO Ilana Wisby says the helium-4 and helium-3 supply chains are distinct, which limits the immediate impact — [Verdict](https://www.verdict.co.uk/us-iran-war-will-Helium-shortages-risk-major-disruption-to-quantum-computing-companies/)

### Inferences
- The number of quantum systems placed in third-party data centres worldwide is in the tens. Each placement is negotiated directly between a well-funded vendor and a large operator with in-house engineering. An independent "quantum siting broker" would have perhaps a handful of potential deals a year. Facility-engineering liability and credentials (M&E, cryogenic safety) are required. This is a false good idea for a zero-capital founder.
- The more scalable adjacent opportunity, hybrid HPC–QPU orchestration software, is being built by NVIDIA (CUDA-Q), AWS, Microsoft, IBM and the hardware vendors. Hardly a solo-founder space.
- Helium brokerage needs capital, licences and supplier relationships; it is unrealistic.

### Gaps
- No count was found of quantum systems in colocation or HPC centres worldwide, or of hosting prices per rack or per kW.
- Not checked: specific HPC-centre tenders for "quantum integration services" (e.g. EuroHPC JU quantum procurement lots).

---

## Q9. Candidate capital-light roles: evidence of payment, competitors, credentials, time to first revenue, and the strongest "false good idea" reason

### Takeaway
None of the adjacent quantum technologies offers a clearly validated, solo-friendly, zero-capital niche with evidence of people paying small providers. The least-bad options, roughly ranked:
1. Domain-specific quantum-readiness and use-case translation advisory for one vertical where the founder has credentials (finance, chemistry, logistics OR). Budgets do earmark about 19% for consultation, but incumbents dominate.
2. Commercial and business-development services (lead generation, tender and grant monitoring, SBIR/EU grant writing) sold to cash-poor quantum sensing and communication startups.
3. Classical/GPU optimisation consulting with a "quantum-ready" option, where real value is OR expertise and the quantum label is secondary.
4. Training and content for emerging-market programmes, as subcontractor or local partner to a vendor.

Roles that are unrealistic without capital, clearances or regulatory approvals:
- quantum PNT for defence;
- QKD integration;
- medical OPM-MEG/MCG services;
- sensor distribution at scale;
- quantum-computer siting and brokerage;
- helium brokerage.

The PQC-migration opportunity is the only one with quasi-mandated demand; it belongs to the study's cybersecurity track.

### Cited Findings (evidence base per role; see also Q1–Q8)

**Role A — Vertical quantum-readiness / use-case translation advisory (e.g. for banks, chemicals, logistics)**
- Evidence that people pay:
  - About 19% of enterprise QC budgets go to "consultation"; the average use-case-development budget is about $6M; willingness to pay for use cases is about $13M (McKinsey, 2025 customer study) — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
  - Enterprise QC spend is about $550M (2025), with more than 60% spending over $1M. BCG says enterprises lack "translational capability" and that a "value gap" exists — [BCG](https://web-assets.bcg.com/pdf-src/prod-live/ceos-need-to-shape-where-quantum-creates-value.pdf)
  - Technical and consulting services are 8–13% of the QC value chain and are "expected to have significant educational role", often bundled by full-stack vendors — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
- Competitors:
  - McKinsey, BCG (which co-works with BMW), Accenture, Deloitte, Capgemini, Avasant, The Quantum Insider advisory, Qureca — [TQI consulting guide](https://thequantuminsider.com/guides/quantum-computing-consulting-firms/); [Avasant](https://avasant.com/what-we-do/advisory-for-quantum-computing/)
  - Vendors' own professional services, e.g. D-Wave's growing services line and its free LaunchPad — [The Quantum Insider, Nov 2026](https://thequantuminsider.com/2026/11/10/d-wave-revenue-rises-21-as-customer-deployments-expand-and-chips-agreement-advances/)
- Market-size claims for "quantum consulting services" ($4.5B in 2024 to $25B in 2035, MRFR) are unverified and implausibly large next to McKinsey and BCG figures — [MRFR](https://www.marketresearchfuture.com/reports/quantum-computing-consulting-services-market-67643)
- The only small-firm revenue datapoint found was a tracker showing about $100K revenue in 2025 for a firm called Quantum Consulting (quantumconsulting.ai), from a low-reliability third-party source — [Latka](https://getlatka.com/companies/quantumconsulting.ai)
- Credentials: credible domain background (PhD, quant, process chemistry, OR) plus quantum-algorithm literacy. Enterprise procurement favours brands.
- Time to first revenue (inference): 3–9 months via network or speaking, if the founder has a reputation; otherwise long.
- False good idea: the ~$100M/yr consultation pool (inference) is spread across about 100–300 buyers, who already use incumbents or get free vendor support. 46% expect flat budgets, and budgets are driven by grants, not results (QuEra) — [Intelligent CIO](https://www.intelligentcio.com/north-america/?p=53171). Gartner primes skepticism — [Gartner](https://gartner.com/en/newsroom/press-releases/2026-08-04-gartner-predicts-enterprise-ai-workloads-at-scale-will-not-run-on-quantum-hardware-through-2028)

**Role B — Go-to-market services for quantum sensing/communication vendors (lead generation, tender/grant monitoring, proposal writing)**
- Evidence of need:
  - 36% of sensing companies had no sales in 2025.
  - 69% rely on government R&D funding (56% of financial input on average).
  - Only 31% have commercial end-user payments.
  - Reseller channels are almost non-existent.
  - [QED-C 2026](https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/)
  - Public tenders for quantum instruments exist on TED (e.g. absolute quantum gravimeters, Oct and Dec 2025) — [TED](https://ted.europa.eu/en/notice/239416-2026/pdf)
  - Defence programmes (DIU TQS, DARPA RoQS, the $200M DoW ISR initiative) issue solicitations — [Breaking Defense](https://breakingdefense.com/2025/03/diu-to-start-field-testing-quantum-sensors-in-tough-conditions); [The Quantum Insider](https://thequantuminsider.com/2026/06/24/department-of-war-announces-initiative-to-revolutionize-isr-via-quantum-sensing/)
- Competitors: market-intelligence incumbents (The Quantum Insider, Quantum Computing Report, GQI, IDTechEx, Yole, QED-C itself); generic grant-writing firms.
- Credentials: none formal for EU/civil tenders. US defence SBIR work requires US persons/ITAR awareness for many topics (inference).
- Time to first revenue (inference): 1–3 months for monitoring or newsletter-type services, if sold to a few vendors.
- False good idea: the customers are mostly cash-poor startups (49% of respondents have total revenue under $15M), so willingness to pay is low and churn high. Incumbent media firms bundle intelligence and advisory. A tender-monitoring agent is easy to copy.

**Role C — "Quantum-ready" optimisation services (classical/GPU solvers first; annealer/QPU back-end optional)**
- Evidence:
  - D-Wave has more than 100 revenue customers and production cases at Ford Otosan, NTT DOCOMO and Pattison — [D-Wave](https://www.dwavequantum.com/company/newsroom/press-release/in-production-ford-otosan-deploys-vehicle-manufacturing-application-built-with-d-wave-technology/); [The Quantum Insider](https://thequantuminsider.com/2026/11/10/d-wave-revenue-rises-21-as-customer-deployments-expand-and-chips-agreement-advances/)
  - Fujitsu and Toshiba quantum-inspired references are mostly validations — [Fujitsu](https://www.fujitsu.com/global/imagesgig5/Digital_Annealer_Explainer_May2024_New.pdf); [AFPBB/Toshiba](https://www.afpbb.com/articles/fp/3641170)
- Competitors: Gurobi, Google OR-Tools, NVIDIA cuOpt (not verified this session), Fujitsu DA, Toshiba SQBM+, BQP, Quantagonia, Kipu, D-Wave professional services, OR consultancies.
- Credentials: operations-research and industrial domain expertise. No quantum credential is strictly needed.
- Time to first revenue (inference): 2–6 months for a scheduling or routing project with an SME, if sold on classical ROI.
- False good idea: the quantum part rarely adds measurable value over classical (Gartner). The vendor (D-Wave) is internalising professional services. The whole annealing QCaaS market is about $1.4–2.2M a quarter. Branding a classical OR consultancy "quantum" may reduce trust with operations buyers. The Zapata AI precedent (believed to have wound down in late 2024; unverified this session) shows the risk of a software layer on immature quantum platforms.

**Role D — Training, curriculum and ecosystem-programme support in emerging markets (as subcontractor or local partner)**
- Evidence:
  - Aramco–Pasqal includes training — [Aramco](https://www.aramco.com/en/news-media/news/2025/aramco-and-pasqal-make-history-with-saudi-arabias-first-quantum-computer)
  - WEF Saudi blueprint — [WEF](https://www.weforum.org/stories/emerging-technologies/quantum-economy-blueprint-saudi-arabia/)
  - ITU/TQI World Tour — [TQI](https://thequantuminsider.com/?p=2379504)
  - TQI sells national strategy consulting — [TQI](https://thequantuminsider.com/quantum-computing-consulting/national-quantum-strategy/)
  - Qatar has $150M of public commitments — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
  - McKinsey lists the talent gap among top customer pain points — [McKinsey QTM 2026](https://conteudos.meo.pt/empresarial/Documentos/Outros/quantum-technology-monitor-2026.pdf)
- Competitors: hardware vendors bundling training (Pasqal, IBM, Quantinuum, IQM), universities, Qureca, TQI, big consultancies, free MOOCs (IBM Qiskit, etc.).
- Credentials: academic or industry credibility, language and local presence; government procurement registration.
- Time to first revenue (inference): 6–18 months for government work; faster for corporate workshops.
- False good idea: budgets in Africa and Latin America are minuscule (South Africa about $3M, Brazil about $17M total public), Gulf deals are vendor-bundled, and free training content is abundant.

**Role E — QRNG / entropy-as-a-service reselling or entropy-assurance consulting**
- Evidence: QRNG APIs exist (Quantum Dice QEaaS with Thales HSM, Quside REST appliance, Fraunhofer EaaS, AWS Marketplace listings) — [The Quantum Insider](https://thequantuminsider.com/2025/02/12/quantum-dice-and-thales-offer-qrng-backed-hardware-security-module-for-real-time-security-verification/); [Quside](https://quside.com/product/entropy-core/); [AWS Marketplace](https://aws.amazon.com/marketplace/pp/B09SFWPDRJ)
- Competitors: Cisco Outshift (free API), Fortanix, Qrypt, Thales, HSM vendors.
- Credentials: cryptography and certification knowledge (SP800-90B, FIPS).
- False good idea: entropy is commoditised (free API from Cisco). Regulated buyers need certified hardware inside their HSM perimeter, not a reseller. No market size found.

**Role F (unrealistic for zero capital or uncleared founders) — quantum PNT integration for defence, QKD integration, medical quantum-imaging services, sensor distribution, data-centre siting and brokerage, helium brokerage**
- Defence PNT requires defence-prime relationships and clearances; awards go to Q-CTRL/Lockheed, Honeywell/Vector Atomic, SandboxAQ, Northrop, Leidos and Anduril — [Breaking Defense](https://breakingdefense.com/2025/03/diu-to-start-field-testing-quantum-sensors-in-tough-conditions); [ASDNews](https://www.asdnews.com/news/defense/2025/07/17/honeywell-awarded-us-government-contracts-develop-quantum-sensorbased-navigation-systems)
- QKD is opposed by NSA, NCSC, ANSSI and BSI and deployed by sovereign telcos — [ANSSI et al.](https://cyber.gouv.fr/en/publications/jointly-led-international-publications/position-paper-on-quantum-key-distribution/)
- Medical: CardiAQ is not FDA-cleared; Cerca is still seeking clinical approvals — [SandboxAQ](https://www.sandboxaq.com/solutions/aqmed); [Pulse 2.0](https://pulse2.com/cerca-magnetics-3-8-million-series-a-raised-to-advance-opm-meg-brain-imaging-technology-toward-clinical-deployment/)
- Distribution: reseller activity is 2% of first-ranked sensing activities; unit volumes are in the tens (Exail more than 20 gravimeters total; Cerca 19 systems) — [QED-C 2026](https://quantumconsortium.org/mp-files/quantum-sensing-market-forecast-2026_1.pdf/); [optics.org](https://optics.org/news/exail-quantum-gravimeters-delivered-to-tenerife-for-volcano-monitoring); [TQI/Cerca](https://thequantuminsider.com/?p=2387185)
- Siting: few deals, negotiated directly by vendors and operators — [Equinix](https://blog.equinix.com/blog/2026/01/27/what-does-enterprise-ready-quantum-computing-look-like/)
- Helium: about $20M/kg He-3 and scarce supply — [PostQuantum](https://postquantum.com/quantum-systems-integration/helium-3-quantum-computing/)

### Inferences
- Relative to the broader study (software, security, support services), the adjacent quantum technologies look weak for a zero-capital founder:
  - The money is mostly government and defence money (sensing, QKD), or large-enterprise innovation money captured by top-tier consultancies and vendors (QC).
  - The production use cases are classical OR problems in disguise.
- The most transferable insight: quantum's strongest forced-demand channel is PQC migration, driven by G7, Europol, NCSC, EU and US timelines. That is a cybersecurity service. The founder's quantum literacy can be a differentiator there, positioned as "quantum-risk readiness for regulated SMEs and mid-caps", rather than a standalone quantum-tech business.
- If the founder still wants a quantum-adjacent business, the most capital-efficient experiment is Role B (go-to-market and tender intelligence for quantum vendors) or Role A in a single vertical where they have prior credibility. Both can be run with AI research agents. Both should be validated with 5–10 paid pilots before committing, given the weak buyer economics shown above (inference).
- AI tools and agents lower the cost of producing strategy reports, tender monitoring and use-case scans. That same fact lowers barriers for competitors and pushes prices down, so a defensible position must rest on domain credibility or exclusive relationships, not on content production.

### Gaps
- No direct evidence (named firm, revenue, client) of a solo or tiny-team business earning steady revenue from quantum-adjacent services in 2025–2026, besides a low-reliability tracker entry (Latka).
- Not found: pricing benchmarks for quantum advisory (day rates, retainer sizes) and conversion rates from quantum PoCs to paid follow-on work.
- Not found: evidence on whether hardware vendors (Q-CTRL, Infleqtion, Exail, Pasqal, D-Wave) run partner, referral or reseller programmes with commissions open to small independent firms; the search budget was exhausted before this could be checked.
