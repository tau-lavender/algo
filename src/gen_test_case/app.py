import typer # type: ignore

import src.gen_test_case.int_arrays as int_arrays


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
