"""
Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.
"""


def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    is_asceding = arr[start] < arr[end]

    while start <= end:
        middle = start + (end - start) // 2
        if arr[middle] == key:
            return middle

        if is_asceding:
            if key > arr[middle]:
                start = middle + 1
            elif key < arr[middle]:
                end = middle - 1
        else:
            if key < arr[middle]:
                start = middle + 1
            elif key > arr[middle]:
                end = middle - 1
    return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()
