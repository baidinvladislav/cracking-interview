"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such
that every key of the original BST is changed to the original key plus the sum
of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

* The left subtree of a node contains only nodes with keys less than the node's key.
* The right subtree of a node contains only nodes with keys greater than the node's key.
* Both the left and right subtrees must also be binary search trees.
"""
from Algorithms.leetcode_tree import TreeNode, buildTree, print_tree


# date: 19.10.21
class Solution:

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            self.inorder.append(node)
            self._inorder_traversal(node.right)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.inorder = []
        self._inorder_traversal(root)

        n = len(self.inorder)
        cur = self.inorder[-1].val
        cumsum = [cur]

        for i in range(n - 2, -1, -1):
            cur = cur + self.inorder[i].val
            cumsum.append(cur)

        for i, node in enumerate(self.inorder):
            node.val = node.val + cumsum[n - 1 - i]

        return root


if __name__ == '__main__':
    root_arr = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    root = buildTree(root_arr)
    # print_tree(root)
    print(Solution().bstToGst(root))
    # print_tree(root)
