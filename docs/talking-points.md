# CWI Summer School — Poster Conversation Strategy

**Event:** CWI Summer School on QA & QEC · 24–28 Aug 2026 · Amsterdam
**Poster session:** Wed 26 Aug, 16:30–18:00 · WCW Turingzaal, Science Park 125
**Room:** QEC researchers — academic + industry (IonQ's Nicolas Delfosse, Inria's Anthony Leverrier, surface-code people)
**Framing:** Independent researcher, honest open questions. NOT selling a theory. Here to learn and to ask sharp questions the field doesn't discuss enough.

---

## 1. The One-Minute Pitch (memorize this shape)

> "I'm an independent researcher working on the geometry of noise. I have five open questions about fault-tolerant QEC — the energy cost of active correction, the classical decoding bottleneck, whether noise's hierarchical structure could be exploited passively, why the circuit model is assumed, and the one I care most about: **what would actually falsify the roadmap?** I built a small toy model trying to answer the noise-geometry question, and I'd love your take on whether it's pointing anywhere real."

Then stop and let them react. Do NOT dump more. The questions do the work.

---

## 2. What the Room Knows That You Should Speak Fluently

These are the reference points every QEC person has — name them correctly and you're instantly "one of us":

| Term | What it is | Say it right |
|:-----|:-----------|:-------------|
| **Surface code** | The leading topological QEC candidate (Kitaev toric code family) | "Surface codes are the current leading candidate for practical FTQC." |
| **Threshold** | Physical error rate below which adding more qubits helps (~1% for surface code) | "The surface-code threshold is around one percent physical error rate." |
| **Logical qubit overhead** | ~1000+ physical qubits per logical qubit | "Current estimates are roughly a thousand-plus physical qubits per logical qubit." |
| **Magic states / T factories** | Non-Clifford states made via distillation — the expensive part | "The magic-state distillation factories dominate the resource budget." |
| **NISQ** | Noisy intermediate-scale quantum — current era | "NISQ is the era we're in; fault tolerance is the end goal." |
| **Decoding** | Classical algorithm processing syndromes | "Real-time decoding is a classical bottleneck." |
| **Syndrome extraction** | Measuring stabilizers to detect errors | "Each syndrome-extraction round erases information — that's where Landauer enters." |

**If you can name-drop these correctly, you cannot be dismissed as uninformed.** Each of the five poster questions maps to a real, discussed issue — not a crank concern:

- **Q1 Energy Wall** ↔ real literature on Landauer cost of error correction / refrigeration budgets
- **Q2 Classical Shadow** ↔ real literature on real-time decoding latency (Union-Find decoders, FPGA decoding)
- **Q3 Geometry of Noise** ↔ real literature on spatially correlated noise, non-Markovian dephasing, 1/f noise
- **Q4 Why a Circuit** ↔ real debate on measurement-based / analog / holonomic alternatives
- **Q5 Falsification** ↔ real methodological point (Lakatos, research programmes) — the strongest question, and the least discussed

---

## 3. The Five Questions — How to Explain Each in 30 Seconds

### ① The Energy Wall
> "Landauer says erasing one bit costs at least kT·ln2. Every syndrome-extraction round erases information. So the total thermodynamic cost of a large fault-tolerant computation grows with the number of rounds and qubits. **I've looked for an accepted scaling law for this and I can't find one published.** Does anyone know where it is?"

- Why it's safe: it's a genuine literature question; either they know the answer (you learn) or they don't (you've asked something real).
- Don't claim the wall is fatal — claim it's under-explored.

### ② The Classical Shadow
> "The decoder has to turn syndromes into corrective actions faster than the qubits decohere. As systems scale, that's a real-time classical processing task with its own energy and latency. **At what scale does the classical co-processor's dissipation become a significant part of the error budget?**"

- Real hooks: Union-Find decoding, FPGA-based decoders, the decoder's power draw.

### ③ The Geometry of Noise
> "Real noise isn't independent — it's correlated, often hierarchically. In many systems, correlations look like nested clusters — an ultrametric structure. **If noise already organizes itself that way, are we leaving passive resilience on the table by assuming independent noise models?**"

- This is your home turf — the p-adic/ultrametric idea lives here. Frame it as a *question about noise models*, not a claim that QEC is wrong.
- If they push: "I'm not saying error correction is wrong. I'm asking whether the noise-model assumptions leave geometry unused."

### ④ Why a Circuit?
> "The circuit model turns continuous physics into discrete gates, then error correction defends that digital abstraction. In other areas of physics, when you need intense external control to keep a system in your model, that's often a sign to reconsider the model. **Is there a deep reason the circuit model is forced, or is it a historical choice?**"

- Safe framing: you're asking a conceptual question, not proposing a replacement.

### ⑤ What Falsifies the Roadmap? (YOUR BEST QUESTION)
> "The timeline has been 'roughly ten years' since the mid-1990s. I'm not saying it's wrong. But **what empirical result would demonstrate the roadmap needs a fundamental revision, rather than more time and money?** If there's no falsification condition, how do we tell a research programme from a belief?"

- This is the question that makes you memorable. It's respectful, rigorous, and almost nobody asks it.
- Expect responses like "the theory is sound, it's engineering" — that's fine; you've surfaced a real methodological point.

---

## 4. The Toy Model — The Honest Story (30–60 seconds)

> "To test the noise-geometry question, I built a small model of a code living on a tree-like structure. It suggested redundancy might grow in discrete steps rather than smoothly — which surprised me. But when I tested the most interesting feature — a gap where redundancy vanishes — **it didn't survive. It looks like an artifact of my model.** I wrote it up honestly rather than hiding it. **Have you seen anything like that, or a reason it must be wrong?**

- The null result is your credibility shield. Saying "my own result failed my own test" is the single most trust-building sentence you can say to researchers.
- If someone wants details: "I have a working paper if you'd like it — I'd genuinely value a critique." Point to the DOI: 10.5281/zenodo.21819232. Do NOT recite the simulation mechanics unprompted.
- If pressed on ultrametric geometry: "It's the idea that distances in some noise structures obey the strong triangle inequality — things either cluster tightly or are far apart, nothing in between. Think of it as noise that organizes into a hierarchy."

---

## 5. Likely Questions & Grounded Answers

| They ask | Your answer (short, honest) |
|:---------|:----------------------------|
| "What's your background?" | "Independent researcher — I work on ultrametric/p-adic approaches to noise and measurement. I'm here to learn and to pressure-test some questions." |
| "Is the energy wall a real problem?" | "I don't know — that's exactly what I'm asking. The literature has bounds for single operations; I haven't found a total-system scaling law." |
| "Are you saying QEC is wrong?" | "No. I'm asking whether the noise models leave geometry unused, and what would falsify the roadmap. The theorem work is sound." |
| "What's a p-adic number?" | "A different way of measuring closeness where things are either very close or very far — no middle ground. It matches hierarchical clustering naturally." |
| "Did your model work?" | "It produced an interesting suggestion, then failed my own test. That's why I'm asking the room — I want to know if it's a known artifact or something real." |
| "Have you talked to [X] about this?" | "Not yet — that's part of why I'm here." (then name your targets: Delfosse, Leverrier) |

---

## 6. Conversation Targets & Follow-Up Plan

| Person | Why | Ask |
|:-------|:----|:----|
| **Nicolas Delfosse (IonQ)** | Industry QEC; decoder/code-design side | Energy cost of decoding at scale; whether industry tracks the total-system thermodynamic budget |
| **Anthony Leverrier (Inria)** | Theory; code performance bounds | The falsification question — what result would change his view of the roadmap |
| Any surface-code person | Closest to the practical roadmap | Noise-correlation assumptions in their models; do they see ultrametric structure in correlated-error data? |

**Follow-up:** exchange emails/ORCID, mention the paper DOI, ask permission to follow up by email. Target: ≥1 genuine conversation > 5 minutes, ≥1 contact for follow-up (per the poster success criteria).

---

## 7. What NOT to Do

- ❌ Don't recite the simulation (p-values, coupling constants, alpha-sweeps). It's weeds.
- ❌ Don't claim ultrametric QEC is viable or confirmed.
- ❌ Don't argue that the industry is wrong — argue that one question is under-examined.
- ❌ Don't mention internal project names, WBS codes, or the QNFO org structure — you're an independent researcher.
- ❌ Don't over-explain p-adic mathematics. One sentence, then pivot to the *question*.
- ✅ Do say "I don't know" freely — it's your framing's superpower.
- ✅ Do name-drop the field correctly (surface code, threshold, magic states, NISQ).
- ✅ Do end every conversation by asking *their* opinion — you came to learn.

---

## 8. Back Pocket — If the Whole Room Asks "So What's Your Point?"

> "My point is a question, not a claim: **the field has a falsification problem.** What would have to be observed to conclude the fault-tolerant roadmap needs a fundamental revision — not more time, but a different approach? I'm asking because I think the answer matters, and I suspect it's worth more attention than it gets. If the answer is 'nothing would falsify it', that itself is worth saying out loud."

---

*Working paper companion: Archimedean Shadows, v1.10 — DOI 10.5281/zenodo.21819232. Freeze in effect: no further versions. The paper is the deep reference; the poster is the conversation.*
