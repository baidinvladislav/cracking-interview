import unittest


class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        self.assertEqual(4, Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))

    def test_second(self):
        self.assertEqual(-1, Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))

    def test_third(self):
        self.assertEqual(-1, Solution().search(nums=[1], target=0))


if __name__ == "__main__":
    unittest.main()
