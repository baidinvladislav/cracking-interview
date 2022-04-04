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
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            left_subtree = validate(node=node.left, low=low, high=node.val)
            right_subtree = validate(node=node.right, low=node.val, high=high)

            return left_subtree and right_subtree

        return validate(root)
