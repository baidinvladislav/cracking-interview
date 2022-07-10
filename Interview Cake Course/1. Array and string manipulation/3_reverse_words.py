import unittest


def reverse_words(message):
    # reverse whole array
    reverse_characters(message, 0, len(message) - 1)

    # track word's start
    current_word_start_index = 0
    for i in range(len(message) + 1):
        # found the end of the current word!
        if (i == len(message)) or (message[i] == ' '):
            # reverse word
            current_word_end_index = i - 1
            reverse_characters(message, current_word_start_index, current_word_end_index)
            # next word's start is one character ahead
            current_word_start_index = i + 1


def reverse_characters(message, left_index, right_index):
    # walk towards the middle, from both sides
    while left_index < right_index:
        # swap the left char and right char
        message[left_index], message[right_index] = message[right_index], message[left_index]
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
