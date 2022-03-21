"""
Given a sorted array, create a new array containing squares of all the numbers
of the input array in the sorted order.
"""


def make_squares(arr):
    result, inserted_index = [None for _ in arr], len(arr) - 1
    left, right = 0, len(arr) - 1

    while left <= right:
        left_square, right_square = arr[left] ** 2, arr[right] ** 2

        if right_square > left_square:
            result[inserted_index] = right_square
            right -= 1
        else:
            result[inserted_index] = left_square
            left += 1

        inserted_index -= 1
    return result


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
