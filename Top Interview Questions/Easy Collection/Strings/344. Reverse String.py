import unittest
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1


class TestTwoSum(unittest.TestCase):

    def test_first(self):
        expected = ["o", "l", "l", "e", "h"]
        self.assertEqual(expected, Solution().reverseString(["h", "e", "l", "l", "o"]))

    def test_second(self):
        expected = ["h", "a", "n", "n", "a", "H"]
        self.assertEqual(expected, Solution().reverseString(["H", "a", "n", "n", "a", "h"]))

    def test_third(self):
        expected = ["d", "s", "a"]
        self.assertEqual(expected, Solution().reverseString(["a", "s", "d"]))


if __name__ == "__main__":
    unittest.main()
