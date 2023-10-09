# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character,
# and do the same with the other character.

# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
#
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        array1 = [0] * 26
        array2 = [0] * 26

        for char in word1:
            array1[ord(char) - ord("a")] += 1

        for char in word2:
            array2[ord(char) - ord("a")] += 1

        for i in range(26):
            if (array1[i] > 0 and array2[i] == 0) or (array2[i] > 0 and array1 == 0):
                return False

        array1.sort()
        array2.sort()

        return array1 == array2
