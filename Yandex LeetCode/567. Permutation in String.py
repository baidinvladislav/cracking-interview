class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))
        window = ''

        for char in s2:
            # increase the window (equivalent to adding the next character to current string)
            window += char

            # start doing business once the window size is size of target_string
            if len(window) == len(s1):
                # sort the current string and check if it equals the target_string
                if ''.join(sorted(window)) == s1:
                    return True

                # shrink the window for next iteration (remove the leftmost character)
                window = window[1:]

        # we couldn't find a permutation in the string, return False
        return False


def main():
    print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))
    print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))


main()
