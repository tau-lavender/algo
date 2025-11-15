from src.sorts.sort_wrapper import sort_wrapper, T, KeyFunc
from sys import setrecursionlimit

setrecursionlimit(1_000_000)

@sort_wrapper
def run_quick_sort(a: list[T], key: KeyFunc)  -> list[T]:
    """
    run quick_sort
    Применяет быструю сортировку
    Для запуска в typer, тестов ии бенчмарок.
    Не перехватывает ошибки в отличии от quick_sort()
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
    return run_quick_sort(left, key=key) + middle + run_quick_sort(right, key=key)


def quick_sort(a: list[int]) -> None:
    # Функция для typer
    """
    Выводит список отсортированный быстрой сортировкой
    :a: Список для сортировки
    :return: Ничего
    """
    try:
        print(*run_quick_sort(a))
    except ValueError as e:
        print(e)
