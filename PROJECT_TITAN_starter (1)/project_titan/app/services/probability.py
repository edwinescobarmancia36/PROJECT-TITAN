def implied_probability(decimal_odds: float) -> float:
    if decimal_odds <= 1:
        raise ValueError("La cuota decimal debe ser mayor que 1.")
    return 1.0 / decimal_odds

def expected_value(probability: float, decimal_odds: float) -> float:
    if not 0 <= probability <= 1:
        raise ValueError("La probabilidad debe estar entre 0 y 1.")
    if decimal_odds <= 1:
        raise ValueError("La cuota decimal debe ser mayor que 1.")
    return probability * decimal_odds - 1.0
