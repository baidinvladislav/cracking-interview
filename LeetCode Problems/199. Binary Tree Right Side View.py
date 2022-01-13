"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
"""
import collections

from Algorithms.leetcode_tree import buildTree, print_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from Algorithms.leetcode_tree import buildTree


class Solution(object):
    def rightSideView(self, root):
        deque = collections.deque()

        if root:
            deque.append(root)

        result = []
        while deque:
            size, val = len(deque), 0

            for _ in range(size):
                node = deque.popleft()
                val = node.val

                if node.left:
                    deque.append(node.left)

                if node.right:
                    deque.append(node.right)

            result.append(val)
        return result


root_arr = [1, 2, 3, None, 5, None, 4]
root = buildTree(root_arr)
print_tree(root)
print(Solution().rightSideView(root))
