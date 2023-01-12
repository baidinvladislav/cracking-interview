import unittest
from typing import List


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(result) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual([24, 12, 8, 6], Solution().productExceptSelf(nums=[1, 2, 3, 4]))

    def test_second(self):
        self.assertEqual([0, 0, 9, 0, 0], Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]))


if __name__ == "__main__":
    unittest.main()
