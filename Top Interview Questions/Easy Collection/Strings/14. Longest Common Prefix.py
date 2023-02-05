import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        end = min(len(strs[0]), len(strs[len(strs) - 1]))
        result = ""
        counter = 0
        while counter < end and strs[0][counter] == strs[len(strs) - 1][counter]:
            result += strs[0][counter]
            counter += 1

        return result


class TestTwoSum(unittest.TestCase):

    def test_first(self):
        expected = "fl"
        self.assertEqual(expected, Solution().longestCommonPrefix(["flower", "flow", "flight"]))

    def test_second(self):
        expected = ""
        self.assertEqual(expected, Solution().longestCommonPrefix(["dog", "racecar", "car"]))


if __name__ == "__main__":
    unittest.main()
