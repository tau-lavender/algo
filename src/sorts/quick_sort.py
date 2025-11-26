from src.sorts.sort_wrapper import sort_wrapper, T, KeyFunc
from sys import setrecursionlimit

setrecursionlimit(1_000_000)

@sort_wrapper
def quick_sort(a: list[T], key: KeyFunc)  -> list[T]:
    """
    Применяет быструю сортировку
    :a: Список для сортировки
    :return: Отсортированный список a
    """
    if len(a) < 2:
        return a
    if len(a) == 2:
        if key(a[0]) < key(a[1]):
            return a
        else:
            return a[::-1]
    left, middle, right = [], [], []
    mid_el = a[len(a) // 2]
    for el in a:
        if key(el) > key(mid_el):
            right.append(el)
        elif key(el) < key(mid_el):
            left.append(el)
        else:
            middle.append(el)
    return quick_sort(left, key=key) + middle + quick_sort(right, key=key)
