"""
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space;
after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
"""


def remove_duplicates(arr):
    first, second = 0, 1
    while second != len(arr):
        if arr[first] != arr[second]:
            first += 1
            arr[first] = arr[second]
        second += 1
    return first + 1


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()


# Similar question:
# Given an unsorted array of numbers and a target ‘key’,
# remove all instances of ‘key’ in-place and return the new length of the array.
def remove_element(arr, key):
    nextElement = 0  # index of the next element which is not 'key'
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1

    return nextElement


def main():
    print("Array new length: " +
          str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " +
          str(remove_element([2, 11, 2, 2, 1], 2)))


main()
