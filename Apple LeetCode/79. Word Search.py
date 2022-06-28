from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, index):
            # base case
            if index == len(word):
                return True

            # invalid cases
            if (
                not 0 <= x < len(board) or
                not 0 <= y < len(board[0]) or
                board[x][y] == '#' or
                board[x][y] != word[index]
            ):
                return False

            # mark as visited
            curr_letter = board[x][y]
            board[x][y] = '#'

            # recursion
            is_result = False
            for x_offset, y_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if dfs(x + x_offset, y + y_offset, index + 1):
                    is_result = True

            board[x][y] = curr_letter

            return is_result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False
