class Solution:
    def countComponents(n, edges):
        def dfs(n, g, visited):

            if visited[n]:
                return

            visited[n] = 1
            for x in g[n]:
                dfs(x, g, visited)

        visited = [0] * n
        g = {x: [] for x in range(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ret = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, g, visited)
                ret += 1

        return ret
