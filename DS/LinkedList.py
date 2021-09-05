class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
        else:
            new_node = Node(new_data)
            self.head.next = new_node
            new_node.previous = self.head
            self.head = new_node
        return

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end='')
            temp = temp.next
