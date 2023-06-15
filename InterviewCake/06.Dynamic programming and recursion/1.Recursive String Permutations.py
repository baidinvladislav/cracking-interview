import unittest


# my code based on their solution
def get_permutations(string):
    if len(string) <= 1:
        return set([string])

    word_without_last_char = string[:-1]
    last_char = string[-1]
    perms_without_last_char = get_permutations(word_without_last_char)

    result = set()
    for perm in perms_without_last_char:
        for position in range(len(word_without_last_char) + 1):
            permutation = perm[position:] + last_char + perm[:position]
            result.add(permutation)

    return result


# cracking the coding interview solution
def generate_permutations(text):
    """
    1. Base case: len(nums) equal 1
    2. Separate first element from remainder
    3. Generate all possible subarrays based on remainder
    4. Looping through every subarray
    5. Insert first element inside every subarray in every possible place
    """
    if len(text) == 1:
        return [text]

    results = []
    first = text[0]
    remainder = text[1:]

    words = generate_permutations(remainder)
    for word in words:
        for i in range(len(word) + 1):
            # insert first char at each index/position of word
            s = word[:i] + first + word[i:]
            results.append(s)

    return results


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
