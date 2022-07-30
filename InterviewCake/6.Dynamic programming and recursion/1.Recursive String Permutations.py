import unittest


# InterviewCake solution
def get_permutations(string):
    # Base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # Recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

    # Put the last char in all possible positions for each of
    # the above permutations
    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = (
                    permutation_of_all_chars_except_last[:position]
                    + last_char
                    + permutation_of_all_chars_except_last[position:]
            )
            permutations.add(permutation)

    return permutations


# GeeksforGeeks solution

# Python program to print all permutations with
# duplicates allowed

def toString(List):
    return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(string, left, right):
    if left == right:
        print(toString(string))
    else:
        for i in range(left, right):
            string[left], string[i] = string[i], string[left]
            permute(string, left + 1, right)
            string[left], string[i] = string[i], string[left]  # backtrack


# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n)


class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
