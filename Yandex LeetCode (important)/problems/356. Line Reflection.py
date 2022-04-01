from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # remove duplicates
        points = set(map(tuple, points))

        # find max and min on x
        minx, _ = min(points, key=lambda x: x[0])
        maxx, _ = max(points, key=lambda x: x[0])

        # calculate a line between min x and max x
        rx = (minx + maxx) / 2

        result = []
        for x, y in points:
            # create a mirror point
            point = (2 * rx - x, y)
            # check that a mirror point in the points
            result.append(point in points)

        # return True if we have all mirrors points otherwise False
        return all(result)


def main():
    print(Solution().isReflected(points=[[1, 1], [-1, 1]]))
    print(Solution().isReflected(points=[[1, 1], [-1, -1]]))


if __name__ == '__main__':
    main()
