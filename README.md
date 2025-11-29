# Алгоритмический мини-пакет (структуры данных и сортировки)
## Лабораторная работа №3
**Иванющенко Эрик Александрович. М8О-104БВ-25**

---
## Начало работы, устаночка зависимостей
``` bash
uv venv
uv sync
```

---
## Короткое описание работы
- Для CLI используется *typer* с расширением *typer-shell*. Это позволяет запустить CLI одной командой и писать только сами команды для typer
```bash
python -m src.main
```
- Больше информации о запуске можно узнать с помощью
```bash
help # о всех командах
<команда> --help # о конкретной команде
```
- Запуск команд для структуры *stack*. Для CLI создаётся в начале работы 1 stack, который хранится в singleton
```bash
stack <команда для стака> <аргументы>
```
- Запуск остальных команд
```bash
<команда> <аргументы>
```

---
## Реализованные функции
- `functions`
    1) `factorial`
    2) `factorial_recursive`
    3) `fibo`
        - за O(1) спасибо дискретке
    4) `fibo_recursive`
- `sorts`
    1) `bubble_sort`
        - поддерживает key и cmp
    2) `quick_sort`
        - поддерживает key и cmp
    3) `counting_sort`
    4) `radix_sort`
    5) `bucket_sort`
    6) `heap_sort`
        - поддерживает key и cmp
- `stack`
    - Реализован "1b Стек на list"
    1) `push`
    2) `pop`
    3) `peek`
    4) `is_empty`
    5) `__len__`
    6) `min`
        - за константу
    7) `max`
        - за константу
- `gen_test_case`
    1) `rand_int_array`
    2) `nearly_sorted`
    3) `many_duplicates`
    4) `reverse_sorted`
    5) `rand_float_array`
- `benchmark`
    1) `timeit_once`
    2) `benchmark_sorts`
        - не принимает аргументы, работает на заданных внутри значениях
- Поддержка key и cmp
    - `sort_wrapper` - декоратор для сортировок
        ```python
        if cmp is None:
                return func(a, key)
            else:
                return func(a, cmp_to_key(lambda x, y: cmp(key(x), key(y))))
        ```
        Мне кажется, что получилось круто


---
## Принятые решения
- key и cmp реализованны через декоратор в `src/sorts/sort_wrapper.py`
- typer не принимает key и cmp т.к. не реализованна защита от вредоносного кода

# Benchmark
- Получено командой "benchmark-sorts" в CLI
```
Seed: 3498925
Arrays:
1: rand_int_array(2000, 0, 100)
2: rand_int_array(2000, 0, 10000)
3: rand_int_array(2000, -100, 100)
4: nearly_sorted(2000, 5)
5: many_duplicates(2000, 5)
6: reverse_sorted(2000)
7: rand_float_array(2000, 0, 10)
8: rand_float_array(2000, -10, 10)
Sort:                            1       2       3       4       5       6       7       8
bubble_sort                      2.9162  2.4658  2.4887  1.8470  2.3480  2.9887  2.3959  2.3315
quick_sort                       0.0250  0.0522  0.0174  0.0161  0.0156  0.0156  0.0312  0.0313
counting_sort                    0.0000  0.0156  0.0028  0.0000  0.0007  0.0016  None    None
radix_sort                       0.0080  0.0126  None    0.0000  0.0082  0.0045  None    None
bucket_sort                      0.0230  1.2183  0.0000  0.0469  0.0156  0.0469  1.4240  1.4250
heap_sort                        0.0742  0.0494  0.0469  0.0469  0.0313  0.0469  0.0469  0.0494
```
