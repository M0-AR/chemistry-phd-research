"""Ch 2-3: atoms, isotopes, mole, percent composition."""
AVOGADRO = 6.022e23
def neutrons(a_mass: int, z_atomic: int) -> int:
    return a_mass - z_atomic
def percent_composition(n_elem_molar: float, m_compound: float) -> float:
    return n_elem_molar / m_compound * 100.0
def moles_from_atoms(atoms: float) -> float:
    return atoms / AVOGADRO
def atoms_from_moles(moles: float) -> float:
    return moles * AVOGADRO
