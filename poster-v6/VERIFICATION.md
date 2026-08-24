# poster-v6 — VERIFICATION (2026-08-24)

**Title:** Things I Don't Understand About Quantum Error Correction
**Subtitle:** Tree-based vs surface codes: questions that only make sense inside the frame
**Version:** v6 — naive audit, sharp frame-probe questions, 2026-08-24
**Event:** CWI Summer School on Quantum Algorithms & QEC · Poster session Wed 26 Aug 16:30–18:00

## User directive (2026-08-24)

Complete overhaul, back to "Things I Don't Understand" with sharp, pointed questions that
make no sense outside of tautological/definitional frame/domain. Poster frame = tree-based vs
surface codes (supersedes the B-T-hitched v5 framing; Bruhat–Tits = one instance of the broad
class of nested, distinction-based ultrametric trees, never the limiting concept).

## Checks performed (all PASS)

| Check | Method | Result |
|---|---|---|
| Page size | pypdf MediaBox | 841.0 × 1188.9 mm (TRUE A0, portrait) |
| Pages | pypdf | 1 |
| U+FFFD (decompressed text) | pypdf extract_text scan | 0 |
| Text extraction | pypdf | 7564 chars, all probes present |
| Panel overflow (DOM) | Runtime.evaluate scrollHeight vs clientHeight | 6/6 panels zero overflow |
| Content fill (pixels) | Chrome screenshot 3179×4494 + numpy | content bbox 0..1173 mm, bottom margin 15.6 mm (footer padding) |
| Header band | pixel | 98.3% non-white (dark gradient) |
| Footer band | pixel | at true bottom (4275..4494 px) |

## Content gates

- PUBLICATION-BRAND-LANGUAGE-1: no banned brand tokens ("honest ledger", "weigh this record",
  "[speculative]", internal gate names as headers). Plain scholarly prose.
- PUBLICATION-META-PROSE-1: no "published, not hidden" class phrases.
- NAMING-MANDATE-1: full name "Rowan Brad Quni-Gudzinas"; org = QNFO only.
- Frame directive: tree-based vs surface codes; Bruhat–Tits T₂ described as one instance of the
  class ("not the concept").
- Numbers: 50.0% / 75.0% / 17.30% tree vs ~10.9% / ~1.0% / ~18.9% surface; ratios 4.6× / 75× /
  0.92×; qudit ≈2×10⁻⁴ ≈55× below surface — all consistent with poster-v5 table + roadmap.
- DOIs: 20109836, 22038733, 21046993, 22025544, 21809888, 21979060, 21901984, 21901983 — same
  verified set as v5 footer.

## Render

Chrome headless `--print-to-pdf` with @page 841mm 1189mm, no headers/footers.
Source: `poster.html` (this folder). Output: `poster-v6.pdf`.
