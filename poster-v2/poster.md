# Ultrametric Quantum Error Correction

## Testing Discrete Geometry in the Redundancy–Fidelity Tradeoff

**Event:** Summer School on Quantum Algorithms & Quantum Error Correction · CWI, Amsterdam ·
24–28 August 2026 · Poster session Wed 26 Aug 16:30–18:00 · Award ceremony Thu 27 Aug 08:50

**Author:** Rowan Quni-Gudzinas · Independent Researcher · papers.qnfo.org

> Status: VERIFIED 2026-08-16. All references resolved against the Zenodo API; one fabricated
> statistical claim from an earlier draft was removed and replaced with the verified
> cross-check result (see VERIFICATION.md).

---

## Panel 1 — The Hypothesis

- **Standard view:** QEC assumes noise accumulates over a continuous topology; logical fidelity
  improves smoothly as redundancy is added.
- **Alternative to test:** error propagation follows a discrete, hierarchical geometry — a
  Bruhat–Tits tree $T_p$ — and redundancy quantizes in units of $(p+1)$.
- **Signature to look for:** a staircase — flat plateaus followed by sudden jumps — instead of a
  smooth curve.
- **Status: hypothesis only.** No experimental result is claimed on this poster.

## Panel 2 — A Proposed Experiment (not yet run)

1. **Encode:** one logical qubit in the Shor [[9,1,3]] code.
2. **Interact:** expose it to a fixed, structured environment of spectator qubits.
3. **Correct:** run the full error-correction circuit; measure final logical fidelity.
4. **Scale:** group environment qubits into larger, hierarchical fragments; track fidelity
   across fragment boundaries.

- Smooth shift with fragment size = continuous model. Staircase = ultrametric model.
- **What exists today:** a provisional numerical toy model (Archimedean Shadows working paper)
  suggested redundancy may quantize in discrete steps (earlier versions reported steps at 3, 6,
  12, 24) — reported provisionally — and its own most seductive signature (the "forbidden
  window") **failed its own falsification test**. Null reported, not hidden.

## Panel 3 — The Cross-Check I Already Ran (it mostly failed — honestly)

- **Witness idea:** 2-adic valuations as a structural fingerprint. Conjecture C7.3 (Number-
  Theoretic Ultrametric Foundations): the Mahler-spectrum valuation $v_p^{\max}$ separates
  "optimal" codes ($v_p^{\max} = 28$) from random codes ($\approx 4$).
- **What the data say** (ACRP-06, exact weight distributions where known):

| Code family | $v_p^{\max}$ |
|---|---|
| Golay CSS [[23,1,7]] | **28** |
| Extended Golay [[24,1,8]] | **28** |
| Perfect [[5,1,3]] | 1 |
| Steane [[7,1,3]] | 2 |
| Shor [[9,1,3]] | 2 |
| Surface [[16,1,4]] / [[25,1,5]] / [[36,1,6]] | 4 / 2 / 6 |
| Random ensemble (100 trials, n=16, k=4) | mean 4.0, range 2–10 |

- **Result: the conjecture does NOT generalize.** Shor, Steane, perfect and surface codes are
  indistinguishable from the random baseline. The 28-vs-4 gap is specific to Golay-type
  self-dual symmetry — not a general "optimality" witness.
- **What it teaches:** the first witness mostly failed, and the failure is informative — the
  structure lives in an extreme-symmetry corner. **Open:** is there a refined witness (e.g.,
  valuations of the full weight distribution $v_2(A_j)$, not just the Mahler maximum) that
  discriminates where $v_p^{\max}$ fails — and does any witness connect to the staircase?

## Panel 4 — Value & Open Questions

- A smooth curve validates continuous models; a staircase would force code architectures
  designed for hierarchical noise.
- **Open:** (1) What physical mechanism would produce tree-like error geometry? (2) Does any
  valuation witness predict where the staircase should be most visible? ($v_p^{\max}$ does
  not.) (3) How would discrete geometry alter asymptotic fault-tolerance thresholds?
- **I'm here to learn:** has anyone in this room seen staircase-like scaling — or a reason it
  must be wrong?

## References (Zenodo concept DOIs — all resolved 2026-08-16)

1. Ultrametric Code Spaces: The Bruhat–Tits Tree as a Quantum Error-Correction Geometry —
   10.5281/zenodo.21824194
2. Archimedean Shadows: The QEC–Darwinism Tradeoff in Ultrametric Spaces —
   10.5281/zenodo.21809888 (latest v1.11)
3. Number-Theoretic Ultrametric Foundations (Conjecture C7.3) — 10.5281/zenodo.21193003
4. Extending v_p^max Code Classification (ACRP-06) — 10.5281/zenodo.21737221
5. The Adelic Cross-Domain Program v5 — 10.5281/zenodo.21691414 (v5.1)
6. Implications for Computing and Quantum Error Correction ("What Remains") —
   10.5281/zenodo.21922812 (v0.4)

## Footer

- **Contact:** Rowan Quni-Gudzinas · Independent Researcher · Adelic Physics Programme ·
  papers.qnfo.org · zenodo.org/communities/qnfo
- **Acknowledgment:** CWI Summer School — Research Semester Programme "Quantum Algorithms and
  Quantum Error Correction". No external funding.
