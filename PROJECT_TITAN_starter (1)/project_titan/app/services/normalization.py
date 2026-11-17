from datetime import datetime, timezone

def normalize_decimal_odds(value: float) -> float:
    value = float(value)
    if value <= 1:
        raise ValueError("Cuota decimal inválida")
    return value

def utc_now() -> datetime:
    return datetime.now(timezone.utc)
