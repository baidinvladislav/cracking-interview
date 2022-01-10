"""
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates,
which means some numbers will be missing. Find all those missing numbers.
"""


def find_missing_numbers(nums):
    pointer = 0

    while pointer < len(nums):
        correct_idx = nums[pointer] - 1
        if nums[pointer] != nums[correct_idx]:
            nums[pointer], nums[correct_idx] = nums[correct_idx], nums[pointer]
        else:
            pointer += 1

    missing_numbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)
    return missing_numbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


main()
