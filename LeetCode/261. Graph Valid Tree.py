"""
You have a graph of n nodes labeled from 0 to n - 1.
You are given an integer n and a list of edges where edges[i] = [ai, bi]
indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
"""
from typing import List


class UnionFind:

    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1] * n

    def find(self, A):
        root = A
        while root != self.parent[root]:
            root = self.parent[root]

        while A != root:
            old_root = self.parent[A]
            self.parent[A] = root
            A = old_root
        return root

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)

        if root_A == root_B:
            return False

        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        unionFind = UnionFind(n)

        for A, B in edges:
            if not unionFind.union(A, B):
                return False

        return True


print(Solution().validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))
