import pytest #type: ignore
import src.gen_test_case.int_arrays as int_arrays
from src.sorts.radix_sort import radix_sort

def test_radix_sort_int():
    n = int_arrays.rand_int_array(100, 0, 100)
    correct_ans = sorted(n)
    ans = radix_sort(n)
    assert ans == correct_ans
    ans2 = radix_sort(n, base = 2)
    assert ans2 == correct_ans

def test_radix_sort_int_neg():
    n = int_arrays.rand_int_array(100, -100, 0)
    with pytest.raises(ValueError):
        radix_sort(n)

def test_radix_sort_empty():
    ans = radix_sort([])
    assert ans == []

def test_radix_sort_base_value():
    with pytest.raises(ValueError):
        radix_sort([1, 3], base = 0)
    with pytest.raises(ValueError):
        radix_sort([1, 3], base = -1)
