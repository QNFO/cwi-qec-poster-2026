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

## Panel 5 — The Diagrammatic Bridge (ZX-calculus)

> Speaking the room's language — same map, different notation.

**Spiders — the atom.** Green = Z-basis copy/merge, red = X-basis. Graph-state convention:
green spider (0 in, 1 out) = |+⟩; yellow H-box (2 in, 2 out) = CZ = the graph-state edge.

**Pauli webs — the stabilizers, read off the diagram.** A connected sub-diagram that evaluates
to a Pauli operator: the code's stabilizers and logical operators as paths through the spider
web (Wan–Price–Yao, arXiv:2601.04467).

**Gadgets — the field's cost unit.** Phase/Pauli gadgets e^{iαP}: T-count optimization is
gadgetization (Duncan–Kissinger–Perdrix–van de Wetering, arXiv:1902.03178; Pauli Gadget
Synthesis, QPL 2026). The algebraic cousin of an energy cost — the seam this poster cares about.

**Figure 4:** the Bruhat–Tits tree T₂ (p=2, truncated depth 3) drawn as a ZX graph state —
22 spiders = 22 vertices, 21 H-boxes = 21 edges. The ultrametric geometry, in the room's own
diagrammatic language.

**The one-line statement:**
> "I represent the ultrametric geometry as a ZX graph state — the same language as the
> holographic-code construction on tree-like tessellations (Wan–Price–Yao 2026). The
> stabilizers are the Pauli webs of the diagram; the hierarchy is the tree."

**The honest caption (map ≠ territory):** the diagrams import structure from different silos —
internally consistent, externally unprobed. This caption says so. Acknowledging the seam is the
legitimacy move (IAPS §6.2, audit the map).
> "It's a map, not the territory — but it's the same map the field draws."

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

## ZX references (arXiv — all verified 2026-08-18)

7. Wan, Price & Yao, Holographic codes seen through ZX-calculus — arXiv:2601.04467
8. Wan, Iteratively decoded magic state distillation — arXiv:2410.17992
9. van de Wetering, ZX-calculus for the working quantum computer scientist — arXiv:2012.13966
10. Duncan, Kissinger, Perdrix & van de Wetering, Graph-theoretic Simplification of Quantum
    Circuits with the ZX-calculus — arXiv:1902.03178

## Footer

- **Contact:** Rowan Quni-Gudzinas · Independent Researcher · Adelic Physics Programme ·
  papers.qnfo.org · zenodo.org/communities/qnfo
- **Acknowledgment:** CWI Summer School — Research Semester Programme "Quantum Algorithms and
  Quantum Error Correction". No external funding.
