"""Ch 1: measurement, SI, temp, density, dimensional analysis."""
def c_to_f(c: float) -> float:
    return 9.0/5.0*c + 32.0
def f_to_c(f: float) -> float:
    return (f-32.0)*5.0/9.0
def c_to_k(c: float) -> float:
    return c + 273.15
def density(m_g: float, v_ml: float) -> float:
    if v_ml == 0:
        raise ValueError("volume zero")
    return m_g / v_ml
