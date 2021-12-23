# recursive
def fib(n):
    if n == 0:  # base case 1
        return 0
    if n == 1:  # base case 2
        return 1
    else:  # recursive step
        return dp_fib(n - 1) + dp_fib(n - 2)


print(fib(10))

# dynamic programming Memoization
memo = {}  # dictionary for Memoization


def dp_fib(n):
    if n == 0:  # base case 1
        return 0
    if n == 1:  # base case 2
        return 1
    elif n in memo:  # Check if result for n has already been evaluated
        return memo[n]  # return the result if it is available
    else:  # otherwise recursive step
        memo[n] = dp_fib(n - 1) + dp_fib(n - 2)  # store the result of n in memoization dictionary
        return memo[n]  # return the value


print(dp_fib(10))


# dynamic programming tabulation
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # table for tabulation
    table = [None] * (n + 1)
    table[0] = 0  # base case 1, fib(0) = 0
    table[1] = 1  # base case 2, fib(1) = 1
    # filling up tabulation table starting from 2 and going upto n
    for i in range(2, n + 1):
        # we have result of i-1 and i-2 available because these had been evaluated already
        table[i] = table[i - 1] + table[i - 2]
        # return the value of n in tabulation table
    return table[n]


print(fib(10000))


# Space complexity from O(n) to O(1)
def fib(n):
    if n == 0:  # base cases
        return 0
    if n == 1:  # base cases
        return 1
    secondLast = 0  # base case 1, fib(0) = 0
    last = 1  # base case 2, fib(1) = 1
    current = None  # initially set to None
    for i in range(1, n):  # iterate n times to evaluate n-th fibonacci
        # storing ith fibonacci in current by summing up i-1th and i-2th fibonacci
        current = secondLast + last
        secondLast = last  # updating for next iteration
        last = current
    return current  # return the value of n in tabulation table


print(fib(6))
