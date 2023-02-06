import unittest
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]


class TestRotateArray(unittest.TestCase):

    def test_first(self):
        expected = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(expected, Solution().rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))

    def test_second(self):
        expected = [3, 99, -1, -100]
        self.assertEqual(expected, Solution().rotate(nums=[-1, -100, 3, 99], k=2))


if __name__ == "__main__":
    unittest.main()
