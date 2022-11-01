# Queues and stacks
+ [Largest Stack](#largest-stack)
+ [Implement A Queue With Two Stacks](#implement-a-queue-with-two-stacks)


## Largest Stack
Найти максимальный элемент в стеке.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Используем два стека.</li>
 <li>Один для хранения всех элементов, другой для хранения максимумов.</li>
</ol>

</blockquote></details>


```python
class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


# their solution
# Time Complexity: O(1)
# Space Complexity: O(m)
class MaxStack(object):

    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)

        if not self.max_stack.peek() or item >= self.max_stack.peek():
            self.max_stack.push(item)

    def pop(self):
        item = self.stack.pop()

        if self.max_stack.peek() == item:
            self.max_stack.pop()

        return item

    def get_max(self):
        return self.max_stack.peek()

```


## Implement A Queue With Two Stacks
