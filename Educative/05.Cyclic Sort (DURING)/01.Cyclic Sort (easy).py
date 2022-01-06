"""
We are given an array containing n objects. Each object, when created,
was assigned a unique number from the range 1 to n based on their creation sequence.
This means that the object with sequence number 3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in O(n)O(n)
and without using any extra space.
For simplicity, let’s assume we are passed an integer array containing only the sequence numbers,
though each number is actually an object.
"""


def cyclic_sort(nums):
    pointer = 0

    while pointer < len(nums):
        correct_idx = nums[pointer] - 1
        if nums[pointer] != nums[correct_idx]:
            nums[pointer], nums[correct_idx] = nums[correct_idx], nums[pointer]
        else:
            pointer += 1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
