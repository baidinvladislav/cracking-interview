"""
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
The array has only one duplicate, but it can be repeated multiple times.
Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.
"""


def find_duplicate(nums):
    pointer = 0

    while pointer < len(nums):
        if nums[pointer] != pointer + 1:
            correct_idx = nums[pointer] - 1
            if nums[pointer] != nums[correct_idx]:
                nums[pointer], nums[correct_idx] = nums[correct_idx], nums[pointer]
            else:
                return nums[pointer]
        else:
            pointer += 1
    return -1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()
