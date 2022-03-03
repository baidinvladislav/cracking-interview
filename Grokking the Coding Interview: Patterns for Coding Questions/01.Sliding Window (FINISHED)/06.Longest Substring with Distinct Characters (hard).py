"""
Given a string, find the length of the longest substring,
which has all distinct characters.
"""


# Time Complexity: O(N)
# Space Complexity: O(K)
def non_repeat_substring(str1):
    window_start, max_length, hash_map = 0, 0, dict()

    for window_end in range(len(str1)):
        if str1[window_end] in hash_map:
            window_start = max(window_start, hash_map[str1[window_end]] + 1)

        hash_map[str1[window_end]] = window_end
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
