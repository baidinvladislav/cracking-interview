"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


# 1. Отделить все буквенно-цифровые символы
# 2. Привести все символы к нижнему регистру
# 3. Сравнить два среза [:], [::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_symbols = filter(lambda ch: ch.isalnum(), s)
        low_case = map(lambda ch: ch.lower(), filtered_symbols)
        result_list = list(low_case)
        return result_list == result_list[::-1]


print(Solution().isPalindrome(s="race a car"))
