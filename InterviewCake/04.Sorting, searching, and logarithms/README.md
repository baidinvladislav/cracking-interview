# Sorting, searching, and logarithms
+ [Find Rotation Point](#find-rotation-point)
+ [Find Repeat, Space Edition](#find-repeat-space-edition)
+ [Top Scores](#top-scores)
+ [Merging Meeting Times](#merging-meeting-times)


## Find Rotation Point
Дан отсортированный массив с разворотом (rotate array).
Вернуть индекс разворота (rotation point).

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Находим центральный элемент.</li>
 <li>Если центральный элемент больше чем первый элемент, то идем вправо.</li>
 <li>Если центральный элемент меньше чем первый элемент, то идем влево.</li>
 <li>Если остается два элемента в массиве, нам нужно вернуть индекс 2-го элемента.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: ['cape', 'cake']
Output: 1

Example 2:
Input: ['grape', 'orange', 'plum', 'radish', 'apple']
Output: 4

Example 3:
Input: [
    'ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 
    'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage'
]
Output: 5
```

```python
# my code based on their solution
# Time Complexity: O(lg n)
# Space Complexity: O(1)
def find_rotation_point(words):
    first_element = words[0]
    start, end = 0, len(words) - 1

    while start < end:
        middle = (start + end) // 2

        if words[middle] > first_element:
            start = middle
        elif words[middle] < first_element:
            end = middle

        if middle + 1 == end:
            return end

```



## Find Repeat Space Edition
Дан неотсортированный массив чисел в диапозоне  1..n + 1.
В массиве как минимум один дубликат, найти дубликат.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Определить начало и конец массива.</li>
 <li>Определить центр массива.</li>
 <li>Определить нижнюю границу нижнего диапозона + определить верхнюю границу нижнего диапозона.</li>
 <li>Определить нижнюю границу верхнего диапозона + определить верхнюю границу верхнего диапозона.</li>
 <li>Подсчитать кол-во чисел в нижнем диапозоне.</li>
 <li>Подсчитать кол-во УНИКАЛЬНЫХ чисел в нижнем диапозоне.</li>
 <li>Если чисел в нижнем диапозоне больше чем уникальных чисел в нижнем диапозоне, значит сжать массив к нижнему диапозону.</li>
 <li>Иначе дубликат находится в верхнем диапозоне, значит сжать массив к верхнему диапозону.</li>
 <li>Когда указатели начала и конца массива сойдутся, мы получим дубликат под указателем начала массива.</li>
</ol>

</blockquote></details>

```
Example 1: 
Input: [1, 1]
Output: 1

Example 2:
Input: [1, 2, 3, 2]
Output: 2

Example 3:
Input: [1, 2, 5, 5, 5, 5]
Output: 5

Example 4:
Input: [4, 1, 4, 8, 3, 2, 7, 6, 5]
Output: 4
```

```python
# their solution 
# Time Complexity: O(n lg n)
# Space Complexity: O(1)
def find_repeat(numbers):
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint + 1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in numbers:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = lower_range_ceiling - lower_range_floor + 1

        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor

```


## Top Scores
Дан неотсортированный массив чисел и максимальное число, которое может быть в массиве.
Отсортировать массив за время лучшее чем O(n * lg n).
Массив может содержать дубликаты.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Используем "Сортировку подсчётом".</li>
 <li>Создать массив размером с самое максимальное число, которое может быть во входном массиве.</li>
 <li>Индексы созданного массива означают числа входного массива, значения - кол-во появлений числа во входном массиве.</li>
 <li>Итерируем с конца созданный массив, добавляем индексы массивы как числа в результирующий массив, если значение индекса != 0.</li>
</ol>

</blockquote></details>

```
Example 1: 
Input: [], 100
Output: []

Example 2:
Input: [55], 100
Output: [55]

Example 3:
Input: [30, 60], 100
Output: [60, 30]

Example 4:
Input: [37, 89, 41, 65, 91, 53], 100
Output: [91, 89, 65, 53, 41, 37]

Example 5:
Input: [20, 10, 30, 30, 10, 20], 100
Output: [30, 30, 20, 20, 10, 10]
```

```python
# their solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def sort_scores(unsorted_scores, highest_possible_score):
    # List of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score + 1)

    # Populate score_counts
    for score in unsorted_scores:
        score_counts[score] += 1

    # Populate the final sorted list
    sorted_scores = []

    # For each item in score_counts
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        # For the number of times the item occurs
        for time in range(count):
            # Add it to the sorted list
            sorted_scores.append(score)

    return sorted_scores

```


## Merging Meeting Times
Дан массив интервалов, смержите пересекающиеся интервалы.
Вернуть массив смерженных интервалов.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Отсортировать инпут по первым элемента кортежа.</li>
 <li>Инициализировать старт и конец.</li>
 <li>Смержить интервалы, если они пересекаются.</li>
 <li>Добавить, в результат, если не пересекаются, обновить старт и конец.</li>
 <li>После завершения цикла добавить последний элемент в результат.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [(1, 3), (2, 4)]
Output: [(1, 4)]

Example 2:
Input: [(5, 6), (6, 8)]
Output: [(5, 8)]

Example 3:
Input: [(1, 8), (2, 5)]
Output: [(1, 8)]
```

```python
# time: O(n log n) - because of sorting
# space: O(n) - in worse case will save all items
def merge_ranges(meetings):
    meetings.sort(key=lambda x: x[0])
    result = []
    start, end = meetings[0][0], meetings[0][1]
    for new_start, new_end in meetings[1:]:
        if end >= new_start:
            end = max(end, new_end)
        else:
            result.append((start, end))

            start = new_start
            end = new_end

    result.append((start, end))
    return result

```
