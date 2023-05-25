import unittest


# my code
# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse_string(string: list, start: int, end: int):
    while start < end:
        string[start], string[end] = string[end], string[start]

        start += 1
        end -= 1


def reverse_words(message):
    reverse_string(message, 0, len(message) - 1)

    start = 0
    for end in range(len(message) + 1):
        if end == len(message) or not message[end].isalpha():
            reverse_string(message, start, end - 1)
            start = end + 1


# their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse_words(message):
    # First we reverse all the characters in the entire message
    reverse_characters(message, 0, len(message) - 1)

    # This gives us the right word order
    # but with each word backward

    # Now we'll make the words forward again
    # by reversing each word's characters

    # We hold the index of the *start* of the current word
    # as we look for the *end* of the current word
    current_word_start_index = 0
    for i in range(len(message) + 1):
        # Found the end of the current word!
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            # If we haven't exhausted the message our
            # next word's start is one character ahead
            current_word_start_index = i + 1


def reverse_characters(message, left_index, right_index):
    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index += 1
        right_index -= 1


class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)
