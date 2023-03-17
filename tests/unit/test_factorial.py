import pytest

from domain.models.calculator import Calculator


@pytest.mark.parametrize("number, answer", (
        (4, 24),
        (5, 120),
        (6, 720)
))
def test_factorial(number, answer):
    result = Calculator.factorial(number)
    assert result == answer
