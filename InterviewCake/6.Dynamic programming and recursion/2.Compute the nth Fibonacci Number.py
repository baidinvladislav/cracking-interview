import unittest


# my bottom-up solution
def fib(n):
    if n < 0:
        raise ValueError('error')

    if n in [0, 1]:
        return n

    prev_prev, prev = 0, 1
    current = prev_prev + prev
    for i in range(2, n + 1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current

    return current


# my memoization solution
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n in [0, 1]:
            return n

        if n in self.memo:
            return n

        result = self.fib(n - 2) + self.fib(n - 1)
        self.memo[n] = result

        return result


# my own recursive solution
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
def fib(n):
    if n in [0, 1]:
        return n

    return fib(n - 2) + fib(n - 1)


# their bottom-up solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def fib(n):
    # Edge cases:
    if n < 0:
        raise ValueError('Index was negative. No such thing as a '
                         'negative index in a series.')
    elif n in [0, 1]:
        return n

    # We'll be building the fibonacci series from the bottom up
    # so we'll need to track the previous 2 numbers at each step
    prev_prev = 0  # 0th fibonacci
    prev = 1       # 1st fibonacci

    for _ in range(n - 1):
        # Iteration 1: current = 2nd fibonacci
        # Iteration 2: current = 3rd fibonacci
        # Iteration 3: current = 4th fibonacci
        # To get nth fibonacci ... do n-1 iterations.
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current


# their memoization solution
# Time Complexity: O(n)
# Space Complexity: O(n)
class Fibber(object):

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            # Edge case: negative index
            raise ValueError('Index was negative. No such thing as a '
                             'negative index in a series.')
        elif n in [0, 1]:
            # Base case: 0 or 1
            return n

        # See if we've already calculated this
        if n in self.memo:
            return self.memo[n]

        result = self.fib(n - 1) + self.fib(n - 2)

        # Memoize
        self.memo[n] = result

        return result


class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)
