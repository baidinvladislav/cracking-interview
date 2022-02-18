import unittest
from collections import deque


class Solution:
    def isValid(self, s):
        hash_map = {'(': ')', '[': ']', '{': '}'}
        stack = deque()

        for char in s:
            if char in hash_map:
                stack.append(char)
            else:
                if not stack:
                    return False

                last_el = stack.pop()
                if hash_map[last_el] != char:
                    return False

        return not stack


class TestValidParentheses(unittest.TestCase):
    def test_first(self):
        self.assertTrue(Solution().isValid(s="()"))

    def test_second(self):
        self.assertTrue(Solution().isValid(s="{()([]{})}"))

    def test_third(self):
        self.assertFalse(Solution().isValid(s="(]"))


if __name__ == "__main__":
    unittest.main()
