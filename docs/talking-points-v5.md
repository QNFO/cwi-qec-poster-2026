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

## Follow-up logistics
- The poster carries the DOIs and the test table; the repo has the full plan.
- Repo: github.com/QNFO/cwi-qec-poster-2026 — full plan in docs/tree-code-roadmap.md.
- After the event: log each conversation; prioritize Delfosse (IonQ, correlated-noise data) and
  Leverrier (Inria, decoder families); feed answers into the follow-up wave.
