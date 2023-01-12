"""
https://www.youtube.com/watch?v=EIf9zFqufbU
"""
import unittest


class Solution:
    def countSubstrings(self, s):
        n = len(s)
        res = 0

        # create a matrix to store info about the substring
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # set single characters as palindromes
        idx = 0
        while idx < n:
            dp[idx][idx] = 1
            idx += 1
            res += 1

        for col in range(1, len(s)):
            for row in range(col):

                # every two chars are palindromes as well
                if row == col - 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1

                # to determine if substring is a palindrome you should know
                # a) if the inner substring is the palindrome and
                # b) if the outer characters match
                elif dp[row + 1][col - 1] == 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1

        # print matrix
        for line in dp:
            print(line)

        return res


class TestPalindromicSubstrings(unittest.TestCase):
    def test_first(self):
        self.assertEqual(3, Solution().countSubstrings(s="abc"))

    def test_second(self):
        self.assertEqual(6, Solution().countSubstrings(s="aaa"))


if __name__ == "__main__":
    unittest.main()
