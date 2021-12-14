"""
Given a list of intervals representing the start and end time of ‘N’ meetings,
find the minimum number of rooms required to hold all the meetings.
"""


from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end

    def __repr__(self):
        return f'{self.start}:{self.end}'


def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)
    min_room, min_heap = 0, []

    for meeting in meetings:
        while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heappop(min_heap)

        heappush(min_heap, meeting)
        min_room = max(min_room, len(min_heap))
    return min_room


def main():
    print(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)]))
    print(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)]))
    print(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)]))
    print(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))


main()
