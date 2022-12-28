# Yandex Interview
+ [Third Problem](#third_problem)


## Third Problem
Дан массив чисел без дубликатов, смержить интервалы чисел массива.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Отсортировать входной массив.</li>
 <li>Итерируем входной массив.</li>
 <li>Если разница соседних элементов массива равна 1, то обновить конечный элемент текущим элементом.</li>
 <li>Иначе добавить в результирующий массив смерженный интервал через дополнительную ф-ию, а также обновить start и end на текущий элемент.</li>
 <li>Последний смерженный интервал добавить вручную после цикла.</li>
 <li>Преобразовать результирующий массив в результирующую строку.</li>
 <li>Вернуть строку.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [1, 2, 3]
Output: "1-3"

Example 2:
Input: [1, 2, 4, 5, 6, 8]
Output: "1-2,4-6,8"

Example 3:
Input: [1, 4, 5, 2, 3, 9, 8, 11, 0]
Output: "0-5,8-9,11"
```

```python
def helper(group_start, group_end) -> str:
    if group_start == group_end:
        return str(group_end)

    return f'{group_start}-{group_end}'


# Time Complexity: O(n)
# Space Complexity: O(n)
def solution(numbers) -> str:
    numbers_ = sorted(numbers)

    result = []
    start = end = numbers_[0]
    for i in range(1, len(numbers_)):
        if end == numbers_[i] - 1:
            end = numbers_[i]
        else:
            result.append(helper(start, end))
            start = end = numbers_[i]

    result.append(helper(start, end))
    return ','.join(result)

```
