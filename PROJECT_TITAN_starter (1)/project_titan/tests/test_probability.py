import pytest
from app.services.probability import implied_probability, expected_value

def test_implied_probability():
    assert implied_probability(2.0) == pytest.approx(0.5)

def test_expected_value():
    assert expected_value(0.5, 2.2) == pytest.approx(0.1)

def test_invalid_odds():
    with pytest.raises(ValueError):
        implied_probability(1.0)
