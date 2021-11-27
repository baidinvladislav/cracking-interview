"""
Given a string, find the length of the longest substring,
which has all distinct characters.
"""


def non_repeat_substring(str1):
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_index_map:

            # why used max function?
            # we get the same result when we assign `char_index_map[right_char] + 1` to `window_start`
            # window_start = char_index_map[right_char] + 1
            window_start = max(window_start, char_index_map[right_char] + 1)

        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
    # test case explanations why we used max function
    # without max function = 'cadcbefg'
    # with max function = 'adcbefg'
    print("Length of the longest substring: " + str(non_repeat_substring("abcadcbefg")))


main()
