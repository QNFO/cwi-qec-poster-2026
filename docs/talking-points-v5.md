# Talking Points — v5 Tree-Code Roadmap Poster (CWI, Wed 26 Aug 2026)

Companion to `poster-v5-treecode/poster.html` + `docs/tree-code-roadmap.md`. Plain prose;
every number traces to a DOI listed in the roadmap.

## The 30-second opening
"This poster is a testing plan, not a results claim. I work on a tree-based quantum code whose
thresholds come out of classical simulation — bit-flip 50%, depolarizing 75% — and the claim is deliberately narrow: three independent methods agree, nothing has touched hardware yet. The poster
lists the five tests that would change my mind; the first two are pure classical work and start
immediately."

## If asked "75% sounds impossible"
The number is for the depolarizing channel under the code's specific noise structure, from exact
stabilizer simulation and Monte Carlo. Under independent errors the related qudit family sits at
about 2×10⁻⁴ — roughly 55× below surface codes — and that boundary is in the record. The architectural claim targets correlated-failure regimes, which is exactly what
test T1 exists to scrutinize: matched noise, same model, tree versus surface.

## If asked "Why trust the simulation?"
Three independent methods agree; the verification script (35 checks) is deposited with the guide
record (10.5281/zenodo.22038733); and T5 is the reproducibility test — I hand over the simulator
and the protocol. A third-party rerun settles the classical claim. Also: my proposed p-adic reading of stabilizer codes turned out to carry no new content (10.5281/zenodo.21979060).

## If asked "Perfect tensors for p>2?"
The binary [[3,1,1]] case is settled; larger primes are open. This is room ask #3 — pointers welcome.

## If asked "Is this LDPC?"
The tree code is a holographic perfect-tensor construction, not an LDPC family — but the decoder
question is the same one the QLDPC community attacks. Ask #2 is exactly that: is there a known
decoder family covering tree-structured codes, and how does its complexity scale?

## The four asks (same on the poster)
1. Correlated-noise benchmark (model + data) for T1.
2. Decoder reality check for tree-structured codes.
3. Perfect-tensor results for p > 2.
4. Independent re-run of T1.

## Closing line
"If the matched-noise comparison survives, the next step is ion-trap instrumentation — there is a
published protocol with numeric predictions (10.5281/zenodo.22025544). Can I send you the protocol
and the simulator?"

## The tree code vs the surface code — in 30 seconds
"Surface codes lay data qubits on a 2D lattice, measure syndromes, and let a classical decoder
decide what to correct — a loop that costs hardware and energy. The tree code is a different
geometry: a [[3,1,1]] perfect tensor at every internal vertex of a 3-regular tree (each vertex:
one parent, two children), so correction
is built into the structure instead of applied from outside. Simulated thresholds: 50.0% bit-flip
(4.6×), 75.0% depolarizing (75×), 17.30% X+Z — all classical, i.i.d., with the surface
comparators at ~10.9% code-capacity and ~1.0% circuit-level. What's honest: no hardware yet;
under independent errors the qudit family sits at ≈2×10⁻⁴, ~55× below surface — the claim lives
in correlated-failure regimes, and T1 is the test that decides."

## What is [[3,1,1]]?
"[[n,k,d]] is standard code notation: n physical qubits encoding k logical qubits with distance d.
[[3,1,1]] means 3 physical qubits, 1 logical qubit, distance 1 — the minimal perfect tensor, a
one-to-two-qubit isometry. Distance 1 means a single block does not correct errors by itself;
the protection emerges from concatenating the blocks across the tree."

## If asked "No measurement loop — so how is an error actually corrected?"
"The honest answer: the mechanism is the perfect-tensor structure — each [[3,1,1]] block is an
isometry from one qubit to two, and the tree concatenation makes the whole encoding holographic,
so a local error in one leg is mapped onto the redundant structure rather than amplified. That is
the claim; it has been verified in classical simulation — three methods, a deposited 35-check
script — not on hardware. Tests T1–T5 are exactly what would confirm or kill it, especially T1's
matched-noise comparison and T2's decoder accounting. If you have a sharper way to state the
mechanism, I'd like to hear it — that is ask #2 on the poster."

## Follow-up logistics
- The poster carries the DOIs and the test table; the repo has the full plan.
- Repo: github.com/QNFO/cwi-qec-poster-2026 — full plan in docs/tree-code-roadmap.md.
- After the event: log each conversation; prioritize Delfosse (IonQ, correlated-noise data) and
  Leverrier (Inria, decoder families); feed answers into the follow-up wave.
