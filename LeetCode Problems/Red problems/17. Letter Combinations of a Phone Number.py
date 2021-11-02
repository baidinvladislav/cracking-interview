"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        mapping = {"2": "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        ret = []
        self.dfs(mapping, digits, "", ret)
        return ret

    def dfs(self, mapping, digits, path, ret):
        if not digits:
            ret.append(path)
            return

        for c in mapping[digits[0]]:
            self.dfs(mapping, digits[1:], path + c, ret)


print(Solution().letterCombinations(digits="23"))
