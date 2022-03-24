class Solution:
    # time complexity : O(n)
    # space complexity : O(n)
    def isValid(self, s):
        hash_map = {")": "(", "}": "{", "]": "["}
        # stack to keep track of opening brackets
        stack = []

        for char in s:
            # if the character is a closing bracket
            if char in hash_map:
                # pop the topmost element from the stack, if it is not empty
                # otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else "#"
                # the mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if hash_map[char] != top_element:
                    return False
            else:
                # we have an opening bracket, simply push it onto the stack
                stack.append(char)

        # in the end, if the stack is empty, then we have a valid expression
        # the stack won't be empty for cases like ((()
        return not stack


def main():
    print(Solution().isValid(s="()"))
    print(Solution().isValid(s="()[]{}"))
    print(Solution().isValid(s="(]"))


main()
