# poster-v7 — VERIFICATION (2026-08-24)

**Title:** Things I Don't Understand About Quantum Error Correction
**Subtitle:** Tree-based vs surface codes — the questions that only make sense inside the frame
**Version:** v7.1 — standalone (no conversational framing); Q1 answered with the JPCUB computation (2026-08-24)
**Event:** CWI Summer School on Quantum Algorithms & QEC · Poster session Wed 26 Aug 16:30–18:00

## User directives (2026-08-24, overnight revision 24→25 Aug per CWI Day-1 talks)

1. **Reject the v6 question set** — replaced by eight *real-unknown* questions from the
   CWI day-1 material (criterion: a question exposes a real unknown iff its answer is not
   true by definition; if the answer were either value, the field's behavior would change).
2. **Premise rejection:** "I reject the premise that QEC is necessary in well-designed
   hardware." Poster spine = QEC necessity is not a law; NISQ is an imperfect bridge to
   better physics; even on the bridge, better QEC options exist (tree-based class).
3. **ZX fluency:** CWI QEC slides (Nicolas Delfosse, IonQ) show ZX graphs → the poster
   speaks ZX: fig4 (Bruhat–Tits tree as ZX graph state, 22 spiders / 21 H-boxes) + the
   three ZX terms (spiders, Pauli webs, gadgets) + codeword/syndrome/tree-code vocabulary.
4. Source of truth: CWI Obsidian notes 2026-08-24 (D:\Obsidian\notes\v1\2026\08\24\2026-08-24.md)
   — Landauer erasure engine, punch-card→TQC hierarchy, physics-vs-algorithm spine,
   flash-RAM classical opportunity, "reality is a syndrome".

## Checks performed (all PASS)

| Check | Method | Result |
|---|---|---|
| Page size | pypdf MediaBox | 841.0 × 1188.9 mm (TRUE A0, portrait) |
| Pages | pypdf | 1 |
| U+FFFD (decompressed text) | pypdf extract_text scan | 0 |
| Text extraction | pypdf | 8237 chars, all probes present |
| Panel overflow (DOM) | Runtime.evaluate scrollHeight vs clientHeight | 6/6 panels zero overflow (1239 = 1239) |
| Content fill (pixels) | Chrome screenshot 3179×4494 + numpy | content bbox 0..1171 mm, bottom margin 18.3 mm |
| Header band | pixel | 98.9% non-white (dark gradient) |
| Footer band | pixel | at true bottom (4275..4494 px) |
| Panel fill | DOM last-child | 97–98% of panel height (space-between) |

## Content gates

- PUBLICATION-BRAND-LANGUAGE-1: 0 banned tokens (sweep incl. "honest", "ledger",
  "[speculative]", "kill-condition", "weigh this record", "pissing match", "navel-gazing").
- NAMING-MANDATE-1: full name "Rowan Brad Quni-Gudzinas"; org = QNFO only.
- Frame directive: tree-based vs surface codes; Bruhat–Tits T₂ = "one instance among many"
  (Panel 1) / "One instance of the class" (Panel 2 caption) — never the hitching concept.
- Premise directive: Panel 1 opens "QEC is not necessary in well-designed hardware" +
  "NISQ is an imperfect bridge to better physics" + "better QEC options than surface codes".
- ZX directive: Panel 5 = ZX bridge (fig4 graph state + spiders/Pauli webs/gadgets + vocab).
- Question set: the 8 real-unknown questions (joules-per-answer, erasure bill, vanishing
  overhead, decoding complexity class, substrate-intrinsic vs algorithm-chosen, model-free
  quantum speedup, syndrome measurement cost, intrinsic definition of quantum) + the
  discreteness closer ("We compute on discrete matrices yet insist reality is a continuous
  Hilbert space. Which is the real model?").
- Numbers: 50.0% / 75.0% / 17.30% tree vs ~10.9% / ~1.0% / ~18.9% surface; ratios 4.6× /
  75× / 0.92×; qudit ≈2×10⁻⁴ ≈55× below surface; rate ≥ 1 − δb/δc Tanner bound — all
  consistent with poster-v5 table + CWI day-1 notes.
- DOIs: 20109836, 22038733, 21046993, 22025544, 21809888, 21979060, 21901984, 21901983
  (verified set from v6) + 22076816 + 22076806 (both live-resolved 2026-08-24 in the
  red-team consistency audit; the CWI notes name them as consistency anchors).

## Render

Chrome headless `--print-to-pdf` with @page 841mm 1189mm, no headers/footers.
Source: `poster.html` (this folder). Output: `poster-v7.pdf`.
