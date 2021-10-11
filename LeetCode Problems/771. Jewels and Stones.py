"""
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""


# O(N*N)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew = 0

        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    jew += 1

        return jew


print(Solution().numJewelsInStones(jewels="aA", stones="aAAbbbb"))


# O(N)
class Solution1:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = list(jewels)
        s = list(stones)
        res = 0

        for ch in s:
            if ch in j:
                res += 1

        return res


print(Solution1().numJewelsInStones(jewels="aA", stones="aAAbbbb"))
