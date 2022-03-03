"""
Given an array of sorted numbers and a target sum,
find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair)
such that they add up to the given target.
"""


def pair_with_targetsum(arr, target_sum):
    # len(arr) - 1 because we need to get index of last element
    left_pointer, right_pointer = 0, len(arr) - 1

    while left_pointer < right_pointer:
        # calculate current sum
        cur_sum = arr[left_pointer] + arr[right_pointer]

        if cur_sum == target_sum:
            return [left_pointer, right_pointer]

        # if the current amount is greater than the target amount,
        # we decrease it by shifting the right pointer from the end one element closer to the beginning
        elif cur_sum > target_sum:
            right_pointer -= 1

        # if the current amount is less than the target amount,
        # we increase it by shifting the left pointer from the beginning one element closer to the end
        elif cur_sum < target_sum:
            left_pointer += 1

    # if we can not find pair
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
