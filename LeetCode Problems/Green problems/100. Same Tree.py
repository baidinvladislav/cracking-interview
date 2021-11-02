"""
Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional

from Algorithms.leetcode_tree import TreeNode, buildTree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, values):
            if not node:
                return

            dfs(node.left, values)
            values.append(node.val)
            dfs(node.right, values)

            values.append(None)

        first_tree = []
        second_tree = []

        dfs(p, first_tree)
        dfs(q, second_tree)

        return first_tree == second_tree


root_arr1 = [1, 2]
root_arr2 = [1, None, 2]

root1 = buildTree(root_arr1)
root2 = buildTree(root_arr2)

print(Solution().isSameTree(root1, root2))
