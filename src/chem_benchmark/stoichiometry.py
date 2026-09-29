"""Ch 1-3: stoichiometry, molar mass (Chang 10th)."""
import math

ATOMIC_WEIGHTS = {
    "H": 1.008, "He": 4.0026, "C": 12.011, "N": 14.007, "O": 15.999,
    "Na": 22.990, "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974,
    "S": 32.06, "Cl": 35.45, "K": 39.098, "Ca": 40.078, "Fe": 55.845,
    "Cu": 63.546, "Zn": 65.38, "Ag": 107.87,
}

def molar_mass(composition: dict) -> float:
    """composition: {'H':2,'O':1} -> g/mol. Raises KeyError on unknown."""
    total = 0.0
    for el, n in composition.items():
        if el not in ATOMIC_WEIGHTS:
            raise KeyError(f"unknown element {el}")
        total += ATOMIC_WEIGHTS[el] * n
    return total

def moles_to_mass(moles: float, mm: float) -> float:
    return moles * mm

def mass_to_moles(mass_g: float, mm: float) -> float:
    if mm <= 0:
        raise ValueError("molar mass must be >0")
    return mass_g / mm
