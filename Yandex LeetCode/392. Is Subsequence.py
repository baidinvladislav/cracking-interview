class Solution:
    # Approach 1: Divide and Conquer with Greedy
    # Time Complexity: O(T)
    # Space Complexity: O(T)
    def isSubsequence(self, s: str, t: str) -> bool:
        source_length, target_length = len(s), len(t)

        def rec_isSubsequence(left_index, right_index):
            # base cases
            if left_index == source_length:
                return True
            if right_index == target_length:
                return False

            # consume both strings or just the target string
            if s[left_index] == t[right_index]:
                left_index += 1
            right_index += 1
            return rec_isSubsequence(left_index, right_index)

        return rec_isSubsequence(0, 0)


def main():
    print(Solution().isSubsequence(s="abc", t="ahbgdc"))
    print(Solution().isSubsequence(s="axc", t="ahbgdc"))


if __name__ == '__main__':
    main()
