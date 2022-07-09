def merge_ranges(meetings):
    meetings.sort(key=lambda x: x[0])
    merged_intervals = [meetings[0]]

    for (current_start, current_end) in meetings[1:]:
        last_merged_start, last_merged_end = merged_intervals[-1]
        if last_merged_end >= current_start:
            merged_intervals[-1] = last_merged_start, max(last_merged_end, current_end)
        else:
            merged_intervals.append((current_start, current_end))
    return merged_intervals


expected = [(0, 1), (3, 8), (9, 12)]
result = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
assert expected == result
