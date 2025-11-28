import typer # type: ignore

from src.stack.stack import Stack
from src.singleton import StackSingleton

app = typer.Typer(name = "stack", help="Префикс для комманд стака 'stack --help' для помощи")
stack = StackSingleton().stack

@app.command()
def clear() -> None:
    """
    Очистка содержимого стека
    :return: ничего
    """
    global stack
    stack = Stack()


@app.command()
def print_stack() -> None:
    """
    Вывод содержимого стека
    :return: ничего
    """
    print(stack)


@app.command(context_settings={"ignore_unknown_options": True}) # поддержка отрицательных чисел
def push(x: int) -> None:
    """
    Добавление элемента в конец
    :x: элемент для добавления
    :return: ничего
    """
    stack.push(x)


@app.command()
def pop() -> None:
    """
    Удаление и возврат элемента из конца
    :return: последний элемент
    """
    try:
        print(stack.pop())
    except IndexError as e:
        print(f"IndexError: {e}")


@app.command()
def peek() -> None:
    """
    Возврат элемента из конца без удаления
    :return: последний элемент
    """
    try:
        print(stack.peek())
    except IndexError as e:
        print(f"IndexError: {e}")


@app.command()
def is_empty() -> None:
    """
    Проверка стека на пустоту
    :return: True если пустой или False если не пустой
    """
    print(stack.is_empty())


@app.command()
def print_len() -> None:
    """
    Возвращает длину стека
    :return: длина стека
    """
    print(len(stack))


@app.command()
def min() -> None:
    """
    Минимальный элемент стека
    :return: минимальный элемент
    """
    print(stack.min())

@app.command()
def max() -> None:
    """
    Максимальный элемент стека
    :return: максимальный элемент
    """
    print(stack.max())
