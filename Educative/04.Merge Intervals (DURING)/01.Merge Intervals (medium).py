"""
Given a list of intervals, merge all the overlapping intervals to produce a list
that has only mutually exclusive intervals.
"""


from __future__ import print_function


class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

    def __repr__(self):
        return f'[{self.start}, {self.end}]'


def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals on the start time
    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    # take the first interval as a reference point
    start = intervals[0].start
    end = intervals[0].end

    # find overlapping intervals start from second interval in the list
    for i in range(1, len(intervals)):
        interval = intervals[i]
        # if interval overlapped
        if interval.start <= end:
            # calculate its end
            end = max(interval.end, end)
        # if interval not overlapped
        else:
            # add to result list
            mergedIntervals.append(Interval(start, end))
            # change a reference point
            start = interval.start
            end = interval.end

    # add the last interval
    mergedIntervals.append(Interval(start, end))
    return mergedIntervals


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
