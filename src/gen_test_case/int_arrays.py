import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed: int | None = None) -> list[int]:
    """
    Возвращает массив случайных int длинны n
    :n: - кол-во элементов
    :lo: - минимальное значение элемента
    :hi: - максимальное значение элемента
    :distinct: - выбирает должны ли элементы быть разными
    :seed: - сид для рандома
    :return: - массив
    """

    if lo > hi:
        raise ValueError(f"Минимальное значение не должно быть больше максимального. {lo} > {hi}")
    if n <= 0:
        raise ValueError("Кол-во элементов должно быть > нуля")

    random.seed(seed)
    if distinct:
        return random.sample(range(lo, hi + 1), k=n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    return []
