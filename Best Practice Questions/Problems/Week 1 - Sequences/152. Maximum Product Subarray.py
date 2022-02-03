import unittest


class Solution:
    def maxProduct(self, nums):
        answer = nums[0]
        product = 0
        for i in range(len(nums)):
            if product == 0:
                product = nums[i]
            else:
                product *= nums[i]
            answer = max(answer, product)

        product = 0
        for i in range(len(nums) - 1, -1, -1):
            if product == 0:
                product = nums[i]
            else:
                product *= nums[i]
            answer = max(answer, product)
        return answer


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        self.assertEqual(6, Solution().maxProduct(nums=[2, 3, -2, 4]))

    def test_second(self):
        self.assertEqual(0, Solution().maxProduct(nums=[-2, 0, -1]))


if __name__ == "__main__":
    unittest.main()
