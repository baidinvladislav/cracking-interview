"""
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
"""


from __future__ import print_function
from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    min_heap = []

    for root in lists:
        if root is not None:
            heappush(min_heap, root)

    result_head, result_tail = None, None
    while min_heap:
        node = heappop(min_heap)
        if not result_head:
            result_head = result_tail = node
        else:
            result_tail.next = node
            result_tail = result_tail.next

        if node.next:
            heappush(min_heap, node.next)

    return result_head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result is not None:
        print(str(result.value) + " ", end='')
        result = result.next


main()
