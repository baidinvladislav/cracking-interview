"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example,
“abc” has the following six permutations:

    * abc
    * acb
    * bac
    * bca
    * cab
    * cba

If a string has ‘n’ distinct characters, it will have n! permutations.
"""


# Time Complexity: O(N+M)
# Space Complexity: O(M)
def find_permutation(str1, pattern):
    """
    1. Save all the symbols in the pattern with the number of repetitions.
    2. Increase the window size, decrease the frequency of the last character in window by 1.
    3. If the frequency of the last symbol is 0, then we found one match, increase the matched variable.
    4. If number of matches will be equal length of dictionary it means that string contains pattern permutation.
    5. If number of iteration greater than number of arrays elements we must shrink the window.
    6. If first element into window is equal 0, it means we'll lose one matched then we decrease matched variable.
    7. Increment new first element in window by 1.
    """
    window_start, matched, frequency_map = 0, 0, dict()

    for ch in pattern:
        if ch not in frequency_map:
            frequency_map[ch] = 0
        frequency_map[ch] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in frequency_map:
            frequency_map[right_char] -= 1
            if frequency_map[right_char] == 0:
                matched += 1

        if matched == len(frequency_map):
            return True

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in frequency_map:
                if frequency_map[left_char] == 0:
                    matched -= 1
                frequency_map[left_char] += 1

    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
