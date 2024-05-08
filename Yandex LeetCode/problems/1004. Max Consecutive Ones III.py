from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        zeroes = 0
        result = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[start] == 0:
                    zeroes -= 1
                start += 1

            result = max(result, end - start + 1)

        return result
