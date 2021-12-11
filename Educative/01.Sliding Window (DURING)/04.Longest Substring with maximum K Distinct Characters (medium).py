"""
Given a string, find the length of the longest substring in it
with no more than K distinct characters.
"""


# Time Complexity: O(N)
# Space Complexity: O(K)
def longest_substring_with_k_distinct(str1, k):
    """
    1. Initialize `window_start` to tracking beginning of window.
    2. Initialize `max_length` to keeping the max length of sub-array.
    3. Initialize `char_frequency` to keeping the amount of frequency elements.
    4. Looping to input string and adding char to `char_frequency` like key and amount frequency as value.
    5. If length of `char_frequency` greater than `K` then decrease their value by 1.
    6. If value of char equal 0 then delete this key from `char_frequency`.
    7. Increase `window_start` by 1.
    8. Update `max_length` if window_end - window_start + 1 greater than `max_length`.

    :param str1: `str` input string.
    :param k: `int` amount values inside sub-array.
    :return: `int` max_length max length of sub-array distinct K elements.
    """
    window_start, max_length, storage = 0, float('-inf'), dict()

    for window_end in range(len(str1)):
        if str1[window_end] not in storage:
            storage[str1[window_end]] = 0
        storage[str1[window_end]] += 1

        while len(storage) > k:
            storage[str1[window_start]] -= 1
            if storage[str1[window_start]] == 0:
                del storage[str1[window_start]]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 10)))


main()
