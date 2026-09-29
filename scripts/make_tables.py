import argparse, json
ap = argparse.ArgumentParser()
ap.add_argument("--in", dest="inp", default="results/metrics.json")
ap.add_argument("--out", default="results/tables.md")
a = ap.parse_args()
m = json.load(open(a.inp))
lines = ["# Chemistry Benchmark Results (generated — do not hand-edit)", "",
         f"Seed: {m['seed']} | {m['timestamp']}", "",
         "| Benchmark | Value | Chapter |",
         "|---|---|---|"]
labels = {
    "stoichiometry_H2O_gmol": ("g/mol", "Ch 3"),
    "stoichiometry_NaCl_gmol": ("g/mol", "Ch 3"),
    "gas_STP_V_L": ("L", "Ch 5"),
    "thermo_q_100g_water_J": ("J", "Ch 6"),
    "equilibrium_Kc_demo": ("-", "Ch 14"),
    "ph_0_01M_HCl": ("pH", "Ch 15"),
    "nernst_Daniell_V": ("V", "Ch 19"),
    "ch1_density_gml": ("g/mL", "Ch 1"),
    "ch1_K_0C": ("K", "Ch 1"),
    "ch2_neutrons_Na23": ("n", "Ch 2"),
    "ch4_molarity": ("M", "Ch 4"),
    "ch7_photon_500nm_J": ("J", "Ch 7"),
    "ch9_dH_H2Cl2_kJ": ("kJ", "Ch 9"),
    "ch10_bond_order_O2": ("-", "Ch 10"),
    "ch12_osmotic_1M_atm": ("atm", "Ch 12"),
    "ch13_t12_k0693": ("time", "Ch 13"),
    "ch16_sol_AgCl_M": ("M", "Ch 16"),
    "ch18_dG_100kJ_200JK": ("J", "Ch 18"),
    "ch23_decay_C14_half": ("frac", "Ch 23"),
    "ch24_DBE_benzene": ("-", "Ch 24"),
}
for k, v in m["benchmarks"].items():
    unit, ch = labels.get(k, ("", ""))
    lines.append(f"| {k} | {v} {unit} | {ch} |")
open(a.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
