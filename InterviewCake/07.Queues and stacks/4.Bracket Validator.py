import unittest


# my code based on their solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_valid(code):
    parenths = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = []

    for char in code:
        if char in parenths:
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                last = stack.pop()
                if parenths[last] != char:
                    return False

    return len(stack) == 0


# their solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_valid(code):
    d = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    stack = []
    for char in code:
        if char in d:
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                last = stack.pop()
                if not char == d[last]:
                    return False

    return len(stack) == 0


class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)
