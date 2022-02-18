import unittest


class Solution:
    def isAnagram_sorting(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram_additional_memory(self, s: str, t: str) -> bool:
        buffer_1, buffer_2 = {}, {}
        for char in s:
            buffer_1[char] = buffer_1.get(char, 0) + 1

        for char in t:
            buffer_2[char] = buffer_2.get(char, 0) + 1

        return buffer_1 == buffer_2


class TestValidAnagram(unittest.TestCase):
    def test_first(self):
        self.assertTrue(5, Solution().isAnagram_sorting(s="anagram", t="nagaram"))
        self.assertTrue(5, Solution().isAnagram_additional_memory(s="anagram", t="nagaram"))

    def test_second(self):
        self.assertFalse(0, Solution().isAnagram_sorting(s="rat", t="car"))
        self.assertFalse(0, Solution().isAnagram_additional_memory(s="rat", t="car"))


if __name__ == "__main__":
    unittest.main()
