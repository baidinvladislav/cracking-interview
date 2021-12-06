"""
Given an array, find the average of all contiguous sub-arrays of size ‘K’ in it.
"""


# brute-force
def find_averages_of_subarrays(arr, K):
    result = []

    for i in range(len(arr) - K + 1):
        _sum = 0.0
        for j in range(i, i + K):
            _sum += arr[j]
        result.append(_sum / K)

    return result


# sliding window
def find_averages_of_subarrays_v1(arr, K):
    """
    1. Initialize of empty array that we'll return.
    2. Initialize `windowSum` variable for calculate sum of sub-array.
    3. Initialize `windowStart` variable for tracking beginning of the subarray.
    4. Inside every iteration we sum value to `windowSum`.
    5. If number of iteration greater or equal to `K-1`. - create a window size
    6. Add `windowSum / K` to returned array.
    7. Decrease `windowSum` on value tracked in `windowStart` during first iteration it is `0`.
    - removed left element
    8. Increase `windowStart` variable on `1`. - shifting window to the right
    9. Return `list` result.

    :param arr: `list` input array.
    :param K: `int` length of sub-arrays.
    :return: `list` result contains all the averages of the sub-arrays.
    """
    window_start = 0
    window_sum = 0
    result = []

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= K - 1:
            result.append(window_sum / K)
            window_sum -= arr[window_start]
            window_start += 1
    return result


def main():
    result = find_averages_of_subarrays_v1([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
    print("Averages of subarrays of size K: " + str(result))


main()
