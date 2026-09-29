"""Ch 16/18: solubility Ksp, entropy, free energy."""
import math
def ksp_agcl(ag: float, cl: float) -> float:
    return ag * cl
def solubility_from_ksp_11(ksp: float) -> float:
    return math.sqrt(ksp)
def ds_rxn(s_prod: list, s_react: list) -> float:
    return sum(s_prod) - sum(s_react)
def dg_from_dh_ds(dh: float, t_k: float, ds: float) -> float:
    return dh - t_k * ds
def dg0_from_k(k: float, t_k: float) -> float:
    return -8.314 * t_k * math.log(k)
def k_from_dg0(dg0: float, t_k: float) -> float:
    return math.exp(-dg0/(8.314*t_k))
