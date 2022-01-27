class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        1. Insert pattern characters to Python dictionary.
        2. Extend the window if the last window character in dictionary then decrement their frequency.
        3. If after decrement last character frequency it will be equal 0. We got one match.
        4. While number matches equal number character in pattern we shrink the window and update window start index.
        """
        window_start, matched, substr_start = 0, 0, 0
        min_length = len(s) + 1
        char_frequency = {}

        for chr in t:
            if chr not in char_frequency:
                char_frequency[chr] = 0
            char_frequency[chr] += 1

        # try to extend the range [window_start, window_end]
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_frequency:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] >= 0:  # Count every matching of a character
                    matched += 1

            # Shrink the window if we can, finish as soon as we remove a matched character
            while matched == len(t):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    substr_start = window_start

                left_char = s[window_start]
                window_start += 1
                if left_char in char_frequency:
                    # Note that we could have redundant matching characters, therefore we'll decrement the
                    # matched count only when a useful occurrence of a matched character is going out of the window
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        if min_length > len(s):
            return ""

        return s[substr_start:substr_start + min_length]
