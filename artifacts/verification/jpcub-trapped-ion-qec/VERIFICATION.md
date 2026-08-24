# jpcub-trapped-ion-qec — VERIFICATION (v2, 2026-08-24)

**Artifact:** energy-per-correct-answer comparison of QEC code families for a
trapped-ion quantum computer (JPCUB metric, 10.5281/zenodo.21945415).
**Repo:** QNFO/cwi-qec-poster-2026 · `artifacts/verification/jpcub-trapped-ion-qec/`
**Files:** `jpcub-trapped-ion-qec.py` (source) · `jpcub-trapped-ion-qec.output.txt`
(generated output) · `references.bib` · `README.md` · `VERIFICATION.md` (this).

## Red-team findings → remediation (CMD RED TEAM 2026-08-24, commit 7f326ae)

| ID | Severity | Finding | v2 remediation | Status |
|---|---|---|---|---|
| A1 | HARD | E2 cap made sub-1e-3 operation artificially cheap; "XZZX d=3 2nd place" was a cap artifact | E2(p2) UNCAPPED = E2_ref·(1e-3/p2), floored at 1e-4; XZZX d=3 corrected 1.461e6→7.681e6; winner unchanged (qLDPC+erasure 1.163e6) | ✅ verified |
| C1 | HARD | Silent Clifford-only/memory-only scope; T-factory absent; idle_us dead code | Explicit SCOPE declaration in header + output; T-factory caveat in Notes; idle wired via wall-clock (T_MS/T_1Q/T_M/T_COOL) | ✅ |
| C2 | SOFT | No sensitivity sweep | One-at-a-time sweep: bias {1,10,100}, erasure {1.0,1.5,2.0}, threshold {0.5,1.5}×, L {1e3,1e4,1e6}, budget {1e-6,1e-8}. Winner robust at bias 1/10; flips to XZZX at bias 100; L=1e6 flips to XZZX d=7 | ✅ |
| C3 | SOFT | Missing families | Added repetition (corrected weight-1 X-error model → extreme-bias only), Bacon-Shor (rough), concatenated Steane (rough), foliated/treelike T-factory note (ultrametric connection), GKP exclusion note | ✅ |
| C4 | SOFT | No README/VERIFICATION | This file + README.md added | ✅ |
| C5 | SOFT | Flat decoder cost | ED scaled by check weight (ED0·w/4); BP+OSD (w=6) > MWPM (w=4) | ✅ |
| D1 | SOFT | EXIT=0 wrapper in committed output | Output regenerated clean from script (no wrapper) | ✅ |
| D2/D3 | SOFT | Artifact not linked from README/talking-points | Repo README + talking-points-v7 link added | ✅ |
| D4/D5 | SOFT/DESIGN | No citations/license; decoder energy | references.bib + CC BY 4.0 header + check-weight decoder | ✅ |

## Verification results (v2, all reproducible)

- **Headline (fixed p2=1e-3):** qLDPC [[144,12,12]] E_correct = 1.929e6 vs surface
  d=11 = 7.089e7 → **~36.7×**; XZZX d=5 = 6.696e6 between; tree/ultrametric
  excluded under independent noise (p_L = 2.50, threshold 2e-4 ≈ 55× below
  surface ~1.1e-2 — consistent with poster v7 / 10.5281/zenodo.21046993).
- **Operating point (uncapped):** winner = qLDPC + erasure conversion (1.163e6
  at p2=1.79e-3, gate_speed 0.56); plain qLDPC 1.896e6; XZZX d=5 5.776e6;
  XZZX d=3 7.681e6; surface d=5 2.881e7.
- **Absolute scale** (E2 ≈ 0.5 µJ): ~35.4 J vs ~0.96 J per 10⁴ correct logical
  gates (surface d=11 vs qLDPC at p2=1e-3).
- **Sensitivity:** winner qLDPC+erasure robust across bias 1–10, threshold ×0.5–1.5,
  erasure ×1.5–2.0, budgets; **flips to XZZX at bias 100** (9.72e5) and to XZZX d=7
  at L=1e6 (retry-penalty regime) — ranking is bias/workload-dependent, as stated.
- **Reproducibility:** `python jpcub-trapped-ion-qec.py > output.txt` (Python 3.12,
  stdlib only) regenerates the committed output byte-identical; red-team
  Dependency reviewer confirmed for v1, v2 output regenerated same-turn here.
- **Excluded with reason:** GKP (CV hardware); repetition at bias ≤100 (weight-1 X
  error); tree/ultrametric under independent noise (correlated regime only).

## Model caveats (uncalibrated choices — flagged, not hidden)

XZZX threshold mapping 0.010·(1+bias)/2 · erasure d_eff = 1.5×d · Bacon-Shor and
Steane gate counts are rough heuristics · p_L ansatz constant C=0.1 · absolute
energy normalization (0.5 µJ/MS) is a place-holder order-of-magnitude. Sensitivity
block shows the ranking's robustness boundaries.
