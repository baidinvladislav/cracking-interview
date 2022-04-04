class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        val = self.peekMax()
        for i in range(-1, -len(self.stack) - 1, -1):
            if self.stack[i] == val:
                del self.stack[i]
                break
        return val


stk = MaxStack()
stk.push(5)
stk.push(1)
stk.push(5)
stk.top()
stk.popMax()
stk.top()
stk.peekMax()
stk.pop()
stk.top()
