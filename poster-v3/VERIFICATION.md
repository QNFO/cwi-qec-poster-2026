---
modified: 2026-08-18T11:00:00Z
status: VERIFIED v3 PACKAGE
verified_against: arXiv API (4 ZX refs, 2026-08-18) + fig4 DOM check + poster-v2 verified content (2026-08-16)
---
# CWI Poster v3 — Verification Note (ZX Diagrammatic Bridge)

v3 adds **Panel 5 — The Diagrammatic Bridge (ZX-calculus)** to the verified v2 package
(panels 1–4 and all v2 content unchanged). Source note:
`_zx-literacy-spiders-pauli-webs-gadgets-2026-08-18.md` (QPL Day 2 grounding).

## What changed

| File | Change |
|---|---|
| `poster.html` | + Panel 5 (full-width ZX band with embedded fig4 SVG), footer + 4 ZX refs, title → v3, grid 3rd row added |
| `poster.md` | + Panel 5 text, + ZX reference list (items 7–10) |
| `handout.md` / `handout.html` | + Diagrammatic Bridge section (terms + one-line statement + honest caption), + ZX refs |
| `zx-cheat-card.html` | NEW — pocket card for the session (terms, statement, seam, Q1/Q2, rules) |
| `figures/fig4-zx-bruhat-tits.svg` | NEW — Bruhat–Tits tree T₂ (p=2, depth 3) as ZX graph state |

## Reference verification (2026-08-18, arXiv API)

| Ref | arXiv ID | Status |
|---|---|---|
| Wan, Price & Yao — Holographic codes seen through ZX-calculus | 2601.04467 | ✅ verified (2026-01-08; Pauli webs + ZX-diagrams on dual hyperbolic tessellations) |
| Wan — Iteratively decoded magic state distillation | 2410.17992 | ✅ verified (2024-10-23; Pauli webs benchmark stabiliser proxies) |
| van de Wetering — ZX-calculus for the working quantum computer scientist | 2012.13966 | ✅ verified (2020-12-27) |
| Duncan, Kissinger, Perdrix & van de Wetering — Graph-theoretic simplification | 1902.03178 | ✅ verified (2019-02-08) |

Venue attribution discipline (ZENODO-VENUE-ATTRIBUTION-1): the poster cites arXiv IDs for all
ZX references; "Pauli Gadget Synthesis, QPL 2026" (Meijer-van de Griend & Becker) is cited
without a proceedings volume (no EPTCS claim).

## fig4 structural verification

- 22 spiders = 22 vertices (1 + 3 + 6 + 12) ✅
- 21 H-boxes = 21 edges (3 + 6 + 12) ✅
- Tree on 22 vertices ⇒ 21 edges ✅ (3-regular = p=2 Bruhat–Tits truncation, matches fig2 topology)
- Convention cited: green spider 0-in-1-out = |+⟩, yellow H-box = CZ (van de Wetering 2012.13966)

## Honesty framing (cafeteria problem)

Panel 5 carries the explicit caption that the diagrams are maps, not territory — the
import-structure critique is stated on the poster itself (IAPS §6.2 audit-the-map). The
one-line legitimacy statement and the honest seam ("It's a map, not the territory — but it's
the same map the field draws") are the conversation openers for the session.

## Print

- Poster: open `poster.html` → Ctrl+P → A0 portrait → margins none → 100% (or use the
  generated `poster-v3.pdf`).
- Handout: `handout.html` → Ctrl+P → A4.
- Cheat card: `zx-cheat-card.html` → Ctrl+P → A4.
