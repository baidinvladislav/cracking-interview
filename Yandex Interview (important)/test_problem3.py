"""
Дан список интов, повторяющихся элементов в списке нет.
Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.

Примеры:
[1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
[1,4,3,2] => "1-4"
[1,4] => "1,4"
"""


def solution(nums):
    pass


def test_first():
    nums = [1, 2, 3]
    expect = "1-3"

    assert expect == solution(nums)


def test_second():
    nums = [1, 2, 4, 5, 6, 8]
    expect = "1-2,4-6,8"

    assert expect == solution(nums)


def test_third():
    nums = [1, 4, 5, 2, 3, 9, 8, 11, 0]
    expect = "0-5,8-9,11"

    assert expect == solution(nums)


def test_fourth():
    nums = [1, 4, 3, 2]
    expect = "1-4"

    assert expect == solution(nums)


def test_fifth():
    nums = [1, 4]
    expect = "1,4"

    assert expect == solution(nums)
