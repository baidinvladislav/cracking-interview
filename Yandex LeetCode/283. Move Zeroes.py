"""
Given an integer array nums, move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    def moveZeroes(self, nums):
        pos = 0

        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        return nums


print(Solution().moveZeroes(nums=[0, 1, 0, 3, 12]))
