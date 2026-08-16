# Verification Report — CWI Poster Package (2026-08-16)

The 10 chat-generated draft notes from 2026-08-16 were audited against primary sources before
use. Method: Zenodo REST API (9 records, 2026-08-16), the CWI event page (fetched via Python
urllib; session browser had DNS failure), and the QNFO corpus via D1 (ACRP-06 full text).

## HARD findings (all fixed)

### HARD-1 — Fabricated statistical claim removed (Panel 3)

Draft claim: *"Four structured families (Shor, Steane, Perfect, Toric) exhibit >3σ outliers
when benchmarked against 10⁴ random stabilizer codes with identical parameters."*

**False on every axis**, and contradicts the author's own published record — ACRP-06
(10.5281/zenodo.21754148), which extended the Mahler-spectrum valuation conjecture to 8
additional stabilizer families:

| Family | v_p^max | Verdict |
|---|---|---|
| Golay CSS [[23,1,7]] | 28 | separates |
| Ext. Golay [[24,1,8]] | 28 | separates |
| Perfect [[5,1,3]] | 1 | random-like |
| Steane [[7,1,3]] | 2 | random-like |
| Shor [[9,1,3]] | 2 | random-like |
| Surface [[16,1,4]]–[[36,1,6]] | 2–6 | random-like |
| Random ensemble | mean 4.0, range 2–10 | baseline |

- Shor/Steane/Perfect are **indistinguishable from random**, not ">3σ outliers".
- The real outlier is the **Golay-type self-dual family** — the opposite direction.
- The random ensemble was **100 trials**, not 10⁴.
- **Toric codes were never tested** in the cited corpus.

Fix: Panel 3 rewritten to report the verified bounded negative result honestly. The original
C7.3 conjecture (Number-Theoretic Ultrametric Foundations, 10.5281/zenodo.21193487) survives
only in the restricted Golay-type form — now the poster's centerpiece cross-check story.

### HARD-2 — Placeholder and non-existent references

- All draft citations read "10.5281/zenodo:" with **no identifier**.
- Reference [3] "The v_2(A_j) structural witness data repository" — **no such record exists**.
  Replaced with ACRP-06 (concept DOI 10.5281/zenodo.21737221).
- Fix: all references mapped to verified records with concept DOIs.

### HARD-3 — Fabricated funder acknowledgments

Draft footer claimed "NWO/OCW · Quantum Software Consortium · Quantum Delta NL". No such
funding exists for this independent work. Removed; acknowledgment names the venue only.

## Defects fixed

| Defect | Fix |
|---|---|
| Figure caption "Shor [[1] stabilizer code" | → Shor [[9,1,3]] |
| `grid style={line width=pt, ...}` (invalid LaTeX, ×4) | → 0.4pt / 0.8pt |
| `\pgfmathtruncatemacro{\angle}{...}` redefines `\angle` | → `\ang` |
| Mojibake "24â€“28 August" (bad UTF-8 conversion) | → 24–28 August |
| Contact placeholder "[your.email@institution.nl]" | → papers.qnfo.org + Zenodo community (matches v1 poster convention) |
| Q&A answer defending the fabricated claim | → replaced with honest falsification-framing answer |

## SOFT findings (not blocking)

1. **Archimedean Shadows is no longer frozen at v1.10.** The record (concept
   10.5281/zenodo.21809888) now carries **v1.11, published 2026-08-16** with new artifacts
   (bt-tree-post-recovery-analysis.json, pdf-verification-v1.11.txt). The v1.10 freeze decision
   appears superseded. This poster cites the concept DOI and hedges version-specific numbers
   ("earlier versions reported steps at 3, 6, 12, 24").
2. **The existing v1 poster** (`poster/poster.html`) cites the v1.10 record DOI
   (10.5281/zenodo.21819232) rather than the concept DOI — update before printing v1. Its other
   references all resolve (verified today).
3. **Strong claim on the v1 poster** ("already beats classical sensors with hardware that
   exists today") was not re-audited in this cycle; the source record
   (10.5281/zenodo.21748249) resolves, but re-verify the claim against its latest version
   before printing v1.

## Event facts (CWI page, fetched 2026-08-16)

- Poster session: **Wed 26 Aug 16:30–18:00** ("Poster session + Pizza").
- **Poster award ceremony: Thu 27 Aug 08:50–09:00** — the draft notes never mentioned this.
- Registration closed; no poster submission procedure listed on the page → on-site logistics;
  confirm board dimensions at registration (Mon 24 Aug).
- Lecturers confirmed: Delfosse (IonQ), Leverrier (Inria), Nayak (IQC), Gilyén (Rényi).

## Recommendation

Print **poster-v2** (`poster.html`, A0 portrait). It keeps the hypothesis-testing framing,
adds the verified cross-check story (the honest null IS the credibility asset), and removes
every fabricated element. The existing five-questions poster remains a strong alternative; if
chosen, apply SOFT findings 1–2 first. Bring 15–20 handouts, tape/pins, pre-loaded Zenodo tabs.
