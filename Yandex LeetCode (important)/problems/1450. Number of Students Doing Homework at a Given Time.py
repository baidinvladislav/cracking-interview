from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        students = 0
        for i in range(len(endTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                students += 1
        return students


print(Solution().busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4))
