"""
There is an undirected star graph consisting of n nodes labeled from 1 to n.
A star graph is a graph where there is one center node and exactly n - 1 edges
that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that
there is an edge between the nodes ui and vi. Return the center of the given star graph.
"""
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        center = None
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            center = edges[0][0]
        else:
            center = edges[0][1]
        return center


print(Solution().findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]))
