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
        result = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    result = max(result, j - i + 1)
        return result


# Time: O(2n) = O(n)
# Space: O(min(n,m))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ascii_array = [0] * 128
        left = right = 0

        result = 0
        while right < len(s):
            last_character = s[right]
            index = ord(last_character)
            ascii_array[index] += 1

            while ascii_array[ord(last_character)] > 1:
                first_character = s[left]
                index = ord(first_character)
                ascii_array[index] -= 1
                left += 1

            result = max(result, right - left + 1)
            right += 1
        return result


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
