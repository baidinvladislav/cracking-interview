import unittest


# Time: O(n**3)
# Space: O(min(n,m))
class BrutForceSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start, max_length, hash_map = 0, 0, dict()

        for window_end in range(len(s)):
            if s[window_end] in hash_map:
                window_start = max(window_start, hash_map[s[window_end]] + 1)

            hash_map[s[window_end]] = window_end
            max_length = max(max_length, window_end - window_start + 1)
        return max_length


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring(s="abcabcbb"))
        self.assertEqual(3, BrutForceSolution().lengthOfLongestSubstring(s="abcabcbb"))

    def test_second(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring(s="bbbbb"))
        self.assertEqual(1, BrutForceSolution().lengthOfLongestSubstring(s="bbbbb"))

    def test_third(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring(s="pwwkew"))
        self.assertEqual(3, BrutForceSolution().lengthOfLongestSubstring(s="pwwkew"))


if __name__ == "__main__":
    unittest.main()
