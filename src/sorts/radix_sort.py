def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Сортирует список поразрядно
    :a: Список для сортировки
    :base: Основание системы счисления
    :return: Отсортированный список a
    """
    if base <= 0:
        raise ValueError("Основание системы счисления должно быть больше 0")

    if not a:
        return a
    array = a.copy()
    max_elem = max(array)
    cou = 1
    while max_elem // cou > 0:
        bucket_list: list[list[int]] = [[] for _ in range(base)]

        for elem in array:
            current = (elem // cou) % base
            bucket_list[current].append(elem)

        array = []
        for bucket in bucket_list:
            array.extend(bucket)
        cou *= base
    return array
