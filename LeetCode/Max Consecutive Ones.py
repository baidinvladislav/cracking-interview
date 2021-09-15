"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        max_res = 0
        for i in nums:
            if i == 1:
                res += 1
            else:
                res = 0
            max_res = max(max_res, res)
        return max_res
