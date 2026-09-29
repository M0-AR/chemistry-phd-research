"""Ch 13: kinetics."""
import math
def first_order_ln(a0: float, k: float, t: float) -> float:
    return a0 * math.exp(-k*t)
def half_life_first(k: float) -> float:
    return 0.69314718056 / k
def half_life_second(k: float, a0: float) -> float:
    return 1.0 / (k * a0)
def arrhenius_k(a: float, ea_jmol: float, t_k: float) -> float:
    R = 8.314
    return a * math.exp(-ea_jmol/(R*t_k))
def arrhenius_ea(k1: float, k2: float, t1: float, t2: float) -> float:
    R = 8.314
    return R * math.log(k2/k1) / (1.0/t1 - 1.0/t2)
