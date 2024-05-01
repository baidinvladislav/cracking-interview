from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            num = nums[i]
            x = target - num
            if x in hash_map:
                return [hash_map[x], i]

            hash_map[num] = i

        return [-1, -1]
