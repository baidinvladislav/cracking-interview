# 09:30-10:30
# TODO: разобрать задачу
class MultipleStacks:
    def __init__(self, stacks_size):
        self.number_stacks = 3
        self.array = [0] * (stacks_size * self.number_stacks)
        self.sizes = [0] * self.number_stacks
        self.stack_size = stacks_size

    def push(self, item, stack_num):
        if self.is_full(stack_num):
            raise Exception('Stack is full')
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = item

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack is empty')
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack is empty')
        return self.array[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1


def three_in_one():
    new_stack = MultipleStacks(2)
    print(new_stack.is_empty(1))
    new_stack.push(3, 1)
    print(new_stack.peek(1))
    print(new_stack.is_empty(1))
    new_stack.push(2, 1)
    print(new_stack.peek(1))
    print(new_stack.pop(1))
    print(new_stack.peek(1))
    new_stack.push(3, 1)


three_in_one()
