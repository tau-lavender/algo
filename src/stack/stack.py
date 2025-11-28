
class Stack:
    """
    Реализация стака на list (вариант 1b)
    """

    def __init__(self) -> None:
        """
        Инициализация стека
        :data: хранилище
        :min_stack: хранилище минимальных элементов
        :max_stack: хранилище максиальных элементов
        :return: ничего
        """
        self.data: list[int] = []
        self.min_stack: list[int] = []
        self.max_stack: list[int] = []


    def __str__(self):
        """
        Возвращает содержимое стека
        """
        return " ".join(map(str, self.data))


    def push(self, x: int) -> None:
        """
        Добавление элемента в конец
        :x: элемент для добавления
        :return: ничего
        """
        if not self.is_empty():
            if self.data[-1] >= x:
                self.min_stack.append(x)
            if self.data[-1] <= x:
                self.max_stack.append(x)
        else:
            self.min_stack.append(x)
            self.max_stack.append(x)

        self.data.append(x)


    def pop(self) -> int:
        """
        Удаление и возврат элемента из конца
        :return: последний элемент
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        element = self.data.pop()
        if self.max_stack:
            if element == self.max_stack[-1]:
                self.max_stack.pop()
        if self.min_stack:
            if element == self.min_stack[-1]:
                self.min_stack.pop()
        return element


    def peek(self) -> int:
        """
        Возврат элемента из конца без удаления
        :return: последний элемент
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.data[-1]


    def is_empty(self) -> bool:
        """
        Проверка стека на пустоту
        :return: True если пустой или False если не пустой
        """
        return not bool(self.data)


    def __len__(self) -> int:
        """
        Возвращает длину стека
        :return: длина стека
        """
        return len(self.data)


    def min(self) -> int:
        """
        Минимальный элемент стека
        :return: минимальный элемент
        """
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.min_stack[-1]


    def max(self) -> int:
        """
        Максимальный элемент стека
        :return: максимальный элемент
        """
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.max_stack[-1]
