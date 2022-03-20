from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # recursive
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        root.left = right
        root.right = left

        return root

    # iterative
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque()
        queue.append(root)
        while queue:
            current = queue.popleft()
            temp = current.left
            current.left = current.right
            current.right = temp

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return root
