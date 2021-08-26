from random import random


def binary_search(data, found_el):
    """
    Iterative binary search implementation.

    :param data: `list` contains found integer.
    :param found_el: `int` found integer
    :return: `int` or recursion call.
    """
    start = 0
    end = len(data)

    while True:
        middle_index = start + (end - start) // 2

        if data[middle_index] == found_el:
            return data[middle_index]

        elif data[middle_index] > found_el:
            end = middle_index

        else:
            start = middle_index + 1


if __name__ == '__main__':
    test_cases = [
        [int(10 * random()) for i in range(7)],
        [int(100 * random()) for i in range(14)],
        [int(1000 * random()) for i in range(21)]
    ]

    for array in test_cases:
        array.sort()
        array_length = len(array)
        random_index = int((array_length - 1) * random())
        found_el = array[random_index]
        print(
            f'It returned algorithm -> {binary_search(array, found_el)}\n'
            f'It was found integer -> {found_el}\n'
        )
