"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
find the length of the longest contiguous subarray having all 1s.
"""


# Time Complexity: O(N)
# Space Complexity: O(1)
def length_of_longest_substring(arr, k):
    """
    Sliding window approach.

    1. Track number of '1'.
    2. If there is more than `K` zero in the window we shrink the window.
    3. During window shrink look at the beginning of the window if it is '1' then we decrease `ones` variable.
    4. Update maximum length.
    """
    window_start, max_length, ones = 0, 0, 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            ones += 1
        if k < window_end - window_start + 1 - ones:
            if arr[window_start] == 1:
                ones -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
