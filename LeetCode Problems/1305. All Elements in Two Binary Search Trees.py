"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import List

from Algorithms.leetcode_tree import TreeNode, buildTree


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result_1 = []
        result_2 = []

        def dfs(node, result_arr):
            if not node:
                return

            dfs(node.left, result_arr)
            result_arr.append(node.val)
            dfs(node.right, result_arr)

        dfs(root1, result_1)
        dfs(root2, result_2)

        answer = []
        i, j = 0, 0
        while i < len(result_1) and j < len(result_2):

            if result_1[i] <= result_2[j]:
                answer.append(result_1[i])
                i += 1
            else:
                answer.append(result_2[j])
                j += 1

        if j != len(result_2):
            answer += result_2[j:]

        if i != len(result_1):
            answer += result_1[i:]

        return answer


root_arr1 = [2, 1, 4]
root_arr2 = [1, 0, 3]
root1 = buildTree(root_arr1)
root2 = buildTree(root_arr2)
print(Solution().getAllElements(root1, root2))
