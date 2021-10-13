"""
Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n,
упорядоченные лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).

В задаче используются только круглые скобки.

Желательно получить решение, которое работает за время,
пропорциональное общему количеству правильных скобочных последовательностей в ответе,
и при этом использует объём памяти, пропорциональный n.


https://sohabr.net/habr/post/420605/
https://habr.com/ru/post/191298/
"""
import random


class Solution:
    def generate_sequence(self):
        import sys
        n = sys.stdin.readline().strip()

        if not 0 <= len(n) <= 11:
            print(f'Incorrect input data')
            return

        for i in range(int(n)):
            seq = ['(', ')'] * int(n)
            random.shuffle(seq)
            print(seq)

    def correct(self, seq):
        pass


Solution().generate_sequence()
