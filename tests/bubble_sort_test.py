from src.sorts.bubble_sort import run_bubble_sort

def test_bubble_sort_key():
    n = [(1, 3), (1, 2), (2, 1)]
    correct_ans = sorted(n, key = lambda x: (x[0], x[1]))
    ans = run_bubble_sort(n, lambda x: (x[0], x[1]))
    assert ans == correct_ans
