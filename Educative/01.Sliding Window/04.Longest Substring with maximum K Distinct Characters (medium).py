"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
"""


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
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_frequency) > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
