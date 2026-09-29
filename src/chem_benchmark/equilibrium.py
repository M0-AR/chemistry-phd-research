"""Ch 14-16: equilibrium, acids/bases."""
import math

def kc(products: list, reactants: list) -> float:
    """Kc = prod[products] / prod[reactants]. Concentrations in mol/L."""
    num = 1.0
    for c in products:
        num *= c
    den = 1.0
    for c in reactants:
        den *= c
    if den == 0:
        raise ValueError("reactant concentration zero")
    return num / den

def ph_from_h(h_m: float) -> float:
    if h_m <= 0:
        raise ValueError("H+ must be >0")
    return -math.log10(h_m)

def h_from_ph(ph: float) -> float:
    return 10.0 ** (-ph)

def henderson_hasselbalch(pka: float, base_m: float, acid_m: float) -> float:
    if acid_m <= 0 or base_m <= 0:
        raise ValueError("concentrations must be >0")
    return pka + math.log10(base_m / acid_m)
