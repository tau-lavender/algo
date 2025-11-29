import pytest #type: ignore
import src.functions.fibo as fibo

def test_fibo():
    assert fibo.fibo(1) == 1
    assert fibo.fibo(2) == 1
    assert fibo.fibo(3) == 2
    assert fibo.fibo(4) == 3
    assert fibo.fibo(5) == 5
    assert fibo.fibo(6) == 8
    assert fibo.fibo(7) == 13

def test_fibo_zero_and_less():
    with pytest.raises(ValueError):
        fibo.fibo(0)
    with pytest.raises(ValueError):
        fibo.fibo(-1)
    with pytest.raises(ValueError):
        fibo.fibo(-100)


def test_fibo_rec():
    assert fibo.fibo_recursive(1) == 1
    assert fibo.fibo_recursive(2) == 1
    assert fibo.fibo_recursive(3) == 2
    assert fibo.fibo_recursive(4) == 3
    assert fibo.fibo_recursive(5) == 5
    assert fibo.fibo_recursive(6) == 8
    assert fibo.fibo_recursive(7) == 13

def test_fibo_rec_zero_and_less():
    with pytest.raises(ValueError):
        fibo.fibo_recursive(0)
    with pytest.raises(ValueError):
        fibo.fibo_recursive(-1)
    with pytest.raises(ValueError):
        fibo.fibo_recursive(-100)
