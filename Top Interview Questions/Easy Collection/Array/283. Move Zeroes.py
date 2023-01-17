import unittest
from typing import List


class Solution:

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def moveZeroesAdditionalSpace(self, nums: List[int]):
        result = []
        zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
            else:
                result.append(nums[i])

        while zeroes:
            result.append(0)
            zeroes -= 1

        return result

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def moveZeroes(self, nums: List[int]):
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1

        return nums


class TestTwoSum(unittest.TestCase):

    def test_first(self):
        expected = [1, 2, 3, 0, 0]
        self.assertEqual(expected, Solution().moveZeroesAdditionalSpace([1, 0, 2, 0, 3]))
        self.assertEqual(expected, Solution().moveZeroes([1, 0, 2, 0, 3]))

    def test_second(self):
        expected = [1, 0, 0]
        self.assertEqual(expected, Solution().moveZeroesAdditionalSpace([0, 0, 1]))
        self.assertEqual(expected, Solution().moveZeroes([0, 0, 1]))

    def test_third(self):
        expected = [1, 2, 3, 0, 0, 0]
        self.assertEqual(expected, Solution().moveZeroesAdditionalSpace([1, 2, 3, 0, 0, 0]))
        self.assertEqual(expected, Solution().moveZeroes([1, 2, 3, 0, 0, 0]))

    def test_no_solution(self):
        expected = [4, 6, 9, 0, 0]
        self.assertEqual(expected, Solution().moveZeroesAdditionalSpace([4, 0, 6, 9, 0]))
        self.assertEqual(expected, Solution().moveZeroes([4, 0, 6, 9, 0]))


if __name__ == "__main__":
    unittest.main()