"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_arr = nums[:n]
        y_arr = nums[n:]

        res = []
        i = 0
        while i < len(x_arr):
            res.append(x_arr[i])
            res.append(y_arr[i])
            i += 1

        return res


print(Solution().shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4))
