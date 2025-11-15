def run_factorial_recursive(n: int) -> int:
    """
    run factorial_recursive_recursive
    Вычисляет факториал числа n рекурсивно
    Для запуска в typer, тестов ии бенчмарок.
    Не перехватывает ошибки в отличии от factorial_recursive_recursive()
    :n: Число факториал которого надо посчитать
    :return: Факториал числа n
    """
    if n <= 0:
        raise ValueError("Номер числа должен быть больше 0")
    elif n in (1, 2):
        return n
    else:
        return run_factorial_recursive(n - 1) * n

def factorial_recursive(n: int) -> None:
    """
    Выводит факториал числа n. Вычисляется рекурсивно
    :n: Число факториал которого надо посчитать
    :return: Ничего
    """
    try:
        print(run_factorial_recursive(n))
    except ValueError as e:
        print(e)
