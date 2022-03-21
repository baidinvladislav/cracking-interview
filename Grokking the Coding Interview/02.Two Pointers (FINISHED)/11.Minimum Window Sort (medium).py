"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
"""


import math


def shortest_window_sort(arr):
    """
    1. Find the first number out of sorting order from the beginning.
    2. Find the first number out of sorting order from the end.
    3. Find the maximum and minimum of the subarray.
    4. Extend the subarray to include any number which is bigger than the minimum of the subarray.
    5. Extend the subarray to include any number which is smaller than the maximum of the subarray.
    """
    low, high = 0, len(arr) - 1
    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1

    # if the array is sorted
    if low == len(arr) - 1:
        return 0

    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1

    subarray_max = -math.inf
    subarray_min = math.inf
    for k in range(low, high + 1):
        subarray_max = max(subarray_max, arr[k])
        subarray_min = min(subarray_min, arr[k])

    while low > 0 and arr[low - 1] > subarray_min:
        low -= 1

    while high < len(arr) - 1 and arr[high + 1] < subarray_max:
        high += 1

    return high - low + 1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))


main()
