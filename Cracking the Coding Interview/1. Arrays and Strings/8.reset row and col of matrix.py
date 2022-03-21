"""
Write a algorithm which resets the row and column of matrix if it has element equal to 0
"""
import unittest


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row] = [0 for i in range(len(matrix[0]))]


def nullify_column(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0


def set_zeroes(matrix):
    row = [False for i in range(len(matrix))]
    column = [False for i in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    for el in row:
        if row[el]:
            nullify_row(matrix, el)

    for val in range(len(column)):
        if column[val]:
            nullify_column(matrix, val)

    return matrix


class Test(unittest.TestCase):
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 0, 4],
        [8, 2, 5, 1, 7]
    ]

    expected_matrix = [
        [1, 2, 3, 0, 5],
        [0, 0, 0, 0, 0],
        [8, 2, 5, 0, 7]
    ]

    def test_zero_matrix(self):
        self.assertEqual(set_zeroes(self.matrix), self.expected_matrix)


if __name__ == "__main__":
    unittest.main()
