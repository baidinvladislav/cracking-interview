import unittest


class Solution:
    def maxSubArray(self, nums):
        current_subarray = max_subarray = nums[0]

        for i in range(1, len(nums)):
            current_subarray = max(nums[i], current_subarray + nums[i])
            max_subarray = max(current_subarray, max_subarray)

        return max_subarray


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        self.assertEqual(6, Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_second(self):
        self.assertEqual(1, Solution().maxSubArray(nums=[1]))

    def test_third(self):
        self.assertEqual(23, Solution().maxSubArray(nums=[5, 4, -1, 7, 8]))


if __name__ == "__main__":
    unittest.main()
