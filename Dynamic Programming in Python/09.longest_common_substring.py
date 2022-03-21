"""
Given two strings, we want to find the length of the longest substring common in both these strings.
For example, if we have two strings, "hello elf" and "hello yourself",
we can see two prominent substrings: "hello " and "elf".
Since "hello " is longer, this will be the longest common substring for the given pair of strings.
"""


def find_substr(str1, str2, i, j, count):
    # base case of when either of string has been exhausted
    if i >= len(str1) or j >= len(str2):
        return count

    # if i and j character matches, increment the count and compare the rest of the strings
    if str1[i] == str2[j]:
        count = find_substr(str1, str2, i + 1, j + 1, count + 1)

    # compare str1[1:] with str2, str1 with str2[1:], and take max of current count and these two results
    return max(count, find_substr(str1, str2, i + 1, j, 0), find_substr(str1, str2, i, j + 1, 0))


def main():
    print(find_substr("hello elf", "hello yourself", 0, 0, 0))  # 6
    print(find_substr("hel", "elf", 0, 0, 0))  # 2


main()
