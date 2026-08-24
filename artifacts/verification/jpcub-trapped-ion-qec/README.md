# jpcub-trapped-ion-qec — README

**Q:** Given noisy qubits in a trapped-ion quantum computer, which QEC code
minimizes **energy per correct answer** (JPCUB)?

**Answer (v2, 2026-08-24):** high-rate quantum LDPC — the [[144,12,12]] gross
code — with erasure conversion where available: **~36.7× less energy per correct
answer than the surface code** at the same logical fidelity (p2=1e-3), and the
winner at the energy-optimal operating point. XZZX (bias-tailored) is second
under strong dephasing bias. The tree/ultrametric class is excluded under
independent noise (verified 2e-4 qudit threshold); its regime is correlated
failure.

This artifact answers **poster v7 Panel 3 Q1** (joules-per-correct-answer) and
**Q4** (tree vs LDPC: under independent noise the answer is the LDPC class).

## Run

```
python jpcub-trapped-ion-qec.py > jpcub-trapped-ion-qec.output.txt
```

Python 3.12+, stdlib only (math). Regenerates the committed output byte-identical.

## Scope

Clifford-only, memory-style workload (syndrome cycles). No T-factory/distillation
(both families need T for universality; qLDPC non-transversal T overhead is a
relative weakness — ranking is workload-dependent), no shuttling, no wall-clock
scheduling, no crosstalk/leakage. GKP excluded (CV hardware). See the SCOPE
declaration in the script header and the Notes section of the output.

## Model caveats (uncalibrated, flagged)

XZZX threshold mapping · erasure d_eff=1.5× · Bacon-Shor/Steane rough gate
counts · p_L ansatz C=0.1 · 0.5 µJ/MS absolute normalization. The sensitivity
sweep in the output shows ranking robustness: winner flips to XZZX at bias ≥100
and at retry-dominated depth L=1e6.

## Files

- `jpcub-trapped-ion-qec.py` — model + sweep (CC BY 4.0, QNFO)
- `jpcub-trapped-ion-qec.output.txt` — generated output (clean, no wrapper)
- `references.bib` — sources (Bravyi 2024, XZZX, erasure, ion-trap, QNFO DOIs)
- `VERIFICATION.md` — red-team findings → remediation + verification results

Related: poster v7 (CWI 2026) `poster-v7/` · `docs/talking-points-v7.md` ·
JPCUB record 10.5281/zenodo.21945415.
