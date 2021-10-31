"""
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's
to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.
"""


# input decimal -> convert to binary system -> !bool -> convert back to decimal
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        result = ''
        for ch in bin(n)[2:]:
            if ch == '0':
                result += '1'

            elif ch == '1':
                result += '0'

        return int(result, base=2)


print(Solution().bitwiseComplement(n=5))
