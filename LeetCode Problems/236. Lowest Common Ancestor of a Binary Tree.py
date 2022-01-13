"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from Algorithms.leetcode_tree import TreeNode, buildTree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        in_order_tr = []

        def dfs(node, value_list):
            if not node:
                return

            dfs(node.left, value_list)
            dfs(node.right, value_list)
            value_list.append(node.val)

        dfs(root, in_order_tr)
        return in_order_tr


root_arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = buildTree(root_arr)
print(Solution().lowestCommonAncestor(root=root, p=TreeNode(5), q=TreeNode(1)))
