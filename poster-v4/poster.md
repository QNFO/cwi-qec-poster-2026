# Things I Don't Understand About Quantum Error Correction

**A naive audit of the constructs — the confusions of a self-taught researcher, treated as data**

**Event:** Summer School on Quantum Algorithms & Quantum Error Correction · CWI, Amsterdam ·
24–28 August 2026 · Poster session Wed 26 Aug 16:30–18:00 · Award ceremony Thu 27 Aug 08:50

**Author:** Rowan Quni-Gudzinas · Independent Researcher · papers.qnfo.org

> Status: v4 candidate (2026-08-18). Anchor verified: ZX Diagrams at the Seam
> (10.5281/zenodo.21992118, concept 21991895, published 2026-08-18, R2-mirrored).
> Replaces the v3 "diagrammatic bridge" framing with the epistemic-audit framing.

---

## Panel 1 — The Thesis: the constructs are cafeteria imports

Every human construct for understanding quantum computing is internally consistent — and the
imports contradict each other. Tools and systems are valid in their own silos; they were never
checked for mutual compatibility.

| Construct | Home silo | What it silently carries |
|---|---|---|
| Spiders | Categorical algebra (2D diagrammatic) | Drawing-plane topology; completeness proves facts about the *algebra*, nothing about spacetime |
| Pauli webs | Stabilizer formalism / QEC | 2+1D code-over-time; in holographic use: entropy, wormholes, black holes |
| Gadgets | MBQC / compilation | Graph-state resources; rewrite soundness — not physical realization |

Fault lines appear exactly where 3+1D particle physics and 1D thermodynamics are mixed into a
2D map without any compatibility check. The diagrams are not wrong — they are maps. The
discipline of using a map is knowing where it ends.

**Anchor:** "ZX Diagrams at the Seam: Spiders, Pauli Webs, Gadgets, and the Cafeteria Problem
of Cross-Disciplinary Imports" — 10.5281/zenodo.21992118 (2026-08-18).

## Panel 2 — The Method: feigned naivete as probe

I learned the room's language — the Bruhat–Tits tree T₂ (p=2, depth 3) as a ZX graph state:
22 spiders = 22 vertices, 21 H-boxes = 21 edges (fig4). Learning the language is when the seams
became visible.

I ask the questions I'm not supposed to need to ask. The naive question is the external
structural probe: it finds the locales and the seams. Where imports contradict, understanding
breaks — that break is data, not deficit.

**Method lineage:** IAPS §6.2 audit-the-map; the Universal Ignorance Audit (15 questions,
10.5281/zenodo.21901984); "Knowing What We Do Not Know" (10.5281/zenodo.21901983).

## Panel 3 — Things I don't understand about QEC

1. **Why the discreteness?** — QEC protects a discrete abstraction (gates, qubits, circuits).
   Is the discreteness physical, or imported from the circuit model? If the abstraction is a
   choice, fault tolerance is the tax on the choice.
2. **What is a logical qubit, physically?** — Hardware is bosonic oscillators with leakage
   levels; codes assume qubits. The map is 2D; the machine is continuous.
3. **What does a threshold actually guarantee?** — The proofs assume stochastic local noise.
   Coherent and correlated errors are the seams nobody prices.
4. **Where is the quantum in the loop?** — Syndrome → classical decoder → feedback. QEC is
   quantum memory + classical control. Why is it called quantum error correction?
5. **Why isn't the decoder part of the code?** — A classical algorithm decides a quantum code's
   performance. Two silos, never audited for compatibility.
6. **Why 2D geometry?** — Why a surface code and not a tree? Noise geometry is assumed
   continuous and Euclidean. What if error propagation is hierarchical — ultrametric? The
   staircase nobody has looked for.
7. **Why count T gates, not joules?** — The field prices the algebraic resource. Nobody prices
   the ancilla factory, verification retries, the decoder. What does a correct answer cost in
   energy?
8. **Why is the cat the unit of protection?** — Shor states are cat states — exponentially
   fragile to dephasing; verified ancillas go stale. Why build protection from something that
   fragile?

Each question is a probe: the answer either closes the seam (the imports were compatible all
along) or reveals it (the construct carried more than its proof).

## Panel 4 — The seams: where the map ends

| Seam | The contradiction |
|---|---|
| Discrete abstraction | Continuous physics → discrete gates → QEC defends the discreteness. The defense is priced; the choice is not. |
| Qubit / boson | The model is finite-dimensional; the hardware leaks. Every code assumes what the hardware denies. |
| Noise model | Stochastic-local assumptions meet coherent, correlated reality. Thresholds live inside the model. |
| Classical control | The decoder is classical. The "quantum" loop runs on a classical brain — known, and unpriced. |
| Cost currency | T-count is countable, so it is counted. Joules are measurable, and not measured. |
| Geometry | Euclidean 2D assumed; ultrametric tree unexamined. The staircase signature has never been searched for. |

**What I do understand:** the maps are excellent at what they map. The seam is not the diagram —
it is the silence about where the diagram ends.

## Panel 5 — The statement, the honest caption, and the questions for the room

**The one-line statement:**
> "I cannot grasp quantum computing through the practitioners' constructs because the
> constructs are maps drawn by different cartographers — internally consistent, mutually
> contradictory. My confusions are the fault lines."

**The honest caption (feigned naivete is a method, not a pose):** the naive question is the
probe that finds the seam. I am not claiming the field is wrong — I am claiming the imports
were never checked against each other. If the constructs were compatible, the naive questions
would answer themselves.

**Questions I will ask this week:**
1. "Is the discreteness of the circuit model physical or imported?"
2. "Has anyone priced the energy of the decoder — per correct solution?"
3. "Why a 2D cluster and not a tree?" (Bruhat–Tits resource states)

## References (verified 2026-08-18)

1. ZX Diagrams at the Seam — 10.5281/zenodo.21992118 (concept 10.5281/zenodo.21991895)
2. Universal Ignorance Audit — 10.5281/zenodo.21901984
3. Knowing What We Do Not Know — 10.5281/zenodo.21901983
4. Ultrametric Code Spaces — 10.5281/zenodo.21824194
5. JPCUB (joules-per-solution) — 10.5281/zenodo.21945415
6. Wan–Price–Yao, Holographic codes seen through ZX-calculus — arXiv:2601.04467
7. van de Wetering, ZX-calculus for the working quantum computer scientist — arXiv:2012.13966
8. Duncan–Kissinger–Perdrix–van de Wetering, Graph-theoretic simplification — arXiv:1902.03178
9. Wan, Iteratively decoded magic state distillation — arXiv:2410.17992

## Footer

- **Contact:** Rowan Quni-Gudzinas · Independent Researcher · Adelic Physics Programme ·
  papers.qnfo.org · zenodo.org/communities/qnfo
- **Acknowledgment:** CWI Summer School — Research Semester Programme "Quantum Algorithms and
  Quantum Error Correction". No external funding.
