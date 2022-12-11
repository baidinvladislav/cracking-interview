# their solution
# Time Complexity: O(inf)
# Space Complexity: O(1)
def rand5():
    result = 7  # arbitrarily large
    while result > 5:
        result = rand7()
    return result
