"""
You are given an immutable linked list, print out all values of each node in reverse
with the help of the following interface:

ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):

ImmutableListNode.printValue(): Print value of the current node.
ImmutableListNode.getNext(): Return the next node.

The input is only given to initialize the linked list internally.
You must solve this problem without modifying the linked list.
In other words, you must operate the linked list using only the mentioned APIs.
"""


# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head:
            node = head.getNext()
            self.printLinkedListInReverse(node)
            head.printValue()


print(Solution().printLinkedListInReverse(head=[1, 2, 3, 4]))
