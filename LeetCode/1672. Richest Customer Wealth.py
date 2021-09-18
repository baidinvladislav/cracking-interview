"""
You are given an m x n integer grid accounts
where accounts[i][j] is the amount of money the i-th customer has in the j-th bank.
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            max_wealth = max(sum(customer), max_wealth)
        return max_wealth


print(Solution().maximumWealth([[1, 5], [7, 3], [3, 5]]))
