"""
Даны две строки.

Написать функцию, которая вернёт True, если из первой строки можно получить вторую,
совершив не более 1 изменения (== удаление / замена символа).
"""


def solution(str1, str2):
    stack = []
    p1 = p2 = 0
    while not (p1 == len(str1) - 1 and p2 == len(str2) - 1):
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

    return len(stack) <= 2


solution("abec", "abc")
