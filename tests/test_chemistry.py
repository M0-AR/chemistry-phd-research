import math
from chem_benchmark import (
    molar_mass, moles_to_mass, mass_to_moles,
    ideal_gas_pressure, ideal_gas_volume,
    heat_q, hess_enthalpy,
    kc, ph_from_h, h_from_ph, henderson_hasselbalch,
    nernst_e,
)

def test_molar_mass_water():
    assert abs(molar_mass({"H": 2, "O": 1}) - 18.015) < 0.01

def test_molar_mass_nacl():
    assert abs(molar_mass({"Na": 1, "Cl": 1}) - 58.44) < 0.02

def test_mole_conversions():
    mm = molar_mass({"H": 2, "O": 1})
    assert abs(moles_to_mass(2.0, mm) - 36.03) < 0.02
    assert abs(mass_to_moles(36.03, mm) - 2.0) < 0.01

def test_ideal_gas_stp():
    # 1 mol at 273.15K 1 atm -> 22.414 L
    v = ideal_gas_volume(1.0, 1.0, 273.15)
    assert abs(v - 22.414) < 0.02
    p = ideal_gas_pressure(1.0, v, 273.15)
    assert abs(p - 1.0) < 1e-6

def test_heat_water():
    assert abs(heat_q(100.0, 4.184, 10.0) - 4184.0) < 1e-6
    assert abs(hess_enthalpy([-110.5, -283.0]) - (-393.5)) < 1e-9

def test_kc():
    # N2+3H2<->2NH3 toy: [NH3]=0.5, [N2]=0.1,[H2]=0.2 => 0.25/(0.1*0.008)=312.5
    assert abs(kc([0.5, 0.5], [0.1, 0.2, 0.2, 0.2]) - 312.5) < 1e-9

def test_ph():
    assert abs(ph_from_h(0.01) - 2.0) < 1e-9
    assert abs(h_from_ph(2.0) - 0.01) < 1e-9
    assert abs(henderson_hasselbalch(4.76, 0.1, 0.1) - 4.76) < 1e-9

def test_nernst():
    # Daniell Zn/Cu E0=1.10 Q=1 -> 1.10
    assert abs(nernst_e(1.10, 2, 1.0) - 1.10) < 1e-9
    # Q=10, n=2 at 298K: drop ~0.0296 V
    assert abs(nernst_e(1.10, 2, 10.0) - (1.10 - 0.02958)) < 0.001
