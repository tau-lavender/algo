import typer # type: ignore

import src.sorts.bubble_sort
import src.sorts.quick_sort


app = typer.Typer()


@app.command()
def bubble_sort(a: list[int]) -> None:
    # Функция для typer
    """
    Выводит список отсортированный пузырьком
    :a: Список для сортировки
    :return: Ничего
    """
    try:
        print(*src.sorts.bubble_sort.bubble_sort(a))
    except ValueError as e:
        print(e)


@app.command()
def quick_sort(a: list[int]) -> None:
    # Функция для typer
    """
    Выводит список отсортированный быстрой сортировкой
    :a: Список для сортировки
    :return: Ничего
    """
    try:
        print(*src.sorts.quick_sort.quick_sort(a))
    except ValueError as e:
        print(e)
