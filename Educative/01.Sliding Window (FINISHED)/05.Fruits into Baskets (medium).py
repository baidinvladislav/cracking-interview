"""
Given an array of characters where each character represents a fruit tree, you are given two baskets,
and your goal is to put maximum number of fruits in each basket.
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started.
You will pick one fruit from each tree until you cannot,
i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.
"""


# Time Complexity: O(N)
# Space Complexity: O(1)
def fruits_into_baskets(fruits):
    window_start, max_length, storage = 0, float('-inf'), dict()

    for window_end in range(len(fruits)):
        if fruits[window_end] not in storage:
            storage[fruits[window_end]] = 0
        storage[fruits[window_end]] += 1

        while len(storage) > 2:
            storage[fruits[window_start]] -= 1
            if storage[fruits[window_start]] == 0:
                del storage[fruits[window_start]]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
