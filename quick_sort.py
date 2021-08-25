from random import random


def quicksort(arr):
    qs(arr, 0, len(arr) - 1)


def qs(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r)

    qs(arr, l, p - 1)
    qs(arr, p + 1, r)


def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


if __name__ == '__main__':
    test_cases = [
        [int(10 * random()) for i in range(7)],
        [int(100 * random()) for i in range(14)],
        [int(1000 * random()) for i in range(21)]
    ]

    for array in test_cases:
        quicksort(array)
        print(array)
