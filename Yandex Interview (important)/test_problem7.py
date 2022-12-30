"""
Слияние отрезков:

Вход: [1, 3] [100, 200] [2, 4]
Выход: [1, 4] [100, 200]
"""


# Time Complexity: O(n)
# Space Complexity: O(n)
def solution(intervals):
    intervals.sort(key=lambda x: x[0])
    result = []

    interval = intervals[0]
    for i in range(1, len(intervals)):
        if interval[1] > intervals[i][0]:
            interval[1] = max(interval[1], intervals[i][1])
        else:
            result.append([interval[0], interval[1]])

            interval = intervals[i]

    result.append([interval[0], intervals[i][1]])
    return result


def test_first():
    intervals = [[1, 3], [100, 200], [2, 4]]
    expect = [[1, 4], [100, 200]]

    assert expect == solution(intervals)


def test_second():
    intervals = [[1, 3], [5, 7], [6, 9], [10, 15], [12, 16]]
    expect = [[1, 3], [5, 9], [10, 16]]

    assert expect == solution(intervals)


def test_third():
    intervals = [[100, 300], [200, 400], [700, 800], [750, 1000]]
    expect = [[100, 400], [700, 1000]]

    assert expect == solution(intervals)
