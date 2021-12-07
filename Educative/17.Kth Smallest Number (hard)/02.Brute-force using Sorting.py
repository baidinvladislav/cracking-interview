"""
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.
"""


def find_Kth_smallest_number(nums, k):
    return sorted(nums)[k - 1]


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
