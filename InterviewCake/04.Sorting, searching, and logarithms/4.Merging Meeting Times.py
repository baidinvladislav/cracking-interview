import unittest


# my code
# time: O(n log n) - because of sorting
# space: O(n) - in worse case will save all items
def merge_ranges(meetings):
    meetings.sort(key=lambda x: x[0])
    result = []
    start, end = meetings[0][0], meetings[0][1]
    for new_start, new_end in meetings[1:]:
        if end >= new_start:
            end = max(end, new_end)
        else:
            result.append((start, end))

            start = new_start
            end = new_end

    result.append((start, end))
    return result


# their solution
# Time complexity: O(n lg n)
# Space complexity: O(n)
def merge_ranges(meetings):
    """
    Merge them if first one has `end` greater than `start` of second one.

    Args:
        meetings: [tuple(), ..]
    Return:
        merged_intervals: [tuple(), ..]
    """
    meetings.sort(key=lambda x: x[0])
    # begin from the earliest
    merged_intervals = [meetings[0]]

    for (current_start, current_end) in meetings[1:]:
        last_merged_start, last_merged_end = merged_intervals[-1]
        if last_merged_end >= current_start:
            # update the last
            merged_intervals[-1] = last_merged_start, max(last_merged_end, current_end)
        else:
            # add new to the end
            merged_intervals.append((current_start, current_end))
    return merged_intervals


class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)
