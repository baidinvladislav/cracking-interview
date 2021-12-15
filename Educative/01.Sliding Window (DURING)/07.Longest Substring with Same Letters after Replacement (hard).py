"""
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter,
find the length of the longest substring having the same letters after replacement.
"""


# Time Complexity: O(N)
# Space Complexity: O(1) - because there are only 26 symbols in alphabet
def length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat = 0, 0, 0
    dict_index = {}

    for window_end in range(len(str1)):
        if str1[window_end] not in dict_index:
            dict_index[str1[window_end]] = 0
        dict_index[str1[window_end]] += 1
        max_repeat = max(max_repeat, dict_index[str1[window_end]])

        if k < window_end - window_start + 1 - max_repeat:
            dict_index[str1[window_start]] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring("aaaaaaacc", 2))
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
