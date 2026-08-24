# Talking Points — v6 "Things I Don't Understand About QEC" (CWI, Wed 26 Aug 2026)

Companion to `poster-v6/poster.html` + `poster-v6/poster-v6.pdf`. Plain prose; every number
traces to a DOI listed on the poster footer.

## The 30-second opening
"This poster is a notebook of confusions treated as data. I came to QEC from ultrametric
geometry and the energy cost of computation, and I kept bumping into questions that only make
sense inside the frame they question. That is the point: where a question becomes nonsense is
exactly where a definition is doing the work. The frame under comparison is tree-based codes
versus surface codes — and Bruhat–Tits is just one instance of the tree class, not the concept."

## If asked "So you're saying the field is wrong?"
"No. I'm asking where the pieces were checked against each other. If the constructs were
compatible, the naive questions would answer themselves. They don't — and that's data, not a
verdict. Correct me, and the poster has done its job."

## If asked about question 1 — "What is a logical qubit, physically?"
"The term 'logical qubit' is defined as what the code protects. So the code defines the thing
it protects — the definition is the protection. My question is whether anything physical is
left over after the definition. The non-tautological residue is the price: joules per correct
answer, which is where the JPCUB benchmark comes in (10.5281/zenodo.21945415)."

## If asked about the numbers
"All classical simulation: bit-flip 50.0% vs ~10.9% surface (4.6×), depolarizing 75.0% vs
~1.0% (75×), independent X+Z 17.30% vs ~18.9% (0.92× — the tree loses there). The depolarizing
figure uses the code's structured-noise channel, which is not yet published — that is an open
caveat. Under independent errors the qudit generalization sits at ≈2×10⁻⁴, about 55× below
surface codes. No tree code has run on hardware. The claim is narrow: under correlated
failure, the tree geometry may need fewer active interventions — and the matched-noise
comparison decides it."

## If asked "Why the 'outside the frame' phrasing on every question?"
"It's the probe. Question 2 — why does a surface code need a surface? — is nonsense outside
the frame, because outside the frame a code is just a set of states. Inside the frame, the
logical operators are defined by the boundary, so the surface defines the code that defines
the surface. The geometry is the definition. Each question is built the same way: it only
parses inside the frame, and inside the frame the answer is a definition — which is exactly
what I want to test."

## If asked "What would actually change your mind?"
"Four things, all on the poster with their criteria: a matched-noise comparison under the same
correlated-noise model — if the advantage falls to parity, the comparison is answered and the
advantage claim is withdrawn; a decoder reality check — does a known decoder family already
cover tree-structured codes; an independent re-run — the simulator and protocol are handed
over to anyone who wants them; and perfect tensors for p > 2, since the binary [[3,1,1]] case
is settled."

## If asked "Is this LDPC?"
"The tree code is a holographic perfect-tensor construction, not an LDPC family — but the
decoder question is the same one the QLDPC community attacks. Ask 2 on the poster is exactly
that: is there a known decoder family covering tree-structured codes, and how does its
complexity scale?"

## The four asks (same on the poster)
1. A correlated-noise benchmark (model + data) to run the matched comparison against.
2. A decoder pointer for tree-structured codes.
3. An independent re-run of the simulation.
4. Perfect-tensor results for p > 2.

## Closing line
"If the matched comparison survives, the instrument path exists as a published trapped-ion
protocol with numeric predictions (10.5281/zenodo.22025544). Can I send you the simulator and
the protocol?"

## Frame directive (user, 2026-08-24)
The poster is NOT Bruhat–Tits-hitched. The broad class is nested, distinction-based ultrametric
trees; Bruhat–Tits T₂ is one instance among many, mentioned as a class member only. Surface
codes are the comparison baseline. Title is the "Things I Don't Understand" naive-audit framing
with sharp pointed questions — never assert a better answer; the question is the probe.
