def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Сортирует список поразрядно
    :a: Список для сортировки
    :base: Основание системы счисления
    :return: Отсортированный список a
    """
    if not a:
        return a
    array = a.copy()
    max_elem = max(array)
    cou = 1
    while max_elem // cou > 0:
        buckets: list[list[int]] = [[] for _ in range(base)]

        for elem in array:
            current = (elem // cou) % base
            buckets[current].append(elem)

        array = []
        for bucket in buckets:
            array.extend(bucket)
        cou *= base
    return array
