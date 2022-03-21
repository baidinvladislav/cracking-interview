"""
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.
"""


def find_all_duplicates(nums):
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    duplicates = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicates.append(nums[i])

    return duplicates


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
    print(find_all_duplicates([1, 2, 3, 3, 2, 5, 6]))


main()
