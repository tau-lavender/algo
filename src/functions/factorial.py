def factorial(n: int) -> int:
    """
    Вычисляет факториал числа n
    :n: Число факториал которого надо посчитать
    :return: Факториал числа n
    """
    if n <= 0:
        raise ValueError("Номер числа должен быть больше 0")
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans


def factorial_recursive(n: int) -> int:
    """
    Вычисляет факториал числа n рекурсивно
    :n: Число факториал которого надо посчитать
    :return: Факториал числа n
    """
    if n <= 0:
        raise ValueError("Номер числа должен быть больше 0")
    elif n in (1, 2):
        return n
    else:
        return factorial_recursive(n - 1) * n
