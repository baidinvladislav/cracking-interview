"""
Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n,
упорядоченные лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).

В задаче используются только круглые скобки.

Желательно получить решение, которое работает за время,
пропорциональное общему количеству правильных скобочных последовательностей в ответе,
и при этом использует объём памяти, пропорциональный n.


https://sohabr.net/habr/post/420605/
https://habr.com/ru/post/191298/
https://hashsum.ru/generaciya-skobochnyx-posledovatelnostej/
"""


import sys


n = int(sys.stdin.readline())


def bracket(count, s='', left=0, right=0):
    if left == count and right == count:
        print(s)
    else:
        if left < count:
            bracket(count, s + '(', left+1, right)
        if right < left:
            bracket(count, s + ')', left, right+1)


bracket(n)
