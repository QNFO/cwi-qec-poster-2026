#!/usr/bin/env python3
"""
JPCUB — energy per correct answer for trapped-ion QEC code families (2026-08-24)

Question: given noisy qubits in a trapped-ion quantum computer, which QEC code
minimizes ENERGY PER CORRECT ANSWER (not gate count, not qubit count)?

Method: model the trapped-ion physical layer (gate times/energies/errors),
the leading code families (surface, high-rate qLDPC/gross, XZZX under bias,
qLDPC+erasure conversion, tree/ultrametric from the QNFO poster), compute
per-logical-gate energy and logical error rate, then minimize
    E_correct = L * E_logical_gate / P_correct ,  P_correct = 1 - L * p_L
over the code choice AND the operating point (gate speed vs fidelity).

Model is explicitly order-of-magnitude, calibrated to published 2024-2026
results (Bravyi et al. 2024 [[144,12,12]] gross code; ion-trap gate/measure
figures; erasure conversion in dual-species traps). Units: energy normalized
to one MS (2-qubit) gate = 1.0.  JPCUB is the joules-per-correct-answer metric.
"""

import math

# ─────────────── trapped-ion layer (model, 2026 state of the art) ───────────────
# MS gate: 50-200 us, error ~1e-3 (best ~1e-4), energy ~0.1-1 uJ
# single-q: 5-20 us, error ~1e-4..1e-5 ;  measurement+reset: 100-300 us, ~1e-3
# T2* seconds with dynamic decoupling -> idle error small
E2  = 1.0      # MS gate energy (normalized; ~0.5 uJ absolute)
E1  = 0.10     # single-qubit gate
EM  = 0.50     # measurement + reset (scattered photons + cooling light)
ED  = 0.02     # classical decoder per syndrome round (electronics; tiny)
EC  = 0.50     # Doppler-cooling block per round (ions need cooling between rounds)
TID = 1.0e-7   # idle dephasing error per us per ion (T2* ~1 s with DD)

p1  = 1.0e-4   # single-qubit gate error
pM  = 1.0e-3   # measurement error
BIAS = 10.0    # dephasing:X error ratio (trapped ions are Z-biased)

def p_logical(p2, p_th, d, C=0.1):
    """Standard ansatz p_L ~ C (p/p_th)^((d+1)/2); C=0.1 typical."""
    return C * (p2 / p_th) ** ((d + 1) / 2.0)

def energy_per_logical_gate(ms, meas, oneq, rounds, n_phys, idle_us=0.0):
    """Energy per logical gate (normalized): MS dominates; cooling+decoder per round."""
    return (ms * E2 + meas * EM + oneq * E1
            + rounds * (EC + ED) + n_phys * idle_us * TID * E2)

def energy_per_correct(L, E_gate, p_L):
    P = 1.0 - min(L * p_L, 0.99)
    return L * E_gate / P, P

# ─────────────────────────────── code families ───────────────────────────────
# All costs are PER LOGICAL GATE (memory-style QEC cycle of d rounds).

def surface(d):
    """Rotated surface code: n=2d^2-1, d rounds/cycle, 4 CNOTs per ancilla per round."""
    n = 2 * d * d - 1
    ms   = 4 * d * d * d          # 4d^2 MS per round x d rounds
    meas = d * d * d              # d^2 ancilla measurements x d rounds
    oneq = 2 * ms
    return dict(name=f"surface d={d}", n=n, ms=ms, meas=meas, oneq=oneq,
                rounds=d, p_th=0.010, d=d, note="standard baseline")

def qldpc_gross():
    """[[144,12,12]] gross code (Bravyi et al. 2024): 24 weight-6 checks,
    12 logical qubits, all-to-all connectivity (trapped ions)."""
    d = 12
    ms_block    = 24 * 6 * d      # 24 checks x 6 CNOTs x d rounds
    meas_block  = 24 * d
    oneq_block  = 2 * ms_block
    return dict(name="qLDPC [[144,12,12]]", n=144 / 12, ms=ms_block / 12,
                meas=meas_block / 12, oneq=oneq_block / 12, rounds=d,
                p_th=0.006, d=d, note="gross code; 12 logical in one block")

def xzzx(d):
    """XZZX surface under bias BIAS: threshold scales ~ (1+BIAS)/2 (conservative)."""
    n = 2 * d * d - 1
    ms   = 4 * d * d * d
    meas = d * d * d
    oneq = 2 * ms
    return dict(name=f"XZZX d={d} (bias {BIAS:.0f})", n=n, ms=ms, meas=meas,
                oneq=oneq, rounds=d, p_th=0.010 * (1 + BIAS) / 2.0, d=d,
                note="bias-tailored; threshold improves with bias")

def qldpc_erasure():
    """qLDPC + erasure conversion (dual-species trap: one species flagged by
    detection, converted to erasure). Erasures cost half distance, so the
    effective exponent grows ~1.5x at the same distance (model)."""
    base = qldpc_gross()
    d_eff = int(1.5 * base["d"])
    return dict(name="qLDPC + erasure conv.", n=base["n"], ms=base["ms"],
                meas=base["meas"], oneq=base["oneq"], rounds=base["rounds"],
                p_th=base["p_th"], d=d_eff,
                note=f"dual-species; effective d {base['d']}->{d_eff} (model)")

def tree_qudit():
    """QNFO tree/ultrametric class under INDEPENDENT errors: qudit generalization
    threshold ~2e-4 (55x below surface ~1.1e-2) per the verified poster numbers.
    Not viable for independent noise at p2 >= 1e-4; its regime is correlated
    failure (structured-noise channel: 50-75% thresholds, classical simulation)."""
    return dict(name="tree/ultrametric (qudit)", n=3.0, ms=9.0, meas=3.0,
                oneq=9.0, rounds=3, p_th=2.0e-4, d=3,
                note="independent-noise threshold 2e-4: EXCLUDED below; "
                     "correlated regime only")

# ─────────────────────────────── workload ───────────────────────────────
L = 10_000            # logical gates per computation
TARGET = 1.0e-6       # p_L per logical gate -> 1% end-to-end failure
families = [
    surface(7), surface(11), surface(15),
    qldpc_gross(), qldpc_erasure(),
    xzzx(5), xzzx(7),
    tree_qudit(),
]

print("=" * 100)
print("JPCUB: energy per correct answer — trapped-ion QEC families")
print(f"workload L={L} logical gates; target p_L <= {TARGET:.0e} "
      f"(<= {100*L*TARGET:.0f}% end-to-end); units: 1 MS gate = 1.0")
print("=" * 100)

hdr = (f"{'family':<28}{'n/log':>7}{'MS/log':>8}{'E/log':>9}  "
       f"{'p_L@1e-3':>10} {'viable':>7}  {'E_correct@1e-3':>14} "
       f"{'E_correct@1e-4':>14}")
print(hdr)
print("-" * 100)

rows = []
for fam in families:
    p2 = 1e-3
    pL = p_logical(p2, fam["p_th"], fam["d"])
    E_gate = energy_per_logical_gate(fam["ms"], fam["meas"], fam["oneq"],
                                     fam["rounds"], fam["n"])
    ok = pL <= TARGET
    if ok:
        Ec1e3, P = energy_per_correct(L, E_gate, pL)
    else:
        Ec1e3 = float("inf")
    # at lower physical error 1e-4
    pL2 = p_logical(1e-4, fam["p_th"], fam["d"])
    E_gate2 = energy_per_logical_gate(fam["ms"], fam["meas"], fam["oneq"],
                                      fam["rounds"], fam["n"])
    ok2 = pL2 <= TARGET
    Ec1e4 = energy_per_correct(L, E_gate2, pL2)[0] if ok2 else float("inf")
    rows.append((fam["name"], fam["n"], fam["ms"], E_gate, pL, ok, Ec1e3, ok2, Ec1e4))
    print(f"{fam['name']:<28}{fam['n']:>7.0f}{fam['ms']:>8.0f}{E_gate:>9.0f}  "
          f"{pL:>10.2e} {str(ok):>7}  {Ec1e3 if math.isfinite(Ec1e3) else float('nan'):>14.3e} "
          f"{Ec1e4 if math.isfinite(Ec1e4) else float('nan'):>14.3e}")

print("-" * 100)
print("\n-- Operating-point scan: gate speed vs fidelity (energy-optimal, not")
print("   fidelity-optimal). Model: MS energy E ~ A/t (fixed pulse area: power")
print("   ~ 1/t^2), spontaneous-emission error ~ E, so E2(p2) = E2_ref*(1e-3/p2)")
print("   capped at the p2 floor 1e-4 (below it, error is floor-limited). The")
print("   energy-optimal operating point sits at the LARGEST p2 that still meets")
print("   the logical-error budget (constraint boundary) -- run each code as fast")
print("   as its budget allows, then compare codes by energy.\n")

P2_FLOOR = 1.0e-4

def scan_family(make_fam, d_min=3, d_max=31):
    best = None
    for d in range(d_min, d_max + 1, 2):
        fam = make_fam(d)
        # largest p2 with p_L(p2) <= TARGET (bisection on log scale), >= P2_FLOOR
        lo, hi = P2_FLOOR, 3e-3
        if p_logical(lo, fam["p_th"], fam["d"]) > TARGET:
            continue  # not viable even at the floor
        for _ in range(60):
            mid = math.sqrt(lo * hi)
            if p_logical(mid, fam["p_th"], fam["d"]) <= TARGET:
                lo = mid
            else:
                hi = mid
        p2_opt = lo
        pL = p_logical(p2_opt, fam["p_th"], fam["d"])
        # energy at this operating point: E2 scales as 1/p2 (capped at floor)
        s = min(1.0, 1e-3 / max(p2_opt, P2_FLOOR))
        E_gate = energy_per_logical_gate(fam["ms"] * s, fam["meas"], fam["oneq"] * s,
                                         fam["rounds"], fam["n"])
        Ec, P = energy_per_correct(L, E_gate, pL)
        if best is None or Ec < best[0]:
            best = (Ec, p2_opt, d, fam["name"].split(" d=")[0], E_gate, pL)
    return best

for label, fn in [("surface", surface), ("XZZX (bias 10)", xzzx)]:
    b = scan_family(fn)
    if b:
        print(f"  {label:<16} min E_correct={b[0]:.3e} at p2={b[1]:.2e}, d={b[2]}, "
              f"E/log={b[4]:.0f}, p_L={b[5]:.2e}")

# qLDPC is a fixed family (not a distance scan)
for fam in [qldpc_gross(), qldpc_erasure()]:
    lo, hi = P2_FLOOR, 3e-3
    if p_logical(lo, fam["p_th"], fam["d"]) > TARGET:
        print(f"  {fam['name']:<16} NOT viable even at p2 floor {P2_FLOOR:.0e}")
        continue
    for _ in range(60):
        mid = math.sqrt(lo * hi)
        if p_logical(mid, fam["p_th"], fam["d"]) <= TARGET:
            lo = mid
        else:
            hi = mid
    p2_opt = lo
    s = min(1.0, 1e-3 / max(p2_opt, P2_FLOOR))
    E_gate = energy_per_logical_gate(fam["ms"] * s, fam["meas"], fam["oneq"] * s,
                                     fam["rounds"], fam["n"])
    Ec, P = energy_per_correct(L, E_gate, p_logical(p2_opt, fam["p_th"], fam["d"]))
    print(f"  {fam['name']:<16} min E_correct={Ec:.3e} at p2={p2_opt:.2e}, "
          f"d_eff={fam['d']}, E/log={E_gate:.0f}, p_L={p_logical(p2_opt, fam['p_th'], fam['d']):.2e}")

print("\n-- Absolute scale (E2 ~ 0.5 uJ/MS gate):")
for fam in [surface(11), qldpc_gross(), qldpc_erasure()]:
    E_gate = energy_per_logical_gate(fam["ms"], fam["meas"], fam["oneq"],
                                     fam["rounds"], fam["n"])
    pL = p_logical(1e-3, fam["p_th"], fam["d"])
    if pL <= TARGET:
        Ec, _ = energy_per_correct(L, E_gate, pL)
        print(f"  {fam['name']:<24} ~{Ec*0.5e-6:>10.3f} J per {L} correct logical gates "
              f"(at p2=1e-3)")

print("\n-- Sensitivity: tighter budget (L=1e6, target p_L=1e-8):")
for fam in [surface(15), qldpc_gross(), qldpc_erasure()]:
    pL = p_logical(1e-3, fam["p_th"], fam["d"])
    ok = pL <= 1e-8
    print(f"  {fam['name']:<24} p_L@1e-3={pL:.2e} viable@{'yes' if ok else 'no'}")
