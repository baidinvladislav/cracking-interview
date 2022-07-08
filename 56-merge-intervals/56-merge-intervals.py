class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_start, last_end = merged_intervals[-1]
            
            if start <= last_end:
                merged_intervals[-1] = [last_start, max(end, last_end)]
            else:
                merged_intervals.append([start, end])
        
        return merged_intervals
            
            