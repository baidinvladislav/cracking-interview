"""
Find the minimum depth of a binary tree.
The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_maximum_depth(root):
    if not root:
        return 0

    queue = deque()
    queue.append(root)
    tree_depth = 0
    while queue:
        level_size = len(queue)
        tree_depth += 1
        for _ in range(level_size):
            current_node = queue.popleft()

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

    return tree_depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))


main()
