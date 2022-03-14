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


def main():
    print(Solution().isSubsequence(s="abc", t="ahbgdc"))
    print(Solution().isSubsequence(s="axc", t="ahbgdc"))


if __name__ == '__main__':
    main()
