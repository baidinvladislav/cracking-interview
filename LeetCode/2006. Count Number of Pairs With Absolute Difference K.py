"""
Given an integer array nums and an integer k,
return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
"""
from itertools import permutations
from typing import List


# O(N^2)
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pairs = 0
        for i in range(n):
            for j in range(n):
                if nums[i] - nums[j] == k:
                    pairs += 1
        return pairs


print(Solution().countKDifference(nums=[3, 2, 1, 5, 4], k=2))


# O(N)
class Solution1:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i, j in permutations(nums, 2):
            if (i - j) == k:
                count += 1
        return count


print(Solution1().countKDifference(nums=[3, 2, 1, 5, 4], k=2))
