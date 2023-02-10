# Дано 2 отсортированных (по возрастанию) массива A и B длины M и N.
# Нужно объединить их в один отсортированный (по возрастанию) массив, состоящий из элементов первых двух.

# Ввод
# [1, 2, 5]
# [1, 2, 3, 4, 6]
# Вывод
# [1, 1, 2, 2, 3, 4, 5, 6]


# Ввод
# []
# [3, 4, 6]
# Вывод
# [1,1,2,2,5]


def solution(arr1, arr2):
    result = []
    while arr1 or arr2:
        if arr1:
            result.append(arr1.pop(0))

        if arr2:
            result.append(arr2.pop(0))

    return result

    # arr1.expend(arr2)
    # return arr1.sort()

    # if arr1 < arr2:
    #     arr1, arr2 = arr2, arr1

    # for item in arr2:
    #     if not item in arr1:
    #         arr1.append(item)

    # return arr1.sort()


print(solution([1, 2, 5], [1, 2, 3, 4, 6]))


# Дан список целых неповторяющихся чисел и целое число.
# Необходимо найти все пары в списке, сумма которых равна заданному числу.
# Перестановки (i, j) и (j, i) считаются одной и той же парой, нужно вывести только одну из них (любую).

# Ввод: [2, 4, 5, 3], 7
# Вывод: [ [2, 5], [4, 3] ]


# Time Complexity: O(n log n)
# Space Complexity: O(n)
def solution(arr1, target):
    # n log n
    arr1.sort()

    left, right = 0, len(arr1) - 1
    result = set()

    while left < right:
        current_sum = arr1[left] + arr1[right]
        if current_sum == target:
            if (left, right) and (right, left) not in result:
                result.add((arr1[left], arr1[right]))

                left += 1
                right -= 1

        elif current_sum < target:
            left += 1

        elif current_sum > target:
            right -= 1

    return result


print(solution([2, 4, 5, 3], 7))
