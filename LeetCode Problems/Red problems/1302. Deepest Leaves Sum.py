"""
Given the root of a binary tree, return the sum of values of its deepest leaves.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        self.levelSumList = []

        self.dfs(root, 0)

        n = len(self.levelSumList)

        return self.levelSumList[n - 1]

    def dfs(self, node, level):

        if node == None:
            return

        n = len(self.levelSumList)

        if level == n:
            self.levelSumList.append(0)

        self.levelSumList[level] = self.levelSumList[level] + node.val

        self.dfs(node.right, level + 1)
        self.dfs(node.left, level + 1)


print(Solution().deepestLeavesSum(root=[1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]))
