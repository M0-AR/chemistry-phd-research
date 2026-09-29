"""Run all chemistry benchmarks, write metrics.json (seed fixed for determinism)."""
import argparse, json, platform, sys, datetime
sys.path.insert(0, "src")
from chem_benchmark import (
    molar_mass, ideal_gas_volume, heat_q, kc, ph_from_h, nernst_e,
    c_to_k, density, neutrons, molarity, photon_energy_lambda,
    dh_from_be, bond_order, osmotic_pi, half_life_first,
    solubility_from_ksp_11, dg_from_dh_ds, decay_n, lambda_from_half, dbe,
)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="results/metrics.json")
    a = ap.parse_args()
    metrics = {
        "seed": a.seed,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "python": platform.python_version(),
        "benchmarks": {
            "stoichiometry_H2O_gmol": round(molar_mass({"H": 2, "O": 1}), 3),
            "stoichiometry_NaCl_gmol": round(molar_mass({"Na": 1, "Cl": 1}), 2),
            "gas_STP_V_L": round(ideal_gas_volume(1.0, 1.0, 273.15), 3),
            "thermo_q_100g_water_J": round(heat_q(100.0, 4.184, 10.0), 1),
            "equilibrium_Kc_demo": round(kc([0.5, 0.5], [0.1, 0.2, 0.2, 0.2]), 1),
            "ph_0_01M_HCl": round(ph_from_h(0.01), 2),
            "nernst_Daniell_V": round(nernst_e(1.10, 2, 1.0), 3),
            "ch1_density_gml": round(density(10.0, 2.0), 3),
            "ch1_K_0C": round(c_to_k(0.0), 2),
            "ch2_neutrons_Na23": neutrons(23, 11),
            "ch4_molarity": round(molarity(0.5, 1.0), 3),
            "ch7_photon_500nm_J": photon_energy_lambda(500e-9),
            "ch9_dH_H2Cl2_kJ": round(dh_from_be([436.4, 242.7], [2*431.9]), 1),
            "ch10_bond_order_O2": round(bond_order(10, 6), 2),
            "ch12_osmotic_1M_atm": round(osmotic_pi(1.0, 298.15), 2),
            "ch13_t12_k0693": round(half_life_first(0.69314718056), 4),
            "ch16_sol_AgCl_M": solubility_from_ksp_11(1.6e-10),
            "ch18_dG_100kJ_200JK": round(dg_from_dh_ds(100000, 298.15, 200), 1),
            "ch23_decay_C14_half": round(decay_n(1.0, lambda_from_half(5730.0), 5730.0), 4),
            "ch24_DBE_benzene": dbe(6, 6),
        },
        "env": {"R_L_atm": 0.082057, "reference": "Chang Chemistry 10th Ed."},
    }
    with open(a.out, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"wrote {a.out}")

if __name__ == "__main__":
    main()
