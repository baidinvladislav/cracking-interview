import random


# my code based on their solution
# Time Complexity: O(inf)
# Space Complexity: O(1)
def rand7():
    return random.randint(1, 7)


def rand5():
    result = 7
    while result > 5:
        result = rand7()
    return result


# their solution
# Time Complexity: O(inf)
# Space Complexity: O(1)
def rand5():
    result = 7  # arbitrarily large
    while result > 5:
        result = rand7()
    return result
