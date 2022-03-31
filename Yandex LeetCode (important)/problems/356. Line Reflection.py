from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = set(map(tuple, points))
        minx, _ = min(points, key=lambda x: x[0])
        maxx, _ = max(points, key=lambda x: x[0])
        rx = (minx + maxx) / 2

        result = []
        for x, y in points:
            is_occurrencied = (2 * rx - x, y) in points
            result.append(is_occurrencied)

        return all(result)


def main():
    print(Solution().isReflected(points=[[1, 1], [-1, 1]]))
    print(Solution().isReflected(points=[[1, 1], [-1, -1]]))


if __name__ == '__main__':
    main()
