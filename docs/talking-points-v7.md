# Talking Points — v7 "Things I Don't Understand About QEC" (CWI, Wed 26 Aug 2026)

Companion to `poster-v7/poster.html` + `poster-v7/poster-v7.pdf`. Built from the CWI Day-1
notes (D:\Obsidian\notes\v1\2026\08\24\2026-08-24.md). Plain prose; every number traces to a
DOI listed on the poster footer.

## The 30-second opening
"I'm going to say the thing the room assumes and I don't: I reject the premise that QEC is
necessary in well-designed hardware. Nature runs uncorrected, robust quantum processes —
photosynthesis, magnetoreception — with no correction scaffold. NISQ is an imperfect bridge to
better physics, and even on the bridge there are better options than surface codes. The poster
is the honest version: eight questions whose answers are not true by definition. Answer one
and you've taught me something real."

## If asked "So you're saying the field is wrong?"
"No. I'm asking where the pieces were checked against each other. The correction burden is a
design choice, not a law — that's the whole spine: 'don't mistake physics for algorithm.' The
fragility of the substrate is fixed; the code architecture is free. TQC doesn't improve the
physics — it changes the math. So does the tree class. If the constructs were compatible, the
naive questions would answer themselves."

## The hierarchy (Panel 1, punch-card → TQC)
"Punch-card machines: reliability improves, correction collapses. Active QEC: surface and LDPC
on noisy hardware — the correction loop. Tree-based class: nested, distinction-based ultrametric
trees — structural protection without an active loop; Bruhat–Tits T₂ is one instance among many,
not the concept. Topological: TQC — protection designed into the topology. The tree class sits
between active QEC and topological: structure-level protection without non-abelian anyons. That
is the open space the poster claims."

## If asked about question 1 — joules-per-correct-answer
"JPCUB's core question: what is the lowest achievable joules-per-correct-answer for a
fault-tolerant machine on a fixed workload, and is it ever below the classical machine's?
It's a real unknown because the field has never priced it — not answerable by definition.
Landauer prices the erasure; nobody prices the erasure bill of QEC."

## If asked about the erasure engine (question 2)
"Every majority vote, syndrome reset, ancilla re-init erases redundant information — Landauer
prices each erasure at kT·ln2. More redundancy means more erasure, which is a thermodynamic
wall, not just a combinatorial one. My question: does the erasure bill grow with code
sophistication, or is there a family whose per-answer cost drops as redundancy rises? The
photosynthesis/magnetoreception witness says structure can replace erasure entirely."

## If asked about the numbers
"All classical simulation: bit-flip 50.0% vs ~10.9% surface (4.6×), depolarizing 75.0% vs
~1.0% (75×), independent X+Z 17.30% vs ~18.9% (0.92× — the tree loses there). The depolarizing
figure uses the code's structured-noise channel, which is not yet published — open caveat.
Under independent errors the qudit generalization sits at ≈2×10⁻⁴, about 55× below surface
codes. No hardware. The Tanner bound on the poster — rate ≥ 1 − δb/δc — is why hierarchical
high-degree graphs carry rate that flat lattices cannot."

## If asked about the ZX panel (Panel 5)
"The slides speak ZX, so the poster speaks ZX. The tree code is a graph state in exactly the
language of the room: green spiders are |+⟩ states, yellow H-boxes are CZ edges, the diagram
is the Bruhat–Tits tree T₂ as a ZX graph state — 22 spiders, 21 H-boxes, p=2, 3-regular.
The stabilizers are Pauli webs read off the diagram; the field's cost unit is the gadget.
Same map the field draws — I just drew the tree on it."

## If asked "What would actually change your mind?"
"Four things, all with numeric criteria on the poster: a matched-noise comparison under the
same correlated-noise model — parity withdraws the advantage claim; a decoder reality check —
does a known decoder family already cover tree-structured codes; an independent re-run — the
simulator and protocol are handed over; and the classical test: these codes already guard
flash RAM, and a tree-structured nested-ball code guarding flash better and cheaper is
falsifiable today — no quantum hardware needed."

## The discreteness closer
"'We compute on discrete matrices yet insist reality is a continuous Hilbert space. Which is
the real model?' — that's the one I keep coming back to. It's the question that only makes
sense inside the frame, and inside the frame the answer is a definition. If the answer were
either value, the field's behavior would have to change."

## The four asks (same on the poster)
1. A correlated-noise benchmark (model + data) to run the matched comparison against.
2. A decoder pointer for tree-structured codes.
3. An independent re-run of the simulation.
4. Pointers on perfect tensors for p > 2 / ZX representation of the tree class.

## Closing line
"If the matched comparison survives, the instrument path exists as a published trapped-ion
protocol with numeric predictions (10.5281/zenodo.22025544). Can I send you the simulator and
the protocol?"

## Frame directives (user, 2026-08-24)
- Poster is NOT Bruhat–Tits-hitched: the class is nested, distinction-based ultrametric trees;
  B-T is one instance among many.
- Title = "Things I Don't Understand" naive-audit framing; questions must be real unknowns
  (not true by definition; either answer changes field behavior).
- Premise: reject QEC-necessity in well-designed hardware; NISQ = imperfect bridge; better
  QEC options exist.
- Poster must speak ZX (Delfosse/IonQ slides show ZX graphs).
- NEVER assert a better answer; the question is the probe.

## Evidence for Q1/Q4 (2026-08-24, JPCUB computation)

`artifacts/verification/jpcub-trapped-ion-qec/` (v2) — the JPCUB answer for trapped ions:
high-rate qLDPC [[144,12,12]] wins ~36.7× over surface at p2=1e-3; XZZX bias-tailored
second; tree/ultrametric excluded under independent noise (verified 2e-4 qudit threshold,
correlated regime only) — exactly the poster's Q1 number and Q4's LDPC-class answer.
If asked "which code is most efficient for your trap?", the honest answer is qLDPC-family,
not the tree class — under independent noise; the tree class enters via correlated-failure
regimes and T-factory (foliated/treelike distillation) layers.

## Winning the award — judge-targeted engagement (2026-08-24)

The award is decided during Wed 26 Aug 16:30–18:00 (Thu 08:50 is the announcement). The
judges are the lecturers; each has ONE question on the poster only they can answer.

- **Delfosse (IonQ)** — primary target; his slides speak ZX, the poster speaks ZX.
  Hook: "Your lecture drew ZX graphs; this poster draws the tree code as a ZX graph
  state — 22 spiders, 21 H-boxes, p=2, 3-regular." Then Q4. Then the trump card:
  "I priced your platform — energy per correct answer: qLDPC [[144,12,12]] ~36× cheaper
  than surface d=11 at p2=1e-3 (~0.96 J vs ~35 J per 10^4 correct gates). Want the model?"
  (artifacts/verification/jpcub-trapped-ion-qec/, commit 117171d)
- **Leverrier (Inria)** — qLDPC authority. Hook: the Tanner bound (rate >= 1 - db/dc)
  + Q4. Let him argue tree-vs-LDPC — that IS the conversation.
- **Nayak (IQC)** — complexity. Hook: Q6 (model-free quantum speedup). If he dismantles
  it, the numeric disconfirmation criteria make that a win, not a loss.
- **Gilyen (Renyi)** — algorithms. Hook: Q2 (erasure bill) or Q8 (intrinsic quantum);
  the discreteness closer is the memorable exit.

Mechanics: stand, don't sit; greet first; ask their research before pitching; one
question per visitor; never argue ("correct me, and the poster has done its job");
exit line: "Can I follow up by email?"; no handouts. The 30-second version must land:
premise rejection + one sharp question + the ZX bridge.
