def summaryRanges(nums):
    ranges = []
    n = len(nums)
    if n == 0:
        return ranges

    # Начало текущего диапазона
    start = nums[0]

    for i in range(1, n):
        # Если текущий элемент не является последовательным
        if nums[i] != nums[i - 1] + 1:
            # Проверяем, если start равен предыдущему элементу
            if start == nums[i - 1]:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}->{nums[i - 1]}")
            # Обновляем начало диапазона
            start = nums[i]

    # Добавляем последний диапазон
    if start == nums[-1]:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}->{nums[-1]}")

    return ranges


# Примеры использования:
print(summaryRanges([0, 1, 2, 4, 5, 7]))  # Вывод: ["0->2", "4->5", "7"]
print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))  # Вывод: ["0", "2->4", "6", "8->9"]
