import unittest


class Solution:
    def threeSum(self, nums):
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            self.searchPair(target=-nums[i], nums=nums, left=i + 1, triplets=triplets)
        return triplets

    def searchPair(self, target, nums, left, triplets):
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                triplets.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))

    def test_second(self):
        self.assertEqual([], Solution().threeSum(nums=[]))

    def test_third(self):
        self.assertEqual([], Solution().threeSum(nums=[0]))


if __name__ == "__main__":
    unittest.main()
