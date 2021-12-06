"""
Given an array of positive numbers and a positive number ‘S’,
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.

Return 0 if no such subarray exists.
"""


import math


def smallest_subarray_with_given_sum(s, arr):
    window_start, window_sum = 0, 0
    min_length_sub = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            length_sub = window_end - window_start + 1
            min_length_sub = min(min_length_sub, length_sub)
            window_sum -= arr[window_start]
            window_start += 1

    if min_length_sub == math.inf:
        return 0

    return min_length_sub


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
