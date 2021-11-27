"""
Given an array of characters where each character represents a fruit tree, you are given two baskets,
and your goal is to put maximum number of fruits in each basket.
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started.
You will pick one fruit from each tree until you cannot,
i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.
"""


def fruits_into_baskets(fruits):
    window_start, max_sub = 0, 0
    hash_map = {}

    for window_end in range(len(fruits)):
        if fruits[window_end] not in hash_map:
            hash_map[fruits[window_end]] = 0
        hash_map[fruits[window_end]] += 1

        while len(hash_map) > 2:
            left_fruit = fruits[window_start]
            hash_map[left_fruit] -= 1
            if hash_map[left_fruit] == 0:
                del hash_map[left_fruit]
            window_start += 1
        max_sub = max(max_sub, window_end - window_start + 1)
    return max_sub


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
