from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start_window = 0
        freq_map = defaultdict(int)
        result = 0

        for end_window in range(len(s)):
            freq_map[s[end_window]] += 1

            while len(freq_map) > k:
                freq_map[s[start_window]] -= 1
                if freq_map[s[start_window]] == 0:
                    del freq_map[s[start_window]]
                start_window += 1

            result = max(result, end_window - start_window + 1)

        return result
