"""
There are n kids with candies. You are given an integer array candies,
where each candies[i] represents the number of candies the ith kid has,
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if,
after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""
from typing import List


# my solution
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        logic_arr = []

        for i in range(n):
            var = candies[i] + extraCandies
            if var >= max(candies):
                logic_arr.append(True)
            else:
                logic_arr.append(False)

        return logic_arr


print(Solution().kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))


# one line solution from discuss
class Solution1:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [candy+extraCandies >= max(candies) for candy in candies]


print(Solution1().kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
