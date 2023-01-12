class Solution:
    def insert(self, intervals, newInterval):
        start, end = 0, 1
        counter = 0
        merged_arr = []

        # add to result array all intervals that come before new interval
        while counter < len(intervals) and intervals[counter][end] < newInterval[start]:
            merged_arr.append(intervals[counter])
            counter += 1

        # merge overlapping intervals with new interval
        while counter < len(intervals) and newInterval[end] >= intervals[counter][start]:
            newInterval[start] = min(intervals[counter][start], newInterval[start])
            newInterval[end] = max(intervals[counter][end], newInterval[end])
            counter += 1

        # insert merged new interval with all overlapping intervals
        merged_arr.append(newInterval)

        # insert other intervals into result array
        while counter < len(intervals):
            merged_arr.append(intervals[counter])
            counter += 1

        return merged_arr
