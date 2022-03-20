"""
Даны две строки строчных латинских символов: строка J и строка S.
Символы, входящие в строку J, — «драгоценности», входящие в строку S — «камни».
Нужно определить, какое количество символов из S одновременно являются «драгоценностями».
Проще говоря, нужно проверить, какое количество символов из S входит в J.
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
