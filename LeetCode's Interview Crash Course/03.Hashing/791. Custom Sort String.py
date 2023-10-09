# You are given two strings order and s. All the characters of order are unique
# and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically,
# if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

# Example 1:
# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation:
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in order,
# it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

# Example 2:
# Input: order = "cbafg", s = "abcd"
# Output: "cbad"


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Create a frequency dictionary for characters in s
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        # Build the result string based on order and character frequencies
        result = []
        for char in order:
            if char in char_freq:
                result.append(char * char_freq[char])
                del char_freq[char]  # Remove processed character from the dictionary

        # Append remaining characters (not in order) to the result
        for char, freq in char_freq.items():
            result.append(char * freq)

        # Join the result list to form the final string
        return "".join(result)
