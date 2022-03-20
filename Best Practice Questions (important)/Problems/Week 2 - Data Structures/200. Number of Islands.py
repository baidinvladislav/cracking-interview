import unittest
from collections import deque


class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        columns = len(grid[0])
        nums_islands = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    nums_islands += 1
                    grid[i][j] = '0'
                    neighbors = deque()
                    neighbors.append([i, j])
                    while neighbors:
                        neighbor = neighbors.popleft()
                        row, column = neighbor[0], neighbor[1]
                        if row - 1 >= 0 and grid[row - 1][column] == '1':
                            neighbors.append([row - 1, column])
                            grid[row - 1][column] = '0'
                        if row + 1 < rows and grid[row + 1][column] == '1':
                            neighbors.append([row + 1, column])
                            grid[row + 1][column] = '0'
                        if column - 1 >= 0 and grid[row][column - 1] == '1':
                            neighbors.append([row, column - 1])
                            grid[row][column - 1] = '0'
                        if column + 1 < columns and grid[row][column + 1] == '1':
                            neighbors.append([row, column + 1])
                            grid[row][column + 1] = '0'
        return nums_islands


class TestNumIslands(unittest.TestCase):
    def test_first(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        self.assertEqual(1, Solution().numIslands(grid))

    def test_second(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        self.assertEqual(3, Solution().numIslands(grid))


if __name__ == "__main__":
    unittest.main()
