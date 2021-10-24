"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples)
"""


# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children


from typing import List


class Solution:
    # Recursive solution
    def dfs(self, root, visited):
        if root not in visited:
            for children in root.children:
                self.dfs(children, visited)
            visited.append(root)

    def postorder(self, root):
        if not root:
            return []
        visited = list()
        self.dfs(root, visited)
        sol = [x.val for x in visited]
        return sol

    # Non-recursive solution
    def postorder1(self, root: 'Node') -> List[int]:
        sol = []
        if root:
            stack = [root]
            while stack:
                curr_node = stack.pop()
                sol.append(curr_node.val)
                for children in curr_node.children:
                    stack.append(children)
        return sol[::-1]


print(Solution().postorder(root=[1, None, 3, 2, 4, None, 5, 6]))
