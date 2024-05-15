import random


class RandomizedSet:
    def __init__(self):
        self.data = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.data.append(val)
        self.val_to_index[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last_element = self.data[-1]

        # Перемещаем последний элемент на место удаляемого элемента
        self.data[index] = last_element
        self.val_to_index[last_element] = index

        # Удаляем последний элемент
        self.data.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Пример использования:
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))  # Вставляет 1 в множество. Возвращает true.
print(randomizedSet.remove(2))  # Возвращает false, так как 2 не существует в множестве.
print(randomizedSet.insert(2))  # Вставляет 2 в множество, возвращает true. Множество теперь содержит [1, 2].
print(randomizedSet.getRandom())  # Должен вернуть либо 1, либо 2 случайным образом.
print(randomizedSet.remove(1))  # Удаляет 1 из множества, возвращает true. Множество теперь содержит [2].
print(randomizedSet.insert(2))  # 2 уже присутствует в множестве, поэтому возвращает false.
print(
    randomizedSet.getRandom())  # Поскольку 2 - единственный элемент в множестве, getRandom() всегда будет возвращать 2.
