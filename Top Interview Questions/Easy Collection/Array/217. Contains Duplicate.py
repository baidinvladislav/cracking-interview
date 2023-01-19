import unittest
from typing import List


class Solution:

    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True

        return False


class TestTwoSum(unittest.TestCase):

    def test_first(self):
        expected = True
        self.assertEqual(expected, Solution().containsDuplicate([1, 2, 3, 1]))

    def test_second(self):
        expected = False
        self.assertEqual(expected, Solution().containsDuplicate([1, 2, 3, 4]))

    def test_third(self):
        expected = True
        self.assertEqual(expected, Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    unittest.main()
