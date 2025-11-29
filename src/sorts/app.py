import typer # type: ignore

import src.sorts.bubble_sort
import src.sorts.quick_sort
import src.sorts.counting_sort
import src.sorts.radix_sort
import src.sorts.bucket_sort


app = typer.Typer()


@app.command(context_settings={"ignore_unknown_options": True}) # поддержка отрицательных чисел
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


@app.command(context_settings={"ignore_unknown_options": True}) # поддержка отрицательных чисел
def quick_sort(a: list[int]) -> None:
    # Функция для typer
    """
    Выводит список отсортированный быстрой сортировкой
    :a: Список для сортировки
    :return: Ничего
    """
    print(*src.sorts.quick_sort.quick_sort(a))


@app.command(context_settings={"ignore_unknown_options": True}) # поддержка отрицательных чисел
def counting_sort(a: list[int]) -> None:
    # Функция для typer
    """
    Сортирует список подсчётом
    :a: Список для сортировки
    :return: Отсортированный список a
    """
    print(*src.sorts.counting_sort.counting_sort(a))


@app.command()
def radix_sort(a: list[int], base: int = 10) -> None:
    # Функция для typer
    """
    Сортирует список поразрядно
    :a: Список для сортировки
    :base: Основание системы счисления
    :return: Отсортированный список a
    """
    print(*src.sorts.radix_sort.radix_sort(a, base))


@app.command()
def bucket_sort(a: list[float], buckets: int | None = None) -> None:
    # Функция для typer
    """
    Сортирует список
    :a: Список для сортировки
    :buckets: Кол-во блоков
    :return: Отсортированный список a
    """
    print(*src.sorts.bucket_sort.bucket_sort(a, buckets=buckets))
