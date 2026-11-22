# Q-Day and digital assets: the transition-driven opportunity (state as of 22 Nov 2026)

Scope note: research done 22 Nov 2026 with a limited web budget (about 35 searches/fetches). Every claim carries its source date. The enterprise PQC migration market (deadlines, CBOM vendors, consulting prices) is deliberately left out because the earlier study (`Meilleure opportunité entrepreneuriale quantique/02_migration_post_quantique.md`) covers it. Many sources are crypto trade press or vendor releases, and they are flagged as such. Conflicts of interest are flagged inline as **[COI]**: Google and IonQ build quantum computers; Project Eleven, BitGo, SEALSQ, Silence Labs and Naoris sell quantum-safe products; Strategy and BlackRock hold or sell BTC exposure. Forecasts for 2027-2041 are labelled **[FORECAST]**. My own reasoning is labelled **[INFERENCE]** and kept in the Inferences subsections.

---

## 1. Q-Day timing: resource estimates, expert surveys, government signals, and the hardware gap

### Takeaway
Breaking Bitcoin/Ethereum's 256-bit elliptic curve (secp256k1) is now estimated to be cheaper than breaking RSA-2048. Google's March 2026 paper gives about 1,200-1,450 logical qubits, under 500,000 physical qubits and roughly 18-23 minutes of runtime. Gidney's May 2025 RSA-2048 estimate was under 1 million physical qubits and under a week. This puts digital assets first in line for Q-Day, not last. Hardware is still 2-3 orders of magnitude short: today's devices have about 100-1,200 physical qubits, and IBM's 2029 Starling target is 200 logical qubits. The 2025 GRI expert survey (published 9 Mar 2026) gives 28-49% odds of a CRQC within 10 years and 51-70% within 15 years. Thin prediction markets put a public break of a Bitcoin key at about 2% by end-2026 and about 12% by end-2027.

### Cited Findings

**Resource estimates (the trend is a steep fall)**
- **RSA-2048, Gidney (Google), arXiv 2505.15917, 21 May 2025:** factoring in under a week with under 1 million noisy qubits. That is a 20x reduction from the 2019 Gidney-Ekerå figure of 20 million. Assumptions: square grid with nearest-neighbour connections, 0.1% gate error, 1 µs surface-code cycle, 10 µs control reaction time. The savings come from approximate modular exponentiation and magic-state cultivation. — [arXiv 2505.15917](https://arxiv.org/abs/2505.15917); [Google Security blog](https://blog.google/security/tracking-cost-of-quantum-factori/); [Google Research page](https://research.google/pubs/how-to-factor-2048-bit-rsa-integers-with-less-than-a-million-noisy-qubits/)
- **secp256k1, Babbush, Zalcman, Gidney, Broughton, Khattar, Neven, Bergamaschi, Justin Drake (Ethereum Foundation) and Dan Boneh (Stanford), "Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities", arXiv 2603.28846, submitted 30 Mar 2026, v2 15 Apr 2026:**
  - Low-qubit variant: under 1,200 logical qubits and under 90M Toffolis. Low-gate variant: under 1,450 logical qubits and under 70M Toffolis.
  - Under 500,000 physical qubits, on superconducting hardware at 1e-3 error with surface code.
  - Full run of about 18-23 minutes. The active phase after the public key is known takes about 9-12 minutes, right at Bitcoin's 10-minute block interval, so "on-spend" mempool attacks become conceivable for fast-clock machines.
  - The circuits were withheld. Google published a zk-SNARK, run in the SP1 zkVM, attesting that circuits with these counts exist. — [alphaXiv abstract](https://www.alphaxiv.org/abs/2603.28846v1); [PostQuantumSecurity.org summary](https://www.postquantumsecurity.org/publications/google_ai_ecc_whitepaper.html) **[COI: Google builds quantum hardware; Drake and Boneh also sit on Coinbase's quantum board]**
- An independent reproduction by Schrottenloher reported about 1,192 logical qubits (space-optimised) and 1,446 (gate-optimised), which supports Google's counts. Luo et al. (July 2026) claim 835 logical qubits. — [PostQuantum.com on the ECC floor](https://postquantum.com/post-quantum/quantum-attack-ecc-circuit-floor/); [PostQuantum.com IonQ analysis](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/)
- **IonQ secp256k1 estimate (70 pages, dated 3 Sep 2026, announced 8 Sep 2026, not peer reviewed):**
  - 19,397 trapped-ion physical qubits, 1,457 logical qubits, about 39M Toffolis.
  - About 25.7 days per attempt, with 63.3% success (Ekerå heuristic) or 40.7% (rigorous bound). Five parallel devices, about 97,000 ions, would give 99.3%.
  - Assumes a two-qubit error of 1e-4 (8.4e-5 has been measured, but only on two ions).
  - IonQ's own roadmap targets 20,000 physical and 1,600 logical qubits in 2028.
  - PostQuantum.com found the memory-failure bound reaches about 89% at 1.5e-4 physical error, so the result is very sensitive to that assumption. The press release said "expected to break" while the paper says "per attempt", and IonQ shares rose about 7% on investor day. — [PostQuantum.com](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/); [The Quantum Insider, 8 Sep 2026](https://thequantuminsider.com/2026/09/08/ionq-estimates-20000-qubit-machine-could-break-bitcoin-secp256k1-26-days/) **[COI: IonQ is a listed hardware vendor]**
- Other 2026 estimates, all from the same PostQuantum.com roundup, Sep 2026:
  - Oratomic/Caltech (Mar 2026): a P-256 attack in a few days on about 26,000 neutral atoms. Cain et al. put the neutral-atom floor at about 10,000. Another source gives 10,000-20,000.
  - Pinnacle architecture (Webster et al.): RSA-2048 on qLDPC codes at about 100,000 qubits.
  - The 2017 reference (Roetteler, Naehrig, Svore, Lauter): about 2,330 logical qubits and about 1.3x10^11 Toffolis, roughly 1,000-2,000x more Toffolis than the 2026 Google figure. — [PostQuantum.com](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/); [Decrypt, 24 Apr 2026](https://decrypt.co/365444/bitcoin-q-day-draws-nearer-quantum-researcher-breaks-simplified-key)
- qLDPC codes from QuEra and Alice & Bob reportedly cut physical-qubit overhead "up to 230-fold" versus rotated surface codes, according to GQI's Q3 2026 State of Play (27 Oct 2026). GQI describes Q-Day timelines for ECC-256 and RSA-2048 as "compressed" but gives no years. — [Quantum Computing Report / GQI](https://quantumcomputingreport.com/gqi-q3-2026-state-of-play-investment-consolidation-accelerating-q-day-horizons-and-the-shift-to-second-generation-architectures/)
- **Largest public ECC break on real hardware:** a 15-bit elliptic-curve key (search space 32,767) broken by Giancarlo Lelli on about 70 qubits of public cloud hardware. It won Project Eleven's 1 BTC Q-Day Prize (24 Apr 2026) and was 512x larger than the previous public demonstration (Sep 2025). 256-bit keys remain "far out of reach". — [CoinDesk, 24 Apr 2026](https://www.coindesk.com/tech/2026/04/24/researcher-wins-1-bitcoin-bounty-for-largest-quantum-attack-on-underlying-tech); [The Quantum Insider](https://thequantuminsider.com/2026/04/24/project-eleven-q-day-prize-quantum-ecc-attack/)
- As of 18 Oct 2026, nobody has publicly factored RSA-2048. — [Tech-Insider (secondary)](https://tech-insider.org/will-rsa-2048-be-factored-before-2040-manifold-market/)

**Wild card: lattice PQC itself**
- In July/Aug 2026, Daniel Simon (described as an Amazon researcher) posted IACR ePrint 2026/1591. It claims a polynomial-time quantum algorithm for the Dihedral Coset Problem that could extend to LWE and approximate SVP, which underpin ML-KEM and ML-DSA.
  - Gupte, Ragavan and Zhandry (ePrint 2026/1693) and a second no-go paper (arXiv 2609.40062) argue it cannot work. Daniel Apon disputed Lemma 3.
  - Simon's 7 Oct 2026 revision still defends the proof.
  - Nothing standardised is broken, and no attack has been costed against any parameter set. — [ePrint 2026/1591](https://eprint.iacr.org/2026/1591); [ePrint 2026/1693](https://eprint.iacr.org/2026/1693); [ePrint 2026/1714](https://eprint.iacr.org/2026/1714); [The Quantum Insider, 6 Aug 2026](https://thequantuminsider.com/2026/08/06/amazon-researcher-claims-quantum-algorithm-could-challenge-pqc-foundations/); [PostQuantum.com](https://postquantum.com/security-pqc/simon-quantum-algorithm-lattice-pqc/)
- GQI's response: lattice assumptions deserve close review, but enterprises should adopt crypto-agility "regardless of any specific rebuttal". — [QCR/GQI, 27 Oct 2026](https://quantumcomputingreport.com/gqi-q3-2026-state-of-play-investment-consolidation-accelerating-q-day-horizons-and-the-shift-to-second-generation-architectures/)

**Expert surveys**
- **GRI/evolutionQ Quantum Threat Timeline Report 2025** (7th edition, by Mosca and Piani, published 9 Mar 2026, 26 experts): a CRQC within 10 years is "quite possible (28-49%)" and within 15 years "likely (51-70%)". The timeline "has accelerated from previous reports". — [GRI](https://globalriskinstitute.org/publication/quantum-threat-timeline-report-2025b/)
- Mosca (via TelecomTV): "a 33% chance that Q-Day will hit us before 2035". In the same survey, a majority of the 22 experts who answered on "under the radar" research thought covert efforts could move the timeline by two or more years. — [TelecomTV](https://www.telecomtv.com/content/security/could-q-day-be-an-existential-threat-to-digital-economies-52754/)
- Presidio Bitcoin (Apr 2026) says "most experts assign a 50% probability to CRQCs emerging by 2030-2035". That is more aggressive than GRI's 28-49% within 10 years, so the two conflict. — [Presidio Bitcoin Quantum Readiness v1, Apr 2026](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)
- Earlier GRI editions (2023 summary and 2024 report) are at [GRI 2024](https://globalriskinstitute.org/publication/2024-quantum-threat-timeline-report/) and [GRI 2023 exec summary](https://globalriskinstitute.org/mp-files/executive-summary-quantum-threat-timeline-report-2023.pdf/). Their numbers were not re-extracted this session (see Gaps).

**Crypto-industry views (the spread is wide)**
- Bernstein (8 Apr 2026): Bitcoin has "roughly three to five years to prepare". It calls quantum a "manageable upgrade cycle" and judges SHA-256 mining not meaningfully vulnerable. — [The Block](https://www.theblock.co/post/396709/bernstein-says-quantum-is-a-manageable-upgrade-cycle-for-bitcoin-not-an-existential-threat); [Cointelegraph](https://cointelegraph.com/news/bitcoin-quantum-risk-3-5-years-bernstein)
- Benchmark (29 Jan 2026): the risk is "long-dated and manageable". — [The Block](https://www.theblock.co/news/regulation/2026-01-29-bitcoins-quantum-risk-long-dated-benchmark-pushes-back-panic-387704)
- CoinShares (Christopher Bendiksen, Feb 2026): a break needs machines about 100,000x more powerful than today's largest, so the threat is "at least a decade away". — [The Block, 8 Feb 2026](https://www.theblock.co/post/388969/coinshares-says-only-10200-btc-face-real-quantum-risk)
- Adam Back (Blockstream, Nov 2025): "no meaningful quantum threat", at least 20-40 years away. Michael Saylor: more than 10 years away. — [Cointelegraph, 23 Jul 2026](https://cointelegraph.com/news/strategy-consortium-15m-quantum-proof-bitcoin); [Cointelegraph on Saylor](https://cointelegraph.com/news/saylor-says-quantum-threat-to-bitcoin-is-more-than-10-years-out-expects-coordinated-global-upgrade-if-risk-emerges) **[COI: large BTC holders]**

**Prediction markets (all thin)**
- **Polymarket**, "Quantum breaks Bitcoin by ___?", opened 8 Apr 2026. It resolves on a public demonstration of deriving a valid private key for an existing Bitcoin address. On 22 Nov 2026: Dec 31 2026 at 2% (volume $2,840) and Dec 31 2027 at 12% (volume $1,512), for $4,352 in total. The FAQ text on the page gives slightly different figures (3% and 14%). — [Polymarket](https://polymarket.com/event/quantum-breaks-bitcoin-by)
- **Kalshi** "first useful quantum computer": "Before 2027" at 6.8% in an undated snapshot. It resolves on RSA-2048 being cracked with Shor *or* certain chemistry targets being simulated, so it is not a pure Q-Day market. A live fetch returned HTTP 429. — [Kalshi](https://kalshi.com/markets/kxquantum/quantum/kxquantum)
- **Manifold** "RSA broken before 2030": about 22% in an undated snapshot. — [Manifold](https://manifold.markets/Dig/will-quantum-computing-break-rsa-en)

**Hardware roadmaps vs requirements**
- IBM Starling (2029, Poughkeepsie): 200 logical qubits and 100M gates on bivariate-bicycle qLDPC codes. Kookaburra in 2026. Blue Jay in 2033+ at about 2,000 logical qubits and about 1B operations. — [IBM roadmap](https://www.ibm.com/quantum-computing/roadmap); [IBM blog](https://www.ibm.com/quantum/blog/large-scale-ftqc)
- Google's public roadmap has six milestones, but its later stages carry no dates or qubit targets. — [Tom's Hardware](https://www.tomshardware.com/tech-industry/quantum-computing/the-future-of-quantum-computing-the-tech-companies-and-roadmaps-that-map-out-a-coherent-quantum-future)
- Today's machines with relevant error rates have "on the order of only 100 to 1000 qubits" (Google, May 2025). A 2026 analysis puts 2026 hardware at about 1,000-1,200 physical qubits. Quantinuum Helios has 98 ions. IonQ's June 2026 qLDPC demonstration used 40 barium ions, with a best logical error near 1% per cycle. — [Google blog](https://blog.google/security/tracking-cost-of-quantum-factori/); [The Quantum Insider, 28 Apr 2026](https://thequantuminsider.com/2026/04/28/why-2026-matters-quantum-security/); [PostQuantum.com](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/)

**Government signals (deadlines, not Q-Day dates)**
- US Executive Order of 22 Jun 2026: KEM deployment for high-value federal civilian assets by 31 Dec 2030 and signature (DSA) migration by 31 Dec 2031. UK NCSC: roadmaps by 2028 and high-priority migrations by 2031. ENISA, ANSSI and BSI are setting PQC certification requirements. — [QCR/GQI, 27 Oct 2026](https://quantumcomputingreport.com/gqi-q3-2026-state-of-play-investment-consolidation-accelerating-q-day-horizons-and-the-shift-to-second-generation-architectures/). The earlier study already covers EO 14412, NIST IR 8547 final (27 Oct 2026) and CNSA 2.0 in detail.
- No government source found in this session names a Q-Day year.

### Inferences
- **[INFERENCE] ECC falls first.** At about 70-90M Toffolis and under 500k physical qubits, or about 20k ions for IonQ, secp256k1, P-256 and probably Ed25519 are now the cheapest high-value targets. They are cheaper than RSA-2048, which needs under 1M qubits and about a week. Blockchains therefore become the most visible "canary" of Q-Day, because a break is publicly observable on-chain, whereas an RSA break against TLS traffic could stay invisible.
- **[INFERENCE] Two kinds of CRQC matter differently.**
  - A *slow* first-generation CRQC (ions or neutral atoms, days per key) threatens only coins whose keys have been exposed for a long time ("at-rest", about 6-7M BTC; see Q2).
  - A *fast* superconducting CRQC (minutes per key) also threatens coins at the moment they are spent ("on-spend").
  - So the first products to sell are the ones that remove at-rest exposure: stopping address reuse, rotating custodian keys, migrating P2PK holdings.
- **[INFERENCE] The gap between roadmaps and requirements.**
  - The logical-qubit requirement for ECC (about 1,200-1,450) is about 6-7x above IBM's 2029 Starling (200) and below Blue Jay (2033+, about 2,000 logical, about 1B operations).
  - Taking IBM's roadmap at face value therefore implies an ECC-capable machine sometime after 2033. Caveat: IBM's "gates" are not the same as Toffolis or T-states.
  - IonQ's roadmap (20k physical / 1,600 logical in 2028) would, by its own paper, suffice for one 26-day attempt per key. That is a vendor-implied 2028. It is heavily discounted for conflict of interest and the history of roadmap slippage.
- **[INFERENCE / FORECAST] Probability by year that a CRQC can break a 256-bit ECC key, synthesised from the sources above.** The weights are mine: survey answers plus a heavy discount on thin markets and vendor roadmaps, with some upward pressure from the 2025-2026 cost collapse.

  | By end of | P(CRQC able to break secp256k1) | Main anchors |
  |---|---|---|
  | 2027 | ~1-3% | Polymarket 2% (2026) and 12% (2027), thin volume; nothing publicly beyond 15-bit keys |
  | 2030 | ~10-20% | Manifold ~22% for RSA by 2030; IonQ 2028 roadmap discounted; IBM 2029 = 200 logical |
  | 2033 | ~20-30% | IBM Blue Jay "2033+"; qLDPC overhead cuts |
  | 2035-2036 | ~30-45% | GRI 28-49% within 10 years; Mosca 33% before 2035 |
  | 2041 | ~55-70% | GRI 51-70% within 15 years |

  Fat tails: a covert CRQC (GRI experts say plausible by 2+ years earlier) or a plateau in error correction (Presidio's physics caveat).
- **[INFERENCE]** The contested Simon paper does not change ECC timing. It does strengthen the case for hash-based signatures (SLH-DSA, SHRINCS, XMSS) in long-lived value stores, and for crypto-agile designs that can swap schemes. Hybrid and agile signing is defensible product territory.

### Gaps
- Gidney 2025's exact logical-qubit and Toffoli counts for RSA-2048 were not extracted.
- No published resource estimate specific to Ed25519 (Solana, Cardano, Aptos, Sui) was found. The IonQ critique notes none exists in IonQ's paper. Oratomic covers P-256.
- GRI 2024 and 2023 headline probabilities were not re-extracted, so the change between years cannot be quantified here.
- No Metaculus Q-Day question was found. The Kalshi page could not be loaded (429).
- No 2026 Quantinuum (Apollo) or Google fault-tolerance dates were found.
- No government statement giving a probability or year for Q-Day was found.

---

## 2. Bitcoin's quantum exposure, the protocol debate, and institutional positions

### Takeaway
Most serious 2025-2026 analyses converge on about 6-7M BTC (roughly 30-35% of supply) exposed "at rest" because their public keys are visible on-chain. About 1.6-1.9M BTC of that is structural (P2PK including Satoshi-era coins, bare multisig, Taproot), and the rest is behavioural (address reuse). Much of the behavioural exposure sits at a few large custodians and exchanges and can be fixed today without any protocol change. The protocol side is still research and drafts:
- BIP-360 (P2MR) was merged as a Draft on 11 Feb 2026.
- BIP-361 (Lopp et al., legacy-signature sunset and freeze) was published in Apr 2026.
- No post-quantum signature BIP exists yet, nothing has activated, and there is no activation timeline.

Institutions have moved from disclosure (BlackRock, 2025) to funding and coordination: Coinbase's board (Jan 2026), Strategy's programme (Feb 2026), and a $15M Bitcoin Security Consortium (Jul 2026).

### Cited Findings

**Exposure estimates (they differ in definition)**

| Source (date) | BTC exposed | Notes |
|---|---|---|
| Project Eleven (Jan 2025) | 6,262,905 | Cited as "the most precise" by Forklog — [Forklog](https://forklog.com/en/chaincode-labs-sizes-up-the-quantum-threat-to-bitcoin/) |
| Chaincode Labs (Milton and Shikhelman/Schickelmann, May 2025, 55 pp.) | 20-50% of supply (~4-10M) | 600k-1.1M BTC in P2PK; migration 76-568 days depending on block space — [Forklog](https://forklog.com/en/chaincode-labs-sizes-up-the-quantum-threat-to-bitcoin/); [Bitcoin Magazine](https://bitcoinmagazine.com/technical/what-happens-to-bitcoin-when-quantum-computers-arrive) |
| Presidio Bitcoin (Apr 2026, data at block 900,000, 6 Jun 2025) | ~6.5M (~1/3 of supply) | Over 2/3 (~4.5M) from address reuse, "concentrated in a small number of large custodians"; 1.72M P2PK coins across ~36,000 addresses — [Presidio PDF](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf) |
| Google / Babbush et al. (Mar 2026) | ~6.9M exposed; ~1.7M in P2PK | — [alphaXiv](https://www.alphaxiv.org/abs/2603.28846v1) |
| Coinbase Independent Advisory Board (21 Apr 2026) | ~6.9M | "Most vulnerable category" — [UCSB](https://cs.ucsb.edu/happenings/announcement/no-quantum-threat-yet-crypto-must-prepare-now-says-coinbase-board-paper-co) |
| Glassnode (20 May 2026) | 6.04M (30.2%) | Structural 1.92M (9.6%): P2PK, bare multisig, P2TR. Operational 4.12M (20.6%): reuse, partial spends, custody practice — [Glassnode](https://research.glassnode.com/measuring-bitcoins-quantum-exposed-supply/) |
| CoinShares (Bendiksen, Feb 2026) | ~1.6M in P2PK (~8%), of which only 10,200 BTC in UTXOs "large enough to cause appreciable market disruption" | The rest is spread over more than 32,000 UTXOs averaging about 50 BTC; argues reuse exposure is "easily mitigated" — [The Block](https://www.theblock.co/post/388969/coinshares-says-only-10200-btc-face-real-quantum-risk) **[COI: BTC fund manager]** |
| Bernstein (Apr 2026) | ~1.7M in early address types | — [The Block](https://www.theblock.co/post/396709/bernstein-says-quantum-is-a-manageable-upgrade-cycle-for-bitcoin-not-an-existential-threat) |

- **Glassnode entity-level exposure (20 May 2026):** exchange balances account for about 1.63-1.66M BTC, roughly 40% of operational exposure. About half of labelled exchange BTC is exposed, versus under 30% of non-exchange supply. By entity: Coinbase ~5%, Binance 85%, Bitfinex 100%, Grayscale ~50%, Fidelity and Cash App ~2%, Robinhood and WisdomTree 100%, sovereign treasuries (US, UK, El Salvador) 0%. — [Glassnode](https://research.glassnode.com/measuring-bitcoins-quantum-exposed-supply/)
- Satoshi-linked coins are commonly estimated at about 1.1M BTC. — [TFTC](https://www.tftc.io/bitcoin-quantum-freeze-satoshi-bip-361-community-split)
- AmericanFortress's funding announcement (May 2026) values exposed BTC at "$483 billion". This is a vendor headline. — [HackerNoon](https://hackernoon.com/americanfortress-raises-$8m-to-defend-the-$483-billion-in-bitcoin-already-exposed-to-quantum-risk) **[COI]**

**Migration capacity**
- Presidio (Apr 2026), from value-weighted UTXO data: with 25% of block space, about 90% of BTC *value* moves in about 4.4 days (~956k UTXOs) and about 98% in about 3.5 weeks (~5.3M UTXOs). With 100% of block space, it takes about 1.1 days and 6.2 days.
  - 97.75% of BTC value sits in 5,267,653 UTXOs, about 3% of 173M UTXOs.
  - The commonly cited 76-305+ / 76-568-day figures count dust UTXOs and so overstate the time needed.
  - The binding constraint is behavioural: wallet upgrades are slow without a forcing function. — [Presidio PDF](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)

**Protocol proposals (status as of Nov 2026)**
- **BIP-360 (P2MR, Pay-to-Merkle-Root; earlier names P2QRH/P2TSH; author Hunter Beast et al.):** merged into the BIP repo as a Draft on 11 Feb 2026, the first quantum proposal to reach that stage.
  - It is a SegWit v2 output with bc1z addresses that keeps Taproot's script tree but removes the key-path spend that exposes the public key.
  - It does not itself add post-quantum signatures.
  - It is not activated, and no activation date is scheduled. One blog projects 2027-2029, which is speculative.
  - BTQ Technologies has a testnet implementation. — [Blockspace](https://blockspace.media/insight/bitcoin-developers-merge-bip-360-in-first-move-to-address-quantum-computing-risks/); [Spark](https://www.spark.money/research/bitcoin-bip-360-quantum-resistant-address-format); [Qubitchain](https://qubitchain.io/blog/bip-360-hardware-wallets-bitcoin-post-quantum-migration-2026); [Q-Day Countdown](https://qdaycountdown.com/crypto/bip-360-and-bip-361/)
- **BIP-361, "Post Quantum Migration and Legacy Signature Sunset"** (Jameson Lopp and five co-authors, 14-15 Apr 2026):
  - Phase A, about 160,000 blocks (~3 years) after activation: no new sends to quantum-vulnerable outputs.
  - Later: legacy signatures invalid, which effectively freezes unmigrated coins including Satoshi's P2PK, about 5 years after activation. A proposed later phase would allow recovery by zero-knowledge proof of the seed phrase.
  - It depends on a post-quantum signature BIP that has not been written yet.
  - Lopp: "I know folks don't like it. I wrote it because I like the alternative even less." He does not expect it to be seriously proposed "unless it looks highly likely that a CRQC is less than 10 years away". — [Spark BIP-361](https://www.spark.money/research/bitcoin-bip-361-quantum-migration-roadmap); [TFTC](https://www.tftc.io/bitcoin-quantum-freeze-satoshi-bip-361-community-split); [Bitcoin.com News](https://news.bitcoin.com/bitcoin-developers-propose-freezing-coins-that-skip-quantum-safe-migration-under-bip-361/); [KuCoin blog](https://www.kucoin.com/blog/bip-361-quantum-migration-freeze-legacy-coins)
- **Other mechanisms, as mapped by Presidio (Apr 2026):**
  - *Hourglass*: rate-limits P2PK spends to one per block.
  - *BitMEX soft-freeze*: turns off all legacy spends, with recovery by zero-knowledge proof of the seed phrase. A proof of concept runs in under a minute on consumer hardware.
  - *P2Q*: keeps Taproot behaviour, with a key path that could later be disabled.
  - *PQC precommitment*: placeholder spend paths, valid today, that a later soft fork activates.
  - *Quantum-Safe Bitcoin (QSB/"Binohash")*: needs no soft fork but costs $75-200 of GPU compute per transaction.
  - *Commit/reveal* migration, plus private mempools such as MARA Slipstream as interim shields; Presidio calls these "centralizing".
  - *Pre-Q-Day hash commitments*, to rescue non-seed P2PK coins.
  - Likely first post-quantum signatures: SHRINCS and SHRIMPS, Bitcoin-tailored SPHINCS+ variants. Blockstream Research deployed a SHRINCS verifier on the Liquid sidechain in Mar 2026. — [Presidio PDF](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)
- **Chaincode Labs "CRQC Response Playbook"** (developed with Bitcoin Core developers): in month 1, prohibit new quantum-vulnerable output types and decide the legacy-coin policy. Around month 6-7, activate a post-quantum signature if none exists. — via [Presidio PDF](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)
- **Developer attention:** the share of bitcoin-dev mailing-list messages on quantum rose from about 5% (2024) to about 50% (2026 through March), out of about 24,073 emails analysed. — [Presidio PDF](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)
- **The "freeze Satoshi" fault line:**
  - Adam Back urges caution about censoring the network.
  - CZ floated freezing with a 6-12-month migration window. Lopp's reply: "not a binary debate".
  - CoinShares opposes burning on property-rights grounds.
  - Presidio calls legacy-coin policy "the likeliest fault line for a fork… resolved by the market", comparing it with the 2017 BCH split.
  - Lopp has also written "Against Allowing Quantum Recovery of Bitcoin". Counter-proposals include QSAVE (escrow) and "Bitcoin Lost and Found" (re-mining vulnerable coins). — [TFTC](https://www.tftc.io/bitcoin-quantum-freeze-satoshi-bip-361-community-split); [The Block/CoinShares](https://www.theblock.co/post/388969/coinshares-says-only-10200-btc-face-real-quantum-risk); [Lopp blog](https://blog.lopp.net/against-quantum-recovery-of-bitcoin/); [QSAVE thread](https://groups.google.com/g/bitcoindev/c/PjpaidcHX4A); [Lost and Found thread](https://groups.google.com/g/bitcoindev/c/YQmrRN0aRvE)

**ETF issuers, treasuries, custodians, exchanges and wallets**
- **BlackRock:** amended the IBIT prospectus on 9 May 2025 to expand the quantum risk factor, with similar language for its ETH ETF. The IBIT 10-Q for the period ended 30 Sep 2026 repeats it and states "no guarantee" that quantum-resistant architectures will be built. Bloomberg's James Seyffart called the disclosure "completely standard". — [The Quantum Insider, 13 May 2025](https://thequantuminsider.com/2025/05/13/blockrock-updates-bitcoin-etf-with-broadened-warning-about-quantum-computing/); [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0001980994/000143774926035539/ibit20260930_10q.htm); [Cointelegraph](https://cointelegraph.com/news/blackrock-flags-quantum-computing-as-risk-for-bitcoin-etfs)
- **Strategy (Saylor):** announced a "Bitcoin Security Program" on its Q4 2025 earnings call (early Feb 2026), covering wallet-security standards, key-management practices and PQC research. It frames the programme as "preventative". — [Yahoo Finance](https://finance.yahoo.com/news/strategy-initiate-bitcoin-security-program-102153710.html); [The Quantum Insider, 12 Feb 2026](https://thequantuminsider.com/2026/02/12/investment-firm-plays-down-near-term-quantum-threats-to-bitcoin-outlines-security-coordination-effort/)
- **Bitcoin Security Consortium (23 Jul 2026):**
  - Led by Strategy with BlackRock as co-lead. Members: Anchorage Digital, ARK Invest, Block, Blockstream, Coinbase, Fidelity Digital Assets and Galaxy.
  - $15M over three years for developers securing Bitcoin against quantum. Mike Schmidt (Brink) coordinates.
  - Galaxy separately pledged up to $5M in grants and formed a quantum advisory council. — [Cointelegraph](https://cointelegraph.com/news/strategy-consortium-15m-quantum-proof-bitcoin)
- **Coinbase:**
  - Formed its Independent Advisory Board on Quantum Computing and Blockchain in Jan 2026: Scott Aaronson, Dahlia Malkhi, Dan Boneh, Justin Drake and others, from Stanford, UT Austin, Bar-Ilan, the Ethereum Foundation and Eigen Labs.
  - The first 50-page position paper (21 Apr 2026) concludes that no CRQC exists yet but preparation "will take years". Mining, hashes and ledger structure are largely safe; the exposure is wallet signatures. Each community should decide early whether to freeze, revoke or leave unupgraded wallets.
  - Coinbase is building PQ-CoreKMS, a post-quantum version of its MPC key-management system.
  - Its blog flags that self-custody users may struggle to manage state for stateful hash-based signatures. — [Fortune, 21 Jan 2026](https://fortune.com/2026/01/21/coinbase-launches-expert-board-to-assess-quantum-computing-threat/); [UCSB](https://cs.ucsb.edu/happenings/announcement/no-quantum-threat-yet-crypto-must-prepare-now-says-coinbase-board-paper-co); [Coinbase blog](https://www.coinbase.com/blog/working-together-on-btc-post-quantum-readiness); [crypto.news](https://crypto.news/coinbase-plans-post-quantum-bitcoin-custody/)
- **BitGo:**
  - 26 May 2026: with Silence Laboratories, completed the "first post-quantum MPC transaction simulation by a regulated custodian".
  - 9 Jul 2026: launched quantum-risk tools for institutional Bitcoin wallets, including UTXO grouping and prioritisation by address (provisional patent) and key-exposure management. They do not cover P2TR or P2PK, which expose keys from the start.
  - CEO Mike Belshe: "the safest key is one whose public key has never been revealed onchain." — [BusinessWire](https://www.businesswire.com/news/home/20260526229210/en/BitGo-and-Silence-Laboratories-Complete-First-Post-Quantum-MPC-Transaction-Simulation-by-a-Regulated-Custodian); [The Block, 9 Jul 2026](https://www.theblock.co/post/407661/bitgo-quantum-protection-institutional-bitcoin-wallets) **[COI: vendor announcements]**
- **Anchorage Digital:** a strategy report on 4 Aug 2026 says it already runs "cryptographic agility" hardware and plans migration capabilities for client assets once chains support post-quantum signatures. Available only through a secondary mirror. — [Mirror of Anchorage report coverage](https://san-1510.aid.brainsum.com/news/top-news/anchorage-digital-details-post-quantum-strategy-institutional-crypto-custody)
- **Fireblocks:** has promised a "full PQC strategy document later this year". No details were found. — [Fireblocks blog](https://www.fireblocks.com/blog/google-quantum-research-institutional-crypto-security)
- **Silence Laboratories:** many post-quantum signature schemes are "not friendly to MPC". Its approach is to use post-quantum signatures at the custody layer while keeping ECDSA on-chain. — [Silence Labs](https://silencelaboratories.com/blog/post-quantum-migration-guide) **[COI]**
- **Trezor Safe 7:** uses SLH-DSA-128 for boot, firmware verification and device authentication (CTO post, 16 Mar 2026). Trezor itself says this "does not protect your assets from quantum computers at this time" until chains upgrade. — [Trezor](https://trezor.io/guides/trezor-devices/trezor-safe-7/the-first-quantum-ready-hardware-wallet); [Trezor blog](https://trezor.io/blog/security/what-quantum-ready-crypto-security-means-and-why-it-matters); [CryptoSlate](https://cryptoslate.com/?p=504195)
- **Ledger:** CTO Charles Guillemet (June 2026 podcast) announced ML-KEM and ML-DSA as firmware primitives for developers. With no hardware accelerator, they run in software. Shipment was not confirmed. — [Ledger podcast](https://www.ledger.com/the-ledger-podcast/quantum-is-not-here-yet-the-trust-problem-is)
- **Blockstream:** tested hash-based signatures on existing Trezor and Ledger devices and found them feasible, but SLH-DSA signing takes about 53-120 seconds. — [Blockstream blog](https://blog.blockstream.com/hardware-wallets-post-quantum-signatures/)

### Inferences
- **[INFERENCE]** The largest risk reduction available today is operational, not cryptographic. Over half of exposed BTC (about 4.1-4.5M) comes from address reuse and custody practice, about 40% of it at exchanges. Glassnode's 85-100% figures for Binance, Bitfinex, Robinhood and WisdomTree versus about 2-5% for Coinbase and Fidelity show that clean practice is possible with today's tools. This is a concrete, sellable remediation job, a "Y2K-style audit and fix", aimed at a small number of large holders.
- **[INFERENCE]** Bitcoin's critical path is social:
  1. pick a post-quantum signature (SHRINCS/SHRIMPS);
  2. bundle it with an output type (P2MR or P2Q) in a soft fork;
  3. resolve legacy-coin policy.

  Taproot took about 4 years from proposal to activation (Nov 2021). Starting from Draft status in 2026, activation before 2028-2029 looks unlikely without a shock. A credible demonstration or a big jump in a Q-Day Prize result would compress this sharply. That is the core "Y2K 1997" dynamic: low spend until a forcing event, then a spike.
- **[INFERENCE]** The first protocol-level product category is already defined by the drafts: tooling that lets users and custodians pre-position. That means PQC precommitments, P2MR-ready wallets, pre-Q-Day hash commitments and zero-knowledge seed-phrase provers. Whoever ships the reference implementations and wallet SDKs will have distribution when activation comes.
- **[INFERENCE]** Institutional money ($15M consortium, $5M Galaxy, $26M Project Eleven) is small next to roughly $480B of exposed value. The sector is under-invested relative to its stakes, which mirrors early Bitcoin infrastructure.

### Gaps
- Deloitte's and River's exposure estimates were not retrieved this session.
- Miner and pool positions on BIP-360/361 were not found, apart from MARA Slipstream being cited as an interim tool.
- No 2026 Bitcoin Core release notes or activation-client discussions were found.
- The primary text of the IBIT prospectus quantum section was not re-read; only the 10-Q summary was used.
- Fireblocks' and Anchorage's dated milestones were not found.
- No current BTC price was retrieved, so the USD value at risk relies on AmericanFortress's $483B headline.

---

## 3. Other chains, stablecoins, tokenised assets and the coordination problem

### Takeaway
Ethereum has the most organised plan:
- an EF Post-Quantum team (Jan 2026);
- Vitalik's four-area roadmap (Feb 2026), with leanXMSS hash-based signatures and SNARK aggregation;
- a 2029 target for full post-quantum protection under "Lean Ethereum".

Solana has an optional Winternitz vault and a Falcon implementation ready to activate. Algorand uses Falcon for state proofs. Aptos and Optimism have proposals or deadlines. Circle published a three-phase USDC/Arc roadmap (May 2026) with public-key registries and recovery frameworks. No Tether plan was found. Central-bank work (BIS Project Leap phase 2, Dec 2025) tests PQC in wholesale payments, not in tokenised assets. Each ecosystem migrates on its own schedule, and bridges, wrapped assets and multi-chain custodians inherit the weakest link.

### Cited Findings
- **Ethereum:**
  - Vitalik Buterin's Feb 2026 roadmap names four areas: validator BLS signatures, KZG data-availability commitments, ECDSA account signatures, and Groth16 zk proofs.
  - leanXMSS (hash-based) would replace BLS. Signatures are about 3,000 bytes versus 96 for BLS, so a minimal zkVM (leanVM) aggregates them with SNARKs.
  - The EF formed a Post-Quantum Security team in Jan 2026, tracked at pq.ethereum.org. Ethereum.org's "Lean Ethereum" roadmap targets 2029 for full post-quantum protection. — [Cointelegraph](https://cointelegraph.com/news/vitalik-proposes-4-fixes-quantum-resistance-roadmap-for-ethereum); [Decrypt](https://decrypt.co/359352/vitalik-buterin-maps-quantum-upgrade-ethereum); [ethereum.org future-proofing](https://ethereum.org/roadmap/future-proofing/); [ethereum.org quantum resistance](https://ethereum.org/roadmap/security/quantum-resistance.md)
- **Ethereum exposure:** the top 1,000 transacting accounts hold over 20M ETH, all vulnerable at rest, because every account that has sent a transaction has revealed its public key. — [Babbush et al., Mar 2026](https://www.alphaxiv.org/abs/2603.28846v1)
- **Solana Foundation (27 Apr 2026):** "no change is required today or likely anytime soon", but there is a plan to activate a post-quantum scheme centred on Falcon, chosen by Anza and Firedancer, with an initial implementation built. The Winternitz Vault (hash-based, optional) has existed for over two years. Project Eleven deployed a Solana testnet with post-quantum signatures. — [Solana Foundation](https://solana.com/news/quantum-readiness); [Yahoo Tech](https://tech.yahoo.com/cybersecurity/articles/solana-aptos-move-harden-blockchains-000519248.html)
- **Algorand** uses lattice-based Falcon for State Proofs. — [SoK, arXiv 2512.13333](https://arxiv.org/pdf/2512.13333v1)
- **Aptos:** AIP-137 would add its first post-quantum signature option. — [Yahoo Tech](https://tech.yahoo.com/cybersecurity/articles/solana-aptos-move-harden-blockchains-000519248.html)
- **Optimism** has announced transition plans "with specific deadlines". Solana, Algorand and Aptos have begun offering or planning quantum-resistant options. — [Coinbase board paper, via UCSB](https://cs.ucsb.edu/happenings/announcement/no-quantum-threat-yet-crypto-must-prepare-now-says-coinbase-board-paper-co)
- **Circle (whitepaper of about 29 May 2026):**
  - Three phases: readiness, a hybrid transition, and final migration that may retire classical signatures.
  - Upgradeable USDC contracts will accept both classical and post-quantum signatures.
  - It proposes public-key registries so users can bind addresses to post-quantum keys before Q-Day, and recovery frameworks tied to cryptographic proofs so users who miss migration do not automatically lose funds.
  - Arc, its L1, offers opt-in post-quantum signatures (SLH-DSA) from mainnet, expected in 2026. — [Circle blog](https://www.circle.com/blog/preparing-blockchains-for-q-day); [Cointelegraph](https://www.cointelegraph.com/news/circle-quantum-proof-roadmap-layer-1-arc); [The Block](https://www.theblock.co/amp/post/396378/circle-layer-1-arc-quantum-resistant)
- **Tether:** no quantum statement or roadmap was found in this session (search of 22 Nov 2026).
- **BIS Project Leap phase 2 (11 Dec 2025):** the BIS Innovation Hub Eurosystem Centre, with Banca d'Italia, Banque de France, Bundesbank, Nexi-Colt and Swift, tested post-quantum signatures on liquidity transfers in TARGET2. Findings: performance differences, interoperability issues, and a need for governance and readiness. It is ongoing. — [BIS](https://www.bis.org/publ/othp107.htm); [Nexi](https://www.nexigroup.com/en/media-relations/news/2025/12/post-quantum-computing-phase2/)
- **Naoris Protocol:** launched a post-quantum L1 mainnet in early Apr 2026. Its token market cap was about $36M at press time, against a $500M FDV at TGE (Jul 2025). It raised a $3M strategic round led by Mason Labs (May 2025). It claims 100M+ post-quantum-validated transactions, unverified. — [CoinDesk, 3 Apr 2026](https://www.coindesk.com/markets/2026/04/03/naoris-protocol-s-quantum-resistance-blockchain-goes-live-as-bitcoin-and-ethereum-face-q-day-threats); [The Quantum Insider](https://thequantuminsider.com/2026/04/01/naoris-protocol-launches-mainnet-introducing-post-quantum-layer-1-blockchain/); [The Block PR](https://www.theblock.co/press-releases/356189/naoris-protocol-raises-3m-in-strategic-round-led-by-mason-labs) **[COI: token issuer]**
- **Privacy, a harvest-now-decrypt-later problem for ledgers:** a Federal Reserve FEDS paper (2025-093, Mascelli and Rodden, Sep 2025) argues that post-quantum upgrades can secure future transactions but cannot restore privacy for data already recorded on a public ledger. Data on a ledger cannot be re-encrypted retroactively. — [Federal Reserve](https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm)

### Inferences
- **[INFERENCE] A cross-ecosystem gap.** Ethereum targets 2029, Bitcoin has no timeline, Solana is "ready if needed", and Tether has said nothing. So for several years, multi-chain custodians, bridges, wrapped BTC and ETH, and stablecoin issuers will run mixed-security estates. That creates demand for:
  - cross-chain exposure inventories at the level of custodians and funds;
  - hybrid signing infrastructure, both classical and post-quantum (Strongpoint, PQ-CoreKMS, Silence Labs);
  - registry-based recovery, as in Circle's proposal and Project Eleven's yellowpages.
- **[INFERENCE]** Account-based chains (Ethereum and EVM) have more structural exposure than UTXO Bitcoin, because every active account has revealed its key. Smart-contract wallets and account abstraction give them a migration lever Bitcoin lacks. Contract-level post-quantum verification (Circle's dual-signature USDC) is the template for tokenised securities.
- **[INFERENCE]** Post-Q-Day deanonymisation of historical chain data (the Fed's harvest-now-decrypt-later argument) is a second-order market both for forensics (blockchain analytics firms) and for privacy-preserving migration tools.

### Gaps
- QRL, Cardano, QANplatform, Quranium, Sui and Hedera: not researched (budget).
- Tokenised-securities platforms (BlackRock BUIDL, Franklin, Broadridge DLR, Canton) and CBDC pilots: no post-quantum plans found or searched beyond BIS Leap.
- Value-at-risk for ETH and stablecoins in USD: not computed (no price data retrieved).
- Optimism's deadlines: dates not retrieved.

---

## 4. Companies already building for this: funding, products, traction, and what's missing

### Takeaway
The dedicated "quantum-for-digital-assets" layer is small:
- **Project Eleven** is the clear category leader: $26M raised, a $120M post-money valuation (Jan 2026), a key registry (yellowpages), an institutional custody product (Strongpoint), the Q-Day Prize, and an insurer partnership.
- **Incumbent custodians** (BitGo, Coinbase, Anchorage, Fireblocks) are absorbing the custody and migration tooling in-house.
- **Chip and hardware vendors** (SEALSQ, Trezor, Ledger) cover the device layer.
- Most other "quantum-safe" crypto plays are token-funded L1s with thin traction (Naoris).

Missing pieces: standardised exposure and migration attestations, neutral post-quantum key registries, consumer and self-custody migration UX, quantum-theft detection and forensics, published insurance underwriting criteria, legal frameworks for lost coins, and an authoritative early-warning benchmark.

### Cited Findings
- **Project Eleven:**
  - Seed: $6M (Jun 2025). Series A: $20M on 14 Jan 2026 at $120M post-money, led by Castle Island Ventures with Coinbase Ventures, Fin Capital, Variant, Quantonation and others. Total raised: $26M. — [The Block](https://www.theblock.co/news/deals/2026-01-14-project-eleven-series-a-funding-crypto-quantum-threats-385583); [Project Eleven blog](https://www.projecteleven.com/blog/announcing-project-elevens-series-a); [Decrypt (seed)](https://decrypt.co/326065)
  - **yellowpages:** a "production-grade registry" where Bitcoin holders generate post-quantum keys and link them to existing addresses without an on-chain transaction. Also a Solana Foundation partnership and a Solana post-quantum testnet. — [The Block](https://www.theblock.co/news/deals/2026-01-14-project-eleven-series-a-funding-crypto-quantum-threats-385583); [Yahoo Tech](https://tech.yahoo.com/cybersecurity/articles/solana-aptos-move-harden-blockchains-000519248.html)
  - **Strongpoint:** an institutional custody product combining classical and post-quantum signing. It separates approval rules and audit history from the cryptography layer, so signing algorithms can be swapped without losing controls. Relm Insurance became a development partner (20 Oct 2026) to define the evidence insurers will need on key exposure, signing, approvals, migration readiness and third parties. The collaboration is exploratory, with no pricing impact. — [The Quantum Insider](https://thequantuminsider.com/2026/10/20/project-eleven-relm-post-quantum-risk-digital-asset-insurance/); [QCR](https://quantumcomputingreport.com/project-eleven-and-relm-insurance-partner-to-introduce-post-quantum-security-metrics-into-digital-asset-underwriting/)
  - **Q-Day Prize:** 1 BTC awarded 24 Apr 2026 for a 15-bit ECC key. — [CoinDesk](https://www.coindesk.com/tech/2026/04/24/researcher-wins-1-bitcoin-bounty-for-largest-quantum-attack-on-underlying-tech)
  - A directory profile lists 1-10 FTEs, which may be stale after the Series A. — [The Quantum Insider profile, via article](https://thequantuminsider.com/2026/10/20/project-eleven-relm-post-quantum-risk-digital-asset-insurance/) **[COI: publishes exposure estimates (6.26M, 6.9M BTC) while selling remediation]**
- **BitGo + Silence Laboratories:** post-quantum MPC simulation (May 2026) and quantum-risk tools with a provisional patent (Jul 2026). See Q2. — [BusinessWire](https://www.businesswire.com/news/home/20260526229210/en/BitGo-and-Silence-Laboratories-Complete-First-Post-Quantum-MPC-Transaction-Simulation-by-a-Regulated-Custodian); [The Block](https://www.theblock.co/post/407661/bitgo-quantum-protection-institutional-bitcoin-wallets)
- **SEALSQ (NASDAQ: LAES):**
  - H1 2026 revenue of $11.2M, up from $4.8M (headlines say +120% preliminary and +131% final). Gross profit $5.4M. Cash of about $486M per the QCR headline.
  - Pipeline above $225M through 2029, of which over $100M is post-quantum. Product: the QS7001 post-quantum secure chip.
  - It markets post-quantum for blockchain and digital transactions. — [The Quantum Insider, 11 Sep 2026](https://thequantuminsider.com/2026/09/11/sealsq-h1-2026-results-fy2026-guidance/); [QCR](https://quantumcomputingreport.com/sealsq-reports-h1-2026-financial-results-revenue-surges-131-to-11-2m-486m-cash-balance-and-post-quantum-hardware-progress/) **[COI: issuer statements]**
- **BTQ Technologies:** four business lines (QCIM, QPerfect, QSSN, "Bitcoin Quantum") per its FY2025 update. It has a BIP-360 testnet implementation. No 2026 revenue was found. — [Barchart/BTQ](https://www.barchart.com/story/news/1050249/btq-technologies-provides-full-year-2025-corporate-update-highlighting-commercial-progress-across-qcim-qperfect-qssn-and-bitcoin-quantum)
- **AmericanFortress:** an $8M seed (May 2026) co-led by SAVA Digital Asset Fund, Moon Pursuit Capital and 0G Labs. It proposes protecting existing BTC, ETH and SOL wallets without moving funds. — [Invezz](https://invezz.com/news/2026/05/06/americanfortress-raises-8m-to-quantum-proof-blockchain-transactions/); [Cointelegraph](https://cointelegraph.com/news/americanfortress-proposes-quantum-safe-crypto-wallet-protection-without-fund-migration)
- **QIZ Security:** a $17M seed led by Bessemer and Merlin Ventures, for enterprise cryptographic-posture management with a blockchain focus. — [KuCoin News (secondary)](https://www.kucoin.com/news/flash/qiz-security-raises-17m-to-prepare-enterprises-for-quantum-computing-threats)
- **Naoris Protocol:** see Q3.
- **Bounty and benchmark programmes:**
  - Project Eleven's Q-Day Prize (above).
  - PostQuantum.com refers to an "ecdsa.fail verifier" for checking claimed circuits. — [PostQuantum.com](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/)
  - Free trackers and countdown sites exist, such as qdaycountdown.com. — [Q-Day Countdown](https://qdaycountdown.com/crypto/bip-360-and-bip-361/)
- **Explicitly open items:**
  - Presidio: "Concrete benchmarks for CRQC progress and legacy-coin policy are open items that still need to be formalized." It proposes activation triggers based on scaling low-error multi-logical-qubit operations, coherence and gate speed rather than qubit counts. — [Presidio PDF](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)
  - Coinbase: self-custody state management for hash-based signatures is a problem. — [Coinbase blog](https://www.coinbase.com/blog/working-together-on-btc-post-quantum-readiness)
  - Insurers: no published quantum underwriting criteria or premium changes were found as of Oct 2026. — [The Quantum Insider](https://thequantuminsider.com/2026/10/20/project-eleven-relm-post-quantum-risk-digital-asset-insurance/)

### Inferences
- **[INFERENCE]** Project Eleven's stack (prize → registry → custody → insurance evidence) is a deliberate attempt to own the "trust layer" of the transition. Its $120M valuation on about $26M raised shows investors pricing the category as a potential chokepoint, but it is not yet a crowded market.
- **[INFERENCE]** For custody and MPC signing, incumbents (BitGo, Coinbase, Anchorage, Fireblocks) have distribution and regulatory licences, so a newcomer would struggle to compete head-on. White space sits where incumbents have weak incentives or neutrality problems:
  - independent attestations;
  - neutral registries;
  - self-custody consumer tools;
  - forensics;
  - legal and insurance data.
- **[INFERENCE]** Token-funded "quantum-safe L1s" (Naoris; QAN/Quranium not verified) look like the 2017 ICO pattern: big FDVs, thin usage. They are not the "SSL certificate" analogue.

### Gaps
- PQShield, Postquant Labs, QANplatform and Quranium: funding and traction not researched this session. The earlier study may cover PQShield.
- Freedom Factory "PQ1", a post-quantum hardware wallet for Ethereum/EVM: it appeared only in a search-engine summary. No primary page was fetched and no funding data was found, so it is unverified.
- Project Eleven revenue and customer names: not public.
- Fireblocks' PQC document: not yet found.

---

## 5. Candidates for "indispensable" products and services: evidence, buyers, urgency, competition, capital, defensibility

### Takeaway
The closest analogues to "SSL certificates in the 1990s" are trust-layer artefacts that every regulated holder will need to show, not consumer apps:
- (a) **post-quantum key registries and binding proofs**, linking today's addresses to post-quantum keys before Q-Day;
- (b) **exposure and migration attestations**, a "proof of quantum readiness" analogous to proof-of-reserves after FTX, for exchanges, ETFs and custodians, feeding insurers and auditors;
- (c) **hybrid, crypto-agile signing infrastructure** for custodians.

(a) and (c) are being built by Project Eleven, Circle, BitGo and Coinbase. (b) has no dedicated provider yet and is the most capital-light entry point. Early-warning dashboards are already commoditised and free. Insurance, ratings and lost-coin legal services are real but mostly emerge after a forcing event.

### Cited Findings (evidence base per candidate)
- **Exposure dashboards and address registries:** Glassnode publishes free entity-level exposure data (May 2026). BitGo ships institutional tools (Jul 2026). Project Eleven's yellowpages is a live registry (Jan 2026). Circle proposes public-key registries (May 2026). — [Glassnode](https://research.glassnode.com/measuring-bitcoins-quantum-exposed-supply/); [The Block/BitGo](https://www.theblock.co/post/407661/bitgo-quantum-protection-institutional-bitcoin-wallets); [The Block/Project Eleven](https://www.theblock.co/news/deals/2026-01-14-project-eleven-series-a-funding-crypto-quantum-threats-385583); [Circle](https://www.circle.com/blog/preparing-blockchains-for-q-day)
- **Migration tooling:** about 4.5M BTC of reuse exposure is "reducible without any protocol change" (Presidio). With 25% of block space, about 90% of value can migrate in about 4.4 days, so the bottleneck is behavioural and operational. — [Presidio](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)
- **Hardware wallets and HSMs:** Trezor Safe 7 (SLH-DSA boot and attestation, Mar 2026), Ledger (software ML-DSA and ML-KEM, Jun 2026), SEALSQ QS7001, Anchorage's crypto-agile HSMs. Hash-based signing on existing hardware wallets takes about 53-120 seconds. — [Trezor](https://trezor.io/guides/trezor-devices/trezor-safe-7/the-first-quantum-ready-hardware-wallet); [Ledger](https://www.ledger.com/the-ledger-podcast/quantum-is-not-here-yet-the-trust-problem-is); [Blockstream](https://blog.blockstream.com/hardware-wallets-post-quantum-signatures/); [The Quantum Insider/SEALSQ](https://thequantuminsider.com/2026/09/11/sealsq-h1-2026-results-fy2026-guidance/)
- **Proof of reserves / proof of migration attestations:** no dedicated product was found. The nearest are Relm and Project Eleven defining "the evidence institutions may need to show insurers they are ready" (Oct 2026), and Glassnode's entity labels (it explicitly warns they are "not a risk ranking or solvency signal"). — [The Quantum Insider](https://thequantuminsider.com/2026/10/20/project-eleven-relm-post-quantum-risk-digital-asset-insurance/); [Glassnode](https://research.glassnode.com/measuring-bitcoins-quantum-exposed-supply/)
- **Early-warning and monitoring:** the GRI annual survey, Project Eleven's Q-Day Prize, Polymarket (about $4.4k total volume), Kalshi, Manifold, PostQuantum.com analyses, the ecdsa.fail verifier, qdaycountdown.com, and the GQI quarterly report (paid). Presidio and Chaincode call standard activation triggers "open items". — sources above; [Polymarket](https://polymarket.com/event/quantum-breaks-bitcoin-by); [Presidio](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)
- **Insurance, ratings and actuarial work:**
  - Relm and Project Eleven are exploratory with no pricing impact (Oct 2026).
  - Aon and Moody's published joint research on quantum risk for cyber re/insurers (Aug 2026). Moody's has a primer, "Demystifying quantum risk".
  - Trade press frames quantum as a potential "systemic" cyber threat.
  - Munich Re's crypto crime cover has no quantum-specific terms in its public material. — [The Quantum Insider](https://thequantuminsider.com/2026/10/20/project-eleven-relm-post-quantum-risk-digital-asset-insurance/); [Moody's PDF](https://www.moodys.com/web/en/us/site-assets/demystifying_quantum-risk.pdf); [Insurance Business](https://www.insurancebusinessmag.com/us/news/cyber/forget-ai--quantum-computing-could-be-cybers-next-systemic-threat-583999.aspx); [Munich Re](https://www.munichre.com/en/solutions/for-industry-clients/crypto-cover.content.html)
  - A Cointelegraph piece frames quantum-proof wallets and insurance as a possible "fear tax". — [Cointelegraph](https://cointelegraph.com/news/quantum-proof-bitcoin-wallets-insurance-fear-tax)
- **Legal and forensic work on lost coins:**
  - UK Property (Digital Assets etc) Act 2025 and US UCC Article 12 (adopted in more than 30 states plus DC): neither treats dormancy as abandonment. The open question is whether a quantum sweep is "recovery" or "theft".
  - Google's paper lists "regulated digital salvage" and "bad sidechains" as policy options. No court ruling exists. — [Bitcoin Magazine (legal commentary)](https://bitcoinmagazine.com/legal/when-quantum-computers-come-for-your-bitcoin-what-classical-property-law-says-happens-next); [alphaXiv/Babbush](https://www.alphaxiv.org/abs/2603.28846v1)
  - Presidio: early quantum thefts "would likely be sporadic, making them hard to distinguish from genuine recovery and custody operations". — [Presidio](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)
- **Long-term archival encryption (harvest-now-decrypt-later):** the Fed paper says ledger data cannot be re-encrypted retroactively. The enterprise harvest-now-decrypt-later market is covered by the earlier study. — [Federal Reserve](https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm)
- **Pre-Q-Day ownership commitments:** non-seed P2PK coins "can be recovered if an owner posted a 'pre-QDay' hash commitment". Zero-knowledge seed-phrase recovery runs in under a minute on consumer hardware (proof of concept). — [Presidio](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)

### Inferences: evaluation matrix **[INFERENCE throughout]**

| # | Candidate | Who pays | Urgency (now → 2031 → post-Q-Day) | Competitors (Nov 2026) | Capital / credentials | Defensibility | Capital-light AI-agent founder? |
|---|---|---|---|---|---|---|---|
| 1 | Exposure dashboards and address analytics | Funds, analysts, media; low willingness to pay | Medium → high → very high | Glassnode (free), Project Eleven, BitGo, Presidio, Chainalysis-type firms | Low: public chain data, node and indexer | Low (commodity); higher only if it becomes the cited standard | **Yes**, but monetisation is weak. Best used as a lead magnet for #2 |
| 2 | **Exposure and migration attestations ("proof of quantum readiness")** for exchanges, ETFs, custodians and treasuries | Custodians and ETF sponsors (disclosure), insurers (underwriting evidence), auditors, regulators | Low-medium now; spikes once BIP-360 activates or after a big Q-Day Prize jump; essential after Q-Day | **No dedicated provider found.** Adjacent: Relm/Project Eleven, Glassnode, proof-of-reserves auditors | Low-medium: on-chain analysis plus cryptographic proofs (address ownership, key-rotation evidence). Credibility needs an audit-firm or insurer partner, plus SOC 2 or ISAE-style method | Medium-high if it becomes the reference standard (network effects with insurers and auditors), like proof-of-reserves after FTX or SSL CAs | **Yes, the best fit.** The methodology, data pipeline and reports are automatable; the bottleneck is trust and partnerships, not capital |
| 3 | Post-quantum key registry and binding proofs (address → post-quantum key, before Q-Day) | Users and custodians, possibly protocols and issuers (Circle) | Medium now; critical in the months before or after Q-Day | Project Eleven yellowpages, Circle's registry plan | Medium: security engineering and audits; the "neutral public good" framing matters | Potentially very high (a registry is a Schelling point, like a CA root store). Risk: a protocol-level standard makes private registries obsolete | Possible as an open-source or standards play; hard to monetise directly; strong as a credibility asset |
| 4 | Migration tooling and runbooks for custodians and exchanges (stop reuse, UTXO consolidation, P2MR/P2Q readiness, hybrid signing) | Exchanges (Binance 85% and Bitfinex 100% exposed), brokers (Robinhood 100%), ETF custodians | Medium now (reuse is fixable today); very high in the activation window | BitGo, Coinbase, Anchorage, Fireblocks (in-house); Silence Labs; consultancies | Medium-high: needs custody-grade security credentials and access to client systems | Medium (service-heavy, Y2K-like) | Partly: an advisory and audit-led service is feasible; building custody software is not |
| 5 | Post-quantum signatures in hardware wallets and HSMs | Consumers, institutions | Rising to 2029-2031 | Trezor, Ledger, SEALSQ, Anchorage, HSM incumbents | High: hardware, certification (CC/FIPS) | High (certification moats) | **No** |
| 6 | Self-custody migration UX (zero-knowledge seed-phrase recovery provers, commit/reveal helpers, pre-Q-Day commitments, inheritance tooling) | Retail holders, inheritance planners, wallet vendors (licensing) | Low now; extreme in a crisis | Wallet vendors; research proofs of concept | Low-medium (software) | Medium (first-mover in wallet integrations) | **Yes** (open-source SDK plus licensing), but timing risk until a protocol path exists |
| 7 | Q-Day early-warning / benchmark index (logical-qubit scaling, gate fidelity, resource-estimate tracker, verified-claims registry) | Risk teams, insurers, funds, protocol developers (activation triggers) | Medium, steady | GRI (annual), GQI (paid), PostQuantum.com, Polymarket/Kalshi, qdaycountdown, ecdsa.fail | Low | Low-medium; reputation-driven | **Yes**, as a research and data product; better as a wedge for #2 and #8 than as a standalone business |
| 8 | Quantum-risk ratings and actuarial models for digital-asset insurers | Insurers, reinsurers, brokers (Aon, Relm, Munich Re) | Low now; rises with premiums and exclusions | Relm/Project Eleven (exploratory); Moody's, Aon research | Medium: actuarial and insurance credentials | High if embedded in underwriting | Partly: data and model as a service is feasible; needs an insurance partner |
| 9 | Legal and forensic "lost coin" services (theft attribution, quantum sweep detection, salvage claims, estate claims) | Estates, courts, exchanges (frozen-funds disputes), regulators | Near zero now; very high after Q-Day | Blockchain analytics firms, law firms | Medium: legal credentials, forensic reputation | Medium | Partly (forensic analytics); the legal side needs lawyers |
| 10 | Long-lived quantum-safe archival and signing (documents, identities) | Enterprises, governments | High (harvest-now-decrypt-later) | Crowded per the earlier study | — | — | Covered in the earlier study; not repeated |

- **[INFERENCE] Why #2 most resembles "SSL certificates in 1995".**
  - Each regulated holder must eventually prove something to a third party (insurer, auditor, regulator, ETF investor) about a cryptographic property of its estate.
  - Proof-of-reserves became expected after FTX (Nov 2022), and quantum readiness is the next attestation ETF prospectuses could cite.
  - BlackRock's disclosure, Glassnode's entity data and the Relm partnership show both demand and gap.
  - The attestation is chain-data-driven (cheap to produce), repeatable (quarterly), and gains value from standardisation.
- **[INFERENCE] Main risk to #2:** incumbents (Glassnode, Chainalysis, Big Four, Project Eleven plus Relm) could define the standard first. A newcomer needs a fast, open methodology and an early partnership with one insurer or auditor.

### Gaps
- No pricing data was found for any quantum-specific digital-asset product (yellowpages, Strongpoint or BitGo tools).
- No regulator (SEC, ESMA/MiCA, MAS) requirement for quantum-readiness disclosure in digital assets was found. This is a key unknown for #2.
- No insurance policy wording with quantum exclusions or credits was found.
- Market-size figures for these niches do not exist in the sources found.

---

## 6. Scenarios: orderly migration vs crisis, demand spikes, and which early positions compound

### Takeaway
Credible analysts (Presidio, Bernstein, Benchmark, CoinShares, Coinbase's board) expect an orderly, multi-year upgrade with on-chain capacity as a non-issue and social coordination as the bottleneck. A rapid-response playbook (Chaincode) and crisis tools (soft-freeze, commit/reveal, private mempools) already exist on paper. The Y2K analogy fits the *shape* of spending, about $300-600B forecast versus about $308B spent, concentrated before a deadline. But Q-Day has no fixed date. Spending is therefore likely to be low and steady until a forcing signal, then spike: a credible ECC demonstration, a theft, BIP activation, or a regulator or insurer mandate. In every scenario, the positions that compound are trust-layer standards (registries, attestations, hybrid signing), set up before the spike.

### Cited Findings
- **Orderly scenario (Presidio, Apr 2026):** three phases: research and BIP drafting (where Bitcoin is now), implementation and activation, then migration. Likely path: SHRINCS/SHRIMPS plus an output type (P2MR or P2Q) bundled in a soft fork. A block-size increase may be proposed. Most value migrates in days to weeks. — [Presidio](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)
- **Rapid response (Chaincode playbook):** month 1, ban new vulnerable outputs and choose the legacy policy. Months 6-7, activate post-quantum signatures. Precedents: emergency fixes in 2010 (value overflow), 2013 (chain split) and 2018 (inflation bug). — [Presidio](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)
- **Live-CRQC theft scenario:** commit/reveal migration, private mempools (MARA Slipstream) as a centralising stopgap, and a "soft-freeze" with seed-phrase zero-knowledge recovery. The "first major hurdle is reaching agreement that quantum-capable theft is even occurring", because breakthroughs could be kept quiet. — [Presidio](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf); GRI experts on covert efforts: [TelecomTV](https://www.telecomtv.com/content/security/could-q-day-be-an-existential-threat-to-digital-economies-52754/)
- **Market impact sizing:**
  - Liquidating the 1.72M assumed-lost P2PK coins would be roughly one year of "peak bull-market" long-term-holder selling (Checkonchain, via Presidio).
  - CoinShares counters that only 10,200 BTC sit in UTXOs big enough to disrupt the market, and that a thief would need a very long time to crack more than 32,000 UTXOs one at a time.
  - Bernstein says the scare is "priced in" with a 3-5-year window. — [Presidio](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf); [The Block/CoinShares](https://www.theblock.co/post/388969/coinshares-says-only-10200-btc-face-real-quantum-risk); [crypto.news/Bernstein](https://crypto.news/bitcoins-quantum-scare-priced-in-bernstein-says-but-3-5-year-window-to-upgrade/)
- **Fork risk:** legacy-coin policy is the "clearest plausible fault line for a contentious fork"; the market picks the winner, as in 2017 with BCH. — [Presidio](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf)
- **Y2K benchmark:**
  - Gartner's widely quoted global fix estimate of $300-600B was based on cost per line of code and excluded disruption losses and chip replacement (OECD, 1998).
  - Other estimates: JP Morgan about $200B, IDC $320B, Cap Gemini about $900B (Journal of Accountancy, Dec 1997).
  - About $308B was estimated as actually spent before the millennium (Computerworld retrospective). — [OECD PUMA(98)10](https://one.oecd.org/document/PUMA(98)10/En/pdf); [Journal of Accountancy](https://www.journalofaccountancy.com/issues/1997/dec/zarowin-dec-1997/); [Computerworld](https://www.computerworld.com/article/1557998/y2k-the-good-the-bad-and-the-crazy.html)
- **Institutional funding to date:** $15M consortium, $5M Galaxy, $26M Project Eleven, $8M AmericanFortress, $17M QIZ. That totals about $70M of identifiable dedicated digital-asset quantum money in 2025-2026. — sources in Q2 and Q4.

### Inferences **[INFERENCE / FORECAST]**

| Scenario (subjective weight) | Trigger | What spikes | Early positions that compound most |
|---|---|---|---|
| **A. Orderly, gradual (≈55-65%)**: CRQC 2033-2040+, Bitcoin soft fork about 2028-2031, Ethereum post-quantum about 2029-2031 | Steady resource-estimate declines; BIP activation; insurer and auditor requirements | Custodian migration projects, attestations for ETF and insurance disclosure, wallet SDKs, hybrid signing | **Attestation standard (#2)**, **registry (#3)**, crypto-agile custody (Strongpoint-like) and benchmark data feeding them |
| **B. Signal shock, then rush (≈25-35%)**: a credible public ECC demonstration at 20-40 bits, a big Q-Day Prize jump, a vendor's verified logical-qubit milestone, or a contested "covert CRQC" rumour | A Polymarket-type event, a BlackRock or SEC disclosure update, insurer exclusions | Y2K-style remediation surge: audits, consolidation of reused-address funds, emergency BIP work, PQ hardware wallet sales, insurance repricing | Whoever already holds **trusted exposure data plus an attestation method** gets the inbound flow; registries with users already bound; developer tooling for P2MR, SHRINCS and commit/reveal |
| **C. Crisis, live theft (≈5-10% before 2035)**: unannounced CRQC sweeps P2PK or reused coins | Anomalous old-coin movements; dispute over whether it is theft or recovery | Forensics and attribution, legal claims and salvage, soft-freeze recovery provers, private relays, insurance claims | **Forensic monitoring of dormant and exposed UTXOs** (an "early theft detector"), zero-knowledge seed-recovery services, legal frameworks; registries that prove pre-Q-Day ownership |

- **[INFERENCE] Y2K vs Q-Day spending shape.** Y2K spending was about $300B, concentrated in 1997-1999 because the deadline was certain. Q-Day lacks a fixed date, so digital-asset spending in Scenario A is likely to be small and continuous (tens to hundreds of $M per year industry-wide). Scenario B would compress multi-year budgets into quarters, the post-Heartbleed pattern of emergency certificate re-issuance (not researched here; see Gaps).
- **[INFERENCE] Answer to "Is there a Bitcoin 2009-2012-style opportunity here?"** Partially, and in a specific place. The protocol and hardware layers are already owned by incumbents and well-funded players: Google, IonQ and IBM on the attack side; Trezor, Ledger and SEALSQ on devices; BitGo and Coinbase on custody. The "2010-era" asymmetric openings are in the trust and evidence layer, which is still unbuilt:
  - neutral exposure and migration attestations;
  - verified CRQC benchmarks that protocol developers can use as activation triggers;
  - ownership-commitment registries;
  - forensic detection of quantum sweeps.

  These need credibility and data more than capital. They suit an AI-agent-assisted founder who can produce rigorous, frequent, open research quickly, but they need a credentialed partner (auditor, insurer or law firm) to monetise.
- **[INFERENCE] Main risks to any newcomer:**
  - Timing: a 5-15-year wait with low willingness to pay before a forcing event.
  - Incumbent capture: Project Eleven plus Relm, Glassnode, BitGo.
  - Protocol obsolescence: a Bitcoin-native registry or commitment scheme could replace private registries.
  - Reputation: doom-marketing is visible and discredited (IonQ's PR overstatement, the "fear tax" critique).

### Gaps
- Post-Heartbleed (2014) certificate-rush spending data: not researched (budget).
- No analyst model of the BTC price impact of a Q-Day event was found beyond the Checkonchain and CoinShares framings.
- No quantified estimate exists of the digital-asset share of global PQC spending.
- The scenario weights above are the researcher's own and are not taken from any source.
- Session budget ran out before: GRI 2024/2023 figures, Deloitte and River estimates, miner positions, Tether, QRL, Cardano, QAN, Quranium, PQShield, Postquant Labs, Metaculus, regulator disclosure rules on quantum readiness (SEC/ESMA/MAS), and insurance policy wordings.
