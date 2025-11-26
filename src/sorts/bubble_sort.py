from src.sorts.sort_wrapper import sort_wrapper, T, KeyFunc

@sort_wrapper
def bubble_sort(a: list[T], key: KeyFunc)  -> list[T]:
    """
    Сортирует список пузырьком
    :a: Список для сортировки
    :return: Отсортированный список a
    """
    array = a.copy()
    for j in range(len(array)):
        for i in range(len(array) - 1 - j):
            if key(array[i]) > key(array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
    return array
