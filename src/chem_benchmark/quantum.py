"""Ch 7: quantum, photon, Bohr."""
H = 6.63e-34
C = 3.00e8
RH = 2.18e-18
def photon_energy_nu(nu_hz: float) -> float:
    return H * nu_hz
def photon_energy_lambda(lambda_m: float) -> float:
    return H * C / lambda_m
def bohr_energy(n: int) -> float:
    if n < 1:
        raise ValueError("n>=1")
    return -RH / (n*n)
def bohr_transition_dE(ni: int, nf: int) -> float:
    """Absorption +, emission -. E_photon = RH(1/ni^2-1/nf^2) with sign."""
    return RH * (1.0/(ni*ni) - 1.0/(nf*nf))
