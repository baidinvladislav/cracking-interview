"""
Даны даты заезда и отъезда каждого гостя. Для каждого гостя дата заезда строго
раньше даты отъезда (то есть каждый гость останавливается хотя бы на одну ночь).
В пределах одного дня считается, что сначала старые гости выезжают, а затем въезжают новые.
Найти максимальное число постояльцев, которые одновременно проживали в гостинице (считаем,
что измерение количества постояльцев происходит в конце дня).

sample = [ (1, 2), (1, 3), (2, 4), (2, 3), ]
"""


# Time Complexity: O(n * m)
# Space Complexity: O(n)
def solution(guests):
    first_day, last_day = float("inf"), float("-inf")
    for guest in guests:
        first_day = min(first_day, guest[0])
        last_day = max(last_day, guest[1])

    days = [0] * last_day
    for d in range(1, len(days)):
        for g in range(len(guests)):
            if guests[g][0] <= d < guests[g][1]:
                days[d] += 1

    return max(days)


def test_first():
    nums = [(1, 2), (1, 3), (2, 4), (2, 3)]
    expect = 3

    assert expect == solution(nums)


def test_second():
    nums = [(1, 3), (2, 5), (4, 5), (2, 4), (3, 4)]
    expect = 3

    assert expect == solution(nums)


def test_third():
    nums = [(1, 2), (2, 3), (3, 5), (4, 5)]
    expect = 2

    assert expect == solution(nums)


def test_fourth():
    nums = [(1, 2), (2, 3), (3, 4)]
    expect = 1

    assert expect == solution(nums)
