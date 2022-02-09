from typing import List
from collections import deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        # Create an adjacency list.
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        # We still need a seen set to prevent our code from infinite
        # looping if there *is* cycles (and on the trivial cycles!)
        seen = {0}
        queue = deque([0])

        while queue:
            node = queue.popleft()
            for neighbour in adj_list[node]:
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                queue.append(neighbour)

        return len(seen) == n


# print(Solution().validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(Solution().validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))
print(Solution().validTree(n=4, edges=[[0, 1], [2, 3]]))
