# Registre horodaté des affirmations quantiques (v0)

> Vue générée par `generer_vue.py` à partir de `affirmations.jsonl` : 158 affirmations, dernière saisie le 2026-11-22, dernière consultation de source le 2026-11-22. Ne pas modifier ce fichier à la main : corriger le JSONL, lancer `valider.py`, puis régénérer.

Ce registre consigne les affirmations datées sur la route de l'informatique quantique tolérante aux fautes et du Q-Day (l'arrivée d'un ordinateur quantique capable de casser la cryptographie à clé publique) : feuilles de route des fabricants, démonstrations publiées, étapes de la DARPA, revendications d'avantage et leurs contestations, estimations de ressources pour RSA et les courbes elliptiques, enquêtes d'experts, marchés prédictifs, prix publics, projections et résultats financiers.

## Méthode : consigner sans trancher

- Chaque ligne reprend une affirmation telle que sa source la formule, avec l'URL, la date de l'affirmation, la date de consultation et un statut. Le registre ne juge pas lui-même si un résultat de physique « tient » une promesse.
- Un statut autre que « promis », « annoncé ou publié » ou « inconnu » doit citer la source qui le fonde : publication à comité de lecture, annonce de la DARPA, dépôt réglementaire, mesure indépendante, ou déclaration ultérieure de l'acteur lui-même. Le lien figure dans la colonne Statut.
- Les conflits d'intérêts connus sont notés (fabricant qui estime sa propre feuille de route, vendeur à découvert, enquête financée par un fabricant).
- Une contestation est une entrée à part, de type « réfutation ou contestation », liée à l'affirmation visée. L'affirmation garde son statut tant qu'aucune source ne la dit réfutée.
- Les métriques des autres (Metriq, DARPA, publications évaluées par les pairs) sont reprises, pas recalculées.

## Politique de correction

- Une correction est une nouvelle ligne ou une mise à jour de statut qui cite sa source (`statut_source_url`, `statut_date`).
- Un identifiant ne change jamais et une ligne n'est jamais supprimée sans trace : l'historique est celui du dépôt git, et chaque modification passe par un commit qui en donne la raison.
- Une erreur matérielle (URL, chiffre mal recopié) se corrige en place, avec la source dans le message de commit.
- Les demandes de correction des acteurs cités sont acceptées si elles s'appuient sur une source publique.

## Lire les statuts

| Code | Libellé | Signification |
|---|---|---|
| `promis` | promis | Engagement ou cible future, non échue, ou sans information de livraison postérieure. |
| `demontre` | annoncé ou publié | L'acteur a publié ou annoncé le résultat, le chiffre ou la cible ; aucune vérification indépendante n'est revendiquée. |
| `verifie_tiers` | vérifié par un tiers | Un tiers indépendant (revue à comité de lecture, DARPA, reproduction, attribution d'un prix) le confirme ; la source du statut est indiquée. |
| `contredit` | contredit | Une source tierce ou un dépôt ultérieur rapporte un résultat contraire ou le réfute ; la source du statut est indiquée. |
| `en_retard` | en retard | L'échéance est passée sans livraison constatée par une source ; la source du statut est indiquée. |
| `retire` | retiré ou remplacé | L'acteur lui-même a retiré ou remplacé l'affirmation ; la source du statut est indiquée. |
| `inconnu` | inconnu, à vérifier | Fait non vérifié, contradictoire ou connu par un simple résumé, ou échéance passée sans information. |

Une date précédée de « ≤ » signifie que la source n'est pas datée : l'affirmation existait au plus tard à cette date. Une année ou un mois seuls indiquent la précision de la source. Les énoncés sont dans la langue de la source et peuvent être tronqués ici ; le JSONL contient le texte complet, les notes et les sources complémentaires.

## Vue d'ensemble

158 affirmations, dont 23 au statut « inconnu, à vérifier » et 40 tirées de sources non datées.

| Type | Entrées |
|---|---|
| feuille de route | 44 |
| démonstration | 20 |
| prix | 15 |
| enquête ou avis d'experts | 14 |
| programme public | 14 |
| financement | 13 |
| estimation de ressources | 12 |
| résultat financier | 12 |
| réfutation ou contestation | 7 |
| marché prédictif | 4 |
| revendication d'avantage | 3 |

| Statut | Entrées |
|---|---|
| annoncé ou publié | 87 |
| promis | 39 |
| inconnu, à vérifier | 23 |
| contredit | 5 |
| retiré ou remplacé | 2 |
| vérifié par un tiers | 2 |

## Q-Day : estimations de ressources, enquêtes et marchés

Estimations publiées du coût d'une attaque contre RSA-2048 ou les courbes elliptiques, plus grande clé cassée publiquement, enquêtes et avis d'experts, marchés prédictifs, et contestations qui les visent. « Horizon » désigne l'échéance de la question posée.

| Date | Acteur | Type | Métrique | Valeur | Horizon | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|---|
| 2017 | Roetteler, Naehrig, Svore, Lauter | estimation de ressources | qubits logiques | ≈ 2 330 qubits<br>≈ 130 Md portes (portes Toffoli) | — | annoncé ou publié | The 2017 reference estimate for 256-bit elliptic curves: about 2,330 logical qubits and about 1.3×10^11 Toffolis, roughly 1,000-2,000x more Toffolis than the 2026 Google figure.<br><sub>`roetteler-ecc256-2017`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |
| 2019 | Google | estimation de ressources | qubits physiques | ≈ 20 M qubits | — | annoncé ou publié | The 2019 Gidney-Ekerå estimate: 20 million noisy qubits to factor RSA-2048.<br><sub>`google-gidney-ekera-rsa2048-2019`</sub> | [Google Security blog, tracking the cost of quantum factoring](https://blog.google/security/tracking-cost-of-quantum-factori/) (vendeur) |
| 2025-05-21 | Google | estimation de ressources | qubits physiques | < 1 M qubits<br>< 7 jours (durée d'exécution) | — | annoncé ou publié | Factoring 2048-bit RSA in under a week with under 1 million noisy qubits, a 20x reduction from the 2019 Gidney-Ekerå figure.<br><sub>`google-gidney-rsa2048-2025-05`</sub> | [arXiv 2505.15917 (Gidney)](https://arxiv.org/abs/2505.15917) (preprint) |
| 2025-11 | Adam Back (Blockstream) | enquête ou avis d'experts | horizon d'un CRQC | 20-40 ans | — | annoncé ou publié | “no meaningful quantum threat”, at least 20-40 years away.<br><sub>`adam-back-horizon-2025-11`</sub> | [Cointelegraph, 23 Jul 2026](https://cointelegraph.com/news/strategy-consortium-15m-quantum-proof-bitcoin) (presse) |
| 2026 | Webster et al. (architecture Pinnacle) | estimation de ressources | qubits physiques | ≈ 100 000 qubits | — | annoncé ou publié | Pinnacle architecture: RSA-2048 on qLDPC codes at about 100,000 qubits.<br><sub>`pinnacle-rsa2048-qldpc-2026`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |
| ≤ 2026-01-23 | Morningstar | enquête ou avis d'experts | horizon de commercialisation | 5-10 ans<br>≈ 20 ans (usage général) | — | inconnu, à vérifier | Morningstar is cited as putting early commercialization 5-10 years away and general-use quantum computing about 20 years out.<br><sub>`morningstar-commercialisation`</sub> | [Motley Fool, 23 Jan 2026](https://www.fool.com/investing/2026/01/23/predict-quantum-computing-ionq-rigetti-d-wave-buy/) (presse) |
| 2026-01-29 | Benchmark | enquête ou avis d'experts | horizon d'un CRQC | risque « long-dated and manageable » | — | annoncé ou publié | Bitcoin's quantum risk is “long-dated and manageable”.<br><sub>`benchmark-horizon-2026-01`</sub> | [The Block, 29 Jan 2026](https://www.theblock.co/news/regulation/2026-01-29-bitcoins-quantum-risk-long-dated-benchmark-pushes-back-panic-387704) (presse) |
| 2026-02 | CoinShares | enquête ou avis d'experts | horizon d'un CRQC | ≥ 10 ans | — | annoncé ou publié | A break needs machines about 100,000x more powerful than today's largest, so the threat is “at least a decade away”.<br><sub>`coinshares-horizon-2026-02`</sub> | [The Block, 8 Feb 2026 (CoinShares)](https://www.theblock.co/post/388969/coinshares-says-only-10200-btc-face-real-quantum-risk) (presse) |
| 2026-03 | Oratomic / Caltech | estimation de ressources | qubits physiques | ≈ 26 000 qubits<br>quelques jours (durée d'exécution) | — | annoncé ou publié | A P-256 attack in a few days on about 26,000 neutral atoms.<br><sub>`oratomic-p256-2026-03`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |
| 2026-03-09 | Global Risk Institute / evolutionQ | enquête ou avis d'experts | probabilité d'un CRQC | 28-49 %<br>10 ans (horizon d'un CRQC) | — | annoncé ou publié | A CRQC within 10 years is “quite possible (28-49%)”; the timeline “has accelerated from previous reports”.<br><sub>`gri-2025-dix-ans`</sub> | [GRI, Quantum Threat Timeline Report 2025](https://globalriskinstitute.org/publication/quantum-threat-timeline-report-2025b/) (enquete) |
| 2026-03-09 | Global Risk Institute / evolutionQ | enquête ou avis d'experts | probabilité d'un CRQC | 51-70 %<br>15 ans (horizon d'un CRQC)<br>≈ 69 % (part des répondants, experts à 50 % ou plus à 15 ans)<br>92 % (part des répondants, experts à 50 % ou plus à 20 ans) | — | annoncé ou publié | A CRQC within 15 years is “likely (51-70%)”; about 69% of experts put it at 50% or more at 15 years and 92% at 20 years.<br><sub>`gri-2025-quinze-ans`</sub> | [GRI, Quantum Threat Timeline Report 2025](https://globalriskinstitute.org/publication/quantum-threat-timeline-report-2025b/) (enquete) |
| 2026-03-30 | Google | estimation de ressources | qubits logiques | < 1 450 qubits<br>< 70 M portes (portes Toffoli)<br>< 500 000 qubits (qubits physiques) | — | annoncé ou publié | Low-gate variant: under 1,450 logical qubits and under 70M Toffolis.<br><sub>`google-secp256k1-2026-03-variante-portes`</sub> | [arXiv 2603.28846, Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities](https://www.alphaxiv.org/abs/2603.28846v1) (preprint) |
| 2026-03-30 | Google | estimation de ressources | qubits logiques | < 1 200 qubits<br>< 90 M portes (portes Toffoli)<br>< 500 000 qubits (qubits physiques)<br>18-23 minutes (durée d'exécution, exécution complète) | — | annoncé ou publié | Low-qubit variant: under 1,200 logical qubits and under 90M Toffolis; under 500,000 physical qubits on superconducting hardware at 1e-3 error with surface code; full run about 18-23 minutes.<br><sub>`google-secp256k1-2026-03-variante-qubits`</sub> | [arXiv 2603.28846, Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities](https://www.alphaxiv.org/abs/2603.28846v1) (preprint) |
| 2026-04 | Presidio Bitcoin | enquête ou avis d'experts | probabilité d'un CRQC | 50 % | 2035 | inconnu, à vérifier | “most experts assign a 50% probability to CRQCs emerging by 2030-2035”.<br><sub>`presidio-cinquante-pct-2030-2035`</sub> | [Presidio Bitcoin Quantum Readiness v1 (Apr 2026)](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf) (analyste) |
| 2026-04-08 | Bernstein | enquête ou avis d'experts | horizon d'un CRQC | 3-5 ans | — | annoncé ou publié | Bitcoin has “roughly three to five years to prepare”; quantum is a “manageable upgrade cycle”.<br><sub>`bernstein-horizon-2026-04`</sub> | [The Block, Bernstein (8 Apr 2026)](https://www.theblock.co/post/396709/bernstein-says-quantum-is-a-manageable-upgrade-cycle-for-bitcoin-not-an-existential-threat) (presse) |
| 2026-04-21 | Coinbase Independent Advisory Board on Quantum Computing and Blockchain | enquête ou avis d'experts | horizon d'un CRQC | aucun CRQC à ce jour ; préparation sur plusieurs années | — | annoncé ou publié | No CRQC exists yet, but preparation “will take years”; the exposure is wallet signatures, not mining or hashes.<br><sub>`coinbase-conseil-2026-04`</sub> | [UCSB, Coinbase board paper](https://cs.ucsb.edu/happenings/announcement/no-quantum-threat-yet-crypto-must-prepare-now-says-coinbase-board-paper-co) (autre) |
| 2026-04-24 | Project Eleven | démonstration | taille de clé cassée | 15 bits<br>≈ 70 qubits (qubits physiques) | — | **vérifié par un tiers** ([source du statut](https://www.coindesk.com/tech/2026/04/24/researcher-wins-1-bitcoin-bounty-for-largest-quantum-attack-on-underlying-tech)) | A 15-bit elliptic-curve key (search space 32,767) was broken by Giancarlo Lelli on about 70 qubits of public cloud hardware; it won Project Eleven's 1 BTC Q-Day Prize and was 512x larger than the pre…<br><sub>`project-eleven-q-day-prize-15-bits-2026-04`</sub> | [CoinDesk, 24 Apr 2026](https://www.coindesk.com/tech/2026/04/24/researcher-wins-1-bitcoin-bounty-for-largest-quantum-attack-on-underlying-tech) (presse) |
| ≤ 2026-05-09 | QuEra | enquête ou avis d'experts | part des répondants | 37,2 %<br>5,6 % (dans 1-2 ans)<br>37,5 % (dans 6-10 ans)<br>16,8 % (au-delà de 10 ans) | — | annoncé ou publié | 5.6% expect “quantum superiority” within 1-2 years, 37.2% in 3-5 years, 37.5% in 6-10 years and 16.8% beyond 10 years (n=291).<br><sub>`quera-enquete-preparation-2026`</sub> | [QuEra, 2026 Quantum Readiness Survey Report](https://cdn.prod.website-files.com/643b94c382e84463a9e52264/6a8ef54f5ca422cd30d018e4_Full_2026_Quantum_Readiness_Survey_Report.pdf) (enquete) |
| 2026-07 | Luo et al. | estimation de ressources | qubits logiques | 835 qubits | — | annoncé ou publié | Luo et al. (July 2026) claim 835 logical qubits.<br><sub>`luo-secp256k1-2026-07`</sub> | [PostQuantum, the ECC circuit floor](https://postquantum.com/post-quantum/quantum-attack-ecc-circuit-floor/) (analyste) |
| 2026-08-17 | S&P Global | enquête ou avis d'experts | horizon de la tolérance aux fautes | 2027-2030 | — | annoncé ou publié | Most major vendors target 2027-2030 for fault tolerance.<br><sub>`sp-global-tolerance-fautes-2027-2030`</sub> | [S&P Global, Quantum Quarterly Q2 2026](https://www.spglobal.com/energy/en/technology-ai-research-insights/blogs/quantum-quarterly-q2-2026) (analyste) |
| ≤ 2026-09 | PostQuantum | réfutation ou contestation | appréciation qualitative | résultat très sensible au taux d'erreur physique supposé | — | annoncé ou publié | The memory-failure bound reaches about 89% at 1.5e-4 physical error, so the result is very sensitive to that assumption; the press release said “expected to break” while the paper says “per attempt”.<br><sub>`postquantum-critique-ionq-secp256k1`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |
| 2026-09-08 | IonQ | estimation de ressources | qubits physiques | 19 397 qubits<br>1 457 qubits (qubits logiques)<br>≈ 39 M portes (portes Toffoli)<br>≈ 25,7 jours (durée d'exécution, par tentative)<br>63,3 % (probabilité de succès, heuristique d'Ekerå)<br>40,7 % (probabilité de succès, borne rigoureuse) | — | annoncé ou publié | 19,397 trapped-ion physical qubits, 1,457 logical qubits, about 39M Toffolis; about 25.7 days per attempt with 63.3% success (Ekerå heuristic) or 40.7% (rigorous bound).<br><sub>`ionq-secp256k1-2026-09`</sub> | [The Quantum Insider, 8 Sep 2026](https://thequantuminsider.com/2026/09/08/ionq-estimates-20000-qubit-machine-could-break-bitcoin-secp256k1-26-days/) (presse) |
| 2026-10-27 | QuEra | estimation de ressources | réduction du surcoût | ≤ 230 fois | — | annoncé ou publié | qLDPC codes from QuEra and Alice & Bob reportedly cut physical-qubit overhead “up to 230-fold” versus rotated surface codes.<br><sub>`quera-alice-bob-qldpc-230x`</sub> | [Quantum Computing Report / GQI, Q3 2026 State of Play](https://quantumcomputingreport.com/gqi-q3-2026-state-of-play-investment-consolidation-accelerating-q-day-horizons-and-the-shift-to-second-generation-architectures/) (analyste) |
| ≤ 2026-11-22 | Cain et al. | estimation de ressources | qubits physiques | ≈ 10 000 qubits | — | inconnu, à vérifier | Cain et al. put the neutral-atom floor for an elliptic-curve attack at about 10,000 atoms.<br><sub>`cain-plancher-atomes-neutres`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |
| ≤ 2026-11-22 | Global Risk Institute / evolutionQ | enquête ou avis d'experts | probabilité d'un CRQC | 17-34 % | 2034 | annoncé ou publié | The 2024 edition gave 17-34% by 2034.<br><sub>`gri-2024-horizon-2034`</sub> | [PostQuantum summary of the GRI Quantum Threat Timeline Report](https://postquantum.com/security-pqc/quantum-threat-timeline-report-2025/) (analyste) |
| ≤ 2026-11-22 | Kalshi | marché prédictif | probabilité de marché | 6,8 % | 2026-12-31 | inconnu, à vérifier | “First useful quantum computer”: “Before 2027” at 6.8%.<br><sub>`kalshi-premier-ordinateur-utile-2027`</sub> | [Kalshi, first useful quantum computer](https://kalshi.com/markets/kxquantum/quantum/kxquantum) (autre) |
| ≤ 2026-11-22 | Manifold | marché prédictif | probabilité de marché | ≈ 22 % | 2029-12-31 | inconnu, à vérifier | “RSA broken before 2030”: about 22%.<br><sub>`manifold-rsa-2030`</sub> | [Manifold, will quantum computing break RSA](https://manifold.markets/Dig/will-quantum-computing-break-rsa-en) (autre) |
| ≤ 2026-11-22 | Michele Mosca (evolutionQ) | enquête ou avis d'experts | probabilité d'un CRQC | 33 % | 2035 | annoncé ou publié | “a 33% chance that Q-Day will hit us before 2035”.<br><sub>`mosca-q-day-2035`</sub> | [TelecomTV, could Q-Day be an existential threat](https://www.telecomtv.com/content/security/could-q-day-be-an-existential-threat-to-digital-economies-52754/) (presse) |
| 2026-11-22 | Polymarket | marché prédictif | probabilité de marché | 2 %<br>2 840 USD (volume du marché) | 2026-12-31 | inconnu, à vérifier | “Quantum breaks Bitcoin by ___?”: Dec 31 2026 at 2% (volume $2,840).<br><sub>`polymarket-bitcoin-2026`</sub> | [Polymarket, Quantum breaks Bitcoin by](https://polymarket.com/event/quantum-breaks-bitcoin-by) (autre) |
| 2026-11-22 | Polymarket | marché prédictif | probabilité de marché | 12 %<br>1 512 USD (volume du marché) | 2027-12-31 | inconnu, à vérifier | “Quantum breaks Bitcoin by ___?”: Dec 31 2027 at 12% (volume $1,512).<br><sub>`polymarket-bitcoin-2027`</sub> | [Polymarket, Quantum breaks Bitcoin by](https://polymarket.com/event/quantum-breaks-bitcoin-by) (autre) |
| ≤ 2026-11-22 | Michael Saylor (Strategy) | enquête ou avis d'experts | horizon d'un CRQC | > 10 ans | — | annoncé ou publié | The quantum threat to Bitcoin is more than 10 years out; he expects a coordinated global upgrade if the risk emerges.<br><sub>`saylor-horizon-plus-de-dix-ans`</sub> | [Cointelegraph, Saylor on the quantum threat](https://cointelegraph.com/news/saylor-says-quantum-threat-to-bitcoin-is-more-than-10-years-out-expects-coordinated-global-upgrade-if-risk-emerges) (presse) |
| ≤ 2026-11-22 | Schrottenloher | estimation de ressources | qubits logiques | ≈ 1 192 qubits<br>≈ 1 446 qubits (variante optimisée en portes) | — | annoncé ou publié | An independent reproduction by Schrottenloher reported about 1,192 logical qubits (space-optimised) and 1,446 (gate-optimised).<br><sub>`schrottenloher-reproduction-secp256k1`</sub> | [PostQuantum, the ECC circuit floor](https://postquantum.com/post-quantum/quantum-attack-ecc-circuit-floor/) (analyste) |

## Par acteur

Une section par acteur auteur d'au moins une affirmation. Les entrées où il n'est qu'associé (entreprise retenue par un programme, partenaire) portent la mention « via ». Les organisations seulement associées sont regroupées dans le dernier tableau.

[Adam Back (Blockstream)](#acteur-adam-back-blockstream) (1) · [Alice & Bob](#acteur-alice-bob) (2) · [Amazon Web Services (Braket)](#acteur-amazon-web-services-braket) (7) · [Arqit](#acteur-arqit) (3) · [Benchmark](#acteur-benchmark) (1) · [Bernstein](#acteur-bernstein) (1) · [Bitcoin (dépôt des BIP)](#acteur-bitcoin-depot-des-bip) (1) · [Bitcoin Security Consortium](#acteur-bitcoin-security-consortium) (1) · [Cain et al.](#acteur-cain-et-al) (1) · [Circle](#acteur-circle) (1) · [Coinbase Independent Advisory Board on Quantum Computing and Blockchain](#acteur-coinbase-independent-advisory-board-on-quantum-computing-and-blockchain) (1) · [CoinShares](#acteur-coinshares) (1) · [Commission européenne](#acteur-commission-europeenne) (1) · [D-Wave](#acteur-d-wave) (5) · [Daniel Simon](#acteur-daniel-simon) (1) · [DARPA](#acteur-darpa) (8) · [Diraq](#acteur-diraq) (6) · [Ethereum Foundation](#acteur-ethereum-foundation) (3) · [Global Risk Institute / evolutionQ](#acteur-global-risk-institute-evolutionq) (3) · [Google](#acteur-google) (6) · [Gouvernement australien](#acteur-gouvernement-australien) (1) · [Gupte, Ragavan, Zhandry](#acteur-gupte-ragavan-zhandry) (1) · [IBM](#acteur-ibm) (21) · [IonQ](#acteur-ionq) (22) · [IQM](#acteur-iqm) (3) · [Jameson Lopp et co-auteurs (BIP-361)](#acteur-jameson-lopp-et-co-auteurs-bip-361) (1) · [Kalshi](#acteur-kalshi) (1) · [Kerrisdale Capital](#acteur-kerrisdale-capital) (1) · [Luo et al.](#acteur-luo-et-al) (1) · [Maison-Blanche (États-Unis)](#acteur-maison-blanche-etats-unis) (1) · [Manifold](#acteur-manifold) (1) · [Michael Saylor (Strategy)](#acteur-michael-saylor-strategy) (1) · [Michele Mosca (evolutionQ)](#acteur-michele-mosca-evolutionq) (1) · [Microsoft](#acteur-microsoft) (3) · [Microsoft (Azure Quantum)](#acteur-microsoft-azure-quantum) (3) · [Morningstar](#acteur-morningstar) (1) · [NCSC (Royaume-Uni)](#acteur-ncsc-royaume-uni) (1) · [NIST](#acteur-nist) (1) · [NSA](#acteur-nsa) (1) · [NVIDIA](#acteur-nvidia) (4) · [Oratomic / Caltech](#acteur-oratomic-caltech) (1) · [Pasqal](#acteur-pasqal) (3) · [Polymarket](#acteur-polymarket) (2) · [PostQuantum](#acteur-postquantum) (4) · [Presidio Bitcoin](#acteur-presidio-bitcoin) (1) · [Project Eleven](#acteur-project-eleven) (2) · [PsiQuantum](#acteur-psiquantum) (5) · [Quantinuum](#acteur-quantinuum) (17) · [Quantum Advantage Tracker](#acteur-quantum-advantage-tracker) (1) · [Quantum Machines](#acteur-quantum-machines) (2) · [QuEra](#acteur-quera) (3) · [Rigetti](#acteur-rigetti) (10) · [Riverlane](#acteur-riverlane) (5) · [Roetteler, Naehrig, Svore, Lauter](#acteur-roetteler-naehrig-svore-lauter) (1) · [S&P Global](#acteur-s-p-global) (1) · [Schrottenloher](#acteur-schrottenloher) (1) · [Solana Foundation](#acteur-solana-foundation) (1) · [The Times (via Capacity Media)](#acteur-the-times-via-capacity-media) (1) · [US Department of Commerce](#acteur-us-department-of-commerce) (1) · [US Department of Energy](#acteur-us-department-of-energy) (1) · [Webster et al. (architecture Pinnacle)](#acteur-webster-et-al-architecture-pinnacle) (1) · [Xanadu](#acteur-xanadu) (6) · [Organisations seulement associées](#acteurs-associes) (30)

<a id="acteur-adam-back-blockstream"></a>

### Adam Back (Blockstream)

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-11 | enquête ou avis d'experts | horizon d'un CRQC | 20-40 ans | — | annoncé ou publié | “no meaningful quantum threat”, at least 20-40 years away.<br><sub>`adam-back-horizon-2025-11`</sub> | [Cointelegraph, 23 Jul 2026](https://cointelegraph.com/news/strategy-consortium-15m-quantum-proof-bitcoin) (presse) |

<a id="acteur-alice-bob"></a>

### Alice & Bob

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-10-27 | estimation de ressources | réduction du surcoût | ≤ 230 fois | — | annoncé ou publié | (via QuEra) qLDPC codes from QuEra and Alice & Bob reportedly cut physical-qubit overhead “up to 230-fold” versus rotated surface codes.<br><sub>`quera-alice-bob-qldpc-230x`</sub> | [Quantum Computing Report / GQI, Q3 2026 State of Play](https://quantumcomputingreport.com/gqi-q3-2026-state-of-play-investment-consolidation-accelerating-q-day-horizons-and-the-shift-to-second-generation-architectures/) (analyste) |
| ≤ 2026-11-22 | démonstration | jalon | test de décodage GPU de codes LDPC-cat via OPX1000 et NVQLink | — | inconnu, à vérifier | Alice & Bob ran an LDPC-cat GPU decoding test via OPX1000 and NVQLink.<br><sub>`alice-bob-decodage-ldpc-cat-gpu`</sub> | [Quantum Computing Report coverage (Quantum Machines, NVQLink)](https://quantumcomputingreport.com/quantum-machines-demonstrates-sub-microsecond-surface-code-decoding-on-opx1000-using-nvidia-cuda-q-qec-and-nvqlink/) (presse) |

<a id="acteur-amazon-web-services-braket"></a>

### Amazon Web Services (Braket)

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-11-22 | prix | prix par tir | 0,08 USD/tir | — | annoncé ou publié | IonQ Forte on Amazon Braket: $0.08 per shot.<br><sub>`braket-prix-ionq-forte`</sub> | [Amazon Braket pricing](https://aws.amazon.com/braket/pricing/) (vendeur) |
| 2026-11-22 | prix | prix par tir | 0,00145 USD/tir | — | annoncé ou publié | IQM Garnet on Amazon Braket: $0.00145 per shot.<br><sub>`braket-prix-iqm-garnet`</sub> | [Amazon Braket pricing](https://aws.amazon.com/braket/pricing/) (vendeur) |
| 2026-11-22 | prix | prix à l'heure | 2 500-7 000 USD/h | — | annoncé ou publié | Reserved access to a whole machine costs $2,500-7,000 per hour.<br><sub>`braket-prix-reservation`</sub> | [Amazon Braket pricing](https://aws.amazon.com/braket/pricing/) (vendeur) |
| 2026-11-22 | prix | prix par tir | 0,000425 USD/tir | — | annoncé ou publié | Rigetti Cepheus on Amazon Braket: $0.000425 per shot.<br><sub>`braket-prix-rigetti-cepheus`</sub> | [Amazon Braket pricing](https://aws.amazon.com/braket/pricing/) (vendeur) |
| 2026-11-22 | prix | prix à la minute | 0,075 USD/min | — | annoncé ou publié | The SV1 simulator costs $0.075/min.<br><sub>`braket-prix-simulateur-sv1`</sub> | [Amazon Braket pricing](https://aws.amazon.com/braket/pricing/) (vendeur) |
| 2026-11-22 | prix | prix par tâche | 0,3 USD/tâche | — | annoncé ou publié | $0.30 per task plus a device-specific per-shot fee.<br><sub>`braket-prix-tache`</sub> | [Amazon Braket pricing](https://aws.amazon.com/braket/pricing/) (vendeur) |
| 2026-11-22 | prix | prix par tâche | 200,3 USD/tâche | — | annoncé ou publié | One IonQ task with error mitigation (minimum 2,500 shots) costs $200.30.<br><sub>`braket-prix-tache-ionq-mitigation`</sub> | [Amazon Braket pricing](https://aws.amazon.com/braket/pricing/) (vendeur) |

<a id="acteur-arqit"></a>

### Arqit

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2021 | feuille de route | chiffre d'affaires | 660 M USD | 2025 | **contredit** ([source du statut](https://postquantum.com/quantum-commercialization/quantum-spac-wave/)) | SPAC-deck projection: revenue of $660M in 2025.<br><sub>`arqit-spac-ca-2025`</sub> | [PostQuantum, Quantum SPAC wave (14 July 2026)](https://postquantum.com/quantum-commercialization/quantum-spac-wave/) (analyste) |
| ≤ 2026-07-14 | résultat financier | chiffre d'affaires | ≈ 530 000 USD | — | annoncé ou publié | Fiscal year to September 2025 revenue of about $0.53M (Form 20-F).<br><sub>`arqit-ca-exercice-2025`</sub> | [MarketScreener, Arqit annual report FY2025 (Form 20-F)](https://www.marketscreener.com/news/arqit-quantum-annual-report-for-fiscal-year-ending-september-30-2025-form-20-f-ce7d51d2d18dfe24) (presse) |
| ≤ 2026-11-22 | résultat financier | chiffre d'affaires | ≈ 1,2 M USD | — | inconnu, à vérifier | H1 2026 net loss of about US$33.1M on revenue of about US$1.2M.<br><sub>`arqit-s1-2026`</sub> | [Simply Wall St, Arqit Quantum](https://simplywall.st/stocks/us/software/nasdaq-arqq/arqit-quantum) (analyste) |

<a id="acteur-benchmark"></a>

### Benchmark

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-01-29 | enquête ou avis d'experts | horizon d'un CRQC | risque « long-dated and manageable » | — | annoncé ou publié | Bitcoin's quantum risk is “long-dated and manageable”.<br><sub>`benchmark-horizon-2026-01`</sub> | [The Block, 29 Jan 2026](https://www.theblock.co/news/regulation/2026-01-29-bitcoins-quantum-risk-long-dated-benchmark-pushes-back-panic-387704) (presse) |

<a id="acteur-bernstein"></a>

### Bernstein

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-04-08 | enquête ou avis d'experts | horizon d'un CRQC | 3-5 ans | — | annoncé ou publié | Bitcoin has “roughly three to five years to prepare”; quantum is a “manageable upgrade cycle”.<br><sub>`bernstein-horizon-2026-04`</sub> | [The Block, Bernstein (8 Apr 2026)](https://www.theblock.co/post/396709/bernstein-says-quantum-is-a-manageable-upgrade-cycle-for-bitcoin-not-an-existential-threat) (presse) |

<a id="acteur-bitcoin-depot-des-bip"></a>

### Bitcoin (dépôt des BIP)

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-02-11 | programme public | statut de la proposition | Draft | — | annoncé ou publié | BIP-360 (P2MR) was merged into the BIP repo as a Draft, the first quantum proposal to reach that stage; it is not activated and no activation date is scheduled.<br><sub>`bip-360-draft-2026-02`</sub> | [Blockspace, BIP-360 merged](https://blockspace.media/insight/bitcoin-developers-merge-bip-360-in-first-move-to-address-quantum-computing-risks/) (presse) |

<a id="acteur-bitcoin-security-consortium"></a>

### Bitcoin Security Consortium

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-07-23 | financement | montant du financement | 15 M USD<br>≤ 5 M USD (subventions de Galaxy) | — | annoncé ou publié | Consortium led by Strategy with BlackRock as co-lead: $15M over three years for developers securing Bitcoin against quantum; Galaxy separately pledged up to $5M in grants.<br><sub>`consortium-securite-bitcoin-2026-07`</sub> | [Cointelegraph, Strategy consortium $15M](https://cointelegraph.com/news/strategy-consortium-15m-quantum-proof-bitcoin) (presse) |

<a id="acteur-cain-et-al"></a>

### Cain et al.

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-11-22 | estimation de ressources | qubits physiques | ≈ 10 000 qubits | — | inconnu, à vérifier | Cain et al. put the neutral-atom floor for an elliptic-curve attack at about 10,000 atoms.<br><sub>`cain-plancher-atomes-neutres`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |

<a id="acteur-circle"></a>

### Circle

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-05 | feuille de route | jalon | signatures post-quantiques optionnelles (SLH-DSA) sur le mainnet d'Arc | 2026 | promis | Arc, Circle's L1, offers opt-in post-quantum signatures (SLH-DSA) from mainnet, expected in 2026.<br><sub>`circle-arc-signatures-pq-2026`</sub> | [Circle blog, preparing blockchains for Q-Day](https://www.circle.com/blog/preparing-blockchains-for-q-day) (vendeur) |

<a id="acteur-coinbase-independent-advisory-board-on-quantum-computing-and-blockchain"></a>

### Coinbase Independent Advisory Board on Quantum Computing and Blockchain

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-04-21 | enquête ou avis d'experts | horizon d'un CRQC | aucun CRQC à ce jour ; préparation sur plusieurs années | — | annoncé ou publié | No CRQC exists yet, but preparation “will take years”; the exposure is wallet signatures, not mining or hashes.<br><sub>`coinbase-conseil-2026-04`</sub> | [UCSB, Coinbase board paper](https://cs.ucsb.edu/happenings/announcement/no-quantum-threat-yet-crypto-must-prepare-now-says-coinbase-board-paper-co) (autre) |

<a id="acteur-coinshares"></a>

### CoinShares

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-02 | enquête ou avis d'experts | horizon d'un CRQC | ≥ 10 ans | — | annoncé ou publié | A break needs machines about 100,000x more powerful than today's largest, so the threat is “at least a decade away”.<br><sub>`coinshares-horizon-2026-02`</sub> | [The Block, 8 Feb 2026 (CoinShares)](https://www.theblock.co/post/388969/coinshares-says-only-10200-btc-face-real-quantum-risk) (presse) |

<a id="acteur-commission-europeenne"></a>

### Commission européenne

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-06-23 | programme public | échéance de migration post-quantique | 2026-12-31<br>2030-12-31 (cas d'usage à haut risque)<br>2035-12-31 (transition achevée) | 2026-12-31 | promis | Member States should start the transition and have national PQC roadmaps by end-2026; high-risk use cases protected by end-2030; everything done by end-2035.<br><sub>`ue-feuille-de-route-pqc-2025-06`</sub> | [European Commission, coordinated implementation roadmap for the PQC transition](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography) (gouvernement) |

<a id="acteur-d-wave"></a>

### D-Wave

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026 | résultat financier | chiffre d'affaires | 24,6 M USD | — | annoncé ou publié | FY2025 revenue $24.6M (up 179%); net loss $355.1M.<br><sub>`dwave-ca-2025`</sub> | [DatacenterDynamics, FY25 quantum earnings](https://www.datacenterdynamics.com/en/news/quantum-computing-earnings-q4-and-fy25-ionq-d-wave-rigetti-results/) (presse) |
| 2026-05 | financement | montant du financement | ≈ 2 Md USD | — | annoncé ou publié | (via US Department of Commerce) About $2B of CHIPS Act money for minority, non-controlling equity stakes in nine quantum companies, as letters of intent.<br><sub>`chips-participations-quantique-2026-05`</sub> | [TheNextWeb, US $2bn quantum equity stakes](https://thenextweb.com/news/us-2bn-quantum-equity-stakes-chips-act) (presse) |
| 2026-11-10 | résultat financier | chiffre d'affaires | 4,5 M USD<br>10,4 M USD (neuf mois 2026) | — | annoncé ou publié | Q3 2026 revenue $4.5M (up 21%); 9M-2026 revenue $10.4M, down from $21.8M in 9M-2025.<br><sub>`dwave-ca-t3-2026`</sub> | [D-Wave 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001907982/000190798226000180/qbts-20261110xexx991.htm) (depot_reglementaire) |
| 2026-11-10 | feuille de route | qubits physiques | 100 000 qubits | — | promis | D-Wave plans to use CHIPS funding for a 100,000-qubit annealer.<br><sub>`dwave-recuit-100000-qubits`</sub> | [D-Wave 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001907982/000190798226000180/qbts-20261110xexx991.htm) (depot_reglementaire) |
| ≤ 2026-11-22 | feuille de route | qubits logiques | 100 qubits | 2032 | promis | Gate-model roadmap: 100 logical qubits by 2032.<br><sub>`dwave-portes-100-qubits-logiques-2032`</sub> | [D-Wave press release, gate-model roadmap](https://www.dwavequantum.com/company/newsroom/press-release/d-wave-charts-a-new-course-to-fault-tolerant-quantum-computing-with-gate-model-roadmap/) (vendeur) |

<a id="acteur-daniel-simon"></a>

### Daniel Simon

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-08-06 | revendication d'avantage | complexité de l'algorithme | temps polynomial | — | **contredit** ([source du statut](https://eprint.iacr.org/2026/1693)) | A claimed polynomial-time quantum algorithm for the Dihedral Coset Problem that could extend to LWE and approximate SVP, which underpin ML-KEM and ML-DSA.<br><sub>`simon-dcp-reseaux-2026`</sub> | [IACR ePrint 2026/1591](https://eprint.iacr.org/2026/1591) (preprint) |

<a id="acteur-darpa"></a>

### DARPA

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-11 | programme public | nombre d'entreprises | 11 entreprises<br>≤ 15 M USD (montant du financement, par entreprise, pour environ un an) | — | annoncé ou publié | DARPA QBI Stage B named 11 companies, with awards of up to about $15M each for roughly a year.<br><sub>`darpa-qbi-etape-b-2025-11`</sub> | [Nextgov, Nov 2025](https://www.nextgov.com/emerging-tech/2025/11/11-companies-move-second-stage-darpas-quantum-benchmarking-initiative/409405/) (presse) |
| 2026-03 | programme public | appréciation qualitative | atteinte de l'échelle utile jugée probable pour au moins un acteur | 2033 | annoncé ou publié | In March 2026 DARPA's Micah Stoutimore said someone appeared likely to achieve utility scale by 2033; the September 2024 briefing had called this “unlikely”.<br><sub>`darpa-qbi-appreciation-2026-03`</sub> | [PostQuantum, DARPA QBI Stage C](https://postquantum.com/industry-news/darpa-quantum-benchmarking-stage-c/) (analyste) |
| 2026-05 | programme public | jalon | entrée de Quandela en étape A | — | annoncé ou publié | Quandela joined QBI Stage A in May 2026.<br><sub>`darpa-qbi-quandela-etape-a-2026-05`</sub> | [DARPA, 7 Oct 2026](https://www.darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage) (gouvernement) |
| 2026-07 | financement | montant du financement | 125 M USD | — | annoncé ou publié | (via PsiQuantum) PsiQuantum has a $125M expanded agreement with DARPA (July 2026), following $31.8M in September 2025.<br><sub>`psiquantum-darpa-125m-2026-07`</sub> | [PostQuantum, DARPA QBI Stage C](https://postquantum.com/industry-news/darpa-quantum-benchmarking-stage-c/) (analyste) |
| 2026-10 | financement | montant du financement | ≤ 300 M USD<br>51 M USD (première tranche de Diraq) | — | annoncé ou publié | Stage C ceiling of up to $300M per company; Diraq received an initial $51M tranche.<br><sub>`darpa-qbi-etape-c-plafond`</sub> | [PostQuantum, DARPA QBI Stage C](https://postquantum.com/industry-news/darpa-quantum-benchmarking-stage-c/) (analyste) |
| 2026-10 | programme public | jalon | discussion d'un périmètre d'étape C avec la DARPA | — | inconnu, à vérifier | (via Quantinuum) Quantinuum said it was “actively discussing” a Stage C scope with DARPA.<br><sub>`quantinuum-etape-c-discussion-2026-10`</sub> | [Fast Company, DARPA QBI Stage C](https://www.fastcompany.com/91620226/darpa-quantum-benchmarking-initiative-stage-c-announcement) (presse) |
| 2026-10-07 | programme public | nombre d'entreprises | 6 entreprises | — | annoncé ou publié | Atom Computing, Diraq, IBM and IonQ advanced to Stage C, joining Microsoft and PsiQuantum from US2QC; Stage C is a government evaluation of whether utility-scale designs can be built.<br><sub>`darpa-qbi-etape-c-2026-10`</sub> | [DARPA, 7 Oct 2026](https://www.darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage) (gouvernement) |
| ≤ 2026-10-07 | programme public | jalon | déterminer si une approche atteint l'échelle utile | 2033 | promis | Goal: determine whether any approach can reach utility scale (value exceeds cost) by 2033.<br><sub>`darpa-qbi-objectif-2033`</sub> | [DARPA, 7 Oct 2026](https://www.darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage) (gouvernement) |

<a id="acteur-diraq"></a>

### Diraq

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-11 | programme public | nombre d'entreprises | 11 entreprises<br>≤ 15 M USD (montant du financement, par entreprise, pour environ un an) | — | annoncé ou publié | (via DARPA) DARPA QBI Stage B named 11 companies, with awards of up to about $15M each for roughly a year.<br><sub>`darpa-qbi-etape-b-2025-11`</sub> | [Nextgov, Nov 2025](https://www.nextgov.com/emerging-tech/2025/11/11-companies-move-second-stage-darpas-quantum-benchmarking-initiative/409405/) (presse) |
| 2026 | feuille de route | qubits physiques | 150 000 qubits | 2029 | promis | Diraq: 150,000 physical qubits in 2029.<br><sub>`diraq-150000-qubits-2029`</sub> | [PostQuantum, DARPA QBI Stage C](https://postquantum.com/industry-news/darpa-quantum-benchmarking-stage-c/) (analyste) |
| 2026 | feuille de route | qubits physiques | > 2 M qubits | 2031 | promis | Diraq: more than 2M qubits on one chip in 2031.<br><sub>`diraq-2-millions-qubits-2031`</sub> | [PostQuantum, DARPA QBI Stage C](https://postquantum.com/industry-news/darpa-quantum-benchmarking-stage-c/) (analyste) |
| 2026-05 | financement | montant du financement | ≈ 2 Md USD | — | annoncé ou publié | (via US Department of Commerce) About $2B of CHIPS Act money for minority, non-controlling equity stakes in nine quantum companies, as letters of intent.<br><sub>`chips-participations-quantique-2026-05`</sub> | [TheNextWeb, US $2bn quantum equity stakes](https://thenextweb.com/news/us-2bn-quantum-equity-stakes-chips-act) (presse) |
| 2026-10 | financement | montant du financement | ≤ 300 M USD<br>51 M USD (première tranche de Diraq) | — | annoncé ou publié | (via DARPA) Stage C ceiling of up to $300M per company; Diraq received an initial $51M tranche.<br><sub>`darpa-qbi-etape-c-plafond`</sub> | [PostQuantum, DARPA QBI Stage C](https://postquantum.com/industry-news/darpa-quantum-benchmarking-stage-c/) (analyste) |
| 2026-10-07 | programme public | nombre d'entreprises | 6 entreprises | — | annoncé ou publié | (via DARPA) Atom Computing, Diraq, IBM and IonQ advanced to Stage C, joining Microsoft and PsiQuantum from US2QC; Stage C is a government evaluation of whether utility-scale designs can be built.<br><sub>`darpa-qbi-etape-c-2026-10`</sub> | [DARPA, 7 Oct 2026](https://www.darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage) (gouvernement) |

<a id="acteur-ethereum-foundation"></a>

### Ethereum Foundation

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-03-30 | estimation de ressources | qubits logiques | < 1 450 qubits<br>< 70 M portes (portes Toffoli)<br>< 500 000 qubits (qubits physiques) | — | annoncé ou publié | (via Google) Low-gate variant: under 1,450 logical qubits and under 70M Toffolis.<br><sub>`google-secp256k1-2026-03-variante-portes`</sub> | [arXiv 2603.28846, Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities](https://www.alphaxiv.org/abs/2603.28846v1) (preprint) |
| 2026-03-30 | estimation de ressources | qubits logiques | < 1 200 qubits<br>< 90 M portes (portes Toffoli)<br>< 500 000 qubits (qubits physiques)<br>18-23 minutes (durée d'exécution, exécution complète) | — | annoncé ou publié | (via Google) Low-qubit variant: under 1,200 logical qubits and under 90M Toffolis; under 500,000 physical qubits on superconducting hardware at 1e-3 error with surface code; full run about 18-23 minutes.<br><sub>`google-secp256k1-2026-03-variante-qubits`</sub> | [arXiv 2603.28846, Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities](https://www.alphaxiv.org/abs/2603.28846v1) (preprint) |
| ≤ 2026-11-22 | feuille de route | jalon | protection post-quantique complète (Lean Ethereum) | 2029 | promis | Ethereum.org's “Lean Ethereum” roadmap targets 2029 for full post-quantum protection.<br><sub>`ethereum-post-quantique-2029`</sub> | [ethereum.org, future-proofing roadmap](https://ethereum.org/roadmap/future-proofing/) (vendeur) |

<a id="acteur-global-risk-institute-evolutionq"></a>

### Global Risk Institute / evolutionQ

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-03-09 | enquête ou avis d'experts | probabilité d'un CRQC | 28-49 %<br>10 ans (horizon d'un CRQC) | — | annoncé ou publié | A CRQC within 10 years is “quite possible (28-49%)”; the timeline “has accelerated from previous reports”.<br><sub>`gri-2025-dix-ans`</sub> | [GRI, Quantum Threat Timeline Report 2025](https://globalriskinstitute.org/publication/quantum-threat-timeline-report-2025b/) (enquete) |
| 2026-03-09 | enquête ou avis d'experts | probabilité d'un CRQC | 51-70 %<br>15 ans (horizon d'un CRQC)<br>≈ 69 % (part des répondants, experts à 50 % ou plus à 15 ans)<br>92 % (part des répondants, experts à 50 % ou plus à 20 ans) | — | annoncé ou publié | A CRQC within 15 years is “likely (51-70%)”; about 69% of experts put it at 50% or more at 15 years and 92% at 20 years.<br><sub>`gri-2025-quinze-ans`</sub> | [GRI, Quantum Threat Timeline Report 2025](https://globalriskinstitute.org/publication/quantum-threat-timeline-report-2025b/) (enquete) |
| ≤ 2026-11-22 | enquête ou avis d'experts | probabilité d'un CRQC | 17-34 % | 2034 | annoncé ou publié | The 2024 edition gave 17-34% by 2034.<br><sub>`gri-2024-horizon-2034`</sub> | [PostQuantum summary of the GRI Quantum Threat Timeline Report](https://postquantum.com/security-pqc/quantum-threat-timeline-report-2025/) (analyste) |

<a id="acteur-google"></a>

### Google

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2019 | estimation de ressources | qubits physiques | ≈ 20 M qubits | — | annoncé ou publié | The 2019 Gidney-Ekerå estimate: 20 million noisy qubits to factor RSA-2048.<br><sub>`google-gidney-ekera-rsa2048-2019`</sub> | [Google Security blog, tracking the cost of quantum factoring](https://blog.google/security/tracking-cost-of-quantum-factori/) (vendeur) |
| 2024-12 | démonstration | latence de décodage | ≈ 63 µs | — | annoncé ou publié | Google's Willow below-threshold result used real-time decoding at about 63 µs latency (d=5).<br><sub>`google-willow-latence-decodage-2024-12`</sub> | [Quantum Computing Report, Riverlane real-time QEC latency](https://quantumcomputingreport.com/riverlane-demonstrates-real-time-qec-latency-performance-advancements/) (presse) |
| 2025-05-21 | estimation de ressources | qubits physiques | < 1 M qubits<br>< 7 jours (durée d'exécution) | — | annoncé ou publié | Factoring 2048-bit RSA in under a week with under 1 million noisy qubits, a 20x reduction from the 2019 Gidney-Ekerå figure.<br><sub>`google-gidney-rsa2048-2025-05`</sub> | [arXiv 2505.15917 (Gidney)](https://arxiv.org/abs/2505.15917) (preprint) |
| 2026-03-30 | estimation de ressources | qubits logiques | < 1 450 qubits<br>< 70 M portes (portes Toffoli)<br>< 500 000 qubits (qubits physiques) | — | annoncé ou publié | Low-gate variant: under 1,450 logical qubits and under 70M Toffolis.<br><sub>`google-secp256k1-2026-03-variante-portes`</sub> | [arXiv 2603.28846, Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities](https://www.alphaxiv.org/abs/2603.28846v1) (preprint) |
| 2026-03-30 | estimation de ressources | qubits logiques | < 1 200 qubits<br>< 90 M portes (portes Toffoli)<br>< 500 000 qubits (qubits physiques)<br>18-23 minutes (durée d'exécution, exécution complète) | — | annoncé ou publié | Low-qubit variant: under 1,200 logical qubits and under 90M Toffolis; under 500,000 physical qubits on superconducting hardware at 1e-3 error with surface code; full run about 18-23 minutes.<br><sub>`google-secp256k1-2026-03-variante-qubits`</sub> | [arXiv 2603.28846, Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities](https://www.alphaxiv.org/abs/2603.28846v1) (preprint) |
| ≤ 2026-11-22 | feuille de route | nombre de jalons | 6 jalons<br>≈ 1 M qubits (qubits physiques, machine corrigée visée, sans date) | — | promis | Google's public roadmap has six milestones, but its later stages carry no dates or qubit targets; no public timeline or metric commitments for its ~1M-physical-qubit error-corrected machine.<br><sub>`google-feuille-de-route-sans-dates`</sub> | [Tom's Hardware, the future of quantum computing roadmaps](https://www.tomshardware.com/tech-industry/quantum-computing/the-future-of-quantum-computing-the-tech-companies-and-roadmaps-that-map-out-a-coherent-quantum-future) (presse) |

<a id="acteur-gouvernement-australien"></a>

### Gouvernement australien

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-08-24 | financement | montant du financement | 940 M AUD | — | annoncé ou publié | Australia: A$940M into PsiQuantum (2023-24).<br><sub>`psiquantum-australie-940m`</sub> | [The Quantum Insider, Nations at the quantum table](https://thequantuminsider.com/2026/08/24/nations-at-the-quantum-table/) (presse) |

<a id="acteur-gupte-ragavan-zhandry"></a>

### Gupte, Ragavan, Zhandry

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-11-22 | réfutation ou contestation | appréciation qualitative | l'algorithme ne peut pas fonctionner | — | annoncé ou publié | Gupte, Ragavan and Zhandry argue that Simon's algorithm cannot work.<br><sub>`gupte-ragavan-zhandry-refutation-simon`</sub> | [IACR ePrint 2026/1693](https://eprint.iacr.org/2026/1693) (preprint) |

<a id="acteur-ibm"></a>

### IBM

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-06-10 | feuille de route | jalon | Cockatoo, intrication entre modules | 2027 | promis | Cockatoo (2027): inter-module entanglement.<br><sub>`ibm-cockatoo-2027`</sub> | [IBM Quantum blog, 10 June 2025 (large-scale FTQC)](https://www.ibm.com/quantum/blog/large-scale-ftqc) (vendeur) |
| 2025-06-10 | feuille de route | jalon | injection d'états magiques entre modules | 2028 | promis | Magic-state injection across modules is planned for 2028.<br><sub>`ibm-injection-etats-magiques-2028`</sub> | [IBM Quantum blog, 10 June 2025 (large-scale FTQC)](https://www.ibm.com/quantum/blog/large-scale-ftqc) (vendeur) |
| 2025-06-10 | feuille de route | jalon | Kookaburra, premier module mémoire qLDPC | 2026 | promis | Kookaburra (2026), the first qLDPC memory module, on the path to Starling.<br><sub>`ibm-kookaburra-2026`</sub> | [IBM Quantum blog, 10 June 2025 (large-scale FTQC)](https://www.ibm.com/quantum/blog/large-scale-ftqc) (vendeur) |
| 2025-06-10 | feuille de route | jalon | Loon | 2025 | inconnu, à vérifier | IBM roadmap to Starling: Loon (2025) → Kookaburra (2026) → Cockatoo (2027) → Starling (2029).<br><sub>`ibm-loon-2025`</sub> | [IBM Quantum blog, 10 June 2025 (large-scale FTQC)](https://www.ibm.com/quantum/blog/large-scale-ftqc) (vendeur) |
| 2025-06-10 | feuille de route | qubits logiques | 200 qubits<br>100 M portes (opérations logiques, « gates » au sens d'IBM) | 2029 | promis | Starling (2029, Poughkeepsie): “one hundred million gates on 200 logical qubits”, on bivariate-bicycle qLDPC codes.<br><sub>`ibm-starling-2029`</sub> | [IBM Quantum blog, 10 June 2025 (large-scale FTQC)](https://www.ibm.com/quantum/blog/large-scale-ftqc) (vendeur) |
| 2025-11 | programme public | nombre d'entreprises | 11 entreprises<br>≤ 15 M USD (montant du financement, par entreprise, pour environ un an) | — | annoncé ou publié | (via DARPA) DARPA QBI Stage B named 11 companies, with awards of up to about $15M each for roughly a year.<br><sub>`darpa-qbi-etape-b-2025-11`</sub> | [Nextgov, Nov 2025](https://www.nextgov.com/emerging-tech/2025/11/11-companies-move-second-stage-darpas-quantum-benchmarking-initiative/409405/) (presse) |
| 2026-03-16 | prix | minutes gratuites | 180 min/12 mois | — | annoncé ou publié | Since 16 Mar 2026, a promotion adds the equivalent of 180 more minutes over 12 months to the Open Plan.<br><sub>`ibm-open-plan-promotion-2026-03`</sub> | [IBM Quantum blog, Open Plan updates](https://www.ibm.com/quantum/blog/open-plan-updates) (vendeur) |
| 2026-05 | financement | montant du financement | ≈ 2 Md USD | — | annoncé ou publié | (via US Department of Commerce) About $2B of CHIPS Act money for minority, non-controlling equity stakes in nine quantum companies, as letters of intent.<br><sub>`chips-participations-quantique-2026-05`</sub> | [TheNextWeb, US $2bn quantum equity stakes](https://thenextweb.com/news/us-2bn-quantum-equity-stakes-chips-act) (presse) |
| 2026-07-30 | revendication d'avantage | avantage quantique | revendiqué | — | annoncé ou publié | IBM and Algorithmiq claim quantum advantage, presented as a framework for trusted quantum computation beyond classical verification.<br><sub>`ibm-algorithmiq-avantage-2026-07`</sub> | [IBM newsroom, 30 July 2026 (IBM and Algorithmiq)](https://newsroom.ibm.com/2026-07-30-ibm-and-algorithmiq-demonstrate-quantum-advantage,-establishing-a-framework-for-trusted-quantum-computation-beyond-classical-verification) (vendeur) |
| 2026-07-30 | démonstration | qubits logiques | 70 qubits<br>2 415 opérations (opérations logiques, opérations logiques à deux qubits)<br>468 portes (portes T logiques) | — | annoncé ou publié | IBM and UChicago ran 70 logical qubits, 2,415 logical two-qubit operations and 468 logical T gates, with logical error about 10x below physical.<br><sub>`ibm-uchicago-circuits-logiques-2026-07`</sub> | [IBM newsroom, 30 July 2026 (IBM and the University of Chicago)](https://newsroom.ibm.com/2026-07-30-ibm-and-the-university-of-chicago-demonstrate-quantum-advantage,-establishing-trusted-quantum-computation-on-logical-circuits) (vendeur) |
| 2026-10-07 | programme public | nombre d'entreprises | 6 entreprises | — | annoncé ou publié | (via DARPA) Atom Computing, Diraq, IBM and IonQ advanced to Stage C, joining Microsoft and PsiQuantum from US2QC; Stage C is a government evaluation of whether utility-scale designs can be built.<br><sub>`darpa-qbi-etape-c-2026-10`</sub> | [DARPA, 7 Oct 2026](https://www.darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage) (gouvernement) |
| ≤ 2026-11-22 | feuille de route | jalon | ASIC de décodage temps réel en 2 nm pour Starling | — | promis | IBM is building a real-time decoder ASIC on 2 nm nanosheet technology to run Relay-BP on Starling.<br><sub>`ibm-asic-decodeur-2nm`</sub> | [IBM Quantum blog, Tracking progress on the path to Starling](https://www.ibm.com/quantum/blog/path-to-ibm-quantum-starling) (vendeur) |
| ≤ 2026-11-22 | feuille de route | jalon | démontrer l'avantage quantique avec le HPC | 2026 | promis | 2026 milestone: demonstrate quantum advantage with HPC.<br><sub>`ibm-avantage-hpc-2026`</sub> | [IBM roadmap 2026](https://ibm.com/roadmaps/quantum/2026) (vendeur) |
| ≤ 2026-11-22 | feuille de route | qubits logiques | ≈ 2 000 qubits<br>≈ 1 Md opérations (opérations logiques) | 2033 | promis | Blue Jay in 2033+ at about 2,000 logical qubits and about 1B operations.<br><sub>`ibm-blue-jay-2033`</sub> | [IBM Quantum roadmap](https://www.ibm.com/quantum-computing/roadmap) (vendeur) |
| ≤ 2026-11-22 | feuille de route | qubits physiques | ≤ 360 qubits | 2026 | promis | 2026 milestone: Nighthawk up to 360 qubits.<br><sub>`ibm-nighthawk-2026`</sub> | [IBM roadmap 2026](https://ibm.com/roadmaps/quantum/2026) (vendeur) |
| 2026-11-22 | prix | prix à la minute | ≥ 72 USD/min<br>400 min/an (engagement minimal) | — | annoncé ou publié | Flex starts at $72/min with a minimum of 400 min/year.<br><sub>`ibm-prix-flex`</sub> | [IBM Quantum pricing](https://www.ibm.com/quantum/pricing) (vendeur) |
| 2026-11-22 | prix | minutes gratuites | ≤ 10 min/mois | — | annoncé ou publié | Open Plan: free for “up to 10 minutes of runtime per month”.<br><sub>`ibm-prix-open-plan`</sub> | [IBM Quantum pricing](https://www.ibm.com/quantum/pricing) (vendeur) |
| 2026-11-22 | prix | prix à la minute | ≥ 96 USD/min | — | annoncé ou publié | Pay-As-You-Go starts at $96/min, billed per second.<br><sub>`ibm-prix-paygo`</sub> | [IBM Quantum pricing](https://www.ibm.com/quantum/pricing) (vendeur) |
| 2026-11-22 | prix | prix à la minute | ≥ 48 USD/min<br>5 200 min/an (engagement minimal) | — | annoncé ou publié | Premium starts at $48/min with a minimum of 5,200 min/year.<br><sub>`ibm-prix-premium`</sub> | [IBM Quantum pricing](https://www.ibm.com/quantum/pricing) (vendeur) |
| ≤ 2026-11-22 | démonstration | jalon | décodeur Relay-BP conforme aux exigences de Starling | — | annoncé ou publié | IBM says its Relay-BP decoder now meets Starling's performance requirements while lowering decoding compute overhead.<br><sub>`ibm-relay-bp-exigences-starling`</sub> | [IBM Quantum blog, Tracking progress on the path to Starling](https://www.ibm.com/quantum/blog/path-to-ibm-quantum-starling) (vendeur) |
| ≤ 2026-11-22 | revendication d'avantage | nombre de soumissions | ≈ 30 soumissions | — | annoncé ou publié | (via Quantum Advantage Tracker) Launched Nov 2025 by IBM, Algorithmiq, Flatiron Institute and BlueQubit; about 30 submissions on IBM and Quantinuum hardware; classical methods have overturned some claims; entries grouped Active / S…<br><sub>`quantum-advantage-tracker-soumissions`</sub> | [Quantum Advantage Tracker, observable estimations](https://quantum-advantage-tracker.github.io/trackers/observable-estimations) (autre) |

<a id="acteur-ionq"></a>

### IonQ

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2021 | feuille de route | chiffre d'affaires | 237 M USD | 2025 | **contredit** ([source du statut](https://postquantum.com/quantum-commercialization/quantum-spac-wave/)) | SPAC-deck projection: revenue of $237M in 2025.<br><sub>`ionq-spac-ca-2025`</sub> | [PostQuantum, Quantum SPAC wave (14 July 2026)](https://postquantum.com/quantum-commercialization/quantum-spac-wave/) (analyste) |
| 2021 | feuille de route | chiffre d'affaires | 522 M USD | 2026 | promis | SPAC-deck projection: revenue of $522M in 2026.<br><sub>`ionq-spac-ca-2026`</sub> | [PostQuantum, Quantum SPAC wave (14 July 2026)](https://postquantum.com/quantum-commercialization/quantum-spac-wave/) (analyste) |
| 2021 | feuille de route | EBITDA ajusté | 61 M USD | 2025 | **contredit** ([source du statut](https://postquantum.com/quantum-commercialization/quantum-spac-wave/)) | SPAC-deck projection: positive 2025 adjusted EBITDA of $61M.<br><sub>`ionq-spac-ebitda-2025`</sub> | [PostQuantum, Quantum SPAC wave (14 July 2026)](https://postquantum.com/quantum-commercialization/quantum-spac-wave/) (analyste) |
| ≤ 2025-03 | feuille de route | qubits physiques | > 4 000 qubits | 2026 | promis | Qubit roadmap as cited by Kerrisdale: 80-100 physical qubits growing to >4,000 by 2026 and 32,000 by 2028.<br><sub>`ionq-feuille-de-route-2026-kerrisdale`</sub> | [Kerrisdale Capital, IonQ (March 2025)](https://www.kerrisdalecap.com/wp-content/uploads/2025/03/IonQ-%E2%80%93-Kerrisdale.pdf) (analyste) |
| ≤ 2025-03 | feuille de route | qubits physiques | 32 000 qubits | 2028 | promis | Qubit roadmap as cited by Kerrisdale: 32,000 physical qubits by 2028.<br><sub>`ionq-feuille-de-route-2028-kerrisdale`</sub> | [Kerrisdale Capital, IonQ (March 2025)](https://www.kerrisdalecap.com/wp-content/uploads/2025/03/IonQ-%E2%80%93-Kerrisdale.pdf) (analyste) |
| 2025-11 | programme public | nombre d'entreprises | 11 entreprises<br>≤ 15 M USD (montant du financement, par entreprise, pour environ un an) | — | annoncé ou publié | (via DARPA) DARPA QBI Stage B named 11 companies, with awards of up to about $15M each for roughly a year.<br><sub>`darpa-qbi-etape-b-2025-11`</sub> | [Nextgov, Nov 2025](https://www.nextgov.com/emerging-tech/2025/11/11-companies-move-second-stage-darpas-quantum-benchmarking-initiative/409405/) (presse) |
| 2026 | résultat financier | chiffre d'affaires | 130 M USD | — | annoncé ou publié | 2025 full-year revenue $130.0M, net loss $510.4M.<br><sub>`ionq-ca-2025`</sub> | [DatacenterDynamics, FY25 quantum earnings](https://www.datacenterdynamics.com/en/news/quantum-computing-earnings-q4-and-fy25-ionq-d-wave-rigetti-results/) (presse) |
| 2026 | résultat financier | chiffre d'affaires | 173,8 M USD<br>90,3 M USD (segment IonQ Platform)<br>83,5 M USD (SkyWater Foundry Services, acquis)<br>-133,6 M USD (EBITDA ajusté, T3 2026) | — | annoncé ou publié | Q3 2026 revenue $173.8M, up 336% from $39.9M; IonQ Platform $90.3M and SkyWater Foundry Services $83.5M.<br><sub>`ionq-ca-t3-2026`</sub> | [IonQ 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526449779/ionq-ex99_1.htm) (depot_reglementaire) |
| 2026 | feuille de route | chiffre d'affaires | 505-515 M USD | 2026-12-31 | promis | FY2026 guidance raised to $505-515M, with quantum computing revenue expected to grow more than 110%.<br><sub>`ionq-prevision-ca-2026`</sub> | [IonQ 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526449779/ionq-ex99_1.htm) (depot_reglementaire) |
| 2026 | feuille de route | chiffre d'affaires | 225-245 M USD | 2026-12-31 | **retiré ou remplacé** ([source du statut](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526449779/ionq-ex99_1.htm)) | Initial 2026 revenue guidance of $225-245M, given with full-year 2025 results.<br><sub>`ionq-prevision-ca-2026-initiale`</sub> | [DatacenterDynamics, FY25 quantum earnings](https://www.datacenterdynamics.com/en/news/quantum-computing-earnings-q4-and-fy25-ionq-d-wave-rigetti-results/) (presse) |
| 2026-06 | démonstration | qubits physiques | 40 qubits<br>≈ 0,01 par cycle (taux d'erreur logique, meilleur résultat) | — | annoncé ou publié | IonQ's June 2026 qLDPC demonstration used 40 barium ions, with a best logical error near 1% per cycle.<br><sub>`ionq-qldpc-40-ions-2026-06`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |
| 2026-08-17 | feuille de route | qubits physiques | > 256 qubits | — | promis | IonQ targeting >256 physical qubits and first logical-qubit development.<br><sub>`ionq-sp-global-256-qubits`</sub> | [S&P Global, Quantum Quarterly Q2 2026](https://www.spglobal.com/energy/en/technology-ai-research-insights/blogs/quantum-quarterly-q2-2026) (analyste) |
| ≤ 2026-09 | démonstration | erreur de porte à 2 qubits | 8,4×10⁻⁵ | — | annoncé ou publié | A two-qubit error of 8.4e-5 has been measured, but only on two ions.<br><sub>`ionq-erreur-2q-deux-ions`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |
| ≤ 2026-09 | feuille de route | qubits physiques | 20 000 qubits<br>1 600 qubits (qubits logiques) | 2028 | promis | IonQ's own roadmap targets 20,000 physical and 1,600 logical qubits in 2028.<br><sub>`ionq-feuille-de-route-2028`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |
| 2026-09-08 | estimation de ressources | qubits physiques | 19 397 qubits<br>1 457 qubits (qubits logiques)<br>≈ 39 M portes (portes Toffoli)<br>≈ 25,7 jours (durée d'exécution, par tentative)<br>63,3 % (probabilité de succès, heuristique d'Ekerå)<br>40,7 % (probabilité de succès, borne rigoureuse) | — | annoncé ou publié | 19,397 trapped-ion physical qubits, 1,457 logical qubits, about 39M Toffolis; about 25.7 days per attempt with 63.3% success (Ekerå heuristic) or 40.7% (rigorous bound).<br><sub>`ionq-secp256k1-2026-09`</sub> | [The Quantum Insider, 8 Sep 2026](https://thequantuminsider.com/2026/09/08/ionq-estimates-20000-qubit-machine-could-break-bitcoin-secp256k1-26-days/) (presse) |
| 2026-10 | financement | montant du financement | ≤ 300 M USD<br>51 M USD (première tranche de Diraq) | — | annoncé ou publié | (via DARPA) Stage C ceiling of up to $300M per company; Diraq received an initial $51M tranche.<br><sub>`darpa-qbi-etape-c-plafond`</sub> | [PostQuantum, DARPA QBI Stage C](https://postquantum.com/industry-news/darpa-quantum-benchmarking-stage-c/) (analyste) |
| 2026-10-07 | programme public | nombre d'entreprises | 6 entreprises | — | annoncé ou publié | (via DARPA) Atom Computing, Diraq, IBM and IonQ advanced to Stage C, joining Microsoft and PsiQuantum from US2QC; Stage C is a government evaluation of whether utility-scale designs can be built.<br><sub>`darpa-qbi-etape-c-2026-10`</sub> | [DARPA, 7 Oct 2026](https://www.darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage) (gouvernement) |
| 2026-10-16 | financement | montant du financement | 2 Md USD | — | annoncé ou publié | A $2.0B equity offering closed on 16 Oct 2026.<br><sub>`ionq-offre-actions-2026-10`</sub> | [IonQ 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526449779/ionq-ex99_1.htm) (depot_reglementaire) |
| 2026-11-22 | prix | prix par porte-tir | 0,000975 USD/porte-tir<br>0,00022 USD/porte-tir (porte à un qubit) | — | annoncé ou publié | (via Microsoft (Azure Quantum)) IonQ Aria on Azure Quantum: $0.000220 per 1-qubit-gate-shot and $0.000975 per 2-qubit-gate-shot.<br><sub>`azure-prix-ionq-aria`</sub> | [Microsoft Learn, Azure Quantum pricing](https://learn.microsoft.com/azure/quantum/pricing) (vendeur) |
| 2026-11-22 | prix | prix minimal par programme | 168,2 USD/programme | — | annoncé ou publié | (via Microsoft (Azure Quantum)) IonQ Forte on Azure Quantum: minimum $168.20 per program with error mitigation.<br><sub>`azure-prix-ionq-forte-minimum`</sub> | [Microsoft Learn, Azure Quantum pricing](https://learn.microsoft.com/azure/quantum/pricing) (vendeur) |
| 2026-11-22 | prix | prix par tir | 0,08 USD/tir | — | annoncé ou publié | (via Amazon Web Services (Braket)) IonQ Forte on Amazon Braket: $0.08 per shot.<br><sub>`braket-prix-ionq-forte`</sub> | [Amazon Braket pricing](https://aws.amazon.com/braket/pricing/) (vendeur) |
| 2026-11-22 | prix | prix par tâche | 200,3 USD/tâche | — | annoncé ou publié | (via Amazon Web Services (Braket)) One IonQ task with error mitigation (minimum 2,500 shots) costs $200.30.<br><sub>`braket-prix-tache-ionq-mitigation`</sub> | [Amazon Braket pricing](https://aws.amazon.com/braket/pricing/) (vendeur) |

<a id="acteur-iqm"></a>

### IQM

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-02-12 | feuille de route | qubits physiques | 150 qubits | 2026-12 | promis | A second 150-qubit Euro-Q-Exa system is planned for end-2026.<br><sub>`iqm-euro-q-exa-150-qubits-2026`</sub> | [The Quantum Insider, 12 Feb 2026](https://thequantuminsider.com/2026/02/12/europe-launches-euro-q-exa-quantum-computer-germany/) (presse) |
| 2026-02-12 | démonstration | qubits physiques | 54 qubits | — | annoncé ou publié | Euro-Q-Exa unveiled at LRZ (Garching): a 54-qubit system on IQM's Radiance platform.<br><sub>`iqm-euro-q-exa-54-qubits-2026-02`</sub> | [The Quantum Insider, 12 Feb 2026](https://thequantuminsider.com/2026/02/12/europe-launches-euro-q-exa-quantum-computer-germany/) (presse) |
| 2026-11-22 | prix | prix par tir | 0,00145 USD/tir | — | annoncé ou publié | (via Amazon Web Services (Braket)) IQM Garnet on Amazon Braket: $0.00145 per shot.<br><sub>`braket-prix-iqm-garnet`</sub> | [Amazon Braket pricing](https://aws.amazon.com/braket/pricing/) (vendeur) |

<a id="acteur-jameson-lopp-et-co-auteurs-bip-361"></a>

### Jameson Lopp et co-auteurs (BIP-361)

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-04-14 | programme public | délai après activation | ≈ 160 000 blocs | — | annoncé ou publié | BIP-361 Phase A, about 160,000 blocks (~3 years) after activation: no new sends to quantum-vulnerable outputs; later, legacy signatures become invalid (about 5 years after activation).<br><sub>`bip-361-proposition-2026-04`</sub> | [Spark, BIP-361](https://www.spark.money/research/bitcoin-bip-361-quantum-migration-roadmap) (analyste) |

<a id="acteur-kalshi"></a>

### Kalshi

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-11-22 | marché prédictif | probabilité de marché | 6,8 % | 2026-12-31 | inconnu, à vérifier | “First useful quantum computer”: “Before 2027” at 6.8%.<br><sub>`kalshi-premier-ordinateur-utile-2027`</sub> | [Kalshi, first useful quantum computer](https://kalshi.com/markets/kxquantum/quantum/kxquantum) (autre) |

<a id="acteur-kerrisdale-capital"></a>

### Kerrisdale Capital

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-03 | réfutation ou contestation | appréciation qualitative | produit commercialement viable hors de portée | — | annoncé ou publié | IonQ is “nowhere close to producing a commercially viable product” because of “massive scaling challenges & reliance on photonic interconnects”.<br><sub>`kerrisdale-ionq-2025-03`</sub> | [Kerrisdale Capital, IonQ (March 2025)](https://www.kerrisdalecap.com/wp-content/uploads/2025/03/IonQ-%E2%80%93-Kerrisdale.pdf) (analyste) |

<a id="acteur-luo-et-al"></a>

### Luo et al.

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-07 | estimation de ressources | qubits logiques | 835 qubits | — | annoncé ou publié | Luo et al. (July 2026) claim 835 logical qubits.<br><sub>`luo-secp256k1-2026-07`</sub> | [PostQuantum, the ECC circuit floor](https://postquantum.com/post-quantum/quantum-attack-ecc-circuit-floor/) (analyste) |

<a id="acteur-maison-blanche-etats-unis"></a>

### Maison-Blanche (États-Unis)

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-06-22 | programme public | échéance de migration post-quantique | 2030-12-31<br>2031-12-31 (signatures) | 2030-12-31 | promis | EO 14412: high-value assets and high-impact systems use PQC key establishment by 31 Dec 2030 and PQC signatures by 31 Dec 2031.<br><sub>`eo-14412-migration-pqc`</sub> | [Cloud Security Alliance research note, 30 Oct 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ir8547-pqc-transition-20261030-csa-st/) (analyste) |

<a id="acteur-manifold"></a>

### Manifold

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-11-22 | marché prédictif | probabilité de marché | ≈ 22 % | 2029-12-31 | inconnu, à vérifier | “RSA broken before 2030”: about 22%.<br><sub>`manifold-rsa-2030`</sub> | [Manifold, will quantum computing break RSA](https://manifold.markets/Dig/will-quantum-computing-break-rsa-en) (autre) |

<a id="acteur-michael-saylor-strategy"></a>

### Michael Saylor (Strategy)

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-11-22 | enquête ou avis d'experts | horizon d'un CRQC | > 10 ans | — | annoncé ou publié | The quantum threat to Bitcoin is more than 10 years out; he expects a coordinated global upgrade if the risk emerges.<br><sub>`saylor-horizon-plus-de-dix-ans`</sub> | [Cointelegraph, Saylor on the quantum threat](https://cointelegraph.com/news/saylor-says-quantum-threat-to-bitcoin-is-more-than-10-years-out-expects-coordinated-global-upgrade-if-risk-emerges) (presse) |

<a id="acteur-michele-mosca-evolutionq"></a>

### Michele Mosca (evolutionQ)

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-11-22 | enquête ou avis d'experts | probabilité d'un CRQC | 33 % | 2035 | annoncé ou publié | “a 33% chance that Q-Day will hit us before 2035”.<br><sub>`mosca-q-day-2035`</sub> | [TelecomTV, could Q-Day be an existential threat](https://www.telecomtv.com/content/security/could-q-day-be-an-existential-threat-to-digital-economies-52754/) (presse) |

<a id="acteur-microsoft"></a>

### Microsoft

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-06 | démonstration | jalon | prototype Majorana 2, cellule unitaire de 4 qubits | — | inconnu, à vérifier | Majorana 2 prototype (June 2026), a 4-qubit unit cell.<br><sub>`microsoft-majorana-2-2026-06`</sub> | [Andes Qubit, quantum hardware roadmaps 2026-2030](https://andesqubit.com/en/blog/quantum-hardware-roadmaps-2026-2030/) (analyste) |
| 2026-10-07 | programme public | nombre d'entreprises | 6 entreprises | — | annoncé ou publié | (via DARPA) Atom Computing, Diraq, IBM and IonQ advanced to Stage C, joining Microsoft and PsiQuantum from US2QC; Stage C is a government evaluation of whether utility-scale designs can be built.<br><sub>`darpa-qbi-etape-c-2026-10`</sub> | [DARPA, 7 Oct 2026](https://www.darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage) (gouvernement) |
| ≤ 2026-11-22 | feuille de route | jalon | ordinateur tolérant aux fautes à l'échelle | 2029 | inconnu, à vérifier | Goal of a scalable fault-tolerant computer by 2029.<br><sub>`microsoft-tolerance-fautes-2029`</sub> | [Andes Qubit, quantum hardware roadmaps 2026-2030](https://andesqubit.com/en/blog/quantum-hardware-roadmaps-2026-2030/) (analyste) |

<a id="acteur-microsoft-azure-quantum"></a>

### Microsoft (Azure Quantum)

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-11-22 | prix | crédits gratuits | 500 USD par fournisseur<br>≤ 10 000 USD (programme Azure Quantum Credits) | — | annoncé ou publié | First-time users get $500 of credits per participating hardware provider, valid 6 months; the Azure Quantum Credits programme offers up to $10,000 more.<br><sub>`azure-credits`</sub> | [Microsoft Learn, Azure Quantum pricing](https://learn.microsoft.com/azure/quantum/pricing) (vendeur) |
| 2026-11-22 | prix | prix par porte-tir | 0,000975 USD/porte-tir<br>0,00022 USD/porte-tir (porte à un qubit) | — | annoncé ou publié | IonQ Aria on Azure Quantum: $0.000220 per 1-qubit-gate-shot and $0.000975 per 2-qubit-gate-shot.<br><sub>`azure-prix-ionq-aria`</sub> | [Microsoft Learn, Azure Quantum pricing](https://learn.microsoft.com/azure/quantum/pricing) (vendeur) |
| 2026-11-22 | prix | prix minimal par programme | 168,2 USD/programme | — | annoncé ou publié | IonQ Forte on Azure Quantum: minimum $168.20 per program with error mitigation.<br><sub>`azure-prix-ionq-forte-minimum`</sub> | [Microsoft Learn, Azure Quantum pricing](https://learn.microsoft.com/azure/quantum/pricing) (vendeur) |

<a id="acteur-morningstar"></a>

### Morningstar

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-01-23 | enquête ou avis d'experts | horizon de commercialisation | 5-10 ans<br>≈ 20 ans (usage général) | — | inconnu, à vérifier | Morningstar is cited as putting early commercialization 5-10 years away and general-use quantum computing about 20 years out.<br><sub>`morningstar-commercialisation`</sub> | [Motley Fool, 23 Jan 2026](https://www.fool.com/investing/2026/01/23/predict-quantum-computing-ionq-rigetti-d-wave-buy/) (presse) |

<a id="acteur-ncsc-royaume-uni"></a>

### NCSC (Royaume-Uni)

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-11-22 | programme public | échéance de migration post-quantique | 2028<br>2031 (migrations prioritaires)<br>2035 (migration achevée) | 2028 | promis | Discovery and initial plan by 2028, priority migration by 2031, complete by 2035.<br><sub>`ncsc-jalons-migration-pqc`</sub> | [NCSC, PQC migration timelines](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines) (gouvernement) |

<a id="acteur-nist"></a>

### NIST

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-10-27 | programme public | échéance de migration post-quantique | 2030<br>2035 (interdiction) | 2030 | promis | All approved quantum-vulnerable public-key algorithms are deprecated after 2030 and disallowed after 2035, at every key size.<br><sub>`nist-ir-8547-final`</sub> | [NIST IR 8547 (final)](https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8547.pdf) (gouvernement) |

<a id="acteur-nsa"></a>

### NSA

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-11-22 | programme public | échéance de migration post-quantique | 2027-01-01 | 2027-01-01 | inconnu, à vérifier | From 1 Jan 2027, new National Security System acquisitions must be CNSA 2.0 compliant by default (CNSSP 15).<br><sub>`nsa-cnsa2-acquisitions-2027`</sub> | [PostQuantum, CNSA 2.0 2027 procurement gate](https://postquantum.com/cnsa-2-0/2027-procurement-gate/) (analyste) |

<a id="acteur-nvidia"></a>

### NVIDIA

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-11 | démonstration | latence de décodage | < 1 µs | — | inconnu, à vérifier | (via Quantum Machines) Quantum Machines ran CUDA-Q QEC decoders (PyMatching on a GH200 over NVQLink) with its OPX1000 controller and reported sub-microsecond surface-code decoding.<br><sub>`quantum-machines-decodage-sous-microseconde`</sub> | [Quantum Machines press release](https://www.quantum-machines.co/press-release/real-time-qec-decoding-opx1000-nvidia-cuda-q/) (vendeur) |
| 2026-04-14 | démonstration | latence de décodage | 2,1 µs | — | annoncé ou publié | CUDA-Q QEC 0.6: the fast Ising pre-decoder plus PyMatching reaches 2.1 µs per round (d=13 surface code, p=0.003, 104 rounds), 2.5x less decoding time than PyMatching alone.<br><sub>`nvidia-cudaq-qec-latence-2026-04`</sub> | [NVIDIA CUDA-Q blog, 14 Apr 2026](https://nvidia.github.io/cuda-quantum/blogs/blog/2026/04/14/cudaq-qec-0.6/) (vendeur) |
| 2026-10-22 | financement | montant du financement | non divulgué | — | annoncé ou publié | NVIDIA took a “strategic minority equity stake” in Riverlane, as part of NVIDIA's $250M UK computing commitment.<br><sub>`nvidia-participation-riverlane-2026-10`</sub> | [Quantum Computing Report, 22 Oct 2026](https://quantumcomputingreport.com/nvidia-takes-strategic-stake-in-riverlane-to-accelerate-real-time-quantum-error-correction-and-gpu-decoder-calibration/) (presse) |
| ≤ 2026-11-22 | démonstration | jalon | test de décodage GPU de codes LDPC-cat via OPX1000 et NVQLink | — | inconnu, à vérifier | (via Alice & Bob) Alice & Bob ran an LDPC-cat GPU decoding test via OPX1000 and NVQLink.<br><sub>`alice-bob-decodage-ldpc-cat-gpu`</sub> | [Quantum Computing Report coverage (Quantum Machines, NVQLink)](https://quantumcomputingreport.com/quantum-machines-demonstrates-sub-microsecond-surface-code-decoding-on-opx1000-using-nvidia-cuda-q-qec-and-nvqlink/) (presse) |

<a id="acteur-oratomic-caltech"></a>

### Oratomic / Caltech

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-03 | estimation de ressources | qubits physiques | ≈ 26 000 qubits<br>quelques jours (durée d'exécution) | — | annoncé ou publié | A P-256 attack in a few days on about 26,000 neutral atoms.<br><sub>`oratomic-p256-2026-03`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |

<a id="acteur-pasqal"></a>

### Pasqal

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-11 | démonstration | qubits physiques | 200 qubits | — | annoncé ou publié | 200-qubit neutral-atom computer installed in Aramco's Dhahran data centre, with a regional QCaaS platform and training for Saudi engineers.<br><sub>`pasqal-aramco-200-qubits-2025-11`</sub> | [Aramco, Aramco and Pasqal make history with Saudi Arabia's first quantum computer](https://www.aramco.com/en/news-media/news/2025/aramco-and-pasqal-make-history-with-saudi-arabias-first-quantum-computer) (vendeur) |
| 2026 | résultat financier | chiffre d'affaires | 0 EUR<br>3,2 M EUR (ventes de QPU au T3 2025) | — | inconnu, à vérifier | No QPU sales in Q3 2026, against €3.2M of QPU revenue in Q3 2025.<br><sub>`pasqal-qpu-t3-2026`</sub> | [DatacenterDynamics, Q3 2026 quantum earnings round-up](https://www.datacenterdynamics.com/en/news/quantum-earnings-q3-2026-d-wave-ionq-iqm-quantinuum-rigetti-and-xanadu-publish-third-quarter-results-alongside-newly-public-pasqal/) (presse) |
| 2026-03 | financement | montant du financement | 395 M USD | — | annoncé ou publié | A $395M raise was announced alongside Pasqal's SPAC in March 2026.<br><sub>`pasqal-levee-spac-2026-03`</sub> | [Qntonsol, quantum venture funding 2024-2026](https://www.qntonsol.com/learn/quantum-venture-funding-2024-2026-explained.html) (analyste) |

<a id="acteur-polymarket"></a>

### Polymarket

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-11-22 | marché prédictif | probabilité de marché | 2 %<br>2 840 USD (volume du marché) | 2026-12-31 | inconnu, à vérifier | “Quantum breaks Bitcoin by ___?”: Dec 31 2026 at 2% (volume $2,840).<br><sub>`polymarket-bitcoin-2026`</sub> | [Polymarket, Quantum breaks Bitcoin by](https://polymarket.com/event/quantum-breaks-bitcoin-by) (autre) |
| 2026-11-22 | marché prédictif | probabilité de marché | 12 %<br>1 512 USD (volume du marché) | 2027-12-31 | inconnu, à vérifier | “Quantum breaks Bitcoin by ___?”: Dec 31 2027 at 12% (volume $1,512).<br><sub>`polymarket-bitcoin-2027`</sub> | [Polymarket, Quantum breaks Bitcoin by](https://polymarket.com/event/quantum-breaks-bitcoin-by) (autre) |

<a id="acteur-postquantum"></a>

### PostQuantum

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026 | réfutation ou contestation | avantage quantique | contesté | — | annoncé ou publié | Skeptical analysis of IBM's three July 2026 quantum-advantage papers.<br><sub>`postquantum-contestation-avantage-ibm-2026`</sub> | [PostQuantum, IBM three quantum advantage papers](https://postquantum.com/industry-news/ibm-three-quantum-advantage-papers/) (analyste) |
| 2026-07-14 | réfutation ou contestation | ratio réalisé / projeté | ≈ 0,12 ratio<br>≈ 1,185 Md USD (chiffre d'affaires, projeté pour 2025)<br>≈ 138 M USD (chiffre d'affaires, réalisé en 2025) | — | annoncé ou publié | The three firms with published 2025 projections (IonQ, Rigetti, Arqit) projected about $1.185B and reported about $138M, roughly 12 cents per projected dollar.<br><sub>`postquantum-spac-projections-2026-07`</sub> | [PostQuantum, Quantum SPAC wave (14 July 2026)](https://postquantum.com/quantum-commercialization/quantum-spac-wave/) (analyste) |
| ≤ 2026-09 | réfutation ou contestation | appréciation qualitative | résultat très sensible au taux d'erreur physique supposé | — | annoncé ou publié | The memory-failure bound reaches about 89% at 1.5e-4 physical error, so the result is very sensitive to that assumption; the press release said “expected to break” while the paper says “per attempt”.<br><sub>`postquantum-critique-ionq-secp256k1`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |
| ≤ 2026-11-22 | réfutation ou contestation | appréciation qualitative | performance sur données d'un processeur réel non validée à la publication | — | annoncé ou publié | The Relay-BP paper decoded no syndromes from a real processor, so its performance on device data was unvalidated at publication.<br><sub>`postquantum-critique-relay-bp`</sub> | [PostQuantum, IBM](https://postquantum.com/quantum-computing-companies/ibm/) (analyste) |

<a id="acteur-presidio-bitcoin"></a>

### Presidio Bitcoin

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-04 | enquête ou avis d'experts | probabilité d'un CRQC | 50 % | 2035 | inconnu, à vérifier | “most experts assign a 50% probability to CRQCs emerging by 2030-2035”.<br><sub>`presidio-cinquante-pct-2030-2035`</sub> | [Presidio Bitcoin Quantum Readiness v1 (Apr 2026)](https://presidiobtc.github.io/bitcoin-quantum/presidio-bitcoin-quantum-readiness-v1-apr-2026.pdf) (analyste) |

<a id="acteur-project-eleven"></a>

### Project Eleven

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-01-14 | financement | montant du financement | 20 M USD<br>120 M USD (valorisation, après l'opération) | — | annoncé ou publié | Series A of $20M at a $120M post-money valuation, led by Castle Island Ventures with Coinbase Ventures; $26M raised in total.<br><sub>`project-eleven-serie-a-2026-01`</sub> | [The Block, 14 Jan 2026](https://www.theblock.co/news/deals/2026-01-14-project-eleven-series-a-funding-crypto-quantum-threats-385583) (presse) |
| 2026-04-24 | démonstration | taille de clé cassée | 15 bits<br>≈ 70 qubits (qubits physiques) | — | **vérifié par un tiers** ([source du statut](https://www.coindesk.com/tech/2026/04/24/researcher-wins-1-bitcoin-bounty-for-largest-quantum-attack-on-underlying-tech)) | A 15-bit elliptic-curve key (search space 32,767) was broken by Giancarlo Lelli on about 70 qubits of public cloud hardware; it won Project Eleven's 1 BTC Q-Day Prize and was 512x larger than the pre…<br><sub>`project-eleven-q-day-prize-15-bits-2026-04`</sub> | [CoinDesk, 24 Apr 2026](https://www.coindesk.com/tech/2026/04/24/researcher-wins-1-bitcoin-bounty-for-largest-quantum-attack-on-underlying-tech) (presse) |

<a id="acteur-psiquantum"></a>

### PsiQuantum

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-09 | financement | montant du financement | 1 Md USD<br>≈ 6 Md USD (valorisation, avant l'opération) | — | inconnu, à vérifier | PsiQuantum raised $1B in September 2025 at about $6B pre-money.<br><sub>`psiquantum-levee-2025-09`</sub> | [Qntonsol, quantum venture funding 2024-2026](https://www.qntonsol.com/learn/quantum-venture-funding-2024-2026-explained.html) (analyste) |
| 2026-05 | financement | montant du financement | ≈ 2 Md USD | — | annoncé ou publié | (via US Department of Commerce) About $2B of CHIPS Act money for minority, non-controlling equity stakes in nine quantum companies, as letters of intent.<br><sub>`chips-participations-quantique-2026-05`</sub> | [TheNextWeb, US $2bn quantum equity stakes](https://thenextweb.com/news/us-2bn-quantum-equity-stakes-chips-act) (presse) |
| 2026-07 | financement | montant du financement | 125 M USD | — | annoncé ou publié | PsiQuantum has a $125M expanded agreement with DARPA (July 2026), following $31.8M in September 2025.<br><sub>`psiquantum-darpa-125m-2026-07`</sub> | [PostQuantum, DARPA QBI Stage C](https://postquantum.com/industry-news/darpa-quantum-benchmarking-stage-c/) (analyste) |
| ≤ 2026-08-24 | financement | montant du financement | 940 M AUD | — | annoncé ou publié | (via Gouvernement australien) Australia: A$940M into PsiQuantum (2023-24).<br><sub>`psiquantum-australie-940m`</sub> | [The Quantum Insider, Nations at the quantum table](https://thequantuminsider.com/2026/08/24/nations-at-the-quantum-table/) (presse) |
| 2026-10-07 | programme public | nombre d'entreprises | 6 entreprises | — | annoncé ou publié | (via DARPA) Atom Computing, Diraq, IBM and IonQ advanced to Stage C, joining Microsoft and PsiQuantum from US2QC; Stage C is a government evaluation of whether utility-scale designs can be built.<br><sub>`darpa-qbi-etape-c-2026-10`</sub> | [DARPA, 7 Oct 2026](https://www.darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage) (gouvernement) |

<a id="acteur-quantinuum"></a>

### Quantinuum

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-03 | démonstration | bits d'entropie certifiés | ≈ 71 313 bits | — | inconnu, à vérifier | The Nature paper certified about 71,313 bits of entropy, using about 1.1 exaFLOPS of classical verification.<br><sub>`quantinuum-aleatoire-certifie-bits`</sub> | [Nature, certified randomness (Quantinuum et al.)](https://www.nature.com/articles/s41586-025-08737-1) (revue_a_comite) |
| 2025-03 | démonstration | aléa certifié | démontré sur le processeur H2 | — | **vérifié par un tiers** ([source du statut](https://www.nature.com/articles/s41586-025-08737-1)) | Certified randomness demonstrated on the H2 trapped-ion processor; Frontier supercomputers verified it with a cross-entropy benchmark; published in Nature.<br><sub>`quantinuum-aleatoire-certifie-nature-2025`</sub> | [Nature, certified randomness (Quantinuum et al.)](https://www.nature.com/articles/s41586-025-08737-1) (revue_a_comite) |
| 2025-03 | feuille de route | jalon | aléa certifié ajouté au portefeuille commercial | 2025 | inconnu, à vérifier | Quantinuum said it would add certified randomness to its commercial portfolio, with a stated target of 2025.<br><sub>`quantinuum-aleatoire-certifie-produit-2025`</sub> | [Quantinuum blog, first commercial application](https://www.quantinuum.com/blog/quantinuum-introduces-first-commercial-application-for-quantum-computers) (vendeur) |
| 2025-09 | financement | montant du financement | ≈ 600 M USD<br>10 Md USD (valorisation, avant l'opération) | — | inconnu, à vérifier | Quantinuum raised about $600M in September 2025 at a $10B pre-money valuation, with NVIDIA's venture arm among the investors.<br><sub>`quantinuum-levee-2025-09`</sub> | [Qntonsol, quantum venture funding 2024-2026](https://www.qntonsol.com/learn/quantum-venture-funding-2024-2026-explained.html) (analyste) |
| 2025-11 | programme public | nombre d'entreprises | 11 entreprises<br>≤ 15 M USD (montant du financement, par entreprise, pour environ un an) | — | annoncé ou publié | (via DARPA) DARPA QBI Stage B named 11 companies, with awards of up to about $15M each for roughly a year.<br><sub>`darpa-qbi-etape-b-2025-11`</sub> | [Nextgov, Nov 2025](https://www.nextgov.com/emerging-tech/2025/11/11-companies-move-second-stage-darpas-quantum-benchmarking-initiative/409405/) (presse) |
| 2025-11 | démonstration | qubits physiques | 98 qubits | — | annoncé ou publié | Quantinuum Helios has 98 trapped-ion qubits.<br><sub>`quantinuum-helios-98-qubits`</sub> | [PostQuantum, Quantinuum color code on Helios](https://postquantum.com/industry-news/quantinuum-color-code-helios/) (analyste) |
| 2026 | résultat financier | chiffre d'affaires | 30,9 M USD | — | annoncé ou publié | 2025 revenue was $30.9M (2024: $23M) with a $192.6M net loss.<br><sub>`quantinuum-ca-2025`</sub> | [Yahoo Finance, Quantinuum IPO targets $12.7B](https://finance.yahoo.com/markets/stocks/articles/quantinuum-ipo-targets-12-7b-162055146.html) (presse) |
| 2026 | résultat financier | chiffre d'affaires | 9,1 M USD<br>22,3 M USD (neuf mois 2026) | — | annoncé ou publié | Q3 2026 revenue $9.1M, up 233% from $2.7M; 9M-2026 $22.3M, below the $23.9M of 9M-2025.<br><sub>`quantinuum-ca-t3-2026`</sub> | [Quantinuum Q3 2026 results release (via Finviz)](https://finviz.com/news/417558/quantinuum-reports-third-quarter-2026-results-and-raises-full-year-revenue-outlook) (vendeur) |
| 2026 | feuille de route | mise en service | système Helios à Singapour | 2027 | promis | A Helios system in Singapore, to be commissioned spring 2027.<br><sub>`quantinuum-helios-singapour-2027`</sub> | [Quantinuum Q3 2026 results release (via Finviz)](https://finviz.com/news/417558/quantinuum-reports-third-quarter-2026-results-and-raises-full-year-revenue-outlook) (vendeur) |
| 2026 | feuille de route | chiffre d'affaires | 31-34 M USD | 2026-12-31 | promis | FY2026 revenue outlook raised to $31-34M.<br><sub>`quantinuum-prevision-ca-2026`</sub> | [Quantinuum Q3 2026 results release (via Finviz)](https://finviz.com/news/417558/quantinuum-reports-third-quarter-2026-results-and-raises-full-year-revenue-outlook) (vendeur) |
| 2026-05 | financement | montant du financement | ≈ 2 Md USD | — | annoncé ou publié | (via US Department of Commerce) About $2B of CHIPS Act money for minority, non-controlling equity stakes in nine quantum companies, as letters of intent.<br><sub>`chips-participations-quantique-2026-05`</sub> | [TheNextWeb, US $2bn quantum equity stakes](https://thenextweb.com/news/us-2bn-quantum-equity-stakes-chips-act) (presse) |
| 2026-06-04 | financement | montant du financement | ≈ 1,7 Md USD<br>17,6 Md USD (valorisation, à l'ouverture, 68 $ par action (Wikipedia)) | — | annoncé ou publié | Quantinuum closed a $1.68-1.7B IPO on Nasdaq (QNT).<br><sub>`quantinuum-ipo-2026-06`</sub> | [SiliconANGLE, 4 June 2026](https://siliconangle.com/2026/06/04/quantum-computer-maker-quantinuum-closes-flat-1-68b-ipo/) (presse) |
| 2026-08-12 | feuille de route | chiffre d'affaires | 28-32 M USD | 2026-12-31 | **retiré ou remplacé** ([source du statut](https://finviz.com/news/417558/quantinuum-reports-third-quarter-2026-results-and-raises-full-year-revenue-outlook)) | Q2 2026 revenue was $8M; FY2026 guidance $28-32M.<br><sub>`quantinuum-prevision-ca-2026-initiale`</sub> | [The Quantum Insider, 12 Aug 2026](https://thequantuminsider.com/?p=2391477) (presse) |
| 2026-10 | programme public | jalon | discussion d'un périmètre d'étape C avec la DARPA | — | inconnu, à vérifier | Quantinuum said it was “actively discussing” a Stage C scope with DARPA.<br><sub>`quantinuum-etape-c-discussion-2026-10`</sub> | [Fast Company, DARPA QBI Stage C](https://www.fastcompany.com/91620226/darpa-quantum-benchmarking-initiative-stage-c-announcement) (presse) |
| 2026-10 | démonstration | taux d'erreur logique | ≈ 5×10⁻⁶ par tour de correction<br>≈ 7×10⁻⁵ (erreur de porte logique à 2 qubits, distance 5) | — | annoncé ou publié | Oct 2026 preprint: logical error ~5×10⁻⁶ per correction round; logical two-qubit gate error ~7×10⁻⁵ at distance 5 (14x below physical).<br><sub>`quantinuum-helios-erreur-logique-2026-10`</sub> | [PostQuantum, Quantinuum color code on Helios](https://postquantum.com/industry-news/quantinuum-color-code-helios/) (analyste) |
| ≤ 2026-11-22 | feuille de route | jalon | Apollo, machine entièrement tolérante aux fautes | 2029 | inconnu, à vérifier | Apollo, the fully fault-tolerant machine, “remains on schedule for 2029”.<br><sub>`quantinuum-apollo-2029`</sub> | [Andes Qubit, quantum hardware roadmaps 2026-2030](https://andesqubit.com/en/blog/quantum-hardware-roadmaps-2026-2030/) (analyste) |
| ≤ 2026-11-22 | démonstration | fidélité à 2 qubits | 99,921 % | — | inconnu, à vérifier | Helios has 99.921% two-qubit fidelity.<br><sub>`quantinuum-helios-fidelite-2q`</sub> | [Andes Qubit, quantum hardware roadmaps 2026-2030](https://andesqubit.com/en/blog/quantum-hardware-roadmaps-2026-2030/) (analyste) |

<a id="acteur-quantum-advantage-tracker"></a>

### Quantum Advantage Tracker

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-11-22 | revendication d'avantage | nombre de soumissions | ≈ 30 soumissions | — | annoncé ou publié | Launched Nov 2025 by IBM, Algorithmiq, Flatiron Institute and BlueQubit; about 30 submissions on IBM and Quantinuum hardware; classical methods have overturned some claims; entries grouped Active / S…<br><sub>`quantum-advantage-tracker-soumissions`</sub> | [Quantum Advantage Tracker, observable estimations](https://quantum-advantage-tracker.github.io/trackers/observable-estimations) (autre) |

<a id="acteur-quantum-machines"></a>

### Quantum Machines

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-11 | démonstration | latence de décodage | < 1 µs | — | inconnu, à vérifier | Quantum Machines ran CUDA-Q QEC decoders (PyMatching on a GH200 over NVQLink) with its OPX1000 controller and reported sub-microsecond surface-code decoding.<br><sub>`quantum-machines-decodage-sous-microseconde`</sub> | [Quantum Machines press release](https://www.quantum-machines.co/press-release/real-time-qec-decoding-opx1000-nvidia-cuda-q/) (vendeur) |
| ≤ 2026-11-22 | démonstration | jalon | test de décodage GPU de codes LDPC-cat via OPX1000 et NVQLink | — | inconnu, à vérifier | (via Alice & Bob) Alice & Bob ran an LDPC-cat GPU decoding test via OPX1000 and NVQLink.<br><sub>`alice-bob-decodage-ldpc-cat-gpu`</sub> | [Quantum Computing Report coverage (Quantum Machines, NVQLink)](https://quantumcomputingreport.com/quantum-machines-demonstrates-sub-microsecond-surface-code-decoding-on-opx1000-using-nvidia-cuda-q-qec-and-nvqlink/) (presse) |

<a id="acteur-quera"></a>

### QuEra

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-11 | programme public | nombre d'entreprises | 11 entreprises<br>≤ 15 M USD (montant du financement, par entreprise, pour environ un an) | — | annoncé ou publié | (via DARPA) DARPA QBI Stage B named 11 companies, with awards of up to about $15M each for roughly a year.<br><sub>`darpa-qbi-etape-b-2025-11`</sub> | [Nextgov, Nov 2025](https://www.nextgov.com/emerging-tech/2025/11/11-companies-move-second-stage-darpas-quantum-benchmarking-initiative/409405/) (presse) |
| ≤ 2026-05-09 | enquête ou avis d'experts | part des répondants | 37,2 %<br>5,6 % (dans 1-2 ans)<br>37,5 % (dans 6-10 ans)<br>16,8 % (au-delà de 10 ans) | — | annoncé ou publié | 5.6% expect “quantum superiority” within 1-2 years, 37.2% in 3-5 years, 37.5% in 6-10 years and 16.8% beyond 10 years (n=291).<br><sub>`quera-enquete-preparation-2026`</sub> | [QuEra, 2026 Quantum Readiness Survey Report](https://cdn.prod.website-files.com/643b94c382e84463a9e52264/6a8ef54f5ca422cd30d018e4_Full_2026_Quantum_Readiness_Survey_Report.pdf) (enquete) |
| 2026-10-27 | estimation de ressources | réduction du surcoût | ≤ 230 fois | — | annoncé ou publié | qLDPC codes from QuEra and Alice & Bob reportedly cut physical-qubit overhead “up to 230-fold” versus rotated surface codes.<br><sub>`quera-alice-bob-qldpc-230x`</sub> | [Quantum Computing Report / GQI, Q3 2026 State of Play](https://quantumcomputingreport.com/gqi-q3-2026-state-of-play-investment-consolidation-accelerating-q-day-horizons-and-the-shift-to-second-generation-architectures/) (analyste) |

<a id="acteur-rigetti"></a>

### Rigetti

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2021 | feuille de route | chiffre d'affaires | 288 M USD | 2025 | **contredit** ([source du statut](https://postquantum.com/quantum-commercialization/quantum-spac-wave/)) | SPAC-deck projection: revenue of $288M in 2025.<br><sub>`rigetti-spac-ca-2025`</sub> | [PostQuantum, Quantum SPAC wave (14 July 2026)](https://postquantum.com/quantum-commercialization/quantum-spac-wave/) (analyste) |
| 2021 | feuille de route | qubits physiques | > 4 000 qubits | 2026 | promis | SPAC-deck projection: 4,000+ qubits by 2026.<br><sub>`rigetti-spac-qubits-2026`</sub> | [PostQuantum, Quantum SPAC wave (14 July 2026)](https://postquantum.com/quantum-commercialization/quantum-spac-wave/) (analyste) |
| 2026 | résultat financier | chiffre d'affaires | 7,1 M USD | — | annoncé ou publié | FY2025 revenue $7.1M (down 34%); net loss $216.2M.<br><sub>`rigetti-ca-2025`</sub> | [DatacenterDynamics, FY25 quantum earnings](https://www.datacenterdynamics.com/en/news/quantum-computing-earnings-q4-and-fy25-ionq-d-wave-rigetti-results/) (presse) |
| 2026-05 | financement | montant du financement | ≈ 2 Md USD | — | annoncé ou publié | (via US Department of Commerce) About $2B of CHIPS Act money for minority, non-controlling equity stakes in nine quantum companies, as letters of intent.<br><sub>`chips-participations-quantique-2026-05`</sub> | [TheNextWeb, US $2bn quantum equity stakes](https://thenextweb.com/news/us-2bn-quantum-equity-stakes-chips-act) (presse) |
| 2026-11-11 | démonstration | qubits physiques | 108 qubits<br>99,5 % (fidélité à 2 qubits, médiane) | — | annoncé ou publié | Rigetti runs a 108-qubit system at 99.5% median two-qubit fidelity.<br><sub>`rigetti-108-qubits-2026`</sub> | [The Quantum Insider, 11 Nov 2026](https://thequantuminsider.com/2026/11/11/rigetti-q3-2026-results-quantum-computing-roadmap/) (presse) |
| 2026-11-11 | résultat financier | chiffre d'affaires | 1,4 M USD<br>≈ 3,67 M USD (consensus des analystes pour le T3)<br>10,9 M USD (neuf mois 2026) | — | annoncé ou publié | Q3 2026 revenue $1.4M, down from $1.9M and against a ~$3.67M consensus; 9M-2026 revenue $10.9M.<br><sub>`rigetti-ca-t3-2026`</sub> | [The Quantum Insider, 11 Nov 2026](https://thequantuminsider.com/2026/11/11/rigetti-q3-2026-results-quantum-computing-roadmap/) (presse) |
| 2026-11-11 | feuille de route | qubits physiques | ≈ 1 000 qubits<br>≈ 99,9 % (fidélité à 2 qubits) | 2029 | promis | About 1,000 qubits at about 99.9% roughly three years out.<br><sub>`rigetti-feuille-de-route-1000-qubits`</sub> | [The Quantum Insider, 11 Nov 2026](https://thequantuminsider.com/2026/11/11/rigetti-q3-2026-results-quantum-computing-roadmap/) (presse) |
| 2026-11-11 | feuille de route | qubits physiques | > 300 qubits<br>≈ 99,7 % (fidélité à 2 qubits) | 2028-06 | promis | 300+ qubits at about 99.7% by mid-2028.<br><sub>`rigetti-feuille-de-route-300-qubits-2028`</sub> | [The Quantum Insider, 11 Nov 2026](https://thequantuminsider.com/2026/11/11/rigetti-q3-2026-results-quantum-computing-roadmap/) (presse) |
| 2026-11-11 | feuille de route | chiffre d'affaires | ≈ 20 M USD | 2026-12-31 | promis | FY2026 guidance of ~$20M depends on “C-DAC customer acceptance” in Q4.<br><sub>`rigetti-prevision-ca-2026`</sub> | [The Quantum Insider, 11 Nov 2026](https://thequantuminsider.com/2026/11/11/rigetti-q3-2026-results-quantum-computing-roadmap/) (presse) |
| 2026-11-22 | prix | prix par tir | 0,000425 USD/tir | — | annoncé ou publié | (via Amazon Web Services (Braket)) Rigetti Cepheus on Amazon Braket: $0.000425 per shot.<br><sub>`braket-prix-rigetti-cepheus`</sub> | [Amazon Braket pricing](https://aws.amazon.com/braket/pricing/) (vendeur) |

<a id="acteur-riverlane"></a>

### Riverlane

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2024-10-22 | feuille de route | opérations logiques | 1 M opérations<br>≈ 50-100 qubits (qubits logiques, nécessaires selon Science News) | 2027 | promis | “MegaQuOp” (1M error-free operations) as the next milestone, expected within 2-3 years.<br><sub>`riverlane-megaquop`</sub> | [The Quantum Insider, 22 Oct 2024 (Riverlane QEC report)](https://thequantuminsider.com/2024/10/22/riverlanes-quantum-error-correction-report-defining-the-path-to-fault-tolerant-computing-and-the-megaquop-milestone/) (presse) |
| 2026-10-22 | financement | montant du financement | non divulgué | — | annoncé ou publié | (via NVIDIA) NVIDIA took a “strategic minority equity stake” in Riverlane, as part of NVIDIA's $250M UK computing commitment.<br><sub>`nvidia-participation-riverlane-2026-10`</sub> | [Quantum Computing Report, 22 Oct 2026](https://quantumcomputingreport.com/nvidia-takes-strategic-stake-in-riverlane-to-accelerate-real-time-quantum-error-correction-and-gpu-decoder-calibration/) (presse) |
| ≤ 2026-11-22 | démonstration | latence de décodage | 16,32 µs | — | annoncé ou publié | Riverlane reported a real-time QEC latency of 16.32 µs with Deltaflow 2, which QCR calls a fourfold improvement over the 63 µs of Google's 2024 Willow experiment.<br><sub>`riverlane-deltaflow2-latence`</sub> | [Quantum Computing Report, Riverlane real-time QEC latency](https://quantumcomputingreport.com/riverlane-demonstrates-real-time-qec-latency-performance-advancements/) (presse) |
| ≤ 2026-11-22 | feuille de route | jalon | Deltaflow 3 | 2026 | promis | Deltaflow 3 is expected in late 2026.<br><sub>`riverlane-deltaflow3-2026`</sub> | [Riverlane news, first hardware decoder](https://www.riverlane.com/news/riverlane-unveils-first-hardware-decoder-to-deliver-real-time-scalable-quantum-error-correction) (vendeur) |
| ≤ 2026-11-22 | démonstration | cycles de correction | 50 000 cycles | — | annoncé ou publié | Riverlane and Qblox closed a full real-time QEC loop over 50,000 QEC cycles.<br><sub>`riverlane-qblox-boucle-qec`</sub> | [Riverlane blog, full real-time QEC loop with Qblox](https://www.riverlane.com/blog/riverlane-and-qblox-have-closed-a-full-real-time-qec-loop) (vendeur) |

<a id="acteur-roetteler-naehrig-svore-lauter"></a>

### Roetteler, Naehrig, Svore, Lauter

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2017 | estimation de ressources | qubits logiques | ≈ 2 330 qubits<br>≈ 130 Md portes (portes Toffoli) | — | annoncé ou publié | The 2017 reference estimate for 256-bit elliptic curves: about 2,330 logical qubits and about 1.3×10^11 Toffolis, roughly 1,000-2,000x more Toffolis than the 2026 Google figure.<br><sub>`roetteler-ecc256-2017`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |

<a id="acteur-s-p-global"></a>

### S&P Global

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-08-17 | enquête ou avis d'experts | horizon de la tolérance aux fautes | 2027-2030 | — | annoncé ou publié | Most major vendors target 2027-2030 for fault tolerance.<br><sub>`sp-global-tolerance-fautes-2027-2030`</sub> | [S&P Global, Quantum Quarterly Q2 2026](https://www.spglobal.com/energy/en/technology-ai-research-insights/blogs/quantum-quarterly-q2-2026) (analyste) |

<a id="acteur-schrottenloher"></a>

### Schrottenloher

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-11-22 | estimation de ressources | qubits logiques | ≈ 1 192 qubits<br>≈ 1 446 qubits (variante optimisée en portes) | — | annoncé ou publié | An independent reproduction by Schrottenloher reported about 1,192 logical qubits (space-optimised) and 1,446 (gate-optimised).<br><sub>`schrottenloher-reproduction-secp256k1`</sub> | [PostQuantum, the ECC circuit floor](https://postquantum.com/post-quantum/quantum-attack-ecc-circuit-floor/) (analyste) |

<a id="acteur-solana-foundation"></a>

### Solana Foundation

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-04-27 | feuille de route | jalon | plan d'activation d'un schéma post-quantique centré sur Falcon | — | promis | “no change is required today or likely anytime soon”, but there is a plan to activate a post-quantum scheme centred on Falcon, with an initial implementation built.<br><sub>`solana-falcon-2026-04`</sub> | [Solana Foundation, quantum readiness](https://solana.com/news/quantum-readiness) (vendeur) |

<a id="acteur-the-times-via-capacity-media"></a>

### The Times (via Capacity Media)

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2022 | réfutation ou contestation | appréciation qualitative | « committed revenue » surtout composé de subventions de recherche | — | annoncé ou publié | In 2022 press reports said Arqit overstated revenue and readiness; The Times reported that most of the “committed revenue” pitched to investors was research grants.<br><sub>`arqit-presse-2022-revenus-engages`</sub> | [Capacity Media, Arqit fights back after critics](https://capacitymedia.com/article/29zvx3vhdiqk09vom3nk0/news/arqit-fights-back-after-critics-send-share-price-down-43-in-a-month) (presse) |

<a id="acteur-us-department-of-commerce"></a>

### US Department of Commerce

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026-05 | financement | montant du financement | ≈ 2 Md USD | — | annoncé ou publié | About $2B of CHIPS Act money for minority, non-controlling equity stakes in nine quantum companies, as letters of intent.<br><sub>`chips-participations-quantique-2026-05`</sub> | [TheNextWeb, US $2bn quantum equity stakes](https://thenextweb.com/news/us-2bn-quantum-equity-stakes-chips-act) (presse) |

<a id="acteur-us-department-of-energy"></a>

### US Department of Energy

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| ≤ 2026-11-22 | programme public | jalon | premier ordinateur tolérant aux fautes scientifiquement utile<br>≤ 215 M USD (montant du financement) | 2028 | inconnu, à vérifier | DOE “Genesis Q” competition: up to $215M, subject to appropriations, for a first-generation fault-tolerant, scientifically useful computer by 2028.<br><sub>`doe-genesis-q-2028`</sub> | [Andes Qubit, quantum hardware roadmaps 2026-2030](https://andesqubit.com/en/blog/quantum-hardware-roadmaps-2026-2030/) (analyste) |

<a id="acteur-webster-et-al-architecture-pinnacle"></a>

### Webster et al. (architecture Pinnacle)

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2026 | estimation de ressources | qubits physiques | ≈ 100 000 qubits | — | annoncé ou publié | Pinnacle architecture: RSA-2048 on qLDPC codes at about 100,000 qubits.<br><sub>`pinnacle-rsa2048-qldpc-2026`</sub> | [PostQuantum, IonQ secp256k1 resource estimate](https://postquantum.com/post-quantum/ionq-secp256k1-resource-estimate/) (analyste) |

<a id="acteur-xanadu"></a>

### Xanadu

| Date | Type | Métrique | Valeur | Échéance | Statut | Énoncé | Source |
|---|---|---|---|---|---|---|---|
| 2025-11 | programme public | nombre d'entreprises | 11 entreprises<br>≤ 15 M USD (montant du financement, par entreprise, pour environ un an) | — | annoncé ou publié | (via DARPA) DARPA QBI Stage B named 11 companies, with awards of up to about $15M each for roughly a year.<br><sub>`darpa-qbi-etape-b-2025-11`</sub> | [Nextgov, Nov 2025](https://www.nextgov.com/emerging-tech/2025/11/11-companies-move-second-stage-darpas-quantum-benchmarking-initiative/409405/) (presse) |
| 2026 | feuille de route | qubits logiques | ≥ 1 000 qubits | 2031 | promis | 1,000+ logical qubits from 2031.<br><sub>`xanadu-1000-qubits-logiques-2031`</sub> | [Investing.com, Xanadu Q3 2026 earnings call transcript](https://uk.investing.com/news/stock-market-news/earnings-call-transcript-xanadu-quantum-falls-after-q3-2026-revenue-growth-93CH-4975848) (presse) |
| 2026 | feuille de route | qubits logiques | ≤ 200 qubits | 2029 | promis | Up to 200 logical qubits in 2029, as part of a commercially viable computer targeted for 2029-2030.<br><sub>`xanadu-200-qubits-logiques-2029`</sub> | [Investing.com, Xanadu Q3 2026 earnings call transcript](https://uk.investing.com/news/stock-market-news/earnings-call-transcript-xanadu-quantum-falls-after-q3-2026-revenue-growth-93CH-4975848) (presse) |
| 2026 | feuille de route | qubits logiques | ≤ 500 qubits | 2030 | promis | Up to 500 logical qubits the year after 2029.<br><sub>`xanadu-500-qubits-logiques-2030`</sub> | [Investing.com, Xanadu Q3 2026 earnings call transcript](https://uk.investing.com/news/stock-market-news/earnings-call-transcript-xanadu-quantum-falls-after-q3-2026-revenue-growth-93CH-4975848) (presse) |
| 2026 | résultat financier | chiffre d'affaires | 2,8 M USD | — | annoncé ou publié | Q1 2026 revenue was $2.8M, “primarily driven by revenue recognized from DARPA QBI Stage B participation”.<br><sub>`xanadu-ca-t1-2026`</sub> | [Yahoo Finance, Xanadu revenue climbs 4x](https://finance.yahoo.com/sectors/technology/articles/xanadu-revenue-climbs-4x-quantum-152853198.html) (presse) |
| 2026-03-27 | financement | montant du financement | ≈ 302 M USD<br>500 M USD (objectif) | — | annoncé ou publié | Xanadu's SPAC listing (XNDU) raised about $302M against $500M targeted, after most SPAC holders redeemed.<br><sub>`xanadu-spac-2026-03`</sub> | [The Quantum Insider, 27 Mar 2026](https://thequantuminsider.com/2026/03/27/xanadu-becomes-first-pure-play-photonic-quantum-computing-company-to-go-public/) (presse) |

<a id="acteurs-associes"></a>

### Organisations seulement associées

| Organisation | Entrées (date · acteur principal · identifiant) |
|---|---|
| Algorithmiq | 2026-07-30 · via IBM · `ibm-algorithmiq-avantage-2026-07`<br>≤ 2026-11-22 · via Quantum Advantage Tracker · `quantum-advantage-tracker-soumissions` |
| Anchorage Digital | 2026-07-23 · via Bitcoin Security Consortium · `consortium-securite-bitcoin-2026-07` |
| Aramco | 2025-11 · via Pasqal · `pasqal-aramco-200-qubits-2025-11` |
| Argonne National Laboratory | 2025-03 · via Quantinuum · `quantinuum-aleatoire-certifie-nature-2025` |
| ARK Invest | 2026-07-23 · via Bitcoin Security Consortium · `consortium-securite-bitcoin-2026-07` |
| Atom Computing | 2025-11 · via DARPA · `darpa-qbi-etape-b-2025-11`<br>2026-05 · via US Department of Commerce · `chips-participations-quantique-2026-05`<br>2026-10-07 · via DARPA · `darpa-qbi-etape-c-2026-10` |
| BlackRock | 2026-07-23 · via Bitcoin Security Consortium · `consortium-securite-bitcoin-2026-07` |
| Block | 2026-07-23 · via Bitcoin Security Consortium · `consortium-securite-bitcoin-2026-07` |
| Blockstream | 2026-07-23 · via Bitcoin Security Consortium · `consortium-securite-bitcoin-2026-07` |
| BlueQubit | ≤ 2026-11-22 · via Quantum Advantage Tracker · `quantum-advantage-tracker-soumissions` |
| Coinbase | 2026-04-21 · via Coinbase Independent Advisory Board on Quantum Computing and Blockchain · `coinbase-conseil-2026-04`<br>2026-07-23 · via Bitcoin Security Consortium · `consortium-securite-bitcoin-2026-07` |
| EuroHPC | 2026-02-12 · via IQM · `iqm-euro-q-exa-150-qubits-2026`<br>2026-02-12 · via IQM · `iqm-euro-q-exa-54-qubits-2026-02` |
| Fidelity Digital Assets | 2026-07-23 · via Bitcoin Security Consortium · `consortium-securite-bitcoin-2026-07` |
| Flatiron Institute | ≤ 2026-11-22 · via Quantum Advantage Tracker · `quantum-advantage-tracker-soumissions` |
| Galaxy | 2026-07-23 · via Bitcoin Security Consortium · `consortium-securite-bitcoin-2026-07` |
| GlobalFoundries | 2026-05 · via US Department of Commerce · `chips-participations-quantique-2026-05` |
| Infleqtion | 2026-05 · via US Department of Commerce · `chips-participations-quantique-2026-05` |
| JPMorgan Chase | 2025-03 · via Quantinuum · `quantinuum-aleatoire-certifie-nature-2025` |
| LRZ | 2026-02-12 · via IQM · `iqm-euro-q-exa-150-qubits-2026`<br>2026-02-12 · via IQM · `iqm-euro-q-exa-54-qubits-2026-02` |
| Nord Quantique | 2025-11 · via DARPA · `darpa-qbi-etape-b-2025-11` |
| Oak Ridge National Laboratory | 2025-03 · via Quantinuum · `quantinuum-aleatoire-certifie-nature-2025` |
| Photonic Inc. | 2025-11 · via DARPA · `darpa-qbi-etape-b-2025-11` |
| Qblox | ≤ 2026-11-22 · via Riverlane · `riverlane-qblox-boucle-qec` |
| Quandela | 2026-05 · via DARPA · `darpa-qbi-quandela-etape-a-2026-05` |
| Quantum Motion | 2025-11 · via DARPA · `darpa-qbi-etape-b-2025-11` |
| Silicon Quantum Computing | 2025-11 · via DARPA · `darpa-qbi-etape-b-2025-11` |
| Stanford University | 2026-03-30 · via Google · `google-secp256k1-2026-03-variante-portes`<br>2026-03-30 · via Google · `google-secp256k1-2026-03-variante-qubits` |
| Strategy | 2026-07-23 · via Bitcoin Security Consortium · `consortium-securite-bitcoin-2026-07` |
| University of Chicago | 2026-07-30 · via IBM · `ibm-uchicago-circuits-logiques-2026-07` |
| UT Austin | 2025-03 · via Quantinuum · `quantinuum-aleatoire-certifie-nature-2025` |
