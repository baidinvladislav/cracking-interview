# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.

# Example 1:
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

# Example 2:
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15


class Solution(object):
    def numSubarraysWithSum(self, A, S):
        prefix_sum = {0: 1}  # Dictionary to store prefix sums and their counts
        current_sum = 0  # Initialize current sum
        count = 0  # Initialize the count of subarrays

        for num in A:
            current_sum += num  # Update the current sum

            # If current_sum - S exists in the prefix_sum dictionary, add its count to the result
            if current_sum - S in prefix_sum:
                count += prefix_sum[current_sum - S]

            # Increment the count for the current_sum in the dictionary
            if current_sum in prefix_sum:
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1

        return count
