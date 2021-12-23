# recursive
def fib(n):
    if n == 0:  # base case 1
        return 0
    if n == 1:  # base case 2
        return 1
    else:  # recursive step
        return dp_fib(n - 1) + dp_fib(n - 2)


print(fib(10))


# dynamic programming
calculated = {}


def dp_fib(n):
    if n == 0:  # base case 1
        return 0
    if n == 1:  # base case 2
        return 1
    elif n in calculated:
        return calculated[n]
    else:  # recursive step
        calculated[n] = dp_fib(n - 1) + dp_fib(n - 2)
        return calculated[n]


print(dp_fib(10))
