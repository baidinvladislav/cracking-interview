class MaxStack(object):
    def __init__(self):
        self.storage = []

    def push(self, x):
        self.storage.append(x)

    def pop(self):
        return self.storage.pop()

    def top(self):
        return self.storage[-1]

    def peekMax(self):
        return max(self.storage)

    def popMax(self) -> int:
        max_val = self.peekMax()
        max_idx = max([i for i, v in enumerate(self.storage) if v == max_val])
        return self.storage.pop(max_idx)
