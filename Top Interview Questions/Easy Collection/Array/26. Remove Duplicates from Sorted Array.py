from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_idx = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[insert_idx] = nums[i]
                insert_idx += 1

        return insert_idx
