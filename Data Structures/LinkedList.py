"""
Worst Case:
    * space: O(n)
    * prepend: O(1)
    * append: O(1)
    * lookup: O(n)
    * insert: O(n)
    * delete: O(n)

Strengths:
    * Fast operations on the ends. Adding elements at either end of a linked list is O(1).
    Removing the first element is also O(1).

    * Flexible size. There's no need to specify how many elements you're going to store ahead of time.
    You can keep adding elements as long as there's enough space on the machine.

Weaknesses:
    * Costly lookups. To access or edit an item in a linked list, you have to take O(i) time
    to walk from the head of the list to the iith item.

Uses:
    * Stacks and queues only need fast operations on the ends, so linked lists are ideal.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node.next.previous = node
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return

        current_node = None
        for current_node in self:
            pass
        current_node.next = node
