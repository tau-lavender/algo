def run_fibo_recursive(n: int):
    """
    run fibo_recursive
    Для запуска в typer, тестов ии бенчмарок.
    Не перехватывает ошибки в отличии от fibo()
    :n: Номер числа Фибоначи начиная с 1
    :return: Число Фибоначи под номером n
    """
    if n <= 0:
        raise ValueError("Номер числа должен быть больше 0")
    elif n in (1, 2):
        return 1
    else:
        return run_fibo_recursive(n - 1) + run_fibo_recursive(n - 2)


def fibo_recursive(n: int) -> None:
    """
    Выводит число Фибоначи под номером n начиная с 1. Знаение считается рекурсивно
    :n: Номер числа Фибоначи начиная с 1
    :return: Число Фибоначи под номером n
    """
    try:
        print(run_fibo_recursive(n))
    except ValueError as e:
        print(e)
