"""
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters
while finding permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters.
For example, here are the six anagrams of the string “abc”:

     * abc
     * acb
     * bac
     * bca
     * cab
     * cba

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
"""


def find_string_anagrams(str1, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    # insert all character from pattern to hash-map
    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    result_indices = []
    # extend our window and if right char in hash-map then decrease their value
    # and if their value equals 0 increase matched variable by 1
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):  # Have we found an anagram?
            result_indices.append(window_start)

        # shrink the sliding window
        # if window size greater then pattern length
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            # if left char in hash-map and their value equals 0
            # then decrease matched variable by 1 because we lose one match
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                # increase by 1 because we face part of pattern again
                char_frequency[left_char] += 1

    return result_indices


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
