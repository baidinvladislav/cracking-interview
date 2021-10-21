"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges,
where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex start to vertex end.

Given edges and the integers n, start, and end, return true if there is a valid path from start to end,
or false otherwise.
"""
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = self.buildGraph(edges)
        visited = set()
        return self.hasPath(graph, start, end, visited)

    def buildGraph(self, edges):
        graph = {}

        for edge in edges:
            a, b = edge

            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            graph[a].append(b)
            graph[b].append(a)

        return graph

    def hasPath(self, graph, start, end, visited):
        if start == end:
            return True

        if start in visited:
            return False

        visited.add(start)
        for neighbour in graph[start]:
            if self.hasPath(graph, neighbour, end, visited) == True:
                return True
        return False


print(Solution().validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], start=0, end=2))
