from random import random


def quicksort(array):
    qs(array, 0, len(array) - 1)


def qs(array, start_index, pivot_index):
    if start_index >= pivot_index:
        return

    p = partition(array, start_index, pivot_index)

    qs(array, start_index, p - 1)
    qs(array, p + 1, pivot_index)


def partition(array, start_index, pivot_index):
    pivot = array[pivot_index]
    current_element = start_index - 1

    for j in range(start_index, pivot_index):
        if array[j] < pivot:
            current_element += 1
            array[current_element], array[j] = array[j], array[current_element]

    array[current_element + 1], array[pivot_index] = array[pivot_index], array[current_element + 1]
    return current_element + 1


if __name__ == '__main__':
    test_cases = [
        [int(10 * random()) for i in range(7)],
        [int(100 * random()) for i in range(14)],
        [int(1000 * random()) for i in range(21)]
    ]

    for array in test_cases:
        quicksort(array)
        print(array)
