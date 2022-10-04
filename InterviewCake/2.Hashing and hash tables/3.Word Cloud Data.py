import unittest


# their solution
# Time Complexity: O(n)
# Space Complexity: O(n)
class WordCloudData:

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        # Iterates over each character in the input string, splitting
        # words and passing them to add_word_to_dictionary()
        current_word_start_index = 0
        current_word_length = 0
        for i, character in enumerate(input_string):

            # If we reached the end of the string we check if the last
            # character is a letter and add the last word to our dictionary
            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[
                        current_word_start_index:current_word_start_index + current_word_length
                    ]

                    self.add_word_to_dictionary(current_word)

            # If we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            # '\u2014 == '—'
            elif character == ' ' or character == '\u2014':
                if current_word_length > 0:
                    current_word = input_string[
                        current_word_start_index:current_word_start_index + current_word_length
                    ]

                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0

            # We want to make sure we split on ellipses so if we get two periods in
            # a row we add the current word to our dictionary and reset our current word
            elif character == '.':
                if i < len(input_string) - 1 and input_string[i + 1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[
                            current_word_start_index:current_word_start_index + current_word_length
                        ]

                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

            # If the character is a letter or an apostrophe, we add it to our current word
            elif character.isalpha() or character == '\'':
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1

            # If the character is a hyphen, we want to check if it's surrounded by letters
            # If it is, we add it to our current word
            elif character == '-':
                if i > 0 and input_string[i - 1].isalpha() and input_string[i + 1].isalpha():
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        current_word = input_string[
                            current_word_start_index:current_word_start_index + current_word_length
                        ]

                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

    def add_word_to_dictionary(self, word):
        # If the word is already in the dictionary we increment its count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # If a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # If an uppercase version is in the dictionary, we know our input word must be lowercase.
        # since we only include uppercase words if they're always uppercase, we add the
        # lowercase version and give it the uppercase version's count
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # Otherwise, the word is not in the dictionary at all, lowercase or uppercase
        # so we add it to the dictionary
        else:
            self.words_to_counts[word] = 1


class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
