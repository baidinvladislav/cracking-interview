from typing import List


# Approach 1: Recursion with Memoization
class Solution:

    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.robFrom(0, nums)

    def robFrom(self, i, nums):
        # No more houses left to examine.
        if i >= len(nums):
            return 0

        # Return cached value.
        if i in self.memo:
            return self.memo[i]

        # Recursive relation evaluation to get the optimal answer.
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])

        # Cache for future use.
        self.memo[i] = ans
        return ans


print(Solution().rob(nums=[1, 2, 3, 1]))


# Approach 2: Dynamic Programming
class Solution:

    def rob(self, nums: List[int]) -> int:
        # Special handling for empty case.
        if not nums:
            return 0

        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        n = len(nums)

        # Base case initialization.
        maxRobbedAmount[n], maxRobbedAmount[n - 1] = 0, nums[n - 1]

        # DP table calculations.
        for i in range(n - 2, -1, -1):
            # Same as recursive solution.
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])

        return max(maxRobbedAmount)


print(Solution().rob(nums=[1, 2, 3, 1]))
