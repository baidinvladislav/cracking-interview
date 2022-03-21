"""
Given an unsorted array containing numbers, find the smallest missing positive number in it.
"""


def find_first_smallest_missing_positive(nums):
    i, n = 0, len(nums)
    while i < n:
        correct_idx = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return [-1, -1]


def main():
    print(find_first_smallest_missing_positive([-3, 1, 5, 4, 9, 2]))
    print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_smallest_missing_positive([3, 2, 5, 1]))


main()
