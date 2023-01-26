import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


class TestTwoSum(unittest.TestCase):

    def test_first(self):
        expected = True
        self.assertEqual(expected, Solution().isPalindrome("A man, a plan, a canal: Panama"))

    def test_second(self):
        expected = False
        self.assertEqual(expected, Solution().isPalindrome("race a car"))

    def test_third(self):
        expected = True
        self.assertEqual(expected, Solution().isPalindrome(" "))


if __name__ == "__main__":
    unittest.main()