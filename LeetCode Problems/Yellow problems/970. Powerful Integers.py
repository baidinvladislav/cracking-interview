"""
Given three integers x, y, and bound, return a list of all the powerful integers
that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.
"""
from typing import List
from math import log


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


# LeetCode solution
class Solution1:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        a = bound if x == 1 else int(log(bound, x))
        b = bound if y == 1 else int(log(bound, y))

        powerful_integers = set([])

        for i in range(a + 1):
            for j in range(b + 1):

                value = x ** i + y ** j

                if value <= bound:
                    powerful_integers.add(value)

                if y == 1:
                    break

            if x == 1:
                break

        return list(powerful_integers)


print(Solution1().powerfulIntegers(x=2, y=3, bound=10))
