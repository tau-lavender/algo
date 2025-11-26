import typer # type: ignore

import src.functions.fibo as fibo_funcs
import src.functions.factorial as factorial_funcs


app = typer.Typer()


@app.command()
def fibo(n: int) -> None:
    """
    Выводит число Фибоначчи под номером n начиная с 1
    :n: Номер числа Фибоначчи начиная с 1
    :return: Ничего
    """
    try:
        print(fibo_funcs.fibo(n))
    except ValueError as e:
        print(e)


@app.command()
def fibo_recursive(n: int) -> None:
    """
    Выводит число Фибоначчи под номером n начиная с 1. Знаение считается рекурсивно
    :n: Номер числа Фибоначчи начиная с 1
    :return: Ничего
    """
    try:
        print(fibo_funcs.fibo_recursive(n))
    except ValueError as e:
        print(e)


@app.command()
def factorial(n: int) -> None:
    """
    Выводит факториал числа n
    :n: Число факториал которого надо посчитать
    :return: Ничего
    """
    try:
        print(factorial_funcs.factorial(n))
    except ValueError as e:
        print(e)


@app.command()
def factorial_recursive(n: int) -> None:
    """
    Выводит факториал числа n. Вычисляется рекурсивно
    :n: Число факториал которого надо посчитать
    :return: Ничего
    """
    try:
        print(factorial_funcs.factorial_recursive(n))
    except ValueError as e:
        print(e)
