import unittest


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "[": "]", "{": "}"}

        stack = []
        for ch in s:
            if ch in d:
                stack.append(ch)
            else:
                if stack and d[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


class TestValidParentheses(unittest.TestCase):
    def test_first(self):
        self.assertTrue(Solution().isValid(s="()"))

    def test_second(self):
        self.assertTrue(Solution().isValid(s="{()([]{})}"))

    def test_third(self):
        self.assertFalse(Solution().isValid(s="(]"))


if __name__ == "__main__":
    unittest.main()
