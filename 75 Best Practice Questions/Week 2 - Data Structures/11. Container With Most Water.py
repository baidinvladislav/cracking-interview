import unittest


class Solution:
    def maxArea(self, height):
        result = 0
        left, right = 0, len(height) - 1

        while left < right:
            result = max(result, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual(49, Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))

    def test_second(self):
        self.assertEqual(1, Solution().maxArea(height=[1, 1]))


if __name__ == "__main__":
    unittest.main()
