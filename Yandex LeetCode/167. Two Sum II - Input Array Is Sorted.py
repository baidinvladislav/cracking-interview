"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while low < high:
            attempt = numbers[low] + numbers[high]

            if attempt == target:
                return [low + 1, high + 1]

            elif attempt < target:
                low += 1

            elif attempt > target:
                high -= 1

        return [-1, -1]


print(Solution().twoSum(numbers=[5, 25, 75], target=100))
