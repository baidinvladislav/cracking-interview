"""
Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.

Желательно получить решение, работающее за линейное время
и при этом проходящее по входному массиву только один раз.
"""


class Solution:

    def determine_sequence(self, sequence):
        n = len(sequence)
        count = 0
        max_count = 0

        for i in range(n):
            if sequence[i] == '1':
                count += 1
            else:
                count = 0

            max_count = max(count, max_count)

        return max_count


print(Solution().determine_sequence('100111011000110'))
