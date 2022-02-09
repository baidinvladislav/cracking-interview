from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        start, end = 0, 1

        for i in range(1, len(intervals)):
            if intervals[i - 1][end] > intervals[i][start]:
                return False
        return True


print(Solution().canAttendMeetings(intervals=[[0, 30], [5, 10], [15, 20]]))
print(Solution().canAttendMeetings(intervals=[[7, 10], [2, 4]]))
