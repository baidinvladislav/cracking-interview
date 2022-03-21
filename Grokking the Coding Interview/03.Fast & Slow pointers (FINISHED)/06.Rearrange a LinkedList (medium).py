"""
Given the head of a Singly LinkedList, write a method to modify the LinkedList
such that the nodes from the second half of the LinkedList are inserted alternately
to the nodes from the first half in reverse order.
So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null,
your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space and the input LinkedList should be modified in-place.
"""


from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()

    def __repr__(self):
        return str(self.value)


def reorder(head):
    if not head or not head.next:
        return

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    def reverse(head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    head_first_half_list = head
    head_second_half_list = reverse(slow)

    while head_first_half_list and head_second_half_list:
        tmp = head_first_half_list.next
        head_first_half_list.next = head_second_half_list
        head_first_half_list = tmp

        tmp = head_second_half_list.next
        head_second_half_list.next = head_first_half_list
        head_second_half_list = tmp

    if head_first_half_list:
        head_first_half_list.next = None


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()
