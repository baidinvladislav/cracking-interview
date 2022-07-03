def merge_ranges(intervals):
    intervals.sort(key=lambda x: x[0])

    start = intervals[0][0]
    end = intervals[0][1]

    result = []
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if end >= interval[0]:
            end = max(end, interval[1])
        else:
            result.append((start, end))
            start = interval[0]
            end = interval[1]

    result.append((start, end))

    return result


expected = [(0, 1), (3, 8), (9, 12)]
result = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
assert expected == result
