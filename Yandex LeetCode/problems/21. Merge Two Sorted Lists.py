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
        # base cases
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        # recursion body
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # Approach 2: Iteration
    # Time complexity: O(n + m)
    # Space complexity: O(1)
    def mergeTwoLists(self, list1, list2):
        # Создаем фиктивный начальный узел, который поможет упростить вставку
        dummy = ListNode()
        current = dummy

        # Пока в обоих списках есть элементы
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Если элементы остались только в одном из списков, присоединяем их
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Возвращаем начало сформированного списка
        return dummy.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


print(Solution().mergeTwoLists(l1, l2))
