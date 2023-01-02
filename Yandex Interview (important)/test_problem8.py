"""
Дан массив точек с целочисленными координатами (x, y). Определить, существует ли вертикальная прямая,
делящая точки на 2 симметричных относительно этой прямой множества. Note: Для удобства точку можно
представлять не как массив [x, y], а как объект {x, y}
"""


# Time Complexity: O(n)
# Space Complexity: O(n)
def solution(points):
    the_most_left_x = min(points, key=lambda x: x[0])
    the_most_right_x = max(points, key=lambda x: x[0])

    middle_x = (the_most_left_x[0] + the_most_right_x[0]) / 2
    for x, y in points:
        symmetry_point = (2 * middle_x - x, y)
        # set's O(1) instead of list's O(n)
        if symmetry_point in set(map(tuple, points)):
            return True

    return False


def test_first():
    points = [[1, 1], [-1, 1]]
    expect = True

    assert expect == solution(points)


def test_second():
    points = [[1, 1], [-1, -1]]
    expect = False

    assert expect == solution(points)


def test_third():
    points = [[2, 0], [2, 6], [6, 6], [0, 6]]
    expect = True

    assert expect == solution(points)


def test_fourth():
    points = [[2, 0], [2, 6], [6, 7], [0, 6]]
    expect = False

    assert expect == solution(points)
