# Future quantum infrastructure layers (2031-2041): which become indispensable, and who owns them as of November 2026

Scope note: these notes cover the technical and commercial infrastructure stack. Q-Day and crypto-asset migration, and open standards and benchmarks, are covered by other researchers. Current-state claims are dated. Anything about 2031-2041 is marked **FORECAST** and names its source or says it is my own inference. Most 2026 evidence comes from vendor press releases and trade press (Quantum Computing Report, The Quantum Insider, PostQuantum). Several search summaries flagged inconsistent page dates, so the exact dates below should be spot-checked before publication. A few facts come from my prior knowledge (cutoff June 2026) and were not re-fetched in this session. Each of those is labelled "[prior knowledge, not re-fetched]".

Research budget: about 18 tool calls. Questions 1-5 have the most coverage; questions 6 and 7 are thinner and their gaps are listed.

---

## 1. Error correction and real-time control: who owns the decoder and control layer, and is it becoming a merchant component?

### Takeaway
The decoder and control layer is splitting in two. The vertically integrated leaders (Google, IBM, Quantinuum) build their own decoders, and IBM is even designing its own decoder ASIC. Everyone else is converging on merchant components. These come from NVIDIA (NVQLink, CUDA-Q QEC, cudaq-realtime, open "Ising" AI pre-decoder models), from Riverlane (Deltaflow FPGA/ASIC decoders and the QECi interface), and from control-electronics vendors (Quantum Machines, Qblox, Zurich Instruments). In October 2026 NVIDIA took an equity stake in Riverlane. That points to the merchant layer consolidating around NVIDIA, roughly the way Nvidia and Mellanox came together in AI. The open-source algorithm layer (Stim, PyMatching, Relay-BP, Tesseract) stays open and is where individuals have historically set de facto standards.

### Cited Findings
**NVIDIA's real-time QEC stack (merchant, cross-vendor):**
- On 14 Apr 2026 NVIDIA released CUDA-Q QEC 0.6. It integrates `cudaq-realtime`, a library announced at GTC 2026 that runs on NVQLink and gives microsecond-latency callbacks between GPUs and quantum controllers. It adds two real-time decoder pipelines: RelayBP for qLDPC codes, and an NVIDIA "Ising" CNN pre-decoder paired with PyMatching for the surface code. It also adds a C++ decoder plugin interface (`decoder.h`). The post says any hardware vendor on NVQLink can use the library. — [NVIDIA CUDA-Q blog, 14 Apr 2026](https://nvidia.github.io/cuda-quantum/blogs/blog/2026/04/14/cudaq-qec-0.6/)
- Benchmark from the same post (d=13 surface code, p=0.003, 104 rounds): latency is "just over 2 µs" per round with pre-decoding. The fast Ising pre-decoder plus PyMatching reaches 2.1 µs per round, 2.5x less decoding time than PyMatching alone. The accurate pre-decoder gives a 1.5x logical-error-rate improvement. Hardware was a Grace Neoverse-V2 CPU plus a B300 GPU. The Ising models are described as an "open source model family", and the CUDA-Q QEC source is on GitHub. — [NVIDIA CUDA-Q blog, 14 Apr 2026](https://nvidia.github.io/cuda-quantum/blogs/blog/2026/04/14/cudaq-qec-0.6/)
- `cudaq-realtime`, for programming the "logical QPU", was launched on 16 Mar 2026. — [NVIDIA CUDA-Q blog, 16 Mar 2026](https://nvidia.github.io/cuda-quantum/blogs/blog/2026/03/16/launching-cudaq-realtime/)
- At launch in Oct 2025, NVQLink was announced with 17 quantum builders, 5 control-system builders (including Quantum Machines, Qblox, Zurich Instruments and Keysight) and 9 US national labs. — [NVIDIA newsroom, Oct 2025](https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing) [prior knowledge, not re-fetched]
- NVQLink integrations reported in 2026:
  - IQM and Zurich Instruments launched a real-time QEC demonstrator. It combines IQM's 20-qubit superconducting QPU, ZI's new ZQCS control system and GPU computing over NVQLink. — [BusinessWire, 16 Mar 2026](https://www.businesswire.com/news/home/20260316511715/en/IQM-and-Zurich-Instruments-Launch-Real-Time-Quantum-Error-Correction-Demonstrator-with-NVIDIA-NVQLink)
  - Quantum Machines ran CUDA-Q QEC decoders (PyMatching on a GH200 over NVQLink) with its OPX1000 controller and reported sub-microsecond surface-code decoding. Customer early access was announced for December. — [Quantum Machines press release](https://www.quantum-machines.co/press-release/real-time-qec-decoding-opx1000-nvidia-cuda-q/); [QCR](https://quantumcomputingreport.com/quantum-machines-demonstrates-sub-microsecond-surface-code-decoding-on-opx1000-using-nvidia-cuda-q-qec-and-nvqlink/); [HPCwire](https://www.hpcwire.com/off-the-wire/quantum-machines-delivers-1st-results-from-cuda-q-qec-real-time-decoders/). *Date conflict:* the search summary gives 16 Nov 2026, but the HPCwire "1st results" item may be from Nov 2025. Verify.
  - SEEQC paired its chip-scale digital pre-decoder with NVIDIA Ising models over NVQLink and reported about 50% lower QEC latency and error rate. — [QCR](https://quantumcomputingreport.com/seeqc-and-nvidia-demonstrate-50-qec-latency-and-error-rate-reduction-via-digital-pre-decoder-architecture/)
  - Quantinuum ran correlated decoding of the Bring code on Helios with NVIDIA's GPU-accelerated BP+OSD decoder. The CUDA-Q post calls this a "custom integration". — [NVIDIA CUDA-Q blog](https://nvidia.github.io/cuda-quantum/blogs/blog/2026/04/14/cudaq-qec-0.6/)
  - Qblox reported sub-4 µs latency with DGX Spark and RTX PRO 6000 over NVQLink (around Oct 2026). Alice & Bob ran an LDPC-cat GPU decoding test via OPX1000 and NVQLink. Diraq uses NVQLink for calibration and autotuning. — search summary of [QCR coverage](https://quantumcomputingreport.com/quantum-machines-demonstrates-sub-microsecond-surface-code-decoding-on-opx1000-using-nvidia-cuda-q-qec-and-nvqlink/) (secondary; verify)

**Riverlane (independent merchant decoder company, now NVIDIA-backed):**
- On 22 Oct 2026 NVIDIA took a "strategic minority equity stake" in Riverlane (Cambridge, UK). The amount was undisclosed, and the stake was announced as part of NVIDIA's $250M UK computing commitment. GPU-accelerated recalibration of Riverlane's Local Clustering Decoder cut a surface-code training cycle from 3.0 min on one CPU core to 2.8 s on H100. Throughput went from about 59k to more than 4M syndromes/s, which the article calls a ~70x speedup. — [QCR, 22 Oct 2026](https://quantumcomputingreport.com/nvidia-takes-strategic-stake-in-riverlane-to-accelerate-real-time-quantum-error-correction-and-gpu-decoder-calibration/)
- Deltaflow 2 (FPGA-based) has been deployed on multiple platforms spanning several qubit modalities and control systems, though no customer list is public. Riverlane and Qblox closed a full real-time QEC loop over 50,000 QEC cycles. Integration runs over QECi, Riverlane's open QEC interface (March 2026). Deltaflow 3 is expected in late 2026. — [Riverlane blog](https://www.riverlane.com/blog/riverlane-and-qblox-have-closed-a-full-real-time-qec-loop); [Riverlane news](https://www.riverlane.com/news/riverlane-unveils-first-hardware-decoder-to-deliver-real-time-scalable-quantum-error-correction); [Datacentre News](https://datacentrenews.uk/story/riverlane-unveils-microsecond-quantum-error-decoder)
- Riverlane reported a real-time QEC latency of 16.32 µs with Deltaflow 2. QCR calls this a fourfold improvement over the 63 µs set in Google's 2024 Willow experiment. — [QCR](https://quantumcomputingreport.com/riverlane-demonstrates-real-time-qec-latency-performance-advancements/)
- Riverlane's QEC Report draws on five years of funding, publication and patent data, plus interviews with experts at Google Quantum AI, IBM, Quantinuum, IonQ, NVIDIA and ORNL. I could not retrieve the 2026 edition's figures. — [Riverlane](https://www.riverlane.com/)

**Vertically integrated players (own the decoder in-house):**
- IBM says its Relay-BP decoder now meets Starling's performance requirements while lowering decoding compute overhead. IBM is building a real-time decoder ASIC on 2 nm nanosheet technology to run Relay-BP on Starling. Starling remains targeted for 2029: 200 logical qubits and 100M operations. — [IBM Quantum blog, "Tracking progress on the path to Starling"](https://www.ibm.com/quantum/blog/path-to-ibm-quantum-starling); [IBM Relay-BP blog](https://www.ibm.com/quantum/blog/relay-bp-error-correction-decoder)
- Skeptical note: one critical analysis says the Relay-BP paper decoded no syndromes from a real processor, so its performance on device data was unvalidated at publication. Kookaburra (2026 roadmap item, the first qLDPC module) had not been confirmed as delivered in the sources found. — [PostQuantum on IBM](https://postquantum.com/quantum-computing-companies/ibm/); [Qntonsol roadmap tracker](https://www.qntonsol.com/learn/ibm-quantum-roadmap-to-starling.html)
- IBM reportedly used AI agents to speed up the design of its decoder chip, which is relevant to the AI-assisted-founder angle. — [PostQuantum](https://postquantum.com/engineering-news/ai-chip-design-quantum-decoder/) (not fetched; title only)
- Google's open-source tools are the field's de facto standards. Stim is the stabilizer-circuit simulator (Craig Gidney) and PyMatching is the MWPM decoder (Oscar Higgott, written as a PhD student). Google also released Tesseract (search-based decoder) and built AlphaQubit (a neural decoder with DeepMind, Nature Nov 2024). — [Stim](https://github.com/quantumlib/Stim), [PyMatching](https://github.com/oscarhiggott/PyMatching), [Tesseract](https://github.com/quantumlib/tesseract-decoder), [AlphaQubit, Nature](https://www.nature.com/articles/s41586-024-08148-8) [prior knowledge, not re-fetched]
- Google's Willow below-threshold result (Nature, Dec 2024) used real-time decoding at about 63 µs latency (d=5). — [Nature](https://www.nature.com/articles/s41586-024-08449-y) [prior knowledge, not re-fetched]; the 63 µs figure is confirmed in [QCR](https://quantumcomputingreport.com/riverlane-demonstrates-real-time-qec-latency-performance-advancements/)

**DARPA as kingmaker for who reaches fault tolerance (and so who needs decoders):**
- DARPA QBI Stage B (Nov 2025) named 11 companies: Atom Computing, Diraq, IBM, IonQ, Nord Quantique, Photonic Inc., Quantinuum, Quantum Motion, QuEra, Silicon Quantum Computing and Xanadu. Awards were up to about $15M each for roughly a year. — [Nextgov, Nov 2025](https://www.nextgov.com/emerging-tech/2025/11/11-companies-move-second-stage-darpas-quantum-benchmarking-initiative/409405/); [QCR](https://quantumcomputingreport.com/darpas-quantum-benchmarking-initiative-qbi-advances-with-eleven-teams-moving-to-stage-b/)
- In Oct 2026, Atom Computing, Diraq, IBM and IonQ advanced to Stage C, alongside Microsoft and PsiQuantum, which came via US2QC. Quantinuum said it was "actively discussing" a Stage C scope with DARPA. Xanadu was absent, which Fast Company links to its GlobalFoundries partnership rather than a drop. DARPA expects more companies to progress. — [Fast Company](https://www.fastcompany.com/91620226/darpa-quantum-benchmarking-initiative-stage-c-announcement) (403 on fetch; via search summary); [Entangled Future QBI tracker](https://entangledfuture.com/stack/darpa-qbi/)
- **FORECAST:** QBI's stated goal is to verify whether any approach can reach utility scale by 2033. — [Qntonsol explainer](https://www.qntonsol.com/learn/darpa-quantum-benchmarking-initiative-explained.html) (secondary)

### Inferences
- The decoder is following the GPU and networking-chip pattern only for the non-integrated majority. Google, IBM and probably Quantinuum treat it as core IP; IBM's 2 nm ASIC is the clearest signal. The roughly 15-20 other hardware makers can't afford custom decoder silicon, so they buy NVIDIA (GPU plus NVQLink), Riverlane (FPGA/ASIC plus QECi), or the decoder bundled by their control vendor (QM, Qblox, ZI).
- NVIDIA's stake in Riverlane suggests the two merchant paths (GPU-centric and FPGA/ASIC-centric) are being aligned under one ecosystem owner rather than competing. This mirrors NVIDIA's AI playbook: own the interconnect (NVQLink, like NVLink and InfiniBand) and the runtime (cudaq-realtime, like CUDA), stay hardware-agnostic on the QPU, and let QPU makers fight each other.
- Openness to new entrants:
  - Hardware decoders and control electronics: low. These need deep FPGA/ASIC/cryo-RF expertise and tens of millions of dollars, and incumbents (QM, Qblox, ZI, Keysight) are well funded.
  - Decoder algorithms and AI pre-decoders: high, open, cheap. PyMatching shows a single PhD student's open-source tool becoming the industry default. NVIDIA's plugin interface (`decoder.h`) and open Ising models explicitly invite third-party decoders.
  - Decoder calibration, noise-model learning and QEC experiment tooling: medium-high.
  - This is the closest analogue in the stack to "early Bitcoin open-source infrastructure". A capital-light, AI-assisted founder could plausibly publish a decoder, pre-decoder or QEC-simulation tool that becomes a default plugin. Monetisation is weak unless the project is acquired or licensed.
- **FORECAST (my inference):** by 2031-2036, real-time decoding is very likely indispensable, since every fault-tolerant machine needs one. It will most likely be sold as a module inside NVIDIA's platform or bundled by control vendors, not as an independent "decoder company". Riverlane is the main independent and is now partly NVIDIA-aligned.

### Gaps
- No public customer list or revenue for Riverlane Deltaflow, and none for Quantum Machines, Qblox or ZI's QEC products.
- The Riverlane QEC Report 2026 figures were not retrieved.
- No official, complete NVQLink adopter list for 2026 was found.
- The Quantum Machines NVQLink decoding date is in conflict (Nov 2025 vs Nov 2026).
- Delivery of IBM's Kookaburra in 2026 is unconfirmed.

---

## 2. Quantum operating systems, compilers and middleware: is a "Windows, Linux or CUDA of quantum" forming?

### Takeaway
Qiskit (IBM) has the largest developer base by a wide margin. NVIDIA's CUDA-Q is the fastest-growing, mainly through HPC and hybrid use. NVIDIA is moving the strategic centre of gravity from the SDK into the real-time runtime (cudaq-realtime and the QEC libraries), which is where fault-tolerant execution will live. Neutral cross-hardware layers (Classiq, qBraid, PennyLane) survive at the developer level, but the "OS" of a fault-tolerant machine is being claimed by NVIDIA or by the integrated vendors.

### Cited Findings
- The Unitary Foundation 2026 Quantum Open Source Software Survey had more than 1,800 respondents. Current or future usage: Qiskit 65.4%, PennyLane 46.2%. Classiq and CUDA-Q showed "major adoption gains". CUDA-Q Algorithms was at 10.5% active usage and 21.2% planned adoption for 2027, among the highest planned rates. — [Unitary Foundation, 2026 survey](https://unitary.foundation/posts/2026_survey_results/); [QCR summary](https://quantumcomputingreport.com/unitary-foundation-releases-2026-quantum-open-source-survey-covering-sdk-adoption-hybrid-hpc-workflows-and-ai-tooling/)
- One 2026 guide says Qiskit has more than 700,000 users. The derivation is unverified. — [Entangled Future software landscape](https://entangledfuture.com/guides/quantum-software-landscape/); [The Quantum Insider, 19 Jun 2026](https://thequantuminsider.com/2026/06/19/state-of-quantum-computing-programming-languages/)
- IBM released Qiskit SDK v2.5 on 14 Jul 2026. Qiskit 1.x reached end of life on 12 Jun 2026. — search summary of the 2026 guides above (verify on [IBM Qiskit](https://www.ibm.com/quantum/qiskit))
- NVIDIA's runtime layer: cudaq-realtime (Mar 2026) gives µs-latency GPU-to-controller callbacks over NVQLink, and CUDA-Q QEC offers a decoder plugin interface. The real-time dispatch path is C++ only. — [NVIDIA CUDA-Q blog](https://nvidia.github.io/cuda-quantum/blogs/blog/2026/04/14/cudaq-qec-0.6/)
- Quantinuum's Helios (Nov 2025) shipped with its own stack: the Guppy language, the Nexus platform and a real-time-capable control system. Quantinuum also integrates with CUDA-Q for GPU decoding. — [NVIDIA CUDA-Q blog](https://nvidia.github.io/cuda-quantum/blogs/blog/2026/04/14/cudaq-qec-0.6/) (for the CUDA-Q integration); Guppy and Nexus details [prior knowledge, not re-fetched]

### Inferences
- There are two lock-in surfaces. (a) Developer mindshare: Qiskit leads today, which resembles Linux or Python-ecosystem lock-in. (b) Execution-runtime lock-in in the fault-tolerant era: the real-time, logical-level runtime that runs decoders, magic-state scheduling and lattice surgery. NVIDIA is building (b) deliberately. IBM owns both for its own hardware only.
- **FORECAST (my inference):** the closest analogue to "CUDA of quantum" by the mid-2030s is NVIDIA's CUDA-Q, cudaq-realtime and NVQLink for third-party hardware, with IBM's Qiskit stack as the "Apple-style" integrated alternative. A neutral compiler company (Classiq, Q-CTRL, Horizon Quantum, qBraid) is viable as a productivity tool or acquisition target, but is unlikely to own the low-level runtime.
- Openness to small players: medium for high-level tooling (domain libraries, AI-agent coding assistants for quantum, resource-estimation front ends, logical-circuit optimisers). Low for runtime and OS. Logical-level compilation for fault-tolerant machines is still early, and its algorithms are published openly, so it is a niche where a small expert team could set a de facto standard before 2030.

### Gaps
- No 2026 revenue or customer data was found for Classiq, Q-CTRL, Horizon Quantum, qBraid or Strangeworks.
- I did not verify Microsoft's 2026 strategy (Azure Quantum Elements, Q#, Majorana) or Pasqal's software stack.
- There is no measured "market share" for SDKs; only survey usage exists.

---

## 3. Hybrid quantum-HPC-AI integration, quantum data centres, cryogenics and supply chain

### Takeaway
Quantum computers are moving into HPC centres, which is the main path in Europe and US national labs, and are starting to appear in commercial colocation (Equinix Sydney with Diraq, OQC with Equinix Tokyo). The pieces most likely to become utilities are: (a) the HPC-QPU interconnect and scheduler (NVQLink and HPC schedulers); (b) cryogenics, with Bluefors dominant; and (c) helium-3 supply, where Interlune's lunar He-3 is a long-dated forward contract from 2028 to 2037. Cryogenic dependence varies by modality: superconducting and spin qubits need dilution refrigerators, while ions and neutral atoms don't.

### Cited Findings
- **EuroHPC:** Euro-Q-Exa was unveiled at LRZ (Garching) in Feb 2026. It is a 54-qubit system on IQM's Radiance platform, with a second 150-qubit system planned for end-2026. A Commission official said the first six European quantum systems were procured and co-funded and four were operational. EuroSSQ-HPC, a semiconductor spin-qubit system, was procured for SURF in Amsterdam. — [The Quantum Insider, 12 Feb 2026](https://thequantuminsider.com/2026/02/12/europe-launches-euro-q-exa-quantum-computer-germany/); [Quantum Spectator](https://quantumspectator.com/europe-launches-euro-q-exa-quantum-computer-to-bolster-sovereign-digital-infrastructure/)
- **Commercial data centres:** Diraq and Equinix announced (1 Sep 2026) Australia's first quantum computer inside a data centre, a silicon spin QPU in Equinix Sydney. A 19 Nov 2026 report says it is now installed in an operational commercial data centre. — [Equinix newsroom, 1 Sep 2026](https://newsroom.equinix.com/2026-09-01-Diraq-and-Equinix-to-Deploy-Australias-First-Quantum-Computer-Inside-a-Data-Centre); [The Quantum Insider, 19 Nov 2026](https://thequantuminsider.com/2026/11/19/from-lab-to-live-inside-the-practical-realities-of-deploying-quantum-computing-at-data-center-scale/)
- OQC signed earlier colocation deals for low-qubit systems at Cyxtera LHR3 (Reading, UK) and Equinix TY11 (Tokyo). These sites have since gone live. — [DCD](https://www.datacenterdynamics.com/en/analysis/qubits-come-of-age-in-the-data-center/)
- IBM's Quantum Data Center in Ehningen, Germany, opened in Oct 2024 and is IBM's first outside the US. IBM's 11 Nov 2026 release covers Nighthawk progress and plans to scale beyond 1,000 qubits in 2027. — search summary; see [DCD](https://www.datacenterdynamics.com/en/analysis/qubits-come-of-age-in-the-data-center/) (IBM primary page not fetched)
- Equinix has published four production requirements and six site checks for hosting quantum computers, an early sign of a "quantum-ready colo" standard. — [Shattered.io summary](https://shattered.io/equinix-quantum-computing-data-center-four-production-requirements-six-site-checks/) (secondary)
- **Cryogenics and helium-3:**
  - In Sep 2025, Bluefors agreed to buy up to 10,000 litres a year of lunar helium-3 from Interlune, with deliveries from 2028 to 2037. One source values the deal at more than $300M. — [PostQuantum cryogenics guide](https://postquantum.com/building-quantum-computers/quantum-cryogenic-infrastructure-helium3/); [Dataintelo](https://dataintelo.com/report/dilution-refrigerators-market) (secondary; primary press releases not retrieved)
  - Interlune booked its first commercial He-3 order in May 2026. In July 2026 it claimed its "Cold Capture" process produced 99% pure He-3 from commercial Grade A helium (company claims, unverified). — [Entangled Future](https://entangledfuture.com/company/interlune/); [Firgun VC](https://firgun.vc/insights/cryogenics-quantum-computing-bottleneck)
  - One full year of Interlune's maximum supply would charge roughly 250 large systems. He-3 price estimates conflict: $1,900-2,600 per litre for bulk supply versus about $20M per kg (quoted from Interlune's CEO). Charge sizes range from 5-12 L for an LD450sl to about 40 L for an XLD1000. — [Firgun VC](https://firgun.vc/insights/cryogenics-quantum-computing-bottleneck); [PostQuantum](https://postquantum.com/building-quantum-computers/quantum-cryogenic-infrastructure-helium3/); [Quantum Academy](https://quantumacademy.com/quantum-engineering/helium-3/)
  - Bluefors has a low-height, HPC-oriented fridge with a first multi-module delivery slated for late 2026. This shipment is unconfirmed. — [PostQuantum](https://postquantum.com/building-quantum-computers/quantum-cryogenic-infrastructure-helium3/)
  - A PostQuantum piece frames "four enabling technologies" (cryogenics, control, interconnects, decoders) as deciding which quantum computers scale. — [PostQuantum](https://postquantum.com/quantum-ecosystem/quantum-infrastructure-technologies/)

### Inferences
- The HPC centre, not the hyperscaler cloud, is becoming the default host for early fault-tolerant machines in Europe and Japan. This happens through sovereign procurement such as EuroHPC, and the integration standard there is increasingly NVQLink plus CUDA-Q.
- Colocation (Equinix) is a real but early channel. **FORECAST (my inference):** "quantum-ready data centre" certification and site engineering (vibration, power, cooling, He-3 logistics) could become a services niche, a "Cloudflare-of-facilities" analogue. It needs facilities credentials, not quantum physics.
- He-3 and dilution refrigerators are the hardest bottleneck for superconducting and spin modalities. The bottleneck is capital-intensive and controlled by Bluefors and a few others (Oxford Instruments, Maybell, ICEoxford: [prior knowledge, not re-fetched]). Interlune's lunar supply is a 2028+ bet. This layer is closed to small players except through trading, recycling and recovery services, or analytics. Its "indispensability" also depends on which modality wins; ions and atoms avoid it.

### Gaps
- Bluefors revenue and 2026 dilution-refrigerator lead times were not found.
- He-3 supply from tritium decay (US DOE and Savannah River) was not quantified.
- I did not verify DOE lab, RIKEN or Jülich NVQLink deployments, or the details of IonQ and Pasqal data-centre deployments.
- No primary Bluefors or Interlune press release was retrieved.

---

## 4. Quantum networking and the quantum internet

### Takeaway
Quantum networking is pre-commercial as of November 2026. Cisco is explicitly building the control plane and "network OS" layer and calls it "Entanglement-as-a-Service", but all of it is still research prototypes. IonQ (through the Lightsynq acquisition) is assembling vertically integrated memory and interconnect hardware plus defence contracts. Europe's Quantum Internet Alliance just got €47.5M for a full-stack prototype. A "quantum ISP" by 2031-2041 is plausible but unproven. The most concrete near-term demand is interconnecting modular quantum computers inside or between data centres, not a public quantum internet.

### Cited Findings
- **Cisco (Outshift incubator):**
  - Its entanglement-source chip reportedly generates about 200 million entangled photon pairs per second at telecom wavelengths and room temperature.
  - In April 2026 it announced a Universal Quantum Switch prototype with less than 4% fidelity degradation in proof-of-concept tests.
  - In Feb 2026, Cisco software coordinated multi-node entanglement distribution and swapping over 17.6 km of commercial fibre in New York City, with hardware from Qunnect and Swabian Instruments, at more than 99% polarisation fidelity (Cisco-reported).
  - In Oct 2026 it released a Quantum Network Controller and a Network-Aware Quantum Compiler v0.2.0. Applications request entanglement and the network works out delivery. The compiler splits programs across QPUs and computes how much entanglement is needed between which nodes.
  - Cisco stresses that both are research prototypes, not commercial products.
  - Sources: [Cisco Investor news, 2026](https://investor.cisco.com/news/news-details/2026/Cisco-Introduces-Universal-Quantum-Switch-Advancing-the-Path-to-a-Quantum-Network/default.aspx); [Cisco Blogs, "Quantum Networking Gets a Control Plane"](https://blogs.cisco.com/news/quantum-networking-gets-a-control-plane); [The Quantum Insider, 7 Oct 2026](https://thequantuminsider.com/2026/10/07/cisco-introduces-software-to-coordinate-larger-quantum-networks/); [Help Net Security, 8 Oct 2026](https://www.helpnetsecurity.com/2026/10/08/cisco-quantum-network-controller-research-prototype/); [SiliconANGLE, 27 Apr 2026](https://siliconangle.com/2026/04/27/ciscos-universal-quantum-switch-rise-quantum-fabric/); [QCR](https://quantumcomputingreport.com/cisco-releases-quantum-network-controller-and-network-aware-compiler-v0-2-0-for-distributed-quantum-infrastructure/)
- **IonQ:**
  - IonQ completed its acquisition of Lightsynq in June 2025.
  - Oct 2026: IonQ entangled a trapped-ion qubit with a solid-state quantum memory more than 1,000 times per second over a photonic link at 88% fidelity. This is a non-peer-reviewed preprint at lab distances.
  - Jun 2026: Duke and IonQ made a GHZ state across three separately trapped Ba-138 ions at independent nodes.
  - IonQ and EPB announced a Chattanooga research centre for quantum memory on a live network. This is not yet a working repeater.
  - 27 Oct 2026: IonQ won an AFRL Phase 2 contract for free-space entanglement to drones using Lightsynq memory.
  - Sources: [PostQuantum](https://postquantum.com/quantum-research/ionq-quantum-memory-interconnect/); [Gordon's STEM blog, Aug 2026](https://www.gordostuff.com/2026/08/ionq-and-epb-are-testing-quantum-memory.html); [TechTimes, 27 Oct 2026](https://www.techtimes.com/articles/329568/20261027/ionq-wins-afrl-phase-2-contract-beam-quantum-entanglement-through-open-air-to-drones.htm); [Netcreat Substack, "From Lightsynq to Skyloom–Capella"](https://netcreat.substack.com/p/from-lightsynq-to-skyloomcapella) (secondary)
- **Europe (QIA):** On 16 Oct 2026 the Quantum Internet Alliance, more than 50 institutions led by TU Delft and coordinated at QuTech, received €47.5M from the European Commission for its next phase: integrating components into a full-stack prototype network that can run applications. Qblox is a participant. — [QuTech, 16 Oct 2026](https://qutech.nl/2026/10/16/qutech-coordinates-european-effort-to-build-worlds-first-full-stack-quantum-internet-prototype/); [Qblox newsroom](https://qblox.com/newsroom/qia-secures-eu47-5-million-to-build-full-stack-quantum-networks-and-qblox-is-part-of-it)
- QuTech and QIA published QNodeOS, an operating system for quantum network nodes, in Nature in March 2025. — [Nature](https://www.nature.com/articles/s41586-025-08704-w) [prior knowledge, not re-fetched]
- McKinsey's 2026 monitor gives no separate revenue figure for quantum networking in the sources found. The nearest figure is post-quantum cryptography, projected at $2.4-3.4B globally by 2035 (**FORECAST**, McKinsey). — search summary of [McKinsey](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/three-horizons-of-quantum-a-business-road-map-to-the-future-computing-economy)

### Inferences
- Two competing models for the "network OS and ISP" layer are visible:
  - Cisco: an open, multi-vendor control plane and compiler that sits on partner hardware such as Qunnect and Swabian. This is the router-and-IOS playbook.
  - IonQ: vertical integration of memory, interconnect, satellite and defence work, through acquisitions of Lightsynq, Capella and Skyloom.
  - Europe's QIA is building the public-research reference stack (QNodeOS).
- **FORECAST (my inference):** the first indispensable networking product (2030-2035) will be QPU-to-QPU interconnect for modular machines (IonQ, Photonic Inc, Nu Quantum, Xanadu-style architectures). It will be sold as part of a quantum computer, not as a telecom service. A true "quantum ISP" offering entanglement-as-a-service between organisations is more likely after 2035 and will be dominated by telcos or state-backed operators. That is my own inference; no source gives a date.
- Funding is overwhelmingly public or defence: EU QIA, AFRL, DOE (EPB Chattanooga), plus DARPA QuANET (not verified this session). This is a strong signal that the commercial market isn't there yet. It is also open in the sense that standards, protocols and software, like Cisco's v0.2.0 compiler, are still being defined. A small player could plausibly own simulation, emulation or testing tools for quantum networks, or a protocol library, but not the hardware.

### Gaps
- No 2026 data was found on Aliro, Qunnect funding, Welinq, Nu Quantum, Photonic Inc or Xanadu Aurora networking.
- DARPA QuANET status was not verified.
- There is no market sizing for quantum networking hardware.

---

## 5. Verification, certification and trust services for quantum computation

### Takeaway
The only trust product with live commercial footing is certified and quantum randomness. Quantinuum, with JPMorgan Chase, Argonne, ORNL and UT Austin, published certified randomness in Nature in March 2025, and Quantinuum's software QRNG "Quantum Origin" achieved NIST validation. Verifiable or blind delegated quantum computing remains academic, with one or two startups such as VeriQloud. No insurance or SLA market for quantum compute results was found. A "certificate authority for quantum results" is an open niche today but has little demand until quantum advantage becomes classically unverifiable.

### Cited Findings
- Quantinuum and partners (JPMorgan Chase, Argonne, ORNL, UT Austin) demonstrated certified randomness on the H2 trapped-ion processor. Frontier supercomputers verified it with a cross-entropy benchmark, and it was published in Nature. Quantinuum said it would add certified randomness to its commercial portfolio (stated target: 2025). — [Nature](https://www.nature.com/articles/s41586-025-08737-1); [Quantinuum blog](https://www.quantinuum.com/blog/quantinuum-introduces-first-commercial-application-for-quantum-computers); [QCR](https://quantumcomputingreport.com/quantinuum-demonstrates-first-commercial-use-case-for-quantum-computers-with-certified-randomness/)
- The Nature paper certified about 71,313 bits of entropy, using about 1.1 exaFLOPS of classical verification. — [Nature](https://www.nature.com/articles/s41586-025-08737-1) [prior knowledge, not re-fetched]
- Follow-up: an arXiv paper describes certified randomness amplification on Quantinuum Helios using gate-streaming. A 2026 arXiv paper claims "certified randomness with optimal rate". A FOCS 2026 paper by Khurana, Roberts and Tal covers certified randomness without structure. No 2026 product announcement was found. — [arXiv 2511.03686](https://arxiv.org/pdf/2511.03686); [arXiv 2609.38945](https://arxiv.org/pdf/2609.38945)
- Quantinuum's "Quantum Origin" became the first software quantum random number generator to achieve NIST validation. — [Quantinuum press release](https://www.quantinuum.com/press-releases/quantinuums-quantum-origin-becomes-first-software-quantum-random-number-generator-to-achieve-nist-validation)
- Blind and verifiable QC: an Oxford-led team demonstrated verifiable blind quantum computing (Physical Review Letters, Apr 2024). VeriQloud (France) and NanoQT partnered on a blind QC architecture with EUREKA Globalstars-Japan support. A Newcastle University paper accepted at CCS 2026 covers "time-delayed publicly verifiable quantum computation for classical verifiers". Inria (Garnier and Ollivier) discusses practical verified and blind delegated QC. — [Oxford](https://ox.ac.uk/node/8767204); [The Quantum Insider, Apr 2024](https://thequantuminsider.com/2024/04/12/private-quantum-cloud-oxford-university-physicists-make-advance-in-blind-quantum-computing/); [Ground News / QCR on VeriQloud-NanoQT](https://ground.news/article/nanoqt-and-veriqloud-partner-on-blind-quantum-computing-architecture-with-eureka-globalstars-japan-support-quantum-computing-report); [Newcastle University](https://from.ncl.ac.uk/how-can-we-ensure-that-quantum-computer-data-is-trustworthy); [ERCIM News](https://ercim-news.ercim.eu/en128/special/prospects-for-practical-verified-and-blind-delegated-quantum-computations)

### Inferences
- The trust layer has a structural reason to become indispensable later. Once fault-tolerant machines run computations that classical supercomputers can't check (2030+ under vendor roadmaps; **FORECAST**, IBM Starling 2029 and DARPA QBI 2033), customers in finance, pharma and government will need attestation that results came from the claimed machine, ran the claimed circuit, and weren't tampered with. Today's certified-randomness verification already needs an exascale supercomputer, which shows how costly verification is.
- Who is positioned:
  - Quantinuum (randomness, NIST validation), with JPMorgan as the anchor customer.
  - Academic groups (Oxford, Inria/LIP6, Newcastle).
  - Tiny startups such as VeriQloud.
  - National metrology institutes (NIST, NPL, PTB) as the likely "root of trust".
  - No dominant private incumbent exists, so this is among the most open layers.
- Credentials matter more than capital here. A CA-like role needs institutional trust (standards bodies, audit firms, metrology labs). A small player could own open-source verification tooling (a cross-entropy benchmark verifier, a result-attestation format, logging and provenance for quantum cloud jobs) and later partner with an auditor. A capital-light, AI-agent-assisted founder could build the provenance and attestation software, but would struggle to become the trusted authority alone.
- Insurance and SLAs for quantum compute: no evidence found. This is an unclaimed niche, but also has no demand signal yet.

### Gaps
- No 2026 commercial certified-randomness product, pricing or customers were found.
- No evidence of SLA, insurance or audit services for quantum cloud results.
- VeriQloud's funding and status are unknown.
- I did not check whether hyperscalers (AWS Braket, Azure) offer any result-provenance or attestation features.

---

## 6. Application-layer infrastructure: chemistry and materials platforms, quantum-generated data, resource estimation, algorithm marketplaces

### Takeaway
This is the least-covered area of my research. Hardware-agnostic algorithm companies (Phasecraft and others) are funded at tens of millions of dollars and are tied to hardware partners and DARPA QBI. No algorithm marketplace with traction was found. Resource estimation is dominated by free vendor tools. Quantum-generated datasets for AI training look like a plausible future "data infrastructure" layer, but I found no 2026 evidence of a market.

### Cited Findings
- Phasecraft (UK) raised a $34M Series B in Sep 2025, co-led by Plural, Playground Global and Novo Holdings' Quantum Fund. Total funding is reported above $50M; CB Insights lists $63.5M over 7 rounds, so sources conflict. Its focus is hardware-agnostic algorithms for materials, chemistry, energy networks and logistics. — [University of Bristol, Sep 2025](https://www.bristol.ac.uk/news/2025/september/phasecraft.html); [The Quantum Insider, 2 Sep 2025](https://thequantuminsider.com/2025/09/02/phasecraft-raises-34-million-from-plural-playground-global-and-novo-holdings/); [CB Insights](https://www.cbinsights.com/company/phasecraft)
- A June 2026 report says Atom Computing and Phasecraft signed a materials-science algorithms partnership. Phasecraft was also selected by DARPA to contribute to QBI. — search summary (source truncated; verify via [CB Insights](https://www.cbinsights.com/investor/phasecraft))
- McKinsey's Quantum Technology Monitor 2026 (published 28 Apr 2026):
  - **FORECAST:** quantum computing could create $1.3-2.7T in economic value by 2035, with chemicals, life sciences, finance and mobility as the main domains.
  - Quantum-computing company revenue exceeded $1B in 2025 and is projected at up to $4.4B by 2028 (one secondary source gives $3.2-4.4B; **FORECAST**).
  - Start-up investment reached $12.6B in 2025, 6.3x 2024, and 90% of it went to quantum-computing start-ups.
  - Sources: [McKinsey QTM 2026](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point); [PDF](https://www.mckinsey.com/~/media/mckinsey/business%20functions/technology/our%20insights/mckinsey%20quantum%20technology%20monitor%202026%20a%20commercial%20tipping%20point/quantum-technology-monitor-2026.pdf); [PostQuantum critique](https://postquantum.com/industry-news/mckinsey-quantum-monitor-2026/)
- Skeptical note: one analyst argues the "$1B revenue" is mostly research contracts and development partnerships, not scaled commercial deployments. — [PostQuantum](https://postquantum.com/industry-news/mckinsey-quantum-monitor-2026/)
- Resource estimation: Microsoft's Azure Quantum Resource Estimator is free and open source (in the `qsharp` package). Google, PsiQuantum and Riverlane all publish resource estimates for chemistry and cryptanalysis targets. — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/quantum/intro-to-resource-estimation) [prior knowledge, not re-fetched]

### Inferences
- Application-layer "default infrastructure" is most likely to form around (a) curated benchmark problem sets and datasets for chemistry and materials, with ground truth labelled by FT quantum computers and usable for training AI models, and (b) resource-estimation and "quantum-readiness" tools that enterprises use to decide when to buy. Both are software and data. Both are open to small, AI-assisted teams, and the free hyperscaler tools set the price floor at zero.
- **FORECAST (my inference):** quantum-generated simulation datasets (high-accuracy electronic-structure data used to train classical AI models, the way DFT data trains current ML force fields) could become an indispensable "data layer" after the first fault-tolerant machines arrive (2029-2033 on vendor roadmaps). Today a small player could build the schema, the curation pipeline and the classical-baseline datasets. This is speculative; no source documents the market.
- Algorithm marketplaces: no traction evidence found. Historically, attempts (such as the earlier Strangeworks and qBraid marketplaces) have not become defaults.

### Gaps
- I did not research Algorithmiq, QSimulate, Qubit Pharmaceuticals, Kvantify, Microsoft Azure Quantum Elements' 2026 status or Google's application work.
- No data was found on quantum-generated datasets for AI training.
- No 2026 algorithm-marketplace evidence was found.

---

## 7. Cloud access, brokerage and pricing

### Takeaway
Quantum compute is already sold like early cloud GPUs. IBM uses per-minute tiers with committed-use discounts. AWS Braket uses per-task plus per-shot pricing, plus reservations at $2,500-7,000 per hour. I found no evidence of a spot market or of independent brokers gaining ground. AWS Braket and Azure act as the de facto aggregators, and IBM sells direct.

### Cited Findings
- IBM Quantum (as reported Oct-Nov 2026):
  - Open Plan: free, up to 10 min per month.
  - Pay-As-You-Go: $96/min, billed per second.
  - Flex: from $72/min, with a 400-min annual minimum.
  - Premium: from $48/min, with a 5,200-min annual minimum.
  - On-prem: by quote.
  - Sources: [quantumcomputingcost.com, IBM pricing](https://quantumcomputingcost.com/ibm-quantum-pricing/); [quantumcomputingcost.com, IBM PAYG](https://quantumcomputingcost.com/provider/ibm-payg/) (third-party aggregator; verify at IBM)
- AWS Braket: $0.30 per task plus a device-specific per-shot fee, e.g. $0.08 per shot on IonQ Forte and $0.000425 on Rigetti Cepheus. Reserving a whole machine is cited at $2,500-7,000 per hour. — [quantumcomputingcost.com, rent a quantum computer](https://quantumcomputingcost.com/rent-a-quantum-computer/); [Eigenorbit](https://eigenorbit.com/library/guides/quantum-computing-cost/) (third-party; verify at AWS)
- qBraid provides cloud access to Azure Quantum and Amazon Braket devices (as of Aug 2025). No acquisition or 2026 growth data was found for qBraid or Strangeworks. — [Wikipedia, cloud-based quantum computing](https://en.wikipedia.org/wiki/Cloud-based_quantum_computing)

### Inferences
- Pricing has three tiers (on-demand, committed and reserved), mirroring the early AWS EC2 model. The roughly 2x discount for commitment (IBM's $96 versus $48 per minute) suggests capacity is not yet scarce enough for spot markets. That is consistent with low commercial demand, per the PostQuantum critique of McKinsey's revenue figure.
- **FORECAST (my inference):** brokers and cost optimisers only become valuable when (a) multiple fault-tolerant vendors offer comparable logical-qubit capacity, and (b) customers have recurring production workloads. Neither is expected before about 2030-2033 on vendor and DARPA timelines. Until then, hyperscaler marketplaces (Braket, Azure) absorb the aggregator role, and independent brokers struggle. A small player could build a cross-vendor cost and benchmark tracker (price per logical operation, queue times) as an information service. Sites like quantumcomputingcost.com show this is cheap to start, but it is a media and data business, not an infrastructure monopoly.

### Gaps
- Primary IBM and AWS pricing pages were not fetched; figures come from third-party aggregators.
- Azure Quantum pricing and credits were not checked.
- No data on Strangeworks or qBraid revenue, acquisitions or customer counts.
- No evidence of spot or auction markets.

---

## 8. Synthesis: ranking the layers and finding a "Bitcoin 2009-2012"-type entry point

### Takeaway
The layers most likely to be indispensable by 2036 are real-time QEC decoding and control, cryogenics and He-3 (for superconducting and spin modalities), and the HPC-QPU integration runtime. These are also the least open: they are being captured by NVIDIA and by vertically integrated vendors, and the supply chain by Bluefors. The most open layers today are the trust and verification layer, open-source decoder and QEC tooling, quantum-network software, and application datasets and resource estimation. They are less certain to become indispensable and are cheap to enter. The closest analogue to early-Bitcoin open infrastructure is open-source QEC and decoder software, plus verification and attestation tooling. These are areas where individuals (for example PyMatching's author) have already set industry defaults, but direct monetisation is weak.

### Cited Findings (the evidence behind the ranking; see sections 1-7 for full citations)
- NVIDIA is consolidating the merchant QEC and integration layer: NVQLink, cudaq-realtime and the CUDA-Q QEC 0.6 plugin interface, plus an equity stake in Riverlane (22 Oct 2026). — [NVIDIA CUDA-Q blog](https://nvidia.github.io/cuda-quantum/blogs/blog/2026/04/14/cudaq-qec-0.6/); [QCR](https://quantumcomputingreport.com/nvidia-takes-strategic-stake-in-riverlane-to-accelerate-real-time-quantum-error-correction-and-gpu-decoder-calibration/)
- IBM is in-sourcing its decoder silicon (a 2 nm Relay-BP ASIC for Starling, 2029 target). — [IBM](https://www.ibm.com/quantum/blog/path-to-ibm-quantum-starling)
- Qiskit leads developer mindshare at 65.4%; CUDA-Q leads planned adoption growth. — [Unitary Foundation 2026](https://unitary.foundation/posts/2026_survey_results/)
- Networking is still at the prototype stage at Cisco, IonQ and QIA, and its funding is mostly public. — [Cisco](https://blogs.cisco.com/news/quantum-networking-gets-a-control-plane); [QuTech](https://qutech.nl/2026/10/16/qutech-coordinates-european-effort-to-build-worlds-first-full-stack-quantum-internet-prototype/)
- Trust: Quantinuum's certified randomness and NIST-validated QRNG are the only commercial-grade products; blind and verifiable QC is academic. — [Nature](https://www.nature.com/articles/s41586-025-08737-1); [Quantinuum](https://www.quantinuum.com/press-releases/quantinuums-quantum-origin-becomes-first-software-quantum-random-number-generator-to-achieve-nist-validation)
- He-3 is a hard bottleneck covered by a forward contract (Bluefors-Interlune, 2028-2037). — [PostQuantum](https://postquantum.com/building-quantum-computers/quantum-cryogenic-infrastructure-helium3/)
- Capital is abundant at the top: $12.6B in 2025 start-up investment, 90% to computing (McKinsey). — [McKinsey QTM 2026](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point)
- Past roadmap slips call for caution on all timing. IBM's Kookaburra (2026) delivery is unconfirmed, and DARPA advanced only 4 of 11 Stage B teams to Stage C in Oct 2026. — [Qntonsol](https://www.qntonsol.com/learn/ibm-quantum-roadmap-to-starling.html); [Entangled Future](https://entangledfuture.com/stack/darpa-qbi/)

### Inferences: ranking table (my own judgement from the evidence above; all 2036 probabilities are **FORECAST, author inference**)

| Layer | (a) P(indispensable by 2036) | (b) Openness to new entrants, Nov 2026 | (c) Capital and credentials needed | Likely owners, Nov 2026 | Small-player foothold |
|---|---|---|---|---|---|
| Real-time QEC decoding (hardware and runtime) | Very high (every FT machine needs it) | Low (NVIDIA plus Riverlane, IBM/Google/Quantinuum in-house) | High: FPGA/ASIC teams, $10M+ | NVIDIA (NVQLink, CUDA-Q QEC, stake in Riverlane), Riverlane, IBM, Google, Quantinuum | Decoder/pre-decoder plugins, QEC calibration and noise-learning tools |
| Decoder algorithms and QEC simulation (open source) | High as a de facto standard; low as a business | **Very high** (open source, cheap, PyMatching precedent) | Low capital; deep expertise | Google (Stim, PyMatching, Tesseract), IBM (Relay-BP), NVIDIA (open Ising models) | **Best "Bitcoin-like" entry point**: publish a better decoder or tool and become a default |
| Control electronics | Very high | Low to medium | High (RF and cryo engineering) | Quantum Machines, Qblox, Zurich Instruments, Keysight | Minimal |
| HPC-QPU integration runtime and scheduler | High | Low (NVIDIA) to medium (HPC schedulers, EuroHPC middleware) | Medium | NVIDIA, IBM, EuroHPC centres (LRZ, Jülich) | Scheduler plugins, integration consulting |
| Cryogenics and He-3 | High for superconducting and spin modalities; depends on which modality wins | Very low | Very high | Bluefors (with Interlune forward supply), Oxford Instruments, Maybell | He-3 recovery and recycling services, supply analytics (niche) |
| Quantum data-centre hosting | Medium-high | Medium | High (facilities) | Equinix, IBM, EuroHPC/LRZ, OQC colocation | Site-readiness certification and engineering services |
| SDK / "OS" / compiler | High (but commoditised) | Medium for high-level tools; low for the runtime | Low to medium | IBM Qiskit, NVIDIA CUDA-Q, Quantinuum Guppy/Nexus, Classiq | Logical-level (FT) compilation tools, AI coding agents for quantum |
| Quantum networking hardware | Medium (QPU interconnect high; public quantum internet low) | Low | High | IonQ (Lightsynq), Cisco (prototypes), Qunnect, Photonic, Nu Quantum | Minimal |
| Quantum network OS and control software | Medium | **High** (Cisco v0.2.0; standards unset) | Low to medium | Cisco (Outshift), QuTech/QIA (QNodeOS) | Network emulators, protocol libraries, entanglement-routing software |
| Verification, certification and trust | Medium now; high after FT advantage (2030s) | **Very high** (no private incumbent) | Low capital; high institutional credentials | Quantinuum (+JPMorgan), metrology labs, academia, VeriQloud | **Second-best entry point**: open attestation and provenance tooling, verifier software; partner with auditors and metrology labs |
| Application datasets and resource estimation | Medium | High | Low to medium (domain expertise) | Microsoft (free estimator), Phasecraft, Google, PsiQuantum | Curated chemistry and materials benchmark datasets; enterprise "quantum readiness" estimators |
| Cloud brokerage and pricing | Low to medium (hyperscalers absorb it) | High but low-value | Low | AWS Braket, Azure, IBM direct; qBraid and Strangeworks marginal | Price and benchmark information services |

Further synthesis inferences:
- The pattern mirrors AI. The highest-probability "indispensable" layers (decoding, control, integration runtime, cryogenics) need capital and credentials and are already being captured by NVIDIA, IBM, Bluefors and the control vendors. This is analogous to the 2012-2016 GPU and InfiniBand capture in AI. No layer is both highly likely to be indispensable and still cheap to enter, except open-source QEC and decoder software and verification tooling. Even there, the payoff is reputation and acquisition, not a self-sustaining toll-booth like early Bitcoin mining or early domain names.
- Timing risk (**FORECAST**, based on vendor roadmaps: IBM Starling 2029, DARPA QBI utility-scale verification by 2033): any layer whose demand depends on fault-tolerant machines generates meaningful revenue only from about 2029-2033. Past slips (Kookaburra unconfirmed; only 4 of 11 QBI teams advanced) argue for adding 2-4 years.
- Realistic opportunities for a capital-light, AI-agent-assisted founder today:
  - (1) Open-source decoder, pre-decoder or QEC-calibration tools that plug into CUDA-Q QEC's `decoder.h` or Riverlane's QECi.
  - (2) Verification and attestation software for quantum cloud results (provenance logs, verifiers for certified-randomness or cross-entropy protocols).
  - (3) Quantum-network emulation and protocol software, while Cisco's stack is at v0.2.0.
  - (4) Chemistry and materials benchmark datasets and resource-estimation front ends.
  - All four are open and cheap now, but none is guaranteed to become a moat. The likeliest exit is acquisition by NVIDIA, IBM, Quantinuum, Cisco or a hyperscaler.

### Gaps
- The ranking is qualitative. No source provides probabilities, and they are my inferences from the cited evidence.
- Revenue by layer (control, decoding, cryogenics, networking) was not found in McKinsey or elsewhere.
- Missing from this session: Bluefors financials, Quantum Machines / Qblox / ZI revenues, Microsoft and Google 2026 stack strategy, Pasqal and QuEra software, Chinese ecosystem (Origin Quantum, CAS networks), and Japanese ecosystem (RIKEN, Fujitsu). Global scope is therefore weighted toward the US and EU.
