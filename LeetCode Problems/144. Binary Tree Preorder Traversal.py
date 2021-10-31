"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import List, Optional

from Algorithms.leetcode_tree import TreeNode, buildTree


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def _preorder_traversal(node, values):
            if not node:
                return

            values.append(node.val)
            _preorder_traversal(node.left, values)
            _preorder_traversal(node.right, values)

        values = []
        _preorder_traversal(root, values)
        return values


root_arr = [1, None, 2, 3]
root = (buildTree(root_arr))
print(Solution().preorderTraversal(root))
