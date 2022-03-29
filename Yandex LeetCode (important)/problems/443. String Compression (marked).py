from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        first_pointer = result = 0

        while first_pointer < len(chars):
            second_pointer = first_pointer
            while second_pointer < len(chars) and chars[second_pointer] == chars[first_pointer]:
                second_pointer += 1

            chars[result] = chars[first_pointer]
            result += 1

            diff = second_pointer - first_pointer
            if diff > 1:
                # multiple characters like 10, 12, etc
                for digit in str(diff):
                    chars[result] = digit
                    result += 1

            first_pointer = second_pointer

        # you also can return a string result
        chars = ''.join(chars[:result])

        return result


print(Solution().compress(chars=["a", "a", "b", "b", "c", "c", "c"]))
