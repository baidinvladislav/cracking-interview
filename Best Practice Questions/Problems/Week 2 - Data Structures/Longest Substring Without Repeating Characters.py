import unittest


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

    def test_second(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring(s="bbbbb"))

    def test_third(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring(s="pwwkew"))


if __name__ == "__main__":
    unittest.main()
