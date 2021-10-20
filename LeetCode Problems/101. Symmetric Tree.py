"""
Given the root of a binary tree, check whether it is a mirror
of itself (i.e., symmetric around its center).
"""
from typing import Optional

from Algorithms.leetcode_tree import TreeNode, buildTree


class Solution:

    def _in_order_traversal_right(self, node):
        if node is not None:
            self._in_order_traversal_right(node.right)
            self.in_order_arr_right.append(node.val)
            self._in_order_traversal_right(node.left)

        self.in_order_arr_right.append(None)

    def _in_order_traversal_left(self, node):
        if node is not None:
            self._in_order_traversal_left(node.left)
            self.in_order_arr_left.append(node.val)
            self._in_order_traversal_left(node.right)

        self.in_order_arr_left.append(None)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.in_order_arr_left = []
        self.in_order_arr_right = []

        self._in_order_traversal_left(root.left)
        self._in_order_traversal_right(root.right)

        if self.in_order_arr_left == self.in_order_arr_right:
            return True
        else:
            return False


root = buildTree([1, 2, 2, None, 3, None, 3])
print(Solution().isSymmetric(root))

