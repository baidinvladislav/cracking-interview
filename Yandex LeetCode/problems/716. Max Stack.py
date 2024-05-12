class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, x: int):
        self.stack.append(x)
        if not self.maxStack or x >= self.maxStack[-1]:
            self.maxStack.append(x)

    def pop(self):
        val = self.stack.pop()
        if val == self.maxStack[-1]:
            self.maxStack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.maxStack[-1]

    def popMax(self):
        max_val = self.maxStack[-1]
        buffer = []
        while self.stack[-1] != max_val:
            buffer.append(self.pop())
        self.pop()  # Remove the max element
        while buffer:
            self.push(buffer.pop())
        return max_val
