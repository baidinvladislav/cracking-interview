"""
There are n people in a social group labeled from 0 to n - 1.
You are given an array logs where logs[i] = [timestampi, xi, yi] indicates
that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a.
Also, person a is acquainted with a person b if a is friends with b,
or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person.
If there is no such earliest time, return -1.
"""


class Solution:
    def earliestAcq(self, logs, N):
        uf = {x: x for x in range(N)}
        self.groups = N

        def merge(x, y):
            x, y = find(x), find(y)
            if x != y:
                self.groups -= 1
                uf[x] = y

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        for t, x, y in sorted(logs):
            merge(x, y)
            if self.groups == 1:
                return t
        return -1


print(Solution().earliestAcq(
    logs=[
        [20190101, 0, 1],
        [20190104, 3, 4],
        [20190107, 2, 3],
        [20190211, 1, 5],
        [20190224, 2, 4],
        [20190301, 0, 3],
        [20190312, 1, 2],
        [20190322, 4, 5]
    ],
    N=6
))
