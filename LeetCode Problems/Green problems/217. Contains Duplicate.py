"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False


def main():
    print(Solution().containsDuplicate(nums=[1, 2, 3, 1]))
    print(Solution().containsDuplicate(nums=[1, 2, 3, 4]))
    print(Solution().containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


main()
