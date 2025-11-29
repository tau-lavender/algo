import src.sorts.bubble_sort as bubble_sort
import src.sorts.quick_sort as quick_sort
import src.sorts.counting_sort as counting_sort
import src.sorts.radix_sort as radix_sort
import src.sorts.bucket_sort as bucket_sort
import src.sorts.heap_sort as heap_sort

import src.gen_test_case.int_arrays as int_arrays
import src.gen_test_case.float_arrays as float_arrays

import time

def timeit_once(func, *args, **kwargs) -> float:
    time_start = time.time()
    func(*args, **kwargs)
    time_end = time.time()
    return time_end - time_start


def benchmark_sorts() -> None:
    seed = 3498925
    sorts = [(bubble_sort.bubble_sort, "bubble_sort"),
    (quick_sort.quick_sort, "quick_sort"),
    (counting_sort.counting_sort, "counting_sort"),
    (radix_sort.radix_sort, "radix_sort"),
    (bucket_sort.bucket_sort, "bucket_sort"),
    (heap_sort.heap_sort, "heap_sort")]
    arrays = [int_arrays.rand_int_array(2000, 0, 100, seed = seed),
    int_arrays.rand_int_array(2000, 0, 10000, seed = seed),
    int_arrays.rand_int_array(2000, -100, 100, seed = seed),
    int_arrays.nearly_sorted(2000, 5, seed = seed),
    int_arrays.many_duplicates(2000, 5, seed = seed),
    int_arrays.reverse_sorted(2000),
    float_arrays.rand_float_array(2000, 0, 10, seed = seed),
    float_arrays.rand_float_array(2000, -10, 10, seed = seed),
    ]
    names = ["rand_int_array(2000, 0, 100)",
    "rand_int_array(2000, 0, 10000)",
    "rand_int_array(2000, -100, 100)",
    "nearly_sorted(2000, 5)",
    "many_duplicates(2000, 5)",
    "reverse_sorted(2000)",
    "rand_float_array(2000, 0, 10)",
    "rand_float_array(2000, -10, 10)",
    ]
    print(f"Seed: {seed}")
    print("Arrays:")
    c = 1
    for name in names:
        print(f"{c}: {name}")
        c += 1
    print("Sort: \t\t\t", end = "")
    for i in range(1, c):
        print(f"\t {i}", end = "")
    print()
    for curent_sort in sorts:
        print(curent_sort[1], "\t\t", end = "")
        for array in arrays:
            try:
                print("\t %2.4f" % (timeit_once(curent_sort[0], a = array)), end = "")
            except ValueError:
                print("\t None", end = "")
            except IndexError:
                print("\t None", end = "")
        print()
