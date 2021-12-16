"""
Given a list of non-overlapping intervals sorted by their start time,
insert a given interval at the correct position and merge all necessary intervals
to produce a list that has only mutually exclusive intervals.
"""


def insert(intervals, new_interval):
    start, end = 0, 1
    counter = 0
    merged_arr = []

    # add to result array all intervals that come before new interval
    while counter < len(intervals) and intervals[counter][end] < new_interval[start]:
        merged_arr.append(intervals[counter])
        counter += 1

    # merge overlapping intervals with new interval
    while counter < len(intervals) and new_interval[end] >= intervals[counter][start]:
        new_interval[start] = min(intervals[counter][start], new_interval[start])
        new_interval[end] = max(intervals[counter][end], new_interval[end])
        counter += 1

    # insert merged new interval with all overlapping intervals
    merged_arr.append(new_interval)

    # insert other intervals into result array
    while counter < len(intervals):
        merged_arr.append(intervals[counter])
        counter += 1

    return merged_arr


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
