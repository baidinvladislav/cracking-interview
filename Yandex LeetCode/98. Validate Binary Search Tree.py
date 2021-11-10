"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional

from Algorithms.leetcode_tree import buildTree, TreeNode


class Solution:

    def dfs(self, node, values):
        if not node:
            return

        self.dfs(node.left, values)
        values.append(node.val)
        self.dfs(node.right, values)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        self.dfs(root, values)

        i = 0
        j = 1

        while j != len(values):
            if values[i] >= values[j]:
                return False

            i += 1
            j += 1

        return True


# root_arr = [2, 1, 3]
root_arr = [5, 1, 4, None, None, 3, 6]
root = buildTree(root_arr)
print(Solution().isValidBST(root))
