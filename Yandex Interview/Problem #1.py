"""
Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
Надо вернуть [1, 2, 2, 3] (порядок неважен).

Фактически нам нужно вернуть пересечение множеств, но с повторением элементов.
"""


class Solution:
    def find_intersections(self, l1, l2):
        result = []
        for number in l1:
            if number in l2:
                result.append(number)
        return result

    def find_intersections_const_space(self, l1, l2):
        for i in range(len(l1)):
            if l1[i] not in l2:
                l1.pop(i)  # or use l1.remove(number)
        return l1


print(Solution().find_intersections_const_space(l1=[1, 2, 3, 2, 0], l2=[5, 1, 2, 7, 3, 2]))
