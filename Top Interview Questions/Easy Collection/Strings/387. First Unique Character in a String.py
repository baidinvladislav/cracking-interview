import unittest


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1


class TestTwoSum(unittest.TestCase):

    def test_first(self):
        expected = 0
        self.assertEqual(expected, Solution().firstUniqChar("leetcode"))

    def test_second(self):
        expected = 2
        self.assertEqual(expected, Solution().firstUniqChar("loveleetcode"))

    def test_third(self):
        expected = -1
        self.assertEqual(expected, Solution().firstUniqChar("aabb"))


if __name__ == "__main__":
    unittest.main()
