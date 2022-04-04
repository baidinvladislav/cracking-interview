import random


class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.array)
            self.array.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            idx = self.hashmap[val]
            last_value = self.array[-1]
            self.array[idx] = last_value
            self.array.pop()
            self.hashmap[last_value] = idx
            del self.hashmap[val]
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.array)
