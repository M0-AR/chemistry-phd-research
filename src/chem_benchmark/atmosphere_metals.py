"""Ch 17/20/21: atmosphere, metals, nonmetals helpers (descriptive + key numbers)."""
def co2_ppm_growth(ppm0: float, rate_per_yr: float, years: float) -> float:
    return ppm0 + rate_per_yr * years
def steel_carbon_class(pct_c: float) -> str:
    if pct_c < 0.03:
        return "iron"
    if pct_c <= 1.4:
        return "steel"
    return "cast iron"
