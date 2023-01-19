import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            attempt = target - nums[i]
            if attempt in map and i != map[attempt]:
                return [i, map[attempt]]

        return [-1, -1]


class TestTwoSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual([-1, -1], Solution().twoSum(nums=[], target=9))

    def test_first(self):
        self.assertEqual([0, 1], Solution().twoSum(nums=[2, 7, 11, 15], target=9))

    def test_second(self):
        self.assertEqual([1, 2], Solution().twoSum(nums=[3, 2, 4], target=6))

    def test_third(self):
        self.assertEqual([0, 1], Solution().twoSum(nums=[3, 3], target=6))

    def test_no_solution(self):
        self.assertEqual([-1, -1], Solution().twoSum(nums=[3, 3, 1, 4, 5], target=16))


if __name__ == "__main__":
    unittest.main()
