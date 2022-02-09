import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        free_rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(free_rooms, intervals[0][1])

        for interval in intervals[1:]:
            if free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, interval[1])
        return len(free_rooms)


print(Solution().minMeetingRooms(intervals=[[0, 30], [5, 10], [15, 20]]))
