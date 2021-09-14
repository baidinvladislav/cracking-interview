"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        buffer = {}
        for i in nums:
            if i in buffer:
                return True
            else:
                buffer[i] = 1
        return False


s = Solution()
print(s.containsDuplicate([1,2,3,1]))
