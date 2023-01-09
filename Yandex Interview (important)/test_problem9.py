"""
Даны две строки.

Написать функцию, которая вернёт True, если из первой строки можно получить вторую,
совершив не более 1 изменения (== удаление / замена символа).
"""


def solution(str1, str2):
    stack = []
    p1 = p2 = 0
    counter = max(len(str1), len(str2))
    while counter:
        if p1 < len(str1):
            stack.append(str1[p1])
            p1 += 1

        if p2 < len(str2):
            stack.append(str2[p2])
            p2 += 1

        if len(stack) > 1:
            if stack[-2] == stack[-1]:
                stack.pop(-2)
                stack.pop(-1)

        counter -= 1

    return len(stack) <= 2


def test_first():
    str1, str2 = "abec", "abc"
    expect = True

    assert expect == solution(str1, str2)


def test_second():
    str1, str2 = "abe", "abc"
    expect = True

    assert expect == solution(str1, str2)


def test_third():
    str1, str2 = "abc", "azz"
    expect = False

    assert expect == solution(str1, str2)


def test_fourth():
    str1, str2 = "abtce", "abce"
    expect = True

    assert expect == solution(str1, str2)
