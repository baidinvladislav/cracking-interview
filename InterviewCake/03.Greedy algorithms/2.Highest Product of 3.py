import unittest


# my code based on their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def highest_product_of_3(list_of_ints):
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    highest_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_of_2 = list_of_ints[0] * list_of_ints[1]

    highest_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for i in range(2, len(list_of_ints)):
        highest_of_3 = max(
            highest_of_3,
            highest_of_2 * list_of_ints[i],
            lowest_of_2 * list_of_ints[i]
        )

        highest_of_2 = max(
            highest_of_2,
            highest * list_of_ints[i],
            lowest * list_of_ints[i]
        )

        lowest_of_2 = min(
            lowest_of_2,
            highest * list_of_ints[i],
            lowest * list_of_ints[i]
        )

        highest = max(highest, list_of_ints[i])
        lowest = max(lowest, list_of_ints[i])

    return highest_of_3


# my brute force solution
# Time Complexity: O(n**3)
# Space Complexity: O(1)
def highest_product_of_3(list_of_ints):
    result = float('-inf')
    for i in range(len(list_of_ints)):
        for j in range(i + 1, len(list_of_ints)):
            for y in range(j + 1, len(list_of_ints)):
                current_result = list_of_ints[i] * list_of_ints[j] * list_of_ints[y]
                result = max(result, current_result)
    return result


# their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # We could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    # Except this one--we pre-populate it for the first *3* items.
    # This means in our first pass it'll check against itself, which is fine.
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # Walk through items, starting at index 2
    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        # Do we have a new highest product of 3?
        # It's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_3 = max(
            highest_product_of_3,
            current * highest_product_of_2,
            current * lowest_product_of_2
        )

        # Do we have a new highest product of two?
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest
        )

        # Do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest
        )

        # Do we have a new highest?
        highest = max(highest, current)

        # Do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_3


class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
