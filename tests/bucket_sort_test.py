import pytest #type: ignore
import src.gen_test_case.int_arrays as int_arrays
import src.gen_test_case.float_arrays as float_arrays
from src.sorts.bucket_sort import bucket_sort

def test_bucket_sort_int():
    n = int_arrays.rand_int_array(100, 0, 100)
    correct_ans = sorted(n)
    ans = bucket_sort(n)
    assert ans == correct_ans

def test_bucket_sort_int_neg():
    n = int_arrays.rand_int_array(100, -100, 0)
    correct_ans = sorted(n)
    ans = bucket_sort(n)
    assert ans == correct_ans

def test_bucket_sort_float():
    n = float_arrays.rand_float_array(100, 0, 10)
    correct_ans = sorted(n)
    ans = bucket_sort(n)
    assert ans == correct_ans

def test_bucket_sort_empty():
    ans = bucket_sort([])
    assert ans == []


def test_bucket_sort_bucket_value():
    with pytest.raises(ValueError):
        bucket_sort([1, 3], buckets = 1)
    with pytest.raises(ValueError):
        bucket_sort([1, 3], buckets = 0)
    with pytest.raises(ValueError):
        bucket_sort([1, 3], buckets = -1)
