import random


def heapify(array, array_length, i):
    largest_idx = i
    left_idx = 2 * i + 1
    right_idx = 2 * i + 2

    if left_idx < array_length and array[largest_idx] < array[left_idx]:
        largest_idx = left_idx

    if right_idx < array_length and array[largest_idx] < array[right_idx]:
        largest_idx = right_idx

    if largest_idx != i:
        array[i], array[largest_idx] = array[largest_idx], array[i]
        heapify(array, array_length, largest_idx)


def heap_sort(array):
    array_length = len(array)

    for i in range(array_length, -1, -1):
        heapify(array, array_length, i)

    for i in range(array_length-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


if __name__ == '__main__':
    test_cases = [
        [int(10 * random.random()) for i in range(7)],
        [int(100 * random.random()) for i in range(14)],
        [int(1000 * random.random()) for i in range(21)]
    ]

    for array in test_cases:
        heap_sort(array)
        print(array)
