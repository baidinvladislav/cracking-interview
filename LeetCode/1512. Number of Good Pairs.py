"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
from typing import List


# Time: O(N^2)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        good_pairs = 0

        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1
        return good_pairs


# Time: 0(N)
class Solution1:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        res = 0
        for number in nums:
            if number in hash_map:
                res += hash_map[number]
                hash_map[number] += 1
            else:
                hash_map[number] = 1
        return res


print(Solution1().numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
