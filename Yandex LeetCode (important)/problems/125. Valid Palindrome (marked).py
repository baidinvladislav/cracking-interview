"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # def isPalindrome(self, s: str) -> bool:
    #     filtered_symbols = filter(lambda ch: ch.isalnum(), s)
    #     low_case = map(lambda ch: ch.lower(), filtered_symbols)
    #     result_list = list(low_case)
    #     return result_list == result_list[::-1]

    # Time complexity: O(n)
    # Space complexity: O(n)
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


print(Solution().isPalindrome(s="race a car"))
