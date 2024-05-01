import unittest
from collections import defaultdict


# Time: O(n**3)
# Space: O(min(n,m))
class BrutForceSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(n):
            for j in range(i, n):
                if self.check(s, i, j):
                    result = max(result, j - i + 1)
        return result

    def check(self, string, start, end):
        ascii_array = [0] * 128

        for i in range(start, end + 1):
            char = string[i]
            # The ord() function returns the number
            # representing the unicode code of a specified character.
            ascii_array[ord(char)] += 1
            if ascii_array[ord(char)] > 1:
                return False
        return True


# Time: O(2n) = O(n)
# Space: O(min(n,m))
class WindowSlidingSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ascii_array = [0] * 128
        window_start = window_end = 0
        result = 0
        while window_end < len(s):
            last_symbol = s[window_end]
            # The ord() function returns the number
            # representing the unicode code of a specified character.
            symbol_unicode = ord(last_symbol)
            ascii_array[symbol_unicode] += 1

            while ascii_array[ord(last_symbol)] > 1:
                first_symbol = s[window_start]
                symbol_unicode = ord(first_symbol)
                ascii_array[symbol_unicode] -= 1
                window_start += 1

            result = max(result, window_end - window_start + 1)
            window_end += 1
        return result


# Time complexity: O(n). Index j will iterate n times.
# Space complexity: O(m). m is the size of the charset.
class OptimizedWindowSlidingSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        d = defaultdict(int)

        result = 0
        for end in range(len(s)):
            d[s[end]] += 1

            while len(d) != end - start + 1:
                d[s[start]] -= 1
                if d[s[start]] == 0:
                    del d[s[start]]
                start += 1

            result = max(result, end - start + 1)

        return result


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual(3, BrutForceSolution().lengthOfLongestSubstring(s="abcabcbb"))
        self.assertEqual(3, WindowSlidingSolution().lengthOfLongestSubstring(s="abcabcbb"))
        self.assertEqual(3, OptimizedWindowSlidingSolution().lengthOfLongestSubstring(s="abcabcbb"))

    def test_second(self):
        self.assertEqual(1, BrutForceSolution().lengthOfLongestSubstring(s="bbbbb"))
        self.assertEqual(1, WindowSlidingSolution().lengthOfLongestSubstring(s="bbbbb"))
        self.assertEqual(1, OptimizedWindowSlidingSolution().lengthOfLongestSubstring(s="bbbbb"))

    def test_third(self):
        self.assertEqual(3, BrutForceSolution().lengthOfLongestSubstring(s="pwwkew"))
        self.assertEqual(3, WindowSlidingSolution().lengthOfLongestSubstring(s="pwwkew"))
        self.assertEqual(3, OptimizedWindowSlidingSolution().lengthOfLongestSubstring(s="pwwkew"))


if __name__ == "__main__":
    unittest.main()
