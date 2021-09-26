"""
You have a graph of n nodes.

You are given an integer n and an array edges where edges[i] = [ai, bi] indicates
that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
"""


# BFS
class Solution:
    def countComponents(self, n, edges):
        g = {x: [] for x in range(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ret = 0
        for i in range(n):
            queue = [i]
            ret += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]

        return ret


print(Solution().countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]]))
