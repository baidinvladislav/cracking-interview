"""
Reverse string through `stack` data structure.
"""


class Stack:
	def __init__(self):
		self.place = []

	def push(self, value):
		self.place.append(value)

	def pop(self):
		return self.place.pop()

	def is_empty(self):
		return len(self.place) == 0


def reverse(string):
	stack = Stack()

	for character in string:
		stack.push(character)

	rev_string = ''
	while stack.is_empty() is not True:
		rev_string += stack.pop()

	return rev_string


print(reverse('Hello World'))
