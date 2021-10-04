"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums = [i * i for i in nums]
        squared_nums.sort()
        return squared_nums
