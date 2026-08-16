# CWI 2026 — Poster Figures Kit

Standalone print-ready vector graphics for the poster panels. All SVGs are scalable to any
size (A0 panel insets to slide-size). Verified against the ACRP-06 data (10.5281/zenodo.21754148)
on 2026-08-16.

| File | Panel | What it shows | In poster.html? |
|---|---|---|---|
| `fig0-bruhat-tits-tree.svg` | (optional, spare) | Bruhat–Tits tree diagram — the tree geometry itself (from poster v1) | no (spare) |
| `fig1-redundancy-staircase.svg` | Panel 1 | Smooth fidelity curve (standard QEC) vs. staircase (ultrametric hypothesis). Hypothesis only; not observed. | yes (inline copy) |
| `fig2-hierarchical-fragments.svg` | Panel 2 | Shor [[9,1,3]] logical qubit at center, environment qubits nested into hierarchical fragments across (p+1) boundaries | yes (inline copy) |
| `fig3-vpmax-witness.svg` | Panel 3 | v_p^max by code family: only Golay-type self-dual codes (28) separate from the random baseline (mean 4.0, range 2–10) | yes (inline copy) |

## Usage

- **Print the whole poster:** open `../poster.html` in Chrome/Edge → Ctrl+P → A0 portrait →
  margins none → 100%. Figures are embedded inline (self-contained file).
- **Print individual figures:** open any `.svg` in a browser → Ctrl+P → A4/A3 as needed.
- **For a slide or handout:** drag any `.svg` into PowerPoint/Word/Inkscape — infinite
  resolution vector.
- **Regenerate from source:** `../tikz-figures.tex` contains the TikZ sources (fixed) for
  Figures 1 and 2; the SVGs here are their rendered equivalents. Figure 3 has no TikZ source —
  it was generated directly from the ACRP-06 results table.

Note: `preview.html` shows all figures on one page for a quick print check.
