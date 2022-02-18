import unittest
from typing import List


class Solution:
    def containsDuplicate_additional_memory(self, nums: List[int]) -> bool:
        buffer = {}

        for num in nums:
            if num not in buffer:
                buffer[num] = 1
            else:
                return True
        return False

    def containsDuplicate_sorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False

    def containsDuplicate_set(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class TestContainsDuplicate(unittest.TestCase):
    def test_first(self):
        self.assertTrue(Solution().containsDuplicate_additional_memory(nums=[1, 2, 3, 1]))
        self.assertTrue(Solution().containsDuplicate_sorting(nums=[1, 2, 3, 1]))
        self.assertTrue(Solution().containsDuplicate_set(nums=[1, 2, 3, 1]))

    def test_second(self):
        self.assertFalse(Solution().containsDuplicate_additional_memory(nums=[1, 2, 3, 4]))
        self.assertFalse(Solution().containsDuplicate_sorting(nums=[1, 2, 3, 4]))
        self.assertFalse(Solution().containsDuplicate_set(nums=[1, 2, 3, 4]))

    def test_third(self):
        self.assertTrue(Solution().containsDuplicate_additional_memory(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertTrue(Solution().containsDuplicate_sorting(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertTrue(Solution().containsDuplicate_set(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    unittest.main()
