"""Ch 5: gases, PV=nRT (R=0.082057 L atm / mol K)."""
R_L_ATM = 0.082057

def ideal_gas_pressure(n_mol: float, v_l: float, t_k: float) -> float:
    return n_mol * R_L_ATM * t_k / v_l

def ideal_gas_volume(n_mol: float, p_atm: float, t_k: float) -> float:
    return n_mol * R_L_ATM * t_k / p_atm

def ideal_gas_moles(p_atm: float, v_l: float, t_k: float) -> float:
    return p_atm * v_l / (R_L_ATM * t_k)
