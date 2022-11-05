# Queues and stacks
+ [Largest Stack](#largest-stack)
+ [Implement A Queue With Two Stacks](#implement-a-queue-with-two-stacks)
+ [Parenthesis Matching](#parenthesis-matching)


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
Реализовать очередь через два стека.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>При enqueue все элементы складываем в стек #1.</li>
 <li>При dequeue все элементы перекладываем в стек #2 и возвращаем элемент со стека #2.</li>
</ol>

</blockquote></details>


```python
# my code based on their solution
# Time Complexity: O(1)
# Space Complexity: O(m)
class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if len(self.stack_out) == 0:
            while len(self.stack_in) > 0:
                item = self.stack_in.pop()
                self.stack_out.append(item)

        return self.stack_out.pop()

```


## Parenthesis Matching
Дана строка со скобками.
Дан индекс одной из открывающих скобок, вернуть индекс соответствующей ей закрывающей скобки.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Итерируем строку, начиная со следующего элемента после входящей открытвающей скобки.</li>
 <li>Храним в переменной количество встречающихся открывающихся скобок, инкрементируем счетчик по мере прохода строки.</li>
 <li>Если натыкаемся на закрывающую скобку, а также наш счетчик раве 0, то вернуть индекс текущего элемента.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: '((((()))))'
Output: 2

Example 2:
Input: '()()((()()))'
Output: 5

Example 3:
Input: '()(()'
Output: 2
```

```python
# their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def get_closing_paren(sentence, opening_paren_index):
    counter = 0
    for i in range(opening_paren_index + 1, len(sentence)):
        char = sentence[i]

        if char == '(':
            counter += 1
        elif char == ')':
            if counter == 0:
                return i

            counter -= 1

    raise

```
