"""
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


def find_middle_of_linked_list(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next = Node(6)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()
