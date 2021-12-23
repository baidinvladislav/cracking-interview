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
memo = {}  # dictionay for Memoization


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
