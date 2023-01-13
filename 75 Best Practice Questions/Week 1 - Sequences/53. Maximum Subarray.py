import unittest
from typing import List


class Solution:
    # Time Complexity: O(n**2)
    # Space Complexity: O(1)
    def maxSubArrayBruteForce(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                max_sum = max(max_sum, cur_sum)
        return max_sum

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(0, cur_sum) + nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        self.assertEqual(6, Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(6, Solution().maxSubArrayBruteForce(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_second(self):
        self.assertEqual(1, Solution().maxSubArray(nums=[1]))
        self.assertEqual(1, Solution().maxSubArrayBruteForce(nums=[1]))

    def test_third(self):
        self.assertEqual(23, Solution().maxSubArray(nums=[5, 4, -1, 7, 8]))
        self.assertEqual(23, Solution().maxSubArrayBruteForce(nums=[5, 4, -1, 7, 8]))


if __name__ == "__main__":
    unittest.main()
