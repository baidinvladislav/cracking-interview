class Solution:
    # Time complexity : O(n log n)
    # Space complexity : O(n log n)
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        merged_intervals = []
        intervals.sort(key=lambda x: x[0])

        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                merged_intervals.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        merged_intervals.append([start, end])
        return merged_intervals
