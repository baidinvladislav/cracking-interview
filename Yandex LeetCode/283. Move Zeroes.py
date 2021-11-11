"""
Given an integer array nums, move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    def moveZeroes(self, nums):
        pointer = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1


print(Solution().moveZeroes(nums=[0, 1, 0, 3, 12]))
