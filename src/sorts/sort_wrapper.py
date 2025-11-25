from typing import Callable, TypeVar, Any
from functools import cmp_to_key
T = TypeVar('T')
KeyFunc = Callable[[T], Any]
CmpFunc = Callable[[T, T], int] | None


def sort_wrapper(func) -> Callable[[list[T], KeyFunc, CmpFunc], list[T]]:
    """
    Декоратор для функций сортировки
    :func: - функция сортировки, которая декорируется
    :return: - декорированную функцию
    """
    def wrapper(a: list[T], key: KeyFunc = lambda x: x, cmp: CmpFunc = None) -> list[T]:
        """
        Передаёт фунции ключ или компаратор, если он задан
        Объединяет ключ и компаратор, если заданы оба
        Не меняет поведение фунции, если ничего не задано
        :a: - массив для сортировки
        :key: - ключ
        :cmp: - компаратор
        :return: - функция сортировки
        """
        if cmp is None:
            return func(a, key)
        else:
            return func(a, cmp_to_key(lambda x, y: cmp(key(x), key(y))))
    return wrapper
