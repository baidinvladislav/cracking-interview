import unittest


class Solution:
    def isAnagramArray(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s, t = list(s), list(t)

        s.sort()
        t.sort()

        return s == t

    def isAnagramDict(self, s: str, t: str) -> bool:
        d1 = {}
        for char in s:
            if char not in d1:
                d1[char] = 0
            d1[char] += 1

        d2 = {}
        for char in t:
            if char not in d2:
                d2[char] = 0
            d2[char] += 1

        return d1 == d2


class TestTwoSum(unittest.TestCase):

    def test_first(self):
        expected = True
        self.assertEqual(expected, Solution().isAnagramArray(s="anagram", t="nagaram"))
        self.assertEqual(expected, Solution().isAnagramDict(s="anagram", t="nagaram"))

    def test_second(self):
        expected = False
        self.assertEqual(expected, Solution().isAnagramArray(s="rat", t="car"))
        self.assertEqual(expected, Solution().isAnagramDict(s="rat", t="car"))


if __name__ == "__main__":
    unittest.main()