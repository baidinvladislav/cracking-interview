"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit
from node i (i.e., there is a directed edge from node i to node graph[i][j]).
"""
from collections import deque
from typing import List


# My unfinished decision
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        g = {x: None for x in range(n)}
        paths = []
        for i in range(n):
            g[i] = graph[i]

        def recurs(vertex, linked_vertex, paths):
            if vertex == n - 1:
                return paths

            for i in linked_vertex:
                paths.append(i)
                recurs(vertex=i, linked_vertex=g[i], paths=paths)

        for i in range(n):
            paths.append(i)
            paths.append(recurs(vertex=i, linked_vertex=graph[i], paths=paths))

        return paths


print(Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))


# backtracking algorithm
class Solution1:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        results = []

        def backtrack(currNode, path):
            # if we reach the target, no need to explore further.
            if currNode == target:
                results.append(list(path))
                return
            # explore the neighbor nodes one after another.
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()
        # kick of the backtracking, starting from the source node (0).
        path = deque([0])
        backtrack(0, path)

        return results


print(Solution1().allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))
