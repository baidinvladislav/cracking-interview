"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Iterative
    def reverseList(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    # Recursive
    def reverseList_v1(self, head):
        if not head or not head.next:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
