import unittest


# their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def get_closing_paren(sentence, opening_paren_index):
    counter = 0
    for i in range(opening_paren_index + 1, len(sentence)):
        char = sentence[i]

        if char == '(':
            counter += 1
        elif char == ')':
            if counter == 0:
                return i

            counter -= 1

    raise


class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)

    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)
