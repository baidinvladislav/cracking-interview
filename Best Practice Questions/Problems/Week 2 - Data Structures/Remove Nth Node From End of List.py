import unittest


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


class TestRemoveNthFromEnd(unittest.TestCase):
    def test_first(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        excepted_head = Node(1)
        excepted_head.next = Node(2)
        excepted_head.next.next = Node(3)
        excepted_head.next.next.next = Node(5)
        self.assertEqual(excepted_head, Solution().removeNthFromEnd(head=head, n=2))

    def test_second(self):
        head = Node(1)
        self.assertIsNone(Solution().removeNthFromEnd(head=head, n=1))

    def test_third(self):
        head = Node(1)
        head.next = Node(2)

        excepted_head = Node(1)
        self.assertEqual(excepted_head, Solution().removeNthFromEnd(head=head, n=1))


if __name__ == "__main__":
    unittest.main()
