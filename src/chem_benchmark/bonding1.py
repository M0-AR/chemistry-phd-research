"""Ch 9: bonding I, electronegativity, bond enthalpy Hess."""
def en_difference(en_a: float, en_b: float) -> float:
    return abs(en_a - en_b)
def bond_type(en_diff: float) -> str:
    if en_diff >= 2.0:
        return "ionic"
    if en_diff >= 0.5:
        return "polar covalent"
    return "nonpolar covalent"
def dh_from_be(be_react: list, be_prod: list) -> float:
    """DH = sum BE react - sum BE prod."""
    return sum(be_react) - sum(be_prod)
