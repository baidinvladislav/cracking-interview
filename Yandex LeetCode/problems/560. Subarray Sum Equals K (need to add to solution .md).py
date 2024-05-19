from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            key = curr - k
            ans += counts[key]
            counts[curr] += 1

        return ans


Solution().subarraySum(nums=[1, 2, 3], k=3)
