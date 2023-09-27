# Given two strings ransomNote and magazine, return true if ransomNote can be constructed
# by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = defaultdict(int)
        for char in magazine:
            hash_map[char] += 1

        for char in ransomNote:
            if char in hash_map:
                hash_map[char] -= 1
                if hash_map[char] == 0:
                    del hash_map[char]
            else:
                return False

        return True
