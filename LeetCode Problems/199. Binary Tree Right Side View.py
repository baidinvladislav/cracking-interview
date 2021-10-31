"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
"""


from Algorithms.leetcode_tree import buildTree, print_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional, List

from Algorithms.leetcode_tree import TreeNode


# incorrect solution 36 / 215 test cases passed.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        def _tree_traversal(node, values):
            if not node:
                return

            values.append(node.val)

            if not node.right and not node.left:
                return

            _tree_traversal(node.right, values)
            _tree_traversal(node.left, values)

        values = [root.val]
        _tree_traversal(root.right, values)
        return values


root_arr = [1, 2, 3, None, 5, None, 4]
root = buildTree(root_arr)
print_tree(root)
print(Solution().rightSideView(root))
