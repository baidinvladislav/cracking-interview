from collections import deque


class Solution:
    def isValid(self, s):
        d = {'(': ')', '{': '}', '[': ']'}
        stack = deque()

        for char in s:
            if char in d:
                stack.append(char)
            else:
                if not stack:
                    return False

                if d[stack.pop()] != char:
                    return False

        return not stack
