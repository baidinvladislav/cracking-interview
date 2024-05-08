from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        result = set()

        for num in s1:
            if num in s2:
                result.add(num)

        for num in s2:
            if num in s1:
                result.add(num)

        result = list(result)
        return result
