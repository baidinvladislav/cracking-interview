class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge them if first one has `end` greater than `start` of second one.

        Args:
            meetings: [tuple(), ..]
        Return:
            merged_intervals: [tuple(), ..]
        """
        intervals.sort(key=lambda x: x[0])
        # begin from the earliest
        merged_intervals = [intervals[0]]

        for (current_start, current_end) in intervals[1:]:
            last_merged_start, last_merged_end = merged_intervals[-1]
            if last_merged_end >= current_start:
                # update the last
                merged_intervals[-1] = last_merged_start, max(last_merged_end, current_end)
            else:
                # add new to the end
                merged_intervals.append((current_start, current_end))
        return merged_intervals