"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
find the length of the longest contiguous subarray having all 1s.
"""


# Time Complexity: O(N)
# Space Complexity: O(1)
def length_of_longest_substring(arr, k):
    ones, window_start, max_length = 0, 0, 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            ones += 1

        if window_end - window_start + 1 - ones > k:
            if arr[window_start] == 1:
                ones -= 1
            window_start += 1
        max_length = max(window_end - window_start + 1, max_length)

    return max_length


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
