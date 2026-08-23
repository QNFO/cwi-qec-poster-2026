# Tree Code Development & Testing Roadmap — CWI Summer School Edition

**Prepared:** 2026-08-21 · **Author:** Rowan Brad Quni-Gudzinas — QNFO
**Scope:** continued development and testing of the Bruhat–Tits tree code (BTQP), as
presented at the CWI Summer School on Quantum Algorithms and QEC poster session
(Wed 26 Aug 2026, 16:30–18:00, WCW Turingzaal, Science Park 125, Amsterdam).
**WBS:** QNFO.UMP (tree-code architecture) · energy-mission tie: QNFO.JPC.001 (joules per correct answer).

---

## 1. Status (verified 2026-08-21)

| Item | Status | Evidence |
|---|---|---|
| Thresholds: bit-flip **50.0%** (4.6× surface ~10.9%), depolarizing **75.0%** (75× ~1.0%), independent X+Z **17.30%** (0.92× vs toric ~18.9%) | Computed by three independent classical methods (analytical recursion, exact Gottesman–Knill stabilizer simulation, Monte Carlo) and re-verified by a deposited 35-check script | 10.5281/zenodo.20109836 · 10.5281/zenodo.22038733 |
| Hardware demonstration | **None yet** — no tree code has run on quantum hardware | guide Ch.16, Objection 6 |
| First falsifiable prediction (log-periodic oscillations in the CMB power spectrum) | **Tested — null.** No certified discrete-scale-invariance signal at any resolvable radix in Planck 2018 TT (bootstrap p = 0.89); bispectrum channel: upper bounds only (ε_p < 2.5 @ 95% CL) | 10.5281/zenodo.21902891 · 10.5281/zenodo.21901664 |
| Independent-error boundary (qudit family) | ≈ 2.0×10⁻⁴, ~55× below surface-code threshold — the architectural claim targets the correlated-failure regime, not independent errors | 10.5281/zenodo.21046993 · 10.5281/zenodo.22025544 |
| QEC–Darwinism no-go (Maity et al., F_L > 0.874) | Audited on tree code spaces; collective fragment refinement moves the first-redundancy boundary to F_L ≈ 0.83–0.85; a residual gap remains, hierarchy-dependent | 10.5281/zenodo.21964674 |
| Valuation reading of stabilizer codes | Self-correction: the naive p-adic valuation mapping carries no new content; code distance admits no valuation reading | 10.5281/zenodo.21979060 |
| ZX representation of tree gates | Underway; CNOT→ZX construction numerically verified (max deviation ~1e-16); arXiv sweep: "ultrametric + QEC" externally unoccupied (0 results) | RES.019 (2026-08-20) · 10.5281/zenodo.21992118 |

## 2. Development tracks

- **D1 — Reproducible simulation.** Release the tree-code stabilizer simulator as an
  open, documented package; define an independent-reimplementation target (reference
  outputs + seeds); extend Monte Carlo to larger depth and to p > 2; settle the
  perfect-tensor existence question for p > 2 (the binary [[3,1,1]] case is
  well-established; larger primes are open).
- **D2 — Gate level / ZX.** Compile tree-automorphism logical gates into ZX diagrams
  (spiders, Pauli webs, gadgets); derive spider/H-box counts for tree encodings as a
  complexity measure; connect to the diagrammatic-bridge material already prepared
  for the poster.
- **D3 — Noise modeling.** Make the "correlated-failure regime" precise: a named,
  parametric error model (hierarchical / burst / spatially correlated) under which
  the advantage claim is testable, ahead of any experimental claim.

## 3. Test plan (near-term first)

| # | Test | Where | Effort | Disconfirmation criterion |
|---|---|---|---|---|
| T1 | Matched-noise threshold comparison: tree vs surface code under the *same* correlated noise model | Classical simulation | days–weeks | Tree advantage falls to parity under matched noise |
| T2 | Decoder complexity + full overhead accounting (physical qubits + classical processing) | Classical | weeks | Advantage disappears when decoding cost is included |
| T3 | Return-probability decay of a random walk on a p-regular tree graph | Analog / ion simulator | ~8 weeks | No change in decay exponent at the predicted value |
| T4 | Clock-rest ultrametricity split: diagonal 0% vs non-diagonal 29–35% violation rate | Trapped ion (conditional state tomography) | ~8 weeks | Measured split outside the predicted range |
| T5 | Independent re-implementation of T1 by an external group (the reproducibility test) | Community | open | — (reproducibility, not a prediction) |

T1 and T2 are pure classical work and are the decisive, cheap next steps; T3/T4
reuse platforms and protocols already specified in the trapped-ion instrumentation
paper (10.5281/zenodo.22025544). Every disconfirmation criterion is stated with
numbers so a null is a result.

## 4. What we ask of this room

1. **Correlated-noise benchmark data** (Delfosse/IonQ, and any lab): an openly
   specified correlated-noise model + dataset the tree code can be run against in T1.
2. **Decoder reality check** (Leverrier/Inria, QLDPC community): is there a known
   decoder family that already covers tree-structured codes, and how does its
   complexity scale?
3. **Perfect tensors for p > 2**: pointers to existence/non-existence results.
4. **Independent replication of T1**: we hand over the simulator and the matched-noise
   protocol; a third-party rerun would settle the classical claim.

## 5. Roadmap horizons

- **Near term (2026):** T1, T2, simulator release (D1); ZX gate compilation (D2).
- **Medium term (2026–2027):** T3/T4 instrumentation runs; noise-model publication (D3).
- **Long term:** fault-tolerant prototype path *only if* T1–T2 survive matched-noise
  scrutiny; energy accounting (JPCUB: joules per correct answer) applied to the
  tree code vs surface code as the mission-level comparison.

## 6. References (all DOIs verified 2026-08-21)

- Bruhat-Tits Quantum Processor: 10.5281/zenodo.20109836
- The Revolutionary Beginner's Guide (v1.2.2, with verification script): 10.5281/zenodo.22038733
- Radix-Agnostic DSI Null Result (Planck 2018): 10.5281/zenodo.21902891
- CMB Bispectrum Upper Bounds: 10.5281/zenodo.21901664
- Qudit Quantum Error Correction: 10.5281/zenodo.21046993
- Trapped-Ion Ultrametric Testbed: 10.5281/zenodo.22025544
- QEC-Darwinism Tradeoff (Archimedean Shadows): 10.5281/zenodo.21964674 (v1.11 record; concept 10.5281/zenodo.21809888)
- Prime-Valuation Correction: 10.5281/zenodo.21979060
- ZX Diagrams at the Seam: 10.5281/zenodo.21992118
