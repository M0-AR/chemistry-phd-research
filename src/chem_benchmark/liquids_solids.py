"""Ch 11: liquids/solids, Clausius-Clapeyron, Bragg."""
import math
def clausius_p2(p1: float, dhvap_jmol: float, t1_k: float, t2_k: float) -> float:
    """ln(P2/P1) = -DH/R (1/T2-1/T1)."""
    R = 8.314
    return p1 * math.exp(-dhvap_jmol/R * (1.0/t2_k - 1.0/t1_k))
def bragg_d(n: int, lam_pm: float, theta_deg: float) -> float:
    th = math.radians(theta_deg)
    return n * lam_pm / (2.0 * math.sin(th))
