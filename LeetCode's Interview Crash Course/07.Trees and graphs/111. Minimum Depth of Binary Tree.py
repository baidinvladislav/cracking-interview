from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = float("inf")
        stack = deque()
        stack.append((root, 1))
        while stack:
            node, depth = stack.popleft()

            if not node.left and not node.right:
                result = min(result, depth)

            if node.left:
                stack.append((node.left, depth + 1))

            if node.right:
                stack.append((node.right, depth + 1))

        return result
