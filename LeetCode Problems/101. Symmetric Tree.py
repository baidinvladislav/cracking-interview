"""
Given the root of a binary tree, check whether it is a mirror
of itself (i.e., symmetric around its center).
"""
from typing import Optional

from Algorithms.leetcode_tree import TreeNode, buildTree


class Solution:

    def traversal_left_tree(self, node, values_arr):

        if node is None:
            return

        self.traversal_left_tree(node.left, values_arr)
        values_arr.append(node.val)
        self.traversal_left_tree(node.right, values_arr)

        values_arr.append(None)

    def traversal_right_tree(self, node, values_arr):

        if node is None:
            return

        self.traversal_right_tree(node.right, values_arr)
        values_arr.append(node.val)
        self.traversal_right_tree(node.left, values_arr)

        values_arr.append(None)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []

        self.traversal_left_tree(root.left, left)
        self.traversal_right_tree(root.right, right)

        return left == right


# root = buildTree([1, 2, 2, 2, None, 2])
# print(Solution().isSymmetric(root))


# elegant short solution
class Solution1:
    def isSymmetric(self, root):
        def isSym(L, R):
            if not L and not R:
                return True

            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False

        return isSym(root, root)


root = buildTree([1, 2, 2, 3, 4, 4, 3])
print(Solution1().isSymmetric(root))
