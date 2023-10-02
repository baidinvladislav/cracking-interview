# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_map = Counter(s1)

        start = 0
        for end in range(len(s2)):
            while start <= end and (s2[end] not in hash_map or hash_map[s2[end]] <= 0):
                if start <= end and s2[start] in hash_map:
                    hash_map[s2[start]] += 1
                start += 1

            hash_map[s2[end]] -= 1

            if all(val <= 0 for val in hash_map.values()):
                return True

        return False
