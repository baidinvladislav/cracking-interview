"""
Write a code that checks that a string is formed by one cyclic shift
"""
import unittest


def is_substring(string, sub):
    return string.find(sub) != -1


def is_cyclic_shift(str1, str2):
    if len(str1) == len(str2) != 0:
        return is_substring(str1 * 2, str2)
    return False


class Test(unittest.TestCase):
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_is_cyclic_shift(self):
        for [str1, str2, expected] in self.data:
            actual = is_cyclic_shift(str1, str2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
