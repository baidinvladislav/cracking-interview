# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict

        def serialize(node):
            if not node:
                return "#"
            # Create a unique string for the current subtree
            serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            # Count the occurrence of this serialization
            count[serial] += 1
            # If this serialization occurs exactly twice, we add it to the result
            if count[serial] == 2:
                result.append(node)
            return serial

        count = defaultdict(int)
        result = []
        serialize(root)
        return result
