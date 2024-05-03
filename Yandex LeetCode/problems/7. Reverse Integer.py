class Solution:
    def reverse(self, x):
        INT_MAX = 2 ** 31 - 1  # 2,147,483,647
        INT_MIN = -2 ** 31  # -2,147,483,648

        result = 0
        negative = x < 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check if appending the digit will cause overflow
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0  # This would cause an overflow

            result = result * 10 + digit

        if negative:
            result = -result

        return result
