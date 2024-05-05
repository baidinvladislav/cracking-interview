from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(string, opened, closed):
            if len(string) == n * 2:
                result.append(string)
                return

            if opened < n:
                backtrack(string + "(", opened + 1, closed)

            if closed < opened:
                backtrack(string + ")", opened, closed + 1)

        result = []
        backtrack("", 0, 0)
        return result
