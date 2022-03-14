class Solution:
    # Approach 1: Divide and Conquer with Greedy
    # Time Complexity: O(T)
    # Space Complexity: O(T)
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = 0
        while True:
            if left == len(s):
                return True
            if right == len(t):
                return False

            if s[left] == t[right]:
                left += 1
            right += 1


def main():
    print(Solution().isSubsequence(s="abc", t="ahbgdc"))
    print(Solution().isSubsequence(s="axc", t="ahbgdc"))


if __name__ == '__main__':
    main()
