# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Example 1:
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15

# Example 2:
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        level_sums = []
        while queue:
            node_on_levels = len(queue)
            level_sum = 0
            for _ in range(node_on_levels):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level_sums.append(level_sum)
        return level_sums[-1]
