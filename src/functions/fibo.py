def fibo(n: int) -> int:
    """
    Вычисляет число Фибоначчи
    :n: Номер числа Фибоначчи начиная с 1
    :return: Число Фибоначчи под номером n
    """
    # дискретка пригодилась
    if n <= 0:
        raise ValueError("Номер числа должен быть больше 0")
    return round(((1 + 5 ** 0.5) ** n - (1 - 5 ** 0.5) ** n) / 2 ** n / 5 ** 0.5)


def fibo_recursive(n: int) -> int:
    """
    Вычисляет значение числа Фибоначчи рекурсивно
    :n: Номер числа Фибоначчи начиная с 1
    :return: Число Фибоначчи под номером n
    """
    if n <= 0:
        raise ValueError("Номер числа должен быть больше 0")
    elif n in (1, 2):
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)
