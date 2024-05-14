"""
Определить что две строки изоморфны.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
"""


# Time Complexity: O(len(s))
# Space Complexity: O(len(s) + len(t)) => O(len(s)): because len(s) == len(t)
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
