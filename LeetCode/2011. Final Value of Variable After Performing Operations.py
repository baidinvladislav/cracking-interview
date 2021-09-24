"""
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations,
return the final value of X after performing all the operations.
"""
from typing import List


# Simple solution
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for i in operations:
            if '+' in i:
                val += 1
            elif '-' in i:
                val -= 1
            else:
                print('Input is not correct')
        return val


print(Solution().finalValueAfterOperations(operations=["--X", "X++", "X++"]))


# One line solution
class Solution1:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if '+' in o else -1 for o in operations)


print(Solution1().finalValueAfterOperations(operations=["--X", "X++", "X++"]))
