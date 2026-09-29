"""Ch 8: periodic trends helpers."""
def zeff_approx(z: int, shielding: float) -> float:
    return z - shielding
def ionic_vs_atomic_hint(charge: int) -> str:
    if charge > 0:
        return "cation smaller"
    if charge < 0:
        return "anion larger"
    return "neutral"
