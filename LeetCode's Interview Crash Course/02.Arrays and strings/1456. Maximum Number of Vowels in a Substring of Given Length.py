# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        vowels = 0
        result = 0
        vowels_set = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

        for end in range(len(s)):
            if s[end] in vowels_set:
                vowels += 1

            while end - start + 1 > k:
                if s[start] in vowels_set:
                    vowels -= 1
                start += 1

            result = max(result, vowels)

        return result
