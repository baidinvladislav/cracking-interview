"""
Given a sorted array, create a new array containing squares of all the numbers
of the input array in the sorted order.
"""


def make_squares(arr):
    n = len(arr)
    squares = [0 for _ in range(n)]

    highest_square_idx = n - 1
    left, right = 0, n - 1

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square > right_square:
            squares[highest_square_idx] = left_square
            left += 1
        else:
            squares[highest_square_idx] = right_square
            right -= 1

        highest_square_idx -= 1

    return squares


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
