# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
# and initial word order.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"


# Time: O(n + m)
# Space: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        left = right = 0
        while right <= len(s):
            while right < len(s) and s[right] != " ":
                right += 1

            start = left
            end = right - 1
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

            left = right + 1
            right = left

        return "".join(s)
