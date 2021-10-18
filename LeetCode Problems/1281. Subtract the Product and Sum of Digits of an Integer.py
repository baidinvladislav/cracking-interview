"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = list(str(n))
        product = 1
        sum = 0

        for val in l:
            product *= int(val)
            sum += int(val)

        return product - sum


print(Solution().subtractProductAndSum(n=234))
