from chem_benchmark import molar_mass, ideal_gas_volume
from chem_benchmark.real_data import NIST_WATER, STP_L_ATM, check_water_mw, check_stp_volume

def test_live_nist_water_mw():
    calc = molar_mass({"H": 2, "O": 1})
    assert check_water_mw(calc), f"{calc} vs NIST {NIST_WATER['mw']}"
    assert abs(calc - 18.0153) < 0.01

def test_live_nist_thermo_anchors():
    # Anchors fetched live 2026-09-29 from NIST WebBook — do not change without re-fetch
    assert NIST_WATER["dfH_gas_kJmol"] == -241.826
    assert NIST_WATER["S_gas_JmolK"] == 188.835

def test_live_stp_volume():
    v = ideal_gas_volume(1.0, 1.0, 273.15)
    assert check_stp_volume(v)
    assert abs(v - STP_L_ATM["V_L"]) < 0.02
