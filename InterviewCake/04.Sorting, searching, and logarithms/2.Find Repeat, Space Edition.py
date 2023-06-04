import unittest


# my code based on their solution
# Time Complexity: O(n lg n)
# Space Complexity: O(1)
def find_repeat(numbers):
    left, right = 1, len(numbers) - 1
    while left < right:
        middle = (left + right) // 2

        low_subbarray_left = left
        low_subbarray_right = middle

        high_subbarray_left = middle + 1
        high_subbarray_right = right

        number_of_items_low_subbarray = 0
        for number in numbers:
            if low_subbarray_left <= number <= low_subbarray_right:
                number_of_items_low_subbarray += 1

        unique_number_of_items_low_subbarray = low_subbarray_right - low_subbarray_left + 1
        if unique_number_of_items_low_subbarray < number_of_items_low_subbarray:
            left, right = low_subbarray_left, low_subbarray_right
        else:
            left, right = high_subbarray_left, high_subbarray_right

    return left


# their solution
# Time Complexity: O(n lg n)
# Space Complexity: O(1)
def find_repeat(numbers):
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint + 1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in numbers:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = lower_range_ceiling - lower_range_floor + 1

        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor


class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
