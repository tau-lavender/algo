import random

def rand_float_array(n: int, lo:float = 0.0, hi: float = 1.0, *, seed: int | None = None) -> list[float]:
    """
    Возвращает массив случайных float длинны n
    :n: - кол-во элементов
    :lo: - минимальное значение элемента
    :hi: - максимальное значение элемента
    :seed: - сид для рандома
    :return: - массив
    """

    if lo > hi:
        raise ValueError(f"Минимальное значение не должно быть больше максимального. {lo} > {hi}")
    if n <= 0:
        raise ValueError("Кол-во элементов должно быть > 0")

    random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]
