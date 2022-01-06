"""
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
"""


def find_missing_number(nums):
    pointer, x = 0, len(nums)

    while pointer < x:
        correct_idx = nums[pointer]
        if nums[pointer] < x and nums[pointer] != nums[correct_idx]:
            nums[pointer], nums[correct_idx] = nums[correct_idx], nums[pointer]
        else:
            pointer += 1

    for i in range(x):
        if i != nums[i]:
            return i

    return x


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
    print(find_missing_number([6, 5, 4, 3, 2, 0]))


main()
