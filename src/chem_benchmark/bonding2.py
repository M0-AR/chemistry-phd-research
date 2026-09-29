"""Ch 10: bonding II, dipole, bond order."""
def dipole(q_c: float, r_m: float) -> float:
    return q_c * r_m
def bond_order(n_bonding: float, n_antibonding: float) -> float:
    return 0.5 * (n_bonding - n_antibonding)
