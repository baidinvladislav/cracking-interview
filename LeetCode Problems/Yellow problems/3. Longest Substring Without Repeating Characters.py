"""
Given a string s, find the length of the longest substring without repeating characters.
"""


# it's work but i do not like code duplication
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
            else:
                if max_sub < len(output):
                    max_sub = len(output)

                idx = output.index(item)
                output = output[idx + 1:]
                output.append(item)

        else:
            if max_sub < len(output):
                max_sub = len(output)

        return max_sub


# print(Solution().lengthOfLongestSubstring(s="dvdf"))
# print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
# print(Solution().lengthOfLongestSubstring(s="pwwkew"))
# print(Solution().lengthOfLongestSubstring(s="au"))


# more elegant solution by LeetCode
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0

        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i - start)
                start = max(start, dic[ch] + 1)
            dic[ch] = i
        return max(res, len(s) - start)


print(Solution1().lengthOfLongestSubstring(s="pwwkew"))
