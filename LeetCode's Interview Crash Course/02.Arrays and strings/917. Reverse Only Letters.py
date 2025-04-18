# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"

# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


# Time: O(n)
# Space: O(n)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [char for char in s if char.isalpha()]
        result = []
        for char in s:
            if char.isalpha():
                result.append(letters.pop())
            else:
                result.append(char)

        return "".join(result)
