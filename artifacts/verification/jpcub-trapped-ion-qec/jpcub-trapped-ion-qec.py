#!/usr/bin/env python3
"""
JPCUB — energy per correct answer for trapped-ion QEC code families
v2 (2026-08-24) — remediation of red-team findings A1/C1-C5/D1-D5.

Question: given noisy qubits in a trapped-ion quantum computer, which QEC
code minimizes ENERGY PER CORRECT ANSWER (not gate count, not qubit count)?

SCOPE DECLARATION (red-team C1 fix):
  This model answers the question for a CLIFFORD-ONLY, MEMORY-STYLE workload:
  syndrome cycles that protect an encoded memory. It does NOT price:
    - magic-state distillation / T factories (both qLDPC and surface need T
      for universality; qLDPC's non-transversal T overhead is a known relative
      weakness -> the winner ranking is workload-dependent; see Notes),
    - logical gate synthesis (lattice surgery, transversal gates),
    - wall-clock scheduling / decoder latency as a time cost (energy only),
    - ion transport/shuttling (single-register trap assumed), crosstalk,
      leakage, state-preparation error, sympathetic cooling for dual-species.
  GKP is excluded by hardware choice: continuous-variable codes need bosonic
  hardware; the trapped-ion register is discrete qubits.

Model: order-of-magnitude, calibrated to published 2024-2026 results.
Energy normalized to one MS (2-qubit) gate = 1.0 (~0.5 uJ absolute).
JPCUB = joules-per-correct-answer metric (10.5281/zenodo.21945415).

References (see references.bib in this folder):
  - Bravyi et al. 2024 (Nature 627:778) gross code [[144,12,12]], arXiv:2308.07915
  - Bonilla Ataides et al. 2021 (Nat. Commun. 12:2172) XZZX surface code, arXiv:2011.14546
  - Kang et al. 2023 (Nature 618:264) erasure conversion, arXiv:2212.09114
  - Bruzewicz et al. 2019 (Appl. Phys. Rev. 6:021314) trapped-ion review
  - Fowler et al. 2012 (PRA 86:032324) surface-code threshold ~1%, arXiv:1208.0928
  - Sorensen & Molmer 1999 (PRL 82:1971) MS gate
  - QNFO: 10.5281/zenodo.21046993 (qudit QEC), 10.5281/zenodo.20109836 (architecture)
License: CC BY 4.0 — QNFO (Rowan Brad Quni-Gudzinas).
"""

import math

# ─────────────────────────── trapped-ion layer (model) ───────────────────────────
E2  = 1.0      # MS gate energy (normalized; ~0.5 uJ absolute)
E1  = 0.10     # single-qubit gate
EM  = 0.50     # measurement + reset (scattered photons + cooling light)
ED0 = 0.02     # decoder energy per round at check weight 4 (MWPM baseline)
EC  = 0.50     # Doppler-cooling block per round
TID = 1.0e-7   # idle dephasing error per us per ion (T2* ~1 s with DD)

T_MS, T_1Q, T_M, T_COOL = 100.0, 10.0, 200.0, 500.0   # us per operation

p1  = 1.0e-4   # single-qubit gate error
pM  = 1.0e-3   # measurement error
BIAS = 10.0    # dephasing:X error ratio (trapped ions are Z-biased)

def p_logical(p2, p_th, d, C=0.1):
    """Standard ansatz p_L ~ C (p/p_th)^((d+1)/2); C=0.1 typical."""
    return C * (p2 / p_th) ** ((d + 1) / 2.0)

def decoder_energy(check_weight):
    """C5/D5 fix: decoder cost scaled by check weight (BP+OSD for weight-6
    qLDPC is costlier than weight-4 MWPM surface matching)."""
    return ED0 * (check_weight / 4.0)

def energy_per_logical_gate(ms, meas, oneq, rounds, n_phys, check_weight=4,
                            gate_speed=1.0):
    """Energy per logical gate (normalized). gate_speed scales MS/1q energies:
    E2(p2) = E2_ref * gate_speed (see scan). Idle priced from wall-clock
    (C1 fix: idle_us was dead code in v1; now wired through)."""
    ED = decoder_energy(check_weight)
    E_gate = (ms * E2 + oneq * E1) * gate_speed + meas * EM + rounds * (EC + ED)
    wallclock_us = (ms * T_MS + oneq * T_1Q + meas * T_M + rounds * T_COOL)
    idle = n_phys * wallclock_us * TID * E2 * gate_speed
    return E_gate + idle

def energy_per_correct(L, E_gate, p_L):
    P = 1.0 - min(L * p_L, 0.99)
    return L * E_gate / P, P

# ─────────────────────────── code families ───────────────────────────
def surface(d):
    """Rotated surface code: n=2d^2-1, d rounds, 4 CNOTs per ancilla per round."""
    n = 2 * d * d - 1
    ms   = 4 * d * d * d
    meas = d * d * d
    oneq = 2 * ms
    return dict(name=f"surface d={d}", n=n, ms=ms, meas=meas, oneq=oneq,
                rounds=d, p_th=0.010, d=d, w=4, note="baseline; ~1% threshold")

def qldpc_gross():
    """[[144,12,12]] gross code (Bravyi 2024): 24 weight-6 checks, 12 logical."""
    d = 12
    ms_block    = 24 * 6 * d
    meas_block  = 24 * d
    oneq_block  = 2 * ms_block
    return dict(name="qLDPC [[144,12,12]]", n=144 / 12, ms=ms_block / 12,
                meas=meas_block / 12, oneq=oneq_block / 12, rounds=d,
                p_th=0.006, d=d, w=6, note="gross code; 12 logical in one block")

def qldpc_erasure(eras=1.5):
    """qLDPC + erasure conversion: erasures cost half distance -> effective
    exponent grows ~eras x at same distance (model, uncalibrated)."""
    base = qldpc_gross()
    d_eff = int(eras * base["d"])
    return dict(name=f"qLDPC + erasure (x{eras:.1f})", n=base["n"], ms=base["ms"],
                meas=base["meas"], oneq=base["oneq"], rounds=base["rounds"],
                p_th=base["p_th"], d=d_eff, w=6,
                note=f"dual-species; effective d {base['d']}->{d_eff} (model)")

def xzzx(d, bias=BIAS):
    """XZZX surface under bias: threshold ~ 0.010*(1+bias)/2 (heuristic,
    uncalibrated vs Bonilla Ataides 2021; flagged)."""
    n = 2 * d * d - 1
    ms   = 4 * d * d * d
    meas = d * d * d
    oneq = 2 * ms
    return dict(name=f"XZZX d={d} (bias {bias:.0f})", n=n, ms=ms, meas=meas,
                oneq=oneq, rounds=d, p_th=0.010 * (1 + bias) / 2.0, d=d, w=4,
                note="bias-tailored; threshold improves with bias (heuristic)")

def repetition(d, bias=BIAS):
    """Phase-flip repetition [[d,1,d]] for Z-bias (C3 addition). Corrects Z
    errors at ~50% threshold; X errors are WEIGHT-1 logical errors, NOT
    correctable: p_L_X = p2/(1+bias). Viable only at extreme bias (>=~1e3
    for p2=1e-3, budget 1e-6)."""
    n = d
    ms   = d * d          # d CNOTs per round x d rounds
    meas = d
    oneq = 2 * ms
    p_z = p2_z = None
    def pl(p2):
        pz = p2 * bias / (1 + bias)
        px = p2 / (1 + bias)
        return 0.1 * (pz / 0.5) ** ((d + 1) / 2.0) + px   # weight-1 X term
    return dict(name=f"repetition d={d} (bias {bias:.0f})", n=n, ms=ms, meas=meas,
                oneq=oneq, rounds=d, p_th=0.5, d=d, w=2, custom_pl=pl,
                note="phase-flip; X errors weight-1 -> extreme-bias limit only")

def bacon_shor(d):
    """Bacon-Shor subsystem code (C3 addition, rough params): n=d^2, weight-2
    checks, transversal-friendly. ms=2d^3 heuristic."""
    n = d * d
    ms   = 2 * d * d * d
    meas = d * d
    oneq = 2 * ms
    return dict(name=f"Bacon-Shor d={d}", n=n, ms=ms, meas=meas, oneq=oneq,
                rounds=d, p_th=0.010, d=d, w=2, note="rough params; simple decoding")

def steane_concat(k):
    """Concatenated Steane [[7,1,3]]^k (C3 addition, rough): n=7^k,
    p_L = (0.1*(p2/p_th)^2)^k level-wise."""
    n = 7 ** k
    ms   = 6 * n
    meas = 2 * n
    oneq = 2 * ms
    def pl(p2):
        return (0.1 * (p2 / 0.02) ** 2) ** k
    return dict(name=f"Steane [[7,1,3]]^k k={k}", n=n, ms=ms, meas=meas, oneq=oneq,
                rounds=k, p_th=0.02, d=3 * k, w=4, custom_pl=pl,
                note="rough; level-wise concatenation")

def tree_qudit():
    """QNFO tree/ultrametric class under INDEPENDENT errors: qudit threshold
    ~2e-4 (55x below surface ~1.1e-2) per the verified poster numbers.
    Not viable for independent noise; its regime is correlated failure."""
    return dict(name="tree/ultrametric (qudit)", n=3.0, ms=9.0, meas=3.0,
                oneq=9.0, rounds=3, p_th=2.0e-4, d=3, w=3,
                note="independent-noise threshold 2e-4: EXCLUDED below; "
                     "correlated regime only (see Notes)")

def family_pL(fam, p2):
    return fam["custom_pl"](p2) if "custom_pl" in fam else p_logical(p2, fam["p_th"], fam["d"])

# ─────────────────────────────── workload ───────────────────────────────
L = 10_000            # logical gates per computation
TARGET = 1.0e-6       # p_L per logical gate -> 1% end-to-end failure

families = [
    surface(7), surface(11), surface(15),
    qldpc_gross(), qldpc_erasure(1.5),
    xzzx(5), xzzx(7),
    repetition(9), bacon_shor(9), steane_concat(3),
    tree_qudit(),
]

print("=" * 108)
print("JPCUB v2: energy per correct answer — trapped-ion QEC families")
print(f"workload L={L} logical gates; target p_L <= {TARGET:.0e} "
      f"(<= {100*L*TARGET:.0f}% end-to-end); units: 1 MS gate = 1.0")
print("SCOPE: Clifford-only, memory-style (syndrome cycles). No T-factory, no")
print("      shuttling, no wall-clock scheduling. GKP excluded (CV hardware).")
print("      E2(p2) UNCAPPED (A1 fix): E ~ 1/p2 scattering-limited.")
print("=" * 108)

print(f"{'family':<32}{'n/log':>7}{'MS/log':>8}{'E/log':>9}  "
      f"{'p_L@1e-3':>10} {'viable':>7}  {'E_correct@1e-3':>14} "
      f"{'E_correct@1e-4':>14}")
print("-" * 108)

rows = []
for fam in families:
    pL = family_pL(fam, 1e-3)
    E_gate = energy_per_logical_gate(fam["ms"], fam["meas"], fam["oneq"],
                                     fam["rounds"], fam["n"], fam.get("w", 4))
    ok = pL <= TARGET
    Ec1e3 = energy_per_correct(L, E_gate, pL)[0] if ok else float("nan")
    pL2 = family_pL(fam, 1e-4)
    E_gate2 = energy_per_logical_gate(fam["ms"], fam["meas"], fam["oneq"],
                                      fam["rounds"], fam["n"], fam.get("w", 4))
    ok2 = pL2 <= TARGET
    Ec1e4 = energy_per_correct(L, E_gate2, pL2)[0] if ok2 else float("nan")
    rows.append((fam["name"], fam["n"], fam["ms"], E_gate, pL, ok, Ec1e3, ok2))
    print(f"{fam['name']:<32}{fam['n']:>7.0f}{fam['ms']:>8.0f}{E_gate:>9.0f}  "
          f"{pL:>10.2e} {str(ok):>7}  {Ec1e3:>14.3e} {Ec1e4:>14.3e}")

print("-" * 108)
print("\n-- Operating-point scan (A1 fix: UNCAPPED E2 ~ 1/p2).")
print("   E2(p2) = E2_ref*(1e-3/p2), floored at p2=1e-4 (E2 <= 10x). v1's")
print("   cap s=min(1,1e-3/p2) made sub-1e-3 operation artificially cheap;")
print("   the v1 'XZZX d=3 second place' (1.461e6) was a cap artifact and is")
print("   corrected below. The energy-optimal point is the LARGEST p2 meeting")
print("   the budget (run as fast as the error budget allows).\n")

P2_FLOOR = 1.0e-4

def op_scan(fam):
    lo, hi = P2_FLOOR, 3e-3
    if family_pL(fam, lo) > TARGET:
        return None
    for _ in range(60):
        mid = math.sqrt(lo * hi)
        if family_pL(fam, mid) <= TARGET:
            lo = mid
        else:
            hi = mid
    p2 = lo
    s = 1e-3 / max(p2, P2_FLOOR)              # uncapped
    E_gate = energy_per_logical_gate(fam["ms"], fam["meas"], fam["oneq"],
                                     fam["rounds"], fam["n"], fam.get("w", 4), s)
    return (energy_per_correct(L, E_gate, family_pL(fam, p2))[0], p2, E_gate, s)

scan_families = [surface(d) for d in (3, 5, 7)] + \
                [xzzx(d) for d in (3, 5, 7)] + \
                [qldpc_gross(), qldpc_erasure(1.5)]
results = []
for fam in scan_families:
    r = op_scan(fam)
    if r:
        results.append((r[0], fam["name"], r[1], r[2], r[3]))
results.sort()
for Ec, name, p2, Eg, s in results:
    print(f"  {name:<30} E_correct={Ec:.3e} at p2={p2:.2e}  E/log={Eg:.0f} "
          f"gate_speed={s:.2f}")
print(f"  -> WINNER: {results[0][1]} ({results[0][0]:.3e})")

print("\n-- Sensitivity sweep (C2 fix). One axis at a time; winner shown.")
def winner_for(bias, eras, th_scale, LL, budget):
    fams = [surface(d) for d in (5, 7, 11)] + \
           [qldpc_gross(), qldpc_erasure(eras)] + \
           [xzzx(d, bias) for d in (3, 5, 7)]
    best = None
    for fam in fams:
        fam2 = dict(fam)
        fam2["p_th"] = fam2["p_th"] * th_scale
        lo, hi = P2_FLOOR, 3e-3
        if family_pL(fam2, lo) > budget:
            continue
        for _ in range(60):
            mid = math.sqrt(lo * hi)
            if family_pL(fam2, mid) <= budget:
                lo = mid
            else:
                hi = mid
        p2 = lo
        s = 1e-3 / max(p2, P2_FLOOR)
        E_gate = energy_per_logical_gate(fam2["ms"], fam2["meas"], fam2["oneq"],
                                         fam2["rounds"], fam2["n"], fam2.get("w", 4), s)
        Ec = energy_per_correct(LL, E_gate, family_pL(fam2, p2))[0]
        if best is None or Ec < best[0]:
            best = (Ec, fam2["name"])
    return best

base = dict(bias=BIAS, eras=1.5, th=1.0, L=L, budget=TARGET)
for label, mutate in [
    ("bias=1    ", dict(bias=1.0)),
    ("bias=10   ", dict(bias=10.0)),
    ("bias=100  ", dict(bias=100.0)),
    ("eras x1.0 ", dict(eras=1.0)),
    ("eras x1.5 ", dict(eras=1.5)),
    ("eras x2.0 ", dict(eras=2.0)),
    ("th x0.5   ", dict(th=0.5)),
    ("th x1.5   ", dict(th=1.5)),
    ("L=1e3     ", dict(L=1_000)),
    ("L=1e6     ", dict(L=1_000_000)),
    ("budget 1e-8", dict(budget=1e-8)),
]:
    kw = dict(base); kw.update(mutate)
    w = winner_for(kw["bias"], kw["eras"], kw["th"], kw["L"], kw["budget"])
    print(f"  {label}: winner={w[1]:<24} E_correct={w[0]:.3e}")

print("\n-- Absolute scale (E2 ~ 0.5 uJ/MS gate):")
for fam in [surface(11), qldpc_gross(), qldpc_erasure(1.5)]:
    E_gate = energy_per_logical_gate(fam["ms"], fam["meas"], fam["oneq"],
                                     fam["rounds"], fam["n"], fam.get("w", 4))
    pL = family_pL(fam, 1e-3)
    if pL <= TARGET:
        Ec, _ = energy_per_correct(L, E_gate, pL)
        print(f"  {fam['name']:<24} ~{Ec*0.5e-6:>10.3f} J per {L} correct "
              f"logical gates (at p2=1e-3)")

print("\n-- Tight budget (L=1e6, target p_L=1e-8):")
for fam in [surface(15), qldpc_gross(), qldpc_erasure(1.5), bacon_shor(11)]:
    pL = family_pL(fam, 1e-3)
    ok = pL <= 1e-8
    print(f"  {fam['name']:<24} p_L@1e-3={pL:.2e} viable@{'yes' if ok else 'no'}")

print("\n-- Notes (C3 fix):")
print("  * Foliated/treelike distillation: the ultrametric class's practical")
print("    QEC appearance is in T-factory treelike/foliated distillation codes")
print("    (Bravyi-Haah family) — a T-density axis would bring the tree class")
print("    back into the comparison via the distillation layer, not the memory.")
print("  * Repetition code: weight-1 uncorrectable X error (p_X = p2/(1+bias))")
print("    makes it viable only at extreme bias (>=~1e3 at p2=1e-3) — the known")
print("    biased-noise limit; XZZX exists precisely to keep bias advantage")
print("    without the repetition's X weakness.")
print("  * T-factory caveat (C1): both qLDPC and surface need magic states for")
print("    universality; qLDPC non-transversal T overhead is a relative")
print("    weakness. Ranking is workload-dependent — this artifact is the")
print("    Clifford/memory slice.")
print("  * Uncalibrated model choices (flagged): XZZX threshold mapping")
print("    0.010*(1+bias)/2; erasure d_eff=1.5x; Bacon-Shor/Steane rough;")
print("    p_L ansatz C=0.1. Sensitivity block shows ranking robustness.")
