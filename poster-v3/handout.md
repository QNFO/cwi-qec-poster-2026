```
========================================================================
HANDOUT: Ultrametric Quantum Error Correction (CWI Summer School 2026)
========================================================================
Core idea: Standard QEC assumes noise accumulates over a continuous topology
and fidelity scales smoothly with redundancy. We are testing an alternative:
error propagation follows a discrete, hierarchical Bruhat-Tits tree geometry,
where redundancy quantizes in units of (p+1).

Experimental signature: a "staircase" of flat plateaus and sudden fidelity
jumps instead of a smooth curve.

Proposed protocol (not yet run):
1. Encode one logical qubit in the Shor [[9,1,3]] code.
2. Interact with a structured spectator-qubit environment.
3. Correct and measure final logical fidelity.
4. Group environment qubits into larger hierarchical fragments; track fidelity.

Cross-check already run - and it mostly failed (reported in full):
A 2-adic valuation witness (v_p^max of the Mahler spectrum) separates the
Golay CSS [[23,1,7]] code (v_p^max = 28) from random codes (~4) - but does NOT
generalize: Shor (2), Steane (2), Perfect (1), surface codes (2-6) all cluster
at the random baseline. The gap is a Golay-symmetry artifact, not an
optimality witness. Open: which witness can detect ultrametric structure?

------------------------------------------------------------------------
THE DIAGRAMMATIC BRIDGE (ZX-calculus) - same map, the room's notation
------------------------------------------------------------------------
Spiders (the atom): green = Z-basis copy/merge, red = X-basis. Graph-state
convention: green spider (0 in, 1 out) = |+>; yellow H-box (2 in, 2 out) = CZ
= the graph-state edge. Figure: the Bruhat-Tits tree T2 as a ZX graph state
(22 spiders = 22 vertices, 21 H-boxes = 21 edges).

Pauli webs (the stabilizers, read off the diagram): a connected sub-diagram
that evaluates to a Pauli operator - the code's stabilizers and logical
operators as paths through the spider web (Wan-Price-Yao, arXiv:2601.04467).

Gadgets (the field's cost unit): phase/Pauli gadgets e^{i aP}; T-count
optimization is gadgetization (arXiv:1902.03178; Pauli Gadget Synthesis,
QPL 2026). The algebraic cousin of an energy cost - the seam this poster
cares about.

One-line statement:
"I represent the ultrametric geometry as a ZX graph state - the same language
as the holographic-code construction on tree-like tessellations (Wan-Price-Yao
2026). The stabilizers are the Pauli webs of the diagram; the hierarchy is the
tree."

Honest caption (map != territory): the diagrams import structure from
different silos - internally consistent, externally unprobed. This handout
says so. "It's a map, not the territory - but it's the same map the field
draws."

------------------------------------------------------------------------
Working papers (Zenodo concept DOIs):
- Ultrametric Code Spaces: 10.5281/zenodo.21824194
- Archimedean Shadows (QEC-Darwinism tradeoff): 10.5281/zenodo.21809888
- Number-Theoretic Ultrametric Foundations (C7.3): 10.5281/zenodo.21193003
- ACRP-06 v_p^max extension: 10.5281/zenodo.21737221
- Adelic Cross-Domain Program v5: 10.5281/zenodo.21691414
- "What Remains" (computing/QEC implications): 10.5281/zenodo.21922812

ZX references (arXiv, verified 2026-08-18):
- Holographic codes seen through ZX-calculus: arXiv:2601.04467
- Iteratively decoded magic state distillation: arXiv:2410.17992
- ZX-calculus for the working quantum computer scientist: arXiv:2012.13966
- Graph-theoretic simplification with ZX-calculus: arXiv:1902.03178

Contact: Rowan Quni-Gudzinas . Independent Researcher . Adelic Physics Programme . papers.qnfo.org . zenodo.org/communities/qnfo
========================================================================
```
