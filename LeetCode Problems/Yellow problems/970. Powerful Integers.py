"""
Given three integers x, y, and bound, return a list of all the powerful integers
that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.
"""
from typing import List


# Works but during testing LeetCode logged Time Exceeded
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        possibilities = [i for i in range(bound + 1)]
        result = []

        for i in range(len(possibilities)):
            for j in range(len(possibilities)):
                if x**possibilities[i] + y**possibilities[j] in possibilities\
                        and x**possibilities[i] + y**possibilities[j] not in result:
                    result.append(x**possibilities[i] + y**possibilities[j])

        return result


print(Solution().powerfulIntegers(x=2, y=3, bound=10))
