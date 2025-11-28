import typer # type: ignore

import src.gen_test_case.int_arrays as int_arrays
import src.gen_test_case.float_arrays as float_arrays


app = typer.Typer()


@app.command(context_settings={"ignore_unknown_options": True}) # поддержка отрицательных чисел
def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed: int | None = None) -> None:
    """
    Возвращает массив случайных int длинны n
    :n: - кол-во элементов
    :lo: - минимальное значение элемента
    :hi: - максимальное значение элемента
    :distinct: - выбирает должны ли элементы быть разными
    :seed: - сид для рандома
    :return: - массив
    """
    try:
        print(*int_arrays.rand_int_array(n, lo, hi, distinct=distinct, seed=seed))
    except ValueError as e:
        print(f"ValueError: {e}")


@app.command()
def nearly_sorted(n: int, swaps: int, *, seed=None) -> None:
    """
    Возвращает массив int от 0 до (n - 1), swaps случайных элементов которого поменяны местами с соседними
    :n: - кол-во элементов
    :swaps: - кол-во замен элементов
    :seed: - сид для рандома
    :return: - массив
    """

    try:
        print(*int_arrays.nearly_sorted(n, swaps, seed=seed))
    except ValueError as e:
        print(f"ValueError: {e}")


@app.command()
def many_duplicates(n: int, k_unique: int = 5, *, seed=None) -> None:
    """
    Возвращает массив из n int от 0 до (k_unique - 1)
    :n: - кол-во элементов
    :k_unique: - кол-во уникальных элементов
    :seed: - сид для рандома
    :return: - массив
    """

    try:
        print(*int_arrays.many_duplicates(n, k_unique, seed=seed))
    except ValueError as e:
        print(f"ValueError: {e}")


@app.command()
def reverse_sorted(n: int) -> None:
    """
    Возвращает массив int от (n - 1) до 0
    :n: - кол-во элементов
    :return: - массив
    """
    try:
        print(*int_arrays.reverse_sorted(n))
    except ValueError as e:
        print(f"ValueError: {e}")


@app.command(context_settings={"ignore_unknown_options": True}) # поддержка отрицательных чисел
def rand_float_array(n: int, lo:float = 0.0, hi: float = 1.0, *, seed: int | None = None) -> None:
    """
    Возвращает массив случайных float длинны n
    :n: - кол-во элементов
    :lo: - минимальное значение элемента
    :hi: - максимальное значение элемента
    :seed: - сид для рандома
    :return: - массив
    """

    try:
        print(*float_arrays.rand_float_array(n, lo, hi, seed=seed))
    except ValueError as e:
        print(f"ValueError: {e}")
