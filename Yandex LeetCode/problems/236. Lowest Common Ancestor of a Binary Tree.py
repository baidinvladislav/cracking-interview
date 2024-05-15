# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


# Approach 1: Recursive Approach
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right


root = TreeNode(3)

root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)


p, q = TreeNode(5), TreeNode(1)
print(Solution().lowestCommonAncestor(root=root, p=p, q=q))


# Approach 2: Iterative using parent pointers
# Time Complexity: O(N)
# Space Complexity: O(N)
# class Solution:
#     def __init__(self):
#         # Variable to store LCA node.
#         self.ans = None
#
#     def lowestCommonAncestor(self, root, p, q):
#         # Stack for tree traversal
#         stack = [root]
#
#         # Dictionary for parent pointers
#         parent = {root: None}
#
#         # Iterate until we find both the nodes p and q
#         while p not in parent or q not in parent:
#             node = stack.pop()
#
#             # While traversing the tree, keep saving the parent pointers.
#             if node.left:
#                 parent[node.left] = node
#                 stack.append(node.left)
#
#             if node.right:
#                 parent[node.right] = node
#                 stack.append(node.right)
#
#         # Ancestors set() for node p.
#         ancestors = set()
#
#         # Process all ancestors for node p using parent pointers.
#         while p:
#             ancestors.add(p)
#             p = parent[p]
#
#         # The first ancestor of q which appears in
#         # p's ancestor set() is their lowest common ancestor.
#         while q not in ancestors:
#             q = parent[q]
#
#         return q
#
#
# root = TreeNode(3)
#
# root.left = TreeNode(5)
# root.left.left = TreeNode(6)
# root.left.right = TreeNode(2)
# root.left.right.left = TreeNode(7)
# root.left.right.right = TreeNode(4)
#
# root.right = TreeNode(1)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(8)
#
#
# p, q = TreeNode(5), TreeNode(1)
# print(Solution().lowestCommonAncestor(root=root, p=p, q=q))
