"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from Algorithms.leetcode_tree import TreeNode, buildTree


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def recursion(root, s):

            if root is None:
                return s
            else:
                s += str(root.val)

            s += str(recursion(root.left, paths))
            s += str(recursion(root.right, paths))


        s = ''
        s += str(root.val)
        paths = []

        s += str(recursion(root.right, s))
        return s


root_arr = [1, 2, 3, None, 5]
root = buildTree(root_arr)
print(Solution().binaryTreePaths(root))
