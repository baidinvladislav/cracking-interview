class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start, matched, frequency_map = 0, 0, {}

        for ch in s1:
            if ch not in frequency_map:
                frequency_map[ch] = 0
            frequency_map[ch] += 1

        for window_end in range(len(s2)):
            right_char = s2[window_end]
            if right_char in frequency_map:
                frequency_map[right_char] -= 1
                if frequency_map[right_char] == 0:
                    matched += 1

            if matched == len(frequency_map):
                return True

            if window_end >= len(s1) - 1:
                left_char = s2[window_start]
                if left_char in frequency_map:
                    if frequency_map[left_char] == 0:
                        matched -= 1
                    frequency_map[left_char] += 1
                window_start += 1

        return False


def main():
    print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))
    print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))


main()
