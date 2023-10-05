# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] not in dict1 and t[i] not in dict2:
                dict1[s[i]] = t[i]
                dict2[t[i]] = s[i]
            else:
                if dict1.get(s[i]) != t[i] or dict2.get(t[i]) != s[i]:
                    return False

        return True
