"""
Given two strings containing backspaces (identified by the character ‘#’),
check if the two strings are equal.
"""


def backspace_compare(str1, str2):
    """
    1. Set two pointer to the end both strings.
    2. Looping while we reach to the beginning of the strings.
    3. Get the index of a character that is not '#' for both strings.
    4. If we do not have positive indices for both strings, then we have reached the end of both strings.
    We return True because cycle was not break and string the same size.
    5. If we have not positive indexes for one string it means we reached to the end only one string.
    We return False because strings not the same size.
    6. If there are different characters under the indices we return False.
    """
    index1, index2 = len(str1) - 1, len(str2) - 1

    while index1 >= 0 or index2 >= 0:
        i1 = get_next_valid_char_index(str1, index1)
        i2 = get_next_valid_char_index(str2, index2)

        if i1 < 0 and i2 < 0:
            return True

        if i1 < 0 or i2 < 0:
            return False

        if str1[i1] != str2[i2]:
            return False

        index1 = i1 - 1
        index2 = i2 - 1

    return True


def get_next_valid_char_index(str, index):
    """
    1. If there is '#' under index we skip element decreasing index integer.
    2. Other case we return valid index.
    """
    backspace_count = 0

    while index >= 0:
        if str[index] == '#':
            backspace_count += 1

        elif backspace_count > 0:
            backspace_count -= 1

        else:
            break

        index -= 1

    return index


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
