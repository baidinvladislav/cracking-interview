"""
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.
"""


import random


def find_Kth_smallest_number(nums, k):
    return find_Kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


def find_Kth_smallest_number_rec(nums, k, start, end):
    p = partition(nums, start, end)

    if p == k - 1:
        return nums[p]

    if p > k - 1:  # search lower part
        return find_Kth_smallest_number_rec(nums, k, start, p - 1)

    # search higher part
    return find_Kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, low, high):
    if low == high:
        return low

    pivotIndex = random.randint(low, high)
    nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]

    pivot = nums[high]
    for i in range(low, high):
        # all elements less than 'pivot' will be before the index 'low'
        if nums[i] < pivot:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1

    # put the pivot in its correct place
    nums[low], nums[high] = nums[high], nums[low]
    return low


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
