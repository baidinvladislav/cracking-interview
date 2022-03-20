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


def gen_brackets(n, s='', opening=0, closing=0):

    if opening == n and closing == n:
        print(s)

    else:
        if opening < n:
            gen_brackets(n, s + '(', opening + 1, closing)

        if closing < opening:
            gen_brackets(n, s + ')', opening, closing + 1)


gen_brackets(n)
