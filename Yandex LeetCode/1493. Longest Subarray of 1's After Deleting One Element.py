"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.
"""


from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Sliding window approach.

        1. Track number of '1'.
        2. If there is more than one zero in the window we shrink the window.
        3. During window shrink look at the beginning of the window if it is '1' then we decrease `ones` variable.
        4. Update maximum length.
        """
        ones, window_start, max_length = 0, 0, 0

        for window_end in range(len(nums)):
            if nums[window_end] == 1:
                ones += 1

            if window_end - window_start + 1 - ones > 1:
                if nums[window_start] == 1:
                    ones -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start)

        return max_length


print(Solution().longestSubarray(nums=[1, 1, 0, 1]))
