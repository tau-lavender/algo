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
        raise ValueError("Кол-во элементов должно быть > 0")

    random.seed(seed)
    if distinct:
        return random.sample(range(lo, hi + 1), k=n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed: int | None = None) -> list[int]:
    """
    Возвращает массив int от 0 до (n - 1), swaps случайных элементов которого поменяны местами с соседними
    :n: - кол-во элементов
    :swaps: - кол-во замен элементов
    :seed: - сид для рандома
    :return: - массив
    """

    if swaps < 0:
        raise ValueError("Кол-во замен должно быть >= 0")
    if n <= 0:
        raise ValueError("Кол-во элементов должно быть > 0")

    random.seed(seed)
    array = list(range(n))
    for _ in range(swaps):
        index = random.randint(0, n - 2)
        print(index)
        array[index], array[index + 1] = array[index + 1], array[index]
    return array


def many_duplicates(n: int, k_unique: int = 5, *, seed=None) -> list[int]:
    """
    Возвращает массив из n int от 0 до (k_unique - 1)
    :n: - кол-во элементов
    :k_unique: - кол-во уникальных элементов
    :seed: - сид для рандома
    :return: - массив
    """

    if k_unique <= 2:
        raise ValueError("Кол-во уникальных элементов должно быть >= 2")
    if n <= 0:
        raise ValueError("Кол-во элементов должно быть > 0")

    random.seed(seed)
    return random.choices(range(k_unique), k = n)
