"""
Given a list of weights and a list of costs, find the optimal subset of things
that form the highest cumulative price bounded by the capacity of the knapsack.
"""


# Solution 1: Simple recursion
def solveKnapsack(weights, prices, capacity, index):
    # base case: either capacity already is 0 or pointer reached the end
    if capacity <= 0 or index >= len(weights):
        return 0

    # check that we can put item to the bag
    if weights[index] > capacity:
        return solveKnapsack(weights, prices, capacity, index + 1)

    # recursive call, either we can include the index-th object or we cannot,
    # we check both possibilities and return the most optimal one using max
    return max(
        prices[index] + solveKnapsack(weights, prices, capacity - weights[index], index + 1),
        solveKnapsack(weights, prices, capacity, index + 1)
    )


def knapsack(weights, prices, capacity):
    return solveKnapsack(weights, prices, capacity, 0)


print(knapsack([2, 1, 1, 3], [2, 8, 1, 10], 4))


# Solution 2: With memoization
def solveKnapsack_v1(weights, prices, capacity, index, memo):
    # base case of when we have run out of capacity or objects
    if capacity <= 0 or index >= len(weights):
        return 0
    # check for solution in memo table
    if (capacity, index) in memo:
        return memo[(capacity, index)]
    # if weight at index-th position is greater than capacity, skip this object
    if weights[index] > capacity:
        # store result in memo table
        memo[(capacity, index)] = solveKnapsack_v1(weights, prices, capacity, index + 1, memo)
        return memo[(capacity, index)]
        # recursive call, either we can include the index-th object or we cannot, we check both possibilities and return the most optimal one using max
    memo[(capacity, index)] = max(
        prices[index] + solveKnapsack_v1(weights, prices, capacity - weights[index], index + 1, memo),
        solveKnapsack_v1(weights, prices, capacity, index + 1, memo))
    return memo[(capacity, index)]


def knapsack(weights, prices, capacity):
    # create a memo dictionary
    memo = {}
    return solveKnapsack_v1(weights, prices, capacity, 0, memo)
