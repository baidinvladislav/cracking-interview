"""
Given a string s, return the length of the longest substring
that contains at most two distinct characters.
"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        window_start = 0
        max_length = float('-inf')
        hash_map = {}

        for window_end in range(len(s)):
            if s[window_end] not in hash_map:
                hash_map[s[window_end]] = 0
            hash_map[s[window_end]] += 1

            while len(hash_map) > 2:
                hash_map[s[window_start]] -= 1
                if hash_map[s[window_start]] == 0:
                    del hash_map[s[window_start]]
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length


print(Solution().lengthOfLongestSubstringTwoDistinct(s="ccaabbb"))
