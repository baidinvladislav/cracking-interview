import random


def merge_two_list(list_a, list_b):
    sorted_list = []
    i = j = 0

    while i < len(list_a) and j < len(list_b):
        if list_a[i] < list_b[j]:
            sorted_list.append(list_a[i])
            i += 1
        else:
            sorted_list.append(list_b[j])
            j += 1

    if i < len(list_a):
        sorted_list += list_a[i:]

    if j < len(list_b):
        sorted_list += list_b[j:]

    return sorted_list


def merge_sort(array):
    if len(array) == 1:
        return array

    middle = len(array)//2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge_two_list(left, right)


if __name__ == '__main__':
    test_cases = [
        [int(10 * random.random()) for i in range(7)],
        [int(100 * random.random()) for i in range(14)],
        [int(1000 * random.random()) for i in range(21)]
    ]

    for array in test_cases:
        print(merge_sort(array))
