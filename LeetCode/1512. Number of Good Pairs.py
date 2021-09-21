"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        good_pairs = 0

        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1
        return good_pairs


print(Solution().numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
