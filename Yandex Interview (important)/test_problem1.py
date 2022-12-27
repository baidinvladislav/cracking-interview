"""
Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
Надо вернуть [1, 2, 2, 3] (порядок неважен).

Фактически нам нужно вернуть пересечение множеств, но с повторением элементов.
"""


def f(nums1, nums2):
    d = {}
    res = []
    for num in nums1:
        if num not in d:
            d[num] = 0
        d[num] += 1

    for num in nums2:
        if num in d:
            d[num] -= 1
            res.append(num)

            if num[d] == 0:
                del num[d]

    return res


# Time Complexity: O(n)
# Space Complexity: O(n * m)
def letter_count(arr):
    d = {}
    for item in arr:
        d[item] = d.get(item, 0) + 1
    return d


def solution(arr1, arr2):
    d1 = letter_count(arr1)
    d2 = letter_count(arr2)

    result = []
    for key, value in d1.items():
        if key in d2 and value != 0:
            value = min(value, d2[key])
            while value > 0:
                result.append(key)
                value -= 1

    return result


def test_first():
    arr1 = [1, 2, 3]
    arr2 = [1, 2]
    expect = [1, 2]

    assert expect == solution(arr1, arr2)


def test_second():
    arr1 = [1, 2, 3, 2, 0]
    arr2 = [5, 1, 2, 7, 3, 2]
    expect = [1, 2, 2, 3]

    assert expect == solution(arr1, arr2)


def test_third():
    arr1 = [1, 2, 3]
    arr2 = [1, 1]
    expect = [1]

    assert expect == solution(arr1, arr2)


def test_fourth():
    arr1 = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [1, 3, 3, 5, 7, 9]
    expect = [1, 3, 3, 5, 7, 9]

    assert expect == solution(arr1, arr2)


def test_fifth():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
    arr2 = [1, 6, 6, 8, 8]
    expect = [1, 6, 8, 8]

    assert expect == solution(arr1, arr2)
