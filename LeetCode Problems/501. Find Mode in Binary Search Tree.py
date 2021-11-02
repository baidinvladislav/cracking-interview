"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e.,
the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        if root.left is None and root.right is None:
            return [root.val]

        def dfs(node, arr):
            if not node:
                return

            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)

        values = []
        dfs(root, values)

        hash_map = {}
        for i in range(len(values)):
            if values[i] in hash_map:
                hash_map[values[i]] += 1
            else:
                hash_map[values[i]] = 1

        max_value = float('-inf')
        for key in hash_map.keys():
            if hash_map[key] > max_value:
                max_value = hash_map[key]

        result = []
        for key in hash_map.keys():
            if hash_map[key] == max_value:
                result.append(key)

        return result


# root_arr = [2, None, 3, None, 4, None, 5, None, 6]
# root_arr = [1, None, 2, 2]
root_arr = [1, 0, 1, 0, 0, 1, 1, 0]
root = buildTree(root_arr)
print(Solution().findMode(root))
