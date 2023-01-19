import unittest
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        return result


class TestTwoSum(unittest.TestCase):

    def test_first(self):
        expected = 1
        self.assertEqual(expected, Solution().singleNumber([2, 2, 1]))

    def test_second(self):
        expected = 4
        self.assertEqual(expected, Solution().singleNumber([4, 1, 2, 1, 2]))

    def test_third(self):
        expected = 1
        self.assertEqual(expected, Solution().singleNumber([1]))


if __name__ == "__main__":
    unittest.main()
