
def counting_sort(a: list[int])  -> list[int]:
    """
    Сортирует список подсчётом
    :a: Список для сортировки
    :return: Отсортированный список a
    """
    if not a:
        return a
    array = []
    min_el = min(a)
    counter = [0] * (max(a) - min_el + 1)
    for element in a:
        counter[element - min_el] += 1

    for i in range(len(counter)):
        for _ in range(counter[i]):
            array.append(i + min_el)

    return array
