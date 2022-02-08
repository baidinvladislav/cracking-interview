from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # my
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, values):
            if not node:
                return

            dfs(node.left, values)
            values.append(node.val)
            dfs(node.right, values)

        values = []
        dfs(root, values)
        return values[k + 1]

    # leetcode one line solution
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]
