"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0

        if not root:
            return 0

        elif not root.children:
            return 1

        for child in root.children:
            result = 1 + self.maxDepth(child)
            depth = max(depth, result)

        return depth


print(Solution().maxDepth(root=[1, None, 3, 2, 4, None, 5, 6]))
