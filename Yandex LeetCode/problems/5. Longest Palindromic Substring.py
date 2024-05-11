class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = expandAroundCenter(i, i)  # Odd length palindromes
            left2, right2 = expandAroundCenter(i, i + 1)  # Even length palindromes

            if right1 - left1 > end - start:
                start = left1
                end = right1
            if right2 - left2 > end - start:
                start = left2
                end = right2

        return s[start:end+1]

# Example usage:
# sol = Solution()
# print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
# print(sol.longestPalindrome("cbbd"))   # Output: "bb"
