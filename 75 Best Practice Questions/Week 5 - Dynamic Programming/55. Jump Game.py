class Solution:
    def canJump(self, nums):
        length = len(nums)
        dp = [0] * length

        dp[0] = nums[0]

        for i in range(1, length - 1):
            if dp[i - 1] < i:
                return False

            dp[i] = max(i + nums[i], dp[i - 1])

            if dp[i] >= length - 1:
                return True

        return dp[length - 2] >= length - 1


# print(Solution().canJump(nums=[2, 3, 1, 1, 4]))  # True
print(Solution().canJump(nums=[3, 2, 1, 0, 4]))  # False
