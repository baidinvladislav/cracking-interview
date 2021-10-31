from typing import Optional, List

from Algorithms.leetcode_tree import TreeNode


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def in_order_tree_traversal(root: Optional[TreeNode]) -> List[int]:
    def _in_order_traversal(node, values):
        if not node:
            return

        _in_order_traversal(node.left, values)
        values.append(node.val)
        _in_order_traversal(node.right, values)

    values = []
    _in_order_traversal(root, values)
    return values


def _pre_order_tree_traversal(root: Optional[TreeNode]) -> List[int]:
    def _pre_order_traversal(node, values):

        if not node:
            return

        values.append(node.val)
        _pre_order_traversal(node.left, values)
        _pre_order_traversal(node.right, values)

    values = []
    _pre_order_traversal(root, values)
    return values


def post_order_tree_traversal(root: Optional[TreeNode]) -> List[int]:
    def _post_order_traversal(node, values):
        if not node:
            return

        _post_order_traversal(node.left, values)
        _post_order_traversal(node.right, values)
        values.append(node.val)

    values = []
    _post_order_traversal(root, values)
    return values
