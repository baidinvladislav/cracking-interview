import unittest
from collections import deque


class Solution:
    def isValid(self, s):
        parentheses = {'(': ')', '{': '}', '[': ']'}
        stack = deque()

        for symbol in s:
            if symbol in parentheses:
                stack.append(symbol)

            elif len(stack) == 0 or parentheses[stack.pop()] != symbol:
                return False

        return len(stack) == 0


class TestContainsDuplicate(unittest.TestCase):
    def test_first(self):
        self.assertTrue(Solution().isValid(s="()"))

    def test_second(self):
        self.assertTrue(Solution().isValid(s="()[]{}"))

    def test_third(self):
        self.assertFalse(Solution().isValid(s="(]"))


if __name__ == "__main__":
    unittest.main()
