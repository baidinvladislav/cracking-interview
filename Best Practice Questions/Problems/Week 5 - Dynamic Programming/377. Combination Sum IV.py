from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for comb_sum in range(target + 1):
            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum - num]
                else:
                    break
        return dp[target]


print(Solution().combinationSum4(nums=[1, 2, 3], target=4))
