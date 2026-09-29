"""Ch 23: nuclear decay."""
import math
def decay_n(n0: float, lam: float, t: float) -> float:
    return n0 * math.exp(-lam*t)
def half_life_from_lambda(lam: float) -> float:
    return math.log(2.0)/lam
def lambda_from_half(t12: float) -> float:
    return math.log(2.0)/t12
def binding_per_nucleon_j(defect_kg: float, nucleons: int) -> float:
    c = 2.99792458e8
    return defect_kg * c * c / nucleons
