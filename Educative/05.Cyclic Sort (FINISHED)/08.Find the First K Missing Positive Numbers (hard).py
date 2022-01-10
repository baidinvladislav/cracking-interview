"""
Given an unsorted array containing numbers and a number ‘k’,
find the first ‘k’ missing positive numbers in the array.
"""


def find_first_k_missing_positive(nums, k):
    n = len(nums)
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers = []
    extra_numbers = set()
    for i in range(n):
        if len(missing_numbers) < k:
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)
                extra_numbers.add(nums[i])

    # add the remaining missing numbers
    i = 1
    while len(missing_numbers) < k:
        candidate_number = i + n
        # ignore if the array contains the candidate number
        if candidate_number not in extra_numbers:
            missing_numbers.append(candidate_number)
        i += 1

    return missing_numbers


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()
