"""
In MATLAB, there is a handy function called reshape
which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r
and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix
in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal,
output the new reshaped matrix; Otherwise, output the original matrix.
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat

        ans = [[0] * c for _ in range(r)]
        for i in range(m * n):
            ans[i // c][i % c] = mat[i // n][i % n]
        return ans


print(Solution().matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4))
