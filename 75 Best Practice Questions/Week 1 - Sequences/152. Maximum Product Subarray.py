import unittest
from typing import List


class Solution:

    # Time Complexity: O(n**2)
    # Space Complexity: O(1)
    def maxProductBruteForce(self, nums: List[int]) -> int:
        max_multiple = nums[0]
        for i in range(len(nums)):
            multiple = 1
            for j in range(i, len(nums)):
                multiple *= nums[j]
                max_multiple = max(max_multiple, multiple)

        return max_multiple

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        min_so_far = max_so_far = nums[0]
        result = max_so_far
        for i in range(1, len(nums)):
            tmp_max = max(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], max_so_far * nums[i], min_so_far * nums[i])

            max_so_far = tmp_max

            result = max(result, max_so_far)

        return result


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        self.assertEqual(6, Solution().maxProduct(nums=[2, -5, 3, 1, -4, 0, -10, 2, 8]))

    def test_second(self):
        self.assertEqual(0, Solution().maxProduct(nums=[-2, 0, -1]))


if __name__ == "__main__":
    unittest.main()
