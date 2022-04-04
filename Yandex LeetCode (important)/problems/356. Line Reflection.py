from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # remove duplicates
        points = set(map(tuple, points))

        # find max and min on x
        point_min_x = min(points, key=lambda x: x[0])
        point_max_x = max(points, key=lambda x: x[0])

        # calculate a line between min x and max x
        middle_line = (point_min_x[0] + point_max_x[0]) / 2

        for x, y in points:
            # create a mirror point
            mirror_point = (2 * middle_line - x, y)
            # check that a mirror point in the points
            if mirror_point not in points:
                return False
        return True


def main():
    print(Solution().isReflected(points=[[1, 1], [-1, 1]]))
    print(Solution().isReflected(points=[[1, 1], [-1, -1]]))


if __name__ == '__main__':
    main()
