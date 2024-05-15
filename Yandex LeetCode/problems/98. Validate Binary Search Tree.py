"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


import math
from typing import Optional

from Algorithms.leetcode_tree import buildTree, TreeNode


# Approach 1: More clearly two steps recursive
# Time complexity: O(N)
# Space complexity: O(N)
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


# Approach 2: Recursive Traversal with Valid Range
# Time complexity: O(N) since we visit each node exactly once.
# Space complexity: O(N) since we keep up to the entire tree.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if node is None:
                return True

            left = validate(node.left, low, node.val)
            right = validate(node.right, node.val, high)

            if not low < node.val < high:
                return False

            return left and right

        return validate(root, float('-inf'), float('inf'))
