def run_factorial(n: int) -> int:
    """
    run factorial
    Вычисляет факториал числа n
    Для запуска в typer, тестов ии бенчмарок.
    Не перехватывает ошибки в отличии от factorial()
    :n: Число факториал которого надо посчитать
    :return: Факториал числа n
    """
    if n <= 0:
        raise ValueError("Номер числа должен быть больше 0")
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans


def factorial(n: int) -> None:
    """
    Выводит факториал числа n
    :n: Число факториал которого надо посчитать
    :return: Ничего
    """
    try:
        print(run_factorial(n))
    except ValueError as e:
        print(e)
