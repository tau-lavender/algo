import src.gen_test_case.int_arrays as int_arrays
import src.gen_test_case.float_arrays as float_arrays
from src.sorts.quick_sort import quick_sort

def test_quick_sort_int():
    n = int_arrays.rand_int_array(100, 0, 100)
    correct_ans = sorted(n)
    ans = quick_sort(n)
    assert ans == correct_ans

def test_quick_sort_int_neg():
    n = int_arrays.rand_int_array(100, -100, 0)
    correct_ans = sorted(n)
    ans = quick_sort(n)
    assert ans == correct_ans

def test_quick_sort_float():
    n = float_arrays.rand_float_array(100, 0, 10)
    correct_ans = sorted(n)
    ans = quick_sort(n)
    assert ans == correct_ans

def test_quick_sort_key():
    def key(x):
        return x[1]
    n = [(1, 3), (1, 2), (2, 1)]
    correct_ans = sorted(n, key = key)
    ans = quick_sort(n, key = key)
    assert ans == correct_ans

def test_quick_sort_empty():
    ans = quick_sort([])
    assert ans == []
