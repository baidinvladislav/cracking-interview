from random import random


def binary_search(data, found_el):
    """
    Recursive binary search implementation.

    :param data: `list` contains found integer.
    :param found_el: `int` found integer
    :return: `int` or recursion call.
    """
    middle_index = len(data) // 2
    middle_el = data[middle_index]

    left_part = data[:middle_index]
    right_part = data[middle_index:]

    if middle_el == found_el:
        return found_el

    elif middle_el > found_el:
        return binary_search(left_part, found_el)

    else:
        return binary_search(right_part, found_el)


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
        print(binary_search(array, found_el))
