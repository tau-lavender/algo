from src.sorts.sort_wrapper import sort_wrapper, T, KeyFunc

@sort_wrapper
def run_bubble_sort(a: list[T], key: KeyFunc)  -> list[T]:
    """
    run bubble_sort
    Сортирует список пузырьком
    Для запуска в typer, тестов ии бенчмарок.
    Не перехватывает ошибки в отличии от bubble_sort()
    :a: Список для сортировки
    :return: Отсортированный список a
    """
    array = a.copy()
    for j in range(len(array)):
        for i in range(len(array) - 1 - j):
            if key(array[i]) > key(array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


def bubble_sort(a: list[int]) -> None:
    # Функция для typer
    """
    Выводит список отсортированный пузырьком
    :a: Список для сортировки
    :return: Ничего
    """
    try:
        print(*run_bubble_sort(a))
    except ValueError as e:
        print(e)
