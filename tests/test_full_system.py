import math
from chem_benchmark import (
    c_to_f, f_to_c, c_to_k, density,
    neutrons, percent_composition, moles_from_atoms, AVOGADRO,
    molarity, dilution_m1v1,
    photon_energy_lambda, bohr_transition_dE,
    en_difference, bond_type, dh_from_be, bond_order,
    clausius_p2, bragg_d,
    molality, boiling_elevation, osmotic_pi, raoult_p,
    first_order_ln, half_life_first, arrhenius_k,
    solubility_from_ksp_11, dg_from_dh_ds, dg0_from_k,
    oxidation_state_complex, coordination_number,
    decay_n, lambda_from_half,
    dbe, degree_polymerization,
)

def test_ch1_measurement():
    assert abs(c_to_f(0) - 32) < 1e-9
    assert abs(f_to_c(32) - 0) < 1e-9
    assert abs(c_to_k(0) - 273.15) < 1e-9
    assert abs(density(10.0, 2.0) - 5.0) < 1e-9

def test_ch2_atomic():
    assert neutrons(23, 11) == 12
    assert abs(percent_composition(2.016, 18.015) - 11.19) < 0.02
    assert abs(moles_from_atoms(AVOGADRO) - 1.0) < 1e-9

def test_ch4_aq():
    assert abs(molarity(0.5, 1.0) - 0.5) < 1e-9
    assert abs(dilution_m1v1(1.0, 0.1, 1.0) - 0.1) < 1e-9

def test_ch7_quantum():
    e = photon_energy_lambda(500e-9)
    assert abs(e - 3.97e-19) < 0.05e-19
    # Balmer H-alpha ni=3->nf=2 emission negative
    assert bohr_transition_dE(3, 2) < 0

def test_ch9_10_bonding():
    assert en_difference(3.98, 2.20) > 1.5
    assert bond_type(2.1) == "ionic"
    assert bond_type(1.0) == "polar covalent"
    assert abs(dh_from_be([436.4, 242.7], [2*431.9]) + 184.7) < 1.0
    assert abs(bond_order(10, 6) - 2.0) < 1e-9

def test_ch11_phase():
    p2 = clausius_p2(401.0, 27000.0, 291.0, 305.0)
    assert p2 > 401.0
    assert abs(bragg_d(1, 154.0, 15.0) - 297.5) < 2.0

def test_ch12_solutions():
    assert abs(molality(1.0, 1.0) - 1.0) < 1e-9
    assert abs(boiling_elevation(0.52, 1.0) - 0.52) < 1e-9
    assert abs(osmotic_pi(1.0, 298.15) - 24.45) < 0.05
    assert abs(raoult_p(0.9, 100.0) - 90.0) < 1e-9

def test_ch13_kinetics():
    assert abs(first_order_ln(1.0, 0.69314718056, 1.0) - 0.5) < 1e-6
    assert abs(half_life_first(0.69314718056) - 1.0) < 1e-6
    assert arrhenius_k(1e13, 50000, 298.15) > 0

def test_ch16_18_sol_entropy():
    assert abs(solubility_from_ksp_11(1.6e-10) - 1.2649e-5) < 1e-7
    assert abs(dg_from_dh_ds(100000, 298.15, 200) - 40370) < 50
    assert dg0_from_k(1.0, 298.15) == 0.0

def test_ch22_transition():
    # K3[Fe(CN)6]: net 0? K3+ Fe? 0 = Fe + 6*(-1) +3*(+1) -> Fe=+3
    assert oxidation_state_complex(0, [-1]*6 + [1]*3) == 3
    assert coordination_number([2, 2, 2]) == 6

def test_ch23_nuclear():
    lam = lambda_from_half(5730.0)
    assert abs(decay_n(1.0, lam, 5730.0) - 0.5) < 1e-9

def test_ch24_25_organic_poly():
    assert dbe(6, 6) == 4  # benzene
    assert abs(degree_polymerization(100000, 100) - 1000) < 1e-9
