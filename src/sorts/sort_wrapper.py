from typing import Callable, TypeVar, Any
from functools import cmp_to_key
T = TypeVar('T')
KeyFunc = Callable[[T], Any]
CmpFunc = Callable[[T, T], int]

def sort_wrapper(func):
    def wrapper(a: list[T], key: KeyFunc = lambda x: x, cmp: CmpFunc = lambda x, y: x > y) -> list[T]:
        return func(a, cmp_to_key(lambda x, y: cmp(key(x), key(y))))
    return wrapper
