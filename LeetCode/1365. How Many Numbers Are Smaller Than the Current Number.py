"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            counter = 0
            for j in nums:
                if i > j:
                    counter += 1
            else:
                res.append(counter)
        return res


print(Solution().smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))
