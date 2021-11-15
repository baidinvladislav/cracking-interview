"""
Given an array of sorted numbers and a target sum,
find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair)
such that they add up to the given target.
"""


def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]

        if target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()


# an alternate approach
def pair_with_targetsum_v1(arr, target_sum):
    nums = {}  # to store numbers and their indices
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]


def main():
    print(pair_with_targetsum_v1([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum_v1([2, 5, 9, 11], 11))


main()
