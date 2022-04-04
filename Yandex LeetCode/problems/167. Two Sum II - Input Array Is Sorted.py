from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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
