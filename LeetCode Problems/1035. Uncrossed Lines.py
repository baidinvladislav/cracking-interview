"""
You are given two integer arrays nums1 and nums2.
We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect
 even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.
"""
from typing import List


# date: 19.10.21
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        pairs = 0
        last_added_idx = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and i >= j >= last_added_idx:
                    last_added_idx = j
                    pairs += 1

        return pairs


print(Solution().maxUncrossedLines(nums1=[2, 5, 1, 2, 5], nums2=[10, 5, 2, 1, 5, 2]))


class Solution1:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        matrix_row = [0] * len(nums2)

        for num1 in nums1:
            top_left = 0
            for i, num2 in enumerate(nums2):
                max_value = matrix_row[i]

                if num1 == num2 and top_left >= max_value:
                    max_value = top_left + 1

                if i and matrix_row[i-1] > max_value:
                    max_value = matrix_row[i-1]

                top_left = matrix_row[i]
                matrix_row[i] = max_value

        return matrix_row[-1]


print(Solution1().maxUncrossedLines(nums1=[2, 5, 1, 2, 5], nums2=[10, 5, 2, 1, 5, 2]))
