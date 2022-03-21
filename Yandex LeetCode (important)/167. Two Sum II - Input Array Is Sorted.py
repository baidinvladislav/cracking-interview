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
    # Time complexity : O(n)
    # Space complexity : O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two pointer approach.
        1. Set left pointer to the beginning of the array and left pointer in the end.
        2. If current sum less than `target` so increase left pointer to select greater integer.
        3. If current sum greater than `target` so decrease right pointer to select less integer.
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
        return [-1, -1]


print(Solution().twoSum(numbers=[5, 25, 75], target=100))
