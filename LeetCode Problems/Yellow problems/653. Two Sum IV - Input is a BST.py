"""
Given the root of a Binary Search Tree and a target number k,
return true if there exist two elements in the BST such that their sum is equal to the given target.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from Algorithms.leetcode_tree import buildTree


class Solution:
    def findTarget(self, root, k):
        if not root:
            return False

        queue, visited = [root], set()
        for node in queue:
            if k - node.val in visited:
                return True

            visited.add(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False


root_arr = [5, 3, 6, 2, 4, None, 7]
# root_arr = [2, None, 3]
# root_arr = [334, 277, 507, None, 285, None, 678]
root = buildTree(root_arr)
print(Solution().findTarget(root=root, k=9))
