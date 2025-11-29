from sys import setrecursionlimit

setrecursionlimit(1_000_000)

def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
    Сортирует список
    :a: Список для сортировки
    :buckets: Кол-во блоков
    :return: Отсортированный список a
    """
    if not a:
        return a

    if buckets is None:
        buckets = len(a)
    if buckets <= 1:
        raise ValueError("Кол-во блоков должно быть больше одного")

    min_elem = min(a)
    max_elem = max(a)
    if min_elem == max_elem:
        return a.copy()

    bucket_list: list[list[float]] = [[] for _ in range(buckets)]
    for elem in a:
        bucket_index = int((elem - min_elem) / (max_elem - min_elem) * (buckets - 1))
        bucket_index = min(bucket_index, buckets - 1)
        bucket_list[bucket_index].append(elem)

    result = []
    for bucket in bucket_list:
        result.extend(bucket_sort(bucket, buckets=buckets))

    return result
