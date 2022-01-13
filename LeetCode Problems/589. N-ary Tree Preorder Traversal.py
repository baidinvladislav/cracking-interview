"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples)
"""

from typing import List


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root):
        def dfs(node, output):

            if node is None:
                return

            output.append(node.val)
            for child in node.children:
                dfs(child, output)

        output = []
        dfs(root, output)
        return output


print(Solution().preorder(root=[1, None, 3, 2, 4, None, 5, 6]))
