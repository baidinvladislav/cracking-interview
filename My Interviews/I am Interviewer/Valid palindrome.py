# Определить, что слово является палиндромом
#
# Example 1:
# Input: 'шалаш'
# Output: True
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: 'заказ'
# Output: True
#
# Example 3:
# Input: 'python'
# Output: False

# =================================================================================


# 1st approach is two pointers method
# Time Complexity: O(N)
# Space Complexity: O(1)
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# 2st approach is python slice
# Time Complexity: O(N)
# Space Complexity: O(N)
def isPalindrome(s: str) -> bool:
    return s == s[::-1]
