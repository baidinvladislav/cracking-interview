"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""
from typing import List


# with additional memory
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        buf = []
        for i in nums:
            if len(str(i)) % 2 == 0:
                buf.append(i)
        return len(buf)

    
print(Solution().findNumbers(nums = [12,345,2,6,7896]))


# memory O(1)
class Solution1:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n):
            if len(str(nums[i])) % 2 == 0:
                count += 1
                
        return count

    
print(Solution1().findNumbers(nums = [12,345,2,6,7896]))
