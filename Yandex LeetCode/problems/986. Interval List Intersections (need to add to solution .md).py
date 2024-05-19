from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            # Determine the intersection between firstList[i] and secondList[j]
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # Check if there is a valid intersection
            if start <= end:
                result.append([start, end])

            # Move the pointer that has the smaller end value
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result

# paused 20:20