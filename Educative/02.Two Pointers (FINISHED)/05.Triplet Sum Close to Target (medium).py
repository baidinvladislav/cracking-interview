"""
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close
to the target number as possible, return the sum of the triplet.

If there are more than one such triplet, return the sum of the triplet with the smallest sum.
"""


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_difference = float('inf')

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            remainder = target_sum - arr[i] - arr[left] - arr[right]

            if remainder == 0:
                return target_sum

            if abs(remainder) < abs(smallest_difference) \
                    or (abs(remainder) == abs(smallest_difference) and remainder > smallest_difference):
                smallest_difference = remainder

            if remainder > 0:
                left += 1

            elif remainder < 0:
                right -= 1

    return target_sum - smallest_difference


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
