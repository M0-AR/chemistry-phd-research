"""Ch 19: electrochemistry, Nernst at 25C."""
import math

def nernst_e(e0_v: float, n_e: int, q: float, t_k: float = 298.15) -> float:
    """E = E0 - (RT/nF) lnQ. R=8.314, F=96485."""
    if n_e <= 0:
        raise ValueError("n must be >0")
    if q <= 0:
        raise ValueError("Q must be >0")
    R, F = 8.314, 96485.0
    return e0_v - (R * t_k / (n_e * F)) * math.log(q)
