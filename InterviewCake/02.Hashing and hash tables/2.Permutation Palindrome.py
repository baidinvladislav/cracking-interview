import unittest


# my code based on their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def has_palindrome_permutation(the_string):
    char_set = set()
    for char in the_string:
        if char not in char_set:
            char_set.add(char)
        else:
            char_set.remove(char)

    return len(char_set) <= 1


# their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def has_palindrome_permutation(the_string):
    s = set()

    for char in the_string:
        if char not in s:
            s.add(char)
        else:
            s.remove(char)

    return len(s) <= 1


class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
