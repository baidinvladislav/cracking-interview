# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution:
    # Approach 1: Recursion
    # Time complexity: O(n + m)
    # Space complexity: O(n + m)
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2

        elif l2 is None:
            return l1

        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # Approach 2: Iteration
    # Time complexity: O(n + m)
    # Space complexity: O(1)
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


print(Solution().mergeTwoLists(l1, l2))
