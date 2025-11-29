import pytest #type: ignore
import src.functions.factorial as factorial

def test_factorial():
    assert factorial.factorial(1) == 1
    assert factorial.factorial(2) == 2
    assert factorial.factorial(3) == 6
    assert factorial.factorial(4) == 24
    assert factorial.factorial(5) == 120
    assert factorial.factorial(6) == 720
    assert factorial.factorial(7) == 5040

def test_factorial_zero_and_less():
    with pytest.raises(ValueError):
        factorial.factorial(0)
    with pytest.raises(ValueError):
        factorial.factorial(-1)
    with pytest.raises(ValueError):
        factorial.factorial(-100)


def test_factorial_rec():
    assert factorial.factorial_recursive(1) == 1
    assert factorial.factorial_recursive(2) == 2
    assert factorial.factorial_recursive(3) == 6
    assert factorial.factorial_recursive(4) == 24
    assert factorial.factorial_recursive(5) == 120
    assert factorial.factorial_recursive(6) == 720
    assert factorial.factorial_recursive(7) == 5040

def test_factorial_rec_zero_and_less():
    with pytest.raises(ValueError):
        factorial.factorial_recursive(0)
    with pytest.raises(ValueError):
        factorial.factorial_recursive(-1)
    with pytest.raises(ValueError):
        factorial.factorial_recursive(-100)
