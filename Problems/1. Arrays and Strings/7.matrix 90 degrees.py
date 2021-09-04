"""
Write a function which rotates the matrix 90 degrees
"""


def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            top = matrix[layer][i]

            matrix[layer][i] = matrix[-i - 1][layer]

            matrix[-i - 1][-i - 1] = matrix[i][- layer - 1]

            matrix[i][- layer - 1] = top

    return matrix


matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
]

print(rotate_matrix(matrix))
