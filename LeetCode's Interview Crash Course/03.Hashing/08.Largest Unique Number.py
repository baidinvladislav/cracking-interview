# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

# Example 1:
# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated.
# The number 8 occurs only once, so it is the answer.

# Example 2:
# Input: nums = [9,9,8,8]
# Output: -1
# Explanation: There is no number that occurs only once.


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1

        result = -1
        for key, val in dic.items():
            if dic[key] == 1 and key > result:
                result = key

        return result
