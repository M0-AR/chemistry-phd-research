"""Ch 24-25: organic/polymer helpers."""
def dbe(c: int, h: int, n: int = 0, x_hal: int = 0) -> int:
    """Double-bond equivalents: C - H/2 - X/2 + N/2 +1."""
    return c - (h + x_hal)//2 + n//2 + 1 if (h+x_hal) % 2 == 0 else c - (h+x_hal)/2 + n/2 + 1
def degree_polymerization(m_polymer: float, m_monomer: float) -> float:
    return m_polymer / m_monomer
