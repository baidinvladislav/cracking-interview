"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        input = list(s)
        output = []
        max_sub = float('-inf')

        for item in input:
            if item not in output:
                output.append(item)
                if max_sub < len(output):
                    max_sub = len(output)
            else:
                if max_sub < len(output):
                    max_sub = len(output)

                idx = output.index(item)
                output = output[idx + 1:]
                output.append(item)

        return max_sub


# print(Solution().lengthOfLongestSubstring(s="dvdf"))
# print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
# print(Solution().lengthOfLongestSubstring(s="pwwkew"))
print(Solution().lengthOfLongestSubstring(s="au"))
