"""
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters
while finding permutations of a string, we get N! permutations (or anagrams) of a string having NN characters.

For example, here are the six anagrams of the string “abc”:

     * abc
     * acb
     * bac
     * bca
     * cab
     * cba

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
"""


# Time Complexity: O(N+M)
# Space Complexity: O(M)
def find_string_anagrams(str1, pattern):
    """
    The same algorithm as in 01.Sliding Window/09.Permutation in a String.
    With the only difference that here we return the indices in the resulting array
    and in 01.Sliding Window/09.Permutation in a String we return only boolean value.
    """
    window_start, matched, char_frequency = 0, 0, {}

    for ch in pattern:
        if ch not in char_frequency:
            char_frequency[ch] = 0
        char_frequency[ch] += 1

    result_indices = []
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            result_indices.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return result_indices


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
