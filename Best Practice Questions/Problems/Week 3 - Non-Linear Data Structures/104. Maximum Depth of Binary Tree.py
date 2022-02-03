from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # bfs
    def maxDepth_bfs(self, root):
        level = 0
        if not root:
            return level

        queue = deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            level += 1
        return level

    # dfs
    def maxDepth_dfs(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth_dfs(root.left)
            right_height = self.maxDepth_dfs(root.right)
            return max(left_height, right_height) + 1
