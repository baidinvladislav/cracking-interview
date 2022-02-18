import unittest
from typing import List


class Solution:
    def productExceptSelf(self, nums):
        answer = []

        prefix = 1
        for i in range(len(nums)):
            answer.append(prefix)
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual([24, 12, 8, 6], Solution().productExceptSelf(nums=[1, 2, 3, 4]))

    def test_second(self):
        self.assertEqual([0, 0, 9, 0, 0], Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]))


if __name__ == "__main__":
    unittest.main()
