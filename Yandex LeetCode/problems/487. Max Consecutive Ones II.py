from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window_start = 0
        result = 0
        zeroes = 0

        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                zeroes += 1

            while zeroes > 1:
                if nums[window_start] == 0:
                    zeroes -= 1
                window_start += 1

            result = max(result, window_end - window_start + 1)

        return result
