"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional, List

from Algorithms.leetcode_tree import TreeNode, buildTree


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]

        result = []

        def dfs(root, path):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                result.append(path)
                return
            dfs(root.left, path + '->')
            dfs(root.right, path + '->')

        dfs(root, "")
        return result


root_arr = [1, 2, 3, None, 5]
root = buildTree(root_arr)
print(Solution().binaryTreePaths(root))
