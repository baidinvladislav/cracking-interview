import unittest
from typing import List


class Solution:

    # Time Complexity: O(n**2)
    # Space Complexity: O(1)
    def containsDuplicateBruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] == nums[j]:
                    return True
        return False

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def containsDuplicateAdditionalMemory(self, nums: List[int]) -> bool:
        buffer = {}
        for num in nums:
            if num not in buffer:
                buffer[num] = 1
            else:
                return True
        return False

    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def containsDuplicateSorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def containsDuplicateSet(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class TestContainsDuplicate(unittest.TestCase):
    def test_first(self):
        self.assertTrue(Solution().containsDuplicateAdditionalMemory(nums=[1, 2, 3, 1]))
        self.assertTrue(Solution().containsDuplicateSorting(nums=[1, 2, 3, 1]))
        self.assertTrue(Solution().containsDuplicateSet(nums=[1, 2, 3, 1]))
        self.assertTrue(Solution().containsDuplicateBruteForce(nums=[1, 2, 3, 1]))

    def test_second(self):
        self.assertFalse(Solution().containsDuplicateAdditionalMemory(nums=[1, 2, 3, 4]))
        self.assertFalse(Solution().containsDuplicateSorting(nums=[1, 2, 3, 4]))
        self.assertFalse(Solution().containsDuplicateSet(nums=[1, 2, 3, 4]))
        self.assertFalse(Solution().containsDuplicateBruteForce(nums=[1, 2, 3, 4]))

    def test_third(self):
        self.assertTrue(Solution().containsDuplicateAdditionalMemory(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertTrue(Solution().containsDuplicateSorting(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertTrue(Solution().containsDuplicateSet(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertTrue(Solution().containsDuplicateBruteForce(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    unittest.main()
