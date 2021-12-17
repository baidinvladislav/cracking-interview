"""
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers
of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue;
and since our input array also consists of three different numbers
that is why it is called Dutch National Flag problem.
"""


def dutch_flag_sort(arr):
    """
    1. Initialize three pointers: left, right, i.
    2. If arr[i] is 0 then we swap arr[i] with arr[left] and increase both pointers left and i.
    3. If arr[i] is 1 increase only i pointer.
    4. If arr[i] is 2 then we swap arr[i] with arr[right] and decrease right pointer.

    All elements < left pointer are 0, and all elements > right are 2.
    All elements from >= left < right are 1.
    """
    left, right, i = 0, len(arr) - 1, 0

    while i <= right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left += 1

        elif arr[i] == 1:
            i += 1

        elif arr[i] == 2:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()
