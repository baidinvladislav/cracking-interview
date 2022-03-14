class Solution:
    # Approach 1: Divide and Conquer with Greedy
    # Time Complexity: O(T)
    # Space Complexity: O(T)
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False

        if s[0] == t[0]:
            s = s[1:]
        t = t[1:]

        return self.isSubsequence(s, t)

    # Approach 2: Two-Pointers
    # Time Complexity: O(T)
    # Space Complexity: O(1)
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
