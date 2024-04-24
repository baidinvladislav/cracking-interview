class MinStack:

    def __init__(self):
        self.common_storage = []
        self.minimum_storage = []

    def push(self, val: int) -> None:
        if len(self.minimum_storage) == 0 or val <= self.minimum_storage[-1]:
            self.minimum_storage.append(val)

        self.common_storage.append(val)

    def pop(self) -> None:
        if self.common_storage[-1] == self.minimum_storage[-1]:
            self.minimum_storage.pop()

        return self.common_storage.pop()

    def top(self) -> int:
        return self.common_storage[-1]

    def getMin(self) -> int:
        return self.minimum_storage[-1] if self.minimum_storage else 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
