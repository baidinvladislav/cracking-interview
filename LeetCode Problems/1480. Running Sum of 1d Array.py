"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            result.append(total)
        return result


print(Solution().runningSum([1, 2, 3, 4]))
