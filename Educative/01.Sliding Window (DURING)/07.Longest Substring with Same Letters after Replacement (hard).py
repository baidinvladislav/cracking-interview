"""
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter,
find the length of the longest substring having the same letters after replacement.
"""


# Time Complexity: O(N)
# Space Complexity: O(1)
def length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    for window_end in range(len(str1)):
        # add character to hash-map
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        # tracking the most repeatable character
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])

        window_size = window_end - window_start + 1
        diff = window_size - max_repeat_letter_count
        # if window size includes unique symbols greater then number of available replacement
        if diff > k:
            # we'll shrink the window
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        # update max length if it greater then it was
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
