"""
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
"""


# my solution
class Solution:
    def removeVowels(self, s: str) -> str:
        n = len(s)
        new_str = ''

        for i in range(n):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                continue
            else:
                new_str += s[i]
        return new_str


print(Solution().removeVowels(s="leetcodeisacommunityforcoders"))


# one line solution
class Solution1:
    def removeVowels(self, S):
        return "".join(c for c in S if c not in "aeiou")
