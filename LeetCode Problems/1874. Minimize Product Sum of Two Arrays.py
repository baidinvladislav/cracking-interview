"""
The product sum of two equal-length arrays a and b is equal to the sum of a[i] * b[i]
for all 0 <= i < a.length (0-indexed).

For example, if a = [1,2,3,4] and b = [5,2,3,1], the product sum would be 1*5 + 2*2 + 3*3 + 4*1 = 22.
Given two arrays nums1 and nums2 of length n,
return the minimum product sum if you are allowed to rearrange the order of the elements in nums1.
"""
from typing import List


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1.sort()
        nums2.sort()
        j = n - 1
        sum = 0

        for i in range(n):
            comp = nums1[i] * nums2[j]
            sum += comp
            j -= 1

        return sum


print(Solution().minProductSum(nums1=[5, 3, 4, 2], nums2=[4, 2, 2, 5]))
