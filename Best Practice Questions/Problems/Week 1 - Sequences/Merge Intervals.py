import unittest


class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])
        merged_intervals = []

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if end >= interval[0]:
                end = max(interval[1], end)
            else:
                merged_intervals.append([start, end])
                start = interval[0]
                end = interval[1]

        merged_intervals.append([start, end])
        return merged_intervals


class TestMergeIntervals(unittest.TestCase):
    def test_first(self):
        self.assertEqual([[1, 6], [8, 10], [15, 18]], Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))

    def test_second(self):
        self.assertEqual([[1, 5]], Solution().merge(intervals=[[1, 4], [4, 5]]))


if __name__ == "__main__":
    unittest.main()
