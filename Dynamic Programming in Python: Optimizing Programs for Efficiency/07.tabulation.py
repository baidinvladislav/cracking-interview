# BottomUp
def bottom_up_factorial(n):
    # tabulation table of size n+1
    table = [0] * (n + 1)
    # base case of 0! = 1
    table[0] = 1
    # iterate until n
    for i in range(1, n + 1):
        # using answer to i-1th problem from tabulation to build answer for ith problem
        table[i] = table[i - 1] * i
        # return answer; the nth recursion_factorial
    return table[n]


# Recursion
def recursion_factorial(n):
    if n == 0:  # base case
        return 1
    return n * recursion_factorial(n - 1)  # tabulation_fib step


def main():
    print(recursion_factorial(30))
    print(bottom_up_factorial(30))


main()
