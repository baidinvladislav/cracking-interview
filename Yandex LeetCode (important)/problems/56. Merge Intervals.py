from typing import List


class Solution:
    # Time complexity: O(n log n)
    # Space complexity: O(n log n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


def main():
    print(Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(Solution().merge(intervals=[[1, 4], [4, 5]]))


main()
