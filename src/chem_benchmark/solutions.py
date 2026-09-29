"""Ch 12: solutions, colligative."""
def molality(moles: float, kg_solvent: float) -> float:
    return moles / kg_solvent
def boiling_elevation(kb: float, m: float) -> float:
    return kb * m
def freezing_depression(kf: float, m: float) -> float:
    return kf * m
def osmotic_pi(molarity_mol_l: float, t_k: float) -> float:
    """pi(atm) = MRT, R=0.082057."""
    return molarity_mol_l * 0.082057 * t_k
def raoult_p(x_solvent: float, p_pure: float) -> float:
    return x_solvent * p_pure
