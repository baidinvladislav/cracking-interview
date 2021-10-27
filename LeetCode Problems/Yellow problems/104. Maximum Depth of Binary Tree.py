"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
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

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# root_arr = [2, None, 3, None, 4, None, 5, None, 6]
root_arr = [3, 9, 20, None, None, 15, 7]
root = buildTree(root_arr)
print(Solution().maxDepth(root))
