"""
Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить,
удалив ровно один элемент массива.

[1, 1, 0]
"""


def solution(arr):
    start = ones = result = 0
    for end in range(len(arr)):
        if arr[end] == 1:
            ones += 1

        if 1 < end - start + 1 - ones:
            if arr[start] == 1:
                ones -= 1
            start += 1
        result = max(result, end - start)

    return result


def test_first():
    nums = [1, 1, 0]
    expect = 2

    assert expect == solution(nums)


def test_second():
    nums = [1, 0, 1, 1, 1, 0, 0, 1]
    expect = 4

    assert expect == solution(nums)


def test_third():
    nums = [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0]
    expect = 7

    assert expect == solution(nums)
