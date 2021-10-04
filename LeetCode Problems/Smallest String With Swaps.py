"""
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b]
indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
"""
from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n):
                self.p = list(range(n))

            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)

            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

        uf, res, m = UF(len(s)), [], defaultdict(list)

        for x, y in pairs:
            uf.union(x, y)

        for i in range(len(s)):
            m[uf.find(i)].append(s[i])

        for comp_id in m.keys():
            m[comp_id].sort(reverse=True)

        for i in range(len(s)):
            res.append(m[uf.find(i)].pop())

        return ''.join(res)


print(Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]))
