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
geometry: a [[3,1,1]] perfect tensor at every internal vertex of a 3-regular tree (each internal
vertex: up to one parent, two children; the root has three children and nothing above it), so correction
is built into the structure instead of applied from outside. Simulated thresholds: 50.0% bit-flip
(4.6×), 75.0% depolarizing (75×), 17.30% X+Z — all classical simulation; bit-flip and X+Z are
under i.i.d. noise, the 75% comes from the code's structured-noise model, and the surface
comparators are ~10.9% code-capacity and ~1.0% circuit-level. No hardware yet; under independent errors the qudit generalization sits at ≈2×10⁻⁴, ~55× below surface — the qubit claim lives
in correlated-failure regimes, and T1 is the test that decides."

## What is [[3,1,1]]?
"[[n,k,d]] is standard code notation: n physical qubits encoding k logical qubits with distance d.
[[3,1,1]] means 3 physical qubits, 1 logical qubit, distance 1 — the minimal perfect tensor, a
one-to-two-qubit isometry. Distance 1 means a single block does not correct errors by itself;
the protection emerges from concatenating the blocks across the tree."

## If asked "No measurement loop — so how is an error actually corrected?"
"The mechanism is the perfect-tensor structure — each [[3,1,1]] block is an
isometry from one qubit to two, and the tree concatenation makes the whole encoding holographic,
so a local error in one leg is mapped onto the redundant structure rather than amplified. That is
the claim; it has been verified in classical simulation — three methods, a deposited 35-check
script — not on hardware. Tests T1–T5 are exactly what would confirm or kill it, especially T1's
matched-noise comparison and T2's decoder accounting. If you have a sharper way to state the
mechanism, I'd like to hear it — that is ask #2 on the poster."

## If asked "Why do you mention both qubits and qudits?"
"The tree code is a qubit code — the [[3,1,1]] tensor has two-level legs, and every threshold in
the table is a qubit number. The qudit mention is the published boundary: the higher-dimensional
generalization of the same family was analyzed under independent errors and sits at ≈2×10⁻⁴,
~55× below surface. I show it because it is the scope line — the advantage claim lives in
correlated-failure regimes, not independent ones, and that's exactly what T1 tests."

## If asked "Are the error models reasonable? Is 75% a real threshold?"
"Bit-flip 50% is exact: the unstable fixed point of the majority recursion 3p² − 2p³ — the tree
corrects X-errors up to exactly half, and I can show that arithmetic on the spot. X+Z 17.3% is the
straight comparison: under independent X+Z the tree sits slightly below the toric code's ~18.9% — the poster
says 0.92× rather than hiding it. The depolarizing 75% is the one I would challenge myself: it
comes from the code's own structured-noise simulation, the channel is not yet pinned down
(roadmap D3), and T1's matched-noise comparison is exactly what would collapse it to parity. I
would rather show the caveat than defend a number I cannot."

## If asked "What is the decoder / recovery map?"
"Bit-flip: majority vote on each [[3,1,1]] block — that is why the 50% figure is exact arithmetic rather
than a fitted number. For the full channels there is no published decoder yet: that is T2 and ask #2 on the
poster, and it is the question I most want this room's answer to. If you know a decoder family that covers
tree-structured codes, I would like the reference."

## If asked "What are the full code's parameters — n, k, d, rate, scaling?"
"The block is [[3,1,1]]: three physical qubits, one logical qubit, distance one. The full code is the
concatenation of these blocks across the truncated tree; the guide record carries physical-qubit counts at
distance-11-equivalent protection, and the complete parameterization — rate and distance as a function of
depth — is exactly what tracks D1 and D3 formalize. I will not quote a scaling law I have not verified."

## If asked "Where does the p-adic / Bruhat–Tits structure actually enter? Isn't this just a 3-regular tree?"
"The tree T₂ is the geometry of the 2-adic numbers: a vertex's three branches are the divisibility-by-2
hierarchy, and the distance between leaves is the p-adic valuation of their difference — the branching is
p+1 = 3 for exactly this reason. The correction structure follows the ultrametric distance, which is where
'built into the geometry' comes from. If the p-adic reading turns out to be relabeling, that is the kind of
thing I have published before — the prime-valuation correction is on the poster."

## If asked "How does this differ from HaPPY and other holographic tensor-network codes?"
"Same building block — perfect tensors on a tree; HaPPY/PYHP use them for bulk-boundary duality with an
erasure threshold around 50%. The difference is the claim: this work claims a threshold advantage under
correlated noise, with the caveats on the poster, and the erasure analogy is exactly why the 75% figure
deserves the scrutiny T1 gives it."

## If asked "What is the QEC–Darwinism audit you cite?"
"Maity et al. proved QEC and Quantum Darwinism cannot coexist above logical fidelity F_L ≈ 0.874. I ran the
collective fragment refinement on tree-code spaces: the boundary moves to F_L ≈ 0.83–0.85, with a residual
gap that does not close — an external no-go applied to my own geometry, and the residual is stated rather
than smoothed over."

## Follow-up logistics
- The poster carries the DOIs and the test table; the repo has the full plan.
- Repo: github.com/QNFO/cwi-qec-poster-2026 — full plan in docs/tree-code-roadmap.md.
- After the event: log each conversation; prioritize Delfosse (IonQ, correlated-noise data) and
  Leverrier (Inria, decoder families); feed answers into the follow-up wave.
