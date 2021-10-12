"""
Дан упорядоченный по неубыванию массив целых 32-разрядных чисел.
Требуется удалить из него все повторения.

Желательно получить решение, которое не считывает входной файл целиком в память,
т.е., использует лишь константный объем памяти в процессе работы.
"""


# with additional memory
class Solution:

    def remove_duplicates(self, arr):
        n = len(arr)
        res = []

        for i in range(n):
            if arr[i] not in res:
                res.append(arr[i])

        return res


print(Solution().remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5, 5]))


# memory N(1)
class Solution1:

    def remove_duplicates(self, arr):
        n = len(arr)
        numb_dupl = 0

        for i in range(1, n):
            if arr[i - 1] == arr[i]:
                numb_dupl += 1

        for i in range(1, n - numb_dupl + 1):
            if arr[i - 1] == arr[i]:
                arr[i - 1] = arr[i]
                arr.remove(i)

        return arr


print(Solution1().remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5]))
