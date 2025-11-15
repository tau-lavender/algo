from typing import Callable, TypeVar, Any
from functools import cmp_to_key
T = TypeVar('T')
KeyFunc = Callable[[T], Any]
CmpFunc = Callable[[T, T], int] | None

def sort_wrapper(func):
    def wrapper(a: list[T], key: KeyFunc = lambda x: x, cmp: CmpFunc = None) -> list[T]:
        if cmp is None:
            return func(a, key)
        else:
            return func(a, cmp_to_key(lambda x, y: cmp(key(x), key(y))))
    return wrapper
