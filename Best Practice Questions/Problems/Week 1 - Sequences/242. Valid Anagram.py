import unittest
from collections import defaultdict


class Solution:
    def isAnagram_sorting(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram_additional_memory(self, s: str, t: str) -> bool:
        d1, d2 = defaultdict(int), defaultdict(int)
        for key in s:
            d1[key] += 1

        for key in t:
            d2[key] += 1

        return d1 == d2


class TestValidAnagram(unittest.TestCase):
    def test_first(self):
        self.assertTrue(5, Solution().isAnagram_sorting(s="anagram", t="nagaram"))
        self.assertTrue(5, Solution().isAnagram_additional_memory(s="anagram", t="nagaram"))

    def test_second(self):
        self.assertFalse(0, Solution().isAnagram_sorting(s="rat", t="car"))
        self.assertFalse(0, Solution().isAnagram_additional_memory(s="rat", t="car"))


if __name__ == "__main__":
    unittest.main()
