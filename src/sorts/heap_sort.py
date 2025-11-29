from src.sorts.sort_wrapper import sort_wrapper, T, KeyFunc
from typing import Any


def do_swaps(array: list[tuple[Any, T]], n: int, i: int):
    """
    Вспомогательная функция для heap_sort
    """
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        do_swaps(array, n, largest)

@sort_wrapper
def heap_sort(a: list[T], key: KeyFunc) -> list[T]:
    """
    Выводит список отсортированный пирамидой
    :a: Список для сортировки
    :return: Ничего
    """
    temp_array = a.copy()
    array: list[tuple[Any, T]] = [(key(x), x) for x in temp_array]
    n = len(array)

    for i in range(n//2 - 1, -1, -1):
        do_swaps(array, n, i)
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        do_swaps(array, i, 0)

    return list(map(lambda x: x[1], array))
