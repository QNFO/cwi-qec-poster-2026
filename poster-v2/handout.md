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

Working papers (Zenodo concept DOIs):
- Ultrametric Code Spaces: 10.5281/zenodo.21824194
- Archimedean Shadows (QEC-Darwinism tradeoff): 10.5281/zenodo.21809888
- Number-Theoretic Ultrametric Foundations (C7.3): 10.5281/zenodo.21193003
- ACRP-06 v_p^max extension: 10.5281/zenodo.21737221
- Adelic Cross-Domain Program v5: 10.5281/zenodo.21691414
- "What Remains" (computing/QEC implications): 10.5281/zenodo.21922812

Contact: Rowan Quni-Gudzinas . papers.qnfo.org . zenodo.org/communities/qnfo
========================================================================
```
