"""Ch 6: thermochemistry."""
def heat_q(mass_g: float, c_j_gk: float, delta_t_k: float) -> float:
    """q = m*c*dT in Joules."""
    return mass_g * c_j_gk * delta_t_k

def hess_enthalpy(steps_kj: list) -> float:
    """Hess's law: sum of step enthalpies."""
    return sum(steps_kj)
