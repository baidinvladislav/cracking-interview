# Approach 3: Dynamic Programming
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1

        # create dp table
        dp_table = [0 for _ in range(n + 1)]

        # fill db table with base cases
        dp_table[1] = 1
        dp_table[2] = 2

        for i in range(3, n + 1):
            dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

        return max(dp_table)


print(Solution().climbStairs(3))
