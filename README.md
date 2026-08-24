# CWI QEC Poster 2026 — Print-Ready Assets

## What's Here

| File | Description | Print Size |
|---|---|---|
| `poster-v5-treecode/poster.html` | **THE poster (decided 2026-08-21)** — "The Bruhat–Tits Tree Code: Status and Test Plan": testing roadmap (T1–T5 with numeric disconfirmation criteria), 6 DOIs, plain prose. PDF: `poster-v5.pdf` (A0). | A0 (841×1189 mm) |
| `poster-v5-treecode/handout.html` | v5 A4 handout — test table + DOIs (internal-only; no handouts, 2026-08-21 decision). PDF: `handout-v5.pdf`. | A4 (210×297 mm) |
| `poster-v4/poster.html` | **CANDIDATE (user's current direction, 2026-08-18)** — "Things I Don't Understand About Quantum Error Correction": naive-audit framing anchored on *ZX Diagrams at the Seam* (10.5281/zenodo.21992118) — 8 questions, 6 seams, fig4 method panel. PDF: `poster-v4.pdf` (A0). | A0 (841×1189 mm) |
| `poster-v4/handout.html` | v4 A4 handout — thesis + method + questions + statement. PDF: `handout-v4.pdf`. | A4 (210×297 mm) |
| `poster-v4-nozx/poster.html` | **CANDIDATE (added 2026-08-21)** — v4 naive audit with the ZX anchor removed (user decision: "ZX maybe leave out"): plain intro + the self-correction credibility line + the 8 QEC questions + 6 seams, zero diagrammatic-calculus content. PDF: `poster-v4-nozx.pdf` (TRUE A0). | A0 (841×1189 mm) |
| `poster-v3/poster.html` | **RECOMMENDED until user decides** — Ultrametric QEC poster **v3**: v2 (panels 1–4, verified 2026-08-16) + **Panel 5 — The Diagrammatic Bridge (ZX-calculus)** with fig4 (Bruhat–Tits tree as ZX graph state), the one-line statement, the map≠territory caption, and 4 arXiv-verified ZX references. PDF: `poster-v3.pdf` (A0). | A0 (841×1189 mm) |
| `poster-v3/handout.html` | v3 A4 handout — leave-behind matching poster v3 (+ ZX section). PDF: `handout-v3.pdf`. | A4 (210×297 mm) |
| `poster-v3/zx-cheat-card.html` | Pocket card for the session: three ZX terms, one-line statement, seam, two questions. PDF: `zx-cheat-card.pdf`. | A4 (210×297 mm) |
| `poster-v3/figures/` | fig4-zx-bruhat-tits.svg (22 spiders / 21 H-boxes, verified) | Scalable vector |
| `poster-v3/VERIFICATION.md` | v3 verification note (arXiv refs + fig4 DOM check) | — |
| `poster-v2/poster.html` | Ultrametric QEC poster v2 (hypothesis-testing framing + verified cross-check). Figures 1–3 embedded inline (self-contained). Verified 2026-08-16; all references resolve. | A0 (841×1189 mm) |
| `poster-v2/figures/` | **Standalone print-ready figures** — fig0 (Bruhat–Tits tree, spare), fig1 (staircase), fig2 (hierarchical fragments), fig3 (v_p^max witness chart) + preview.html | Scalable vector |
| `poster-v2/handout.html` | v2 A4 handout — leave-behind matching poster v2 | A4 (210×297 mm) |
| `poster-v2/poster.md` / `abstract.md` | v2 content source + formal abstract | — |
| `poster-v2/tikz-figures.tex` | Fixed LaTeX/TikZ figures (grid line-width bug + caption typo fixed) | — |
| `poster-v2/VERIFICATION.md` | Full audit: fabricated claim removed, DOI mapping, event facts | — |
| `poster/poster.html` | v1 poster — five open questions framing (still valid alternative) | A0 (841×1189 mm) |
| `poster/tree-diagram.svg` | Bruhat-Tits tree diagram (standalone) | Scalable |
| `poster/handout.html` | v1 A4 handout | A4 (210×297 mm) |

## Quick Start (either poster)

1. **Open the PDF directly** (`poster-v5-treecode/poster-v5.pdf` etc.) — it is already the exact A0 portrait page (841 × 1189 mm, full-bleed, zero margins; MediaBox-verified).
2. Press `Ctrl+P` **on the PDF** (not the HTML).
3. Set **Orientation** → **Portrait**, **Paper** → **A0**, **Scale** → **100%**, **Margins** → **None**.
4. Print.

> ⚠️ **Print trap (2026-08-21):** do NOT judge the layout from a browser print-preview of the HTML — the preview re-flows the poster onto whatever paper is selected (default Letter/A4 can make the portrait poster LOOK landscape with white margins). The PDF is ground truth: portrait A0, content fills the page (pixel-verified 2026-08-21: content 796 × 1156 mm, bottom margin ≈14 mm = footer padding). If the printer only accepts landscape sheets, use auto-rotate/portrait orientation — never rotate the content itself.

## Workshop Details (verified 2026-08-16)

- **Event:** CWI Summer School on Quantum Algorithms and Quantum Error Correction
- **Dates:** 24–28 August 2026
- **Venue:** WCW Turingzaal, Science Park 125, Amsterdam
- **Poster Session:** Wednesday 26 August, 16:30–18:00 ("Poster session + Pizza")
- **Poster Award Ceremony:** Thursday 27 August, 08:50–09:00
- **Registration:** closed. The event page lists no poster submission procedure → bring the
  poster on-site; confirm board dimensions at registration (Mon 24 Aug).
- **Lecturers:** Nicolas Delfosse (IonQ), Anthony Leverrier (Inria), Ashwin Nayak (IQC),
  András Gilyén (Rényi Institute)

## Which poster to print?

**THE poster (decided 2026-08-24, overnight revision 24→25 Aug): `poster-v7/poster-v7.pdf`** —
"Things I Don't Understand About Quantum Error Correction" (v7.1 standalone, 2026-08-24) — built from the CWI Day-1 talks; v7.1 removes conversational framing and answers Q1 on-poster with the JPCUB computation (qLDPC [[144,12,12]] ~36× vs surface).
Frame = **tree-based vs surface codes** (the tree class = nested, distinction-based ultrametric
trees; Bruhat–Tits T₂ one instance among many). Spine = the user's premise rejection: QEC is
**not necessary in well-designed hardware**; NISQ is an imperfect bridge to better physics;
even on the bridge, better QEC options exist. Eight **real-unknown questions** (joules-per-
correct-answer, the Landauer erasure bill, vanishing-overhead codes, decoding complexity
class, substrate-intrinsic vs algorithm-chosen, model-free quantum speedup, syndrome
measurement cost, intrinsic definition of "quantum") + the discreteness closer ("We compute
on discrete matrices yet insist reality is a continuous Hilbert space. Which is the real
model?"). **ZX bridge panel** (fig4: the tree as a ZX graph state — 22 spiders, 21 H-boxes —
plus spiders/Pauli-webs/gadgets vocabulary, so the poster speaks the language of the slides).
TRUE A0 portrait, full-bleed, pixel-verified (content to 1171 mm, bottom margin 18.3 mm),
0 U+FFFD, all 6 panels zero overflow. Self-contained — **no handouts** (user decision).
Supersedes v6 (2026-08-24 morning).

Alternates (kept as A0 PDFs if wanted):
- **poster-v6/poster-v6.pdf** — "Things I Don't Understand About QEC" (naive audit with the
  8 frame-probe outside-the-frame/inside-the-definition questions; superseded by v7).
- **poster-v5-treecode/poster-v5.pdf** — "The Bruhat–Tits Tree Code — Status and Test Plan"
  (previous THE poster; testing roadmap T1–T5, 6 DOIs).
- **poster-v4-nozx/poster-v4-nozx.pdf** — "Things I Don't Understand About QEC" (naive audit
  without the ZX anchor; 8 questions + 6 seams; verified refs).
- **poster-v2/poster-v2.pdf** — the verified v2 package (hypothesis → proposed experiment →
  cross-check that mostly failed → open questions).
- poster-v3/poster-v3.pdf, poster-v4/poster-v4.pdf — earlier versions, kept with ZX content.
- poster v1 (poster/poster.html) — five open questions. Note: v1 cites the Archimedean Shadows
  v1.10 record DOI; update to the concept DOI (10.5281/zenodo.21809888) before printing v1.

## Related Publications (Zenodo concept DOIs)

- Archimedean Shadows (QEC–Darwinism tradeoff, latest v1.11) — 10.5281/zenodo.21809888
- Ultrametric Code Spaces — 10.5281/zenodo.21824194
- Number-Theoretic Ultrametric Foundations (C7.3) — 10.5281/zenodo.21193003
- ACRP-06: Extending v_p^max Code Classification — 10.5281/zenodo.21737221
- Adelic Cross-Domain Program v5 — 10.5281/zenodo.21691414
- "What Remains" (computing/QEC implications) — 10.5281/zenodo.21922812
- p-Adic Quantum Metrology v1.1 — 10.5281/zenodo.21748127
- ACRP-08 Paradigm Forecast — 10.5281/zenodo.21747227
- Adelic Shannon Theory v2.1 — 10.5281/zenodo.21698976
- Adelic Entropic Numbers v1.1 — 10.5281/zenodo.21698978
- Adelic Rate-Distortion Theory v1.0 — 10.5281/zenodo.21705076

## Verification artifacts

- `artifacts/verification/jpcub-trapped-ion-qec/` — **JPCUB energy-per-correct-
  answer for trapped-ion QEC families (v2, 2026-08-24)** — answers poster v7
  Q1/Q4: qLDPC [[144,12,12]] wins ~36.7× over surface at p2=1e-3; XZZX bias-
  tailored second; tree/ultrametric excluded under independent noise (correlated
  regime only). Model + output + references.bib + VERIFICATION.md (red-team
  findings → remediation). JPCUB record: 10.5281/zenodo.21945415.
