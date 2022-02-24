import unittest
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        self.assertEqual(6, Solution().maxProduct(nums=[2, -5, 3, 1, -4, 0, -10, 2, 8]))

    def test_second(self):
        self.assertEqual(0, Solution().maxProduct(nums=[-2, 0, -1]))


if __name__ == "__main__":
    unittest.main()
