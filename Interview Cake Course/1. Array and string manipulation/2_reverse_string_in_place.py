import unittest


# Time complexity: O(n)
# Space complexity: O(1)
def reverse(list_of_chars):
    start, end = 0, len(list_of_chars) - 1
    while start < end:
        list_of_chars[start], list_of_chars[end] = list_of_chars[end], list_of_chars[start]

        start += 1
        end -= 1


class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)
