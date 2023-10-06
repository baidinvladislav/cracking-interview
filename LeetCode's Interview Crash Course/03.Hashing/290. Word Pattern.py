# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s) != len(pattern):
            return False

        dict_characters = {}
        dict_words = {}

        for i in range(len(pattern)):
            if pattern[i] not in dict_characters and s[i] not in dict_words:
                dict_characters[pattern[i]] = s[i]
                dict_words[s[i]] = pattern[i]
            else:
                if dict_characters.get(pattern[i]) != s[i] or dict_words.get(s[i]) != pattern[i]:
                    return False

        return True
