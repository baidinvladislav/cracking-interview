import math


# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def isValidBST_rec(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True

            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return validate(node.right, node.val, high) and validate(node.left, low, node.val)

        return validate(root)

    # iterative
    def isValidBST_it(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = deque([(root, float('-inf'), float('inf'))])
        while queue:
            root, lower, upper = queue.popleft()

            if not root:
                continue

            val = root.val
            if val <= lower or val >= upper:
                return False

            queue.append((root.right, val, upper))
            queue.append((root.left, lower, val))
        return True
