import unittest


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


class Solution:
    # Iterative Time: O(n), Space:O(1)
    def reverseList_iter(self, head):
        previous = None
        current = head
        while current:
            temp_next = current.next
            current.next = previous
            previous = current
            current = temp_next
        return previous

    # Recursive Time: O(n), Space:O(n)
    def reverseList_rec(self, head):
        if not head or not head.next:
            return head

        p = self.reverseList_rec(head.next)
        head.next.next = head
        head.next = None
        return p


class TestReverseLinkedList(unittest.TestCase):
    def test_first(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        excepted_head = Node(5)
        excepted_head.next = Node(4)
        excepted_head.next.next = Node(3)
        excepted_head.next.next.next = Node(2)
        excepted_head.next.next.next.next = Node(1)
        self.assertEqual(excepted_head, Solution().reverseList_rec(head=head))
        self.assertEqual(excepted_head, Solution().reverseList_iter(head=head))

    def test_second(self):
        head = Node(1)
        head.next = Node(2)

        excepted_head = Node(2)
        excepted_head.next = Node(1)
        self.assertIsNone(Solution().reverseList_rec(head=head))
        self.assertEqual(excepted_head, Solution().reverseList_iter(head=head))


if __name__ == "__main__":
    unittest.main()
