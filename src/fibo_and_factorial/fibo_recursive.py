def run_fibo_recursive(n: int) -> int:
    """
    run fibo_recursive
    Вычисляет значение числа Фибоначчи рекурсивно
    Для запуска в typer, тестов ии бенчмарок.
    Не перехватывает ошибки в отличии от fibo()
    :n: Номер числа Фибоначчи начиная с 1
    :return: Число Фибоначчи под номером n
    """
    if n <= 0:
        raise ValueError("Номер числа должен быть больше 0")
    elif n in (1, 2):
        return 1
    else:
        return run_fibo_recursive(n - 1) + run_fibo_recursive(n - 2)


def fibo_recursive(n: int) -> None:
    """
    Выводит число Фибоначчи под номером n начиная с 1. Знаение считается рекурсивно
    :n: Номер числа Фибоначчи начиная с 1
    :return: Ничего
    """
    try:
        print(run_fibo_recursive(n))
    except ValueError as e:
        print(e)
