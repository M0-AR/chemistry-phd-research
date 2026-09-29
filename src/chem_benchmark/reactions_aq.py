"""Ch 4: aqueous, molarity, dilution, titration, redox helper."""
def molarity(moles: float, v_l: float) -> float:
    if v_l <= 0:
        raise ValueError("V must be >0")
    return moles / v_l
def dilution_m1v1(m1: float, v1: float, v2: float) -> float:
    """M2 = M1V1/V2."""
    if v2 <= 0:
        raise ValueError("V2 must be >0")
    return m1 * v1 / v2
def titration_molarity(ma: float, va: float, vb: float, ratio_b_over_a: float = 1.0) -> float:
    """Mb = Ma*Va*ratio / Vb. ratio = mol base / mol acid."""
    return ma * va * ratio_b_over_a / vb
