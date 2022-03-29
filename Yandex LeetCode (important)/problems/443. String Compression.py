from typing import List


class Solution:
    # https://www.youtube.com/watch?v=IhJgguNiYYk
    def compress(self, chars: List[str]) -> int:
        i = 0
        to = 0

        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            num = j - i
            chars[to] = chars[i]
            to += 1
            if num > 1:
                for digit in str(num):
                    chars[to] = digit
                    to += 1
            i = j
        chars = chars[:to]
        return to


print(Solution().compress(chars=["a", "a", "b", "b", "c", "c", "c"]))
