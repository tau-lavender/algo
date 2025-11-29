import pytest #type: ignore

import src.gen_test_case.int_arrays as int_arrays
import src.gen_test_case.float_arrays as float_arrays
from src.sorts.counting_sort import counting_sort

def test_counting_sort_int():
    n = int_arrays.rand_int_array(100, 0, 100)
    correct_ans = sorted(n)
    ans = counting_sort(n)
    assert ans == correct_ans

def test_counting_sort_int_neg():
    n = int_arrays.rand_int_array(100, -100, 0)
    correct_ans = sorted(n)
    ans = counting_sort(n)
    assert ans == correct_ans

def test_counting_sort_float():
    n = float_arrays.rand_float_array(100, 0, 10)
    with pytest.raises(TypeError):
        counting_sort(n)

def test_counting_sort_empty():
    ans = counting_sort([])
    assert ans is list and not ans
