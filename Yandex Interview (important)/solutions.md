# Yandex Interview
+ [First Problem](#first-problem)
+ [Second Problem](#second-problem)
+ [Third Problem](#third-problem)
+ [Fourth Problem](#fourth-problem)
+ [Fifth Problem](#fifth-problem)
+ [Sixth Problem](#sixth-problem)
+ [Seventh Problem](#seventh-problem)
+ [Eighth Problem](#eighth-problem)
+ [Ninth Problem](#ninth-problem)
+ [Tenth Problem](#tenth-problem)
+ [Eleventh Problem](#eleventh-problem)


## First Problem
Даны два массива чисел, вернуть массив с общими элементами и с сохранением дубликатов.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Считаем в мапе кол-во чисел в каждом массиве.</li>
 <li>Формируем массив в котором содержатся одинаковые элементы.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: arr1 = [1, 2, 3], arr2 = [1, 2]
Output: [1, 2]

Example 2:
Input: arr1 = [1, 2, 3, 2, 0], arr2 = [5, 1, 2, 7, 3, 2]
Output: [1, 2, 2, 3]

Example 3:
Input: arr1 = [1, 2, 3], arr2 = [1, 1]
Output: [1]
```

```python
# Time Complexity: O(n)
# Space Complexity: O(n * m)
def solution(arr1, arr2):
    def letter_count(arr):
        d = {}
        for item in arr:
            d[item] = d.get(item, 0) + 1
        return d

    d1 = letter_count(arr1)
    d2 = letter_count(arr2)

    result = []
    for key, value in d1.items():
        if key in d2 and value != 0:
            value = min(value, d2[key])
            while value > 0:
                result.append(key)
                value -= 1

    return result

```


## Second Problem
.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>.</li>
 <li>.</li>
 <li>.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: 
Output: 

Example 2:
Input: 
Output:

Example 3:
Input:
Output:
```

```python


```


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


## Fourth Problem
Дан массив чисел с нулями и единицами, вернуть наибольшую длину последовательности из 1 при условии, 
что удалится ровно один элемент.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Итерируем индексы массива, подсчитывая кол-во единиц.</li>
 <li>Если в окне более чем один 0 - сжать окно, предварительно вычев 1 из счетчика единиц, если начальный индекс стоит на 1.</li>
 <li>На каждой итерации обновляем максимальную длину окна.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [1, 1, 0]
Output: 3

Example 2:
Input: [1, 0, 1, 1, 1, 0, 0, 1]
Output: 5

Example 3:
Input: [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0]
Output: 8
```

```python
# Time Complexity: O(n)
# Space Complexity: O(1)
def solution(arr):
    start = ones = result = 0
    for end in range(len(arr)):
        if arr[end] == 1:
            ones += 1

        if 1 < end - start + 1 - ones:
            if arr[start] == 1:
                ones -= 1
            start += 1
        result = max(result, end - start)

    return result

```


## Fifth Problem
Дан массив кортежей, где кортеж[i] - это гость, а кортеж[i][0] и кортеж[i][1] - день
заезда и день выезда гостя соответственно, найти максимальное кол-во
гостей в рамках одного дня.


<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Сначала нам нужно понять количество рассматриваемых нами дней, для этого проходим по массиву гостей и фиксируем первый день и последний день.</li>
 <li>Затем создаем массив с ячейкой для каждого дня.</li>
 <li>Идем по массиву дней и записываем в него каждого гостя, инкреминтуря число под индексом дня, если дата заезда гостя была в этот день или позже и строго меньше даты выезда гостя.</li>
 <li>Вернуть максимальное число из массива дней.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [(1, 2), (1, 3), (2, 4), (2, 3)]
Output: 3

Example 2:
Input: [(1, 3), (2, 5), (4, 5), (2, 4), (3, 4)]
Output: 3

Example 3:
Input: [(1, 2), (2, 3), (3, 5), (4, 5)]
Output: 2

Example 4:
Input: [(1, 2), (2, 3), (3, 4)]
Output: 1
```

```python
# Time Complexity: O(n * m)
# Space Complexity: O(n)
def solution(guests):
    first_day, last_day = float("inf"), float("-inf")
    for guest in guests:
        first_day = min(first_day, guest[0])
        last_day = max(last_day, guest[1])

    days = [0] * last_day
    for d in range(1, len(days)):
        for g in range(len(guests)):
            if guests[g][0] <= d < guests[g][1]:
                days[d] += 1

    return max(days)

```


## Sixth Problem
Дан массив строк, сгруппировать строки по символьным группам.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Итерируем входной массив.</li>
 <li>Сортируем каждую строку.</li>
 <li>Вставляем в мапу слово как значение, а ключ будет отсортированным словом.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Example 2:
Input: ["xyz", "abc", "qwe", "yxz", "cab", "eqw", "zyx", "bca", "wqe"]
Output: [["xyz", "yxz", "zyx"], ["abc", "cab", "bca"], ["qwe", "eqw", "wqe"]]

Example 3:
Input: ["jkl", "cvb", "lkj", "qaz", "vcb", "kjl"]
Output: [["jkl", "lkj", "kjl"], ["cvb", "vcb"], ["qaz"]]
```

```python
from typing import List
from collections import defaultdict


# Time Complexity: O(n * m) (number of words * length of words)
# Space Complexity: O(n)
def solution(arr: List[str]) -> List[List[str]]:
    buffer = defaultdict(list)
    for s in arr:
        buffer[tuple(sorted(s))].append(s)
    return [val for val in buffer.values()]

```


## Seventh Problem
Дан массив интервалов, смержить перекрывающие интервалы.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Отсортировать интервалы по их началу.</li>
 <li>Если конец первого интервала больше чем начало второго, то они пересекаются, мержим их.</li>
 <li>Иначе добавить интервал в результирующий массив, а также взяться за новый интервал.</li>
 <li>Вернуть результирующий массив.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [[1, 3], [100, 200], [2, 4]]
Output: [[1, 4], [100, 200]]

Example 2:
Input: [[1, 3], [5, 7], [6, 9], [10, 15], [12, 16]]
Output: [[1, 3], [5, 9], [10, 16]]

Example 3:
Input: [[100, 300], [200, 400], [700, 800], [750, 1000]]
Output: [[100, 400], [700, 1000]]
```

```python
# Time Complexity: O(n)
# Space Complexity: O(n)
def solution(intervals):
    intervals.sort(key=lambda x: x[0])
    result = []

    interval = intervals[0]
    for i in range(1, len(intervals)):
        if interval[1] > intervals[i][0]:
            interval[1] = max(interval[1], intervals[i][1])
        else:
            result.append([interval[0], interval[1]])

            interval = intervals[i]

    result.append([interval[0], intervals[i][1]])
    return result

```


## Eighth Problem
Дан массив точек, нужно определить можно ли провести между точками такую линию, чтобы все точки были симметричны 
относительно такой линии.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Найти самую левую точку по абцисс.</li>
 <li>Найти самую правую точку по абцисс.</li>
 <li>Вычислить точку абцисс ровно посередине между самой левой и самой правой точкой.</li>
 <li>Отталкиваясь от точки посередине вычисляем отражаемую точку, если такая отражаемая точка есть в массиве, значит между точками можно провести линию симметрии.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [[1, 1], [-1, 1]]
Output: True

Example 2:
Input: [[1, 1], [-1, -1]]
Output: False

Example 3:
Input: [[2, 0], [2, 6], [6, 6], [0, 6]]
Output: True
```

```python
# Time Complexity: O(n)
# Space Complexity: 0(n)
def solution(points):
    the_most_left_x = min(points, key=lambda x: x[0])
    the_most_right_x = max(points, key=lambda x: x[0])

    middle_x = (the_most_left_x[0] + the_most_right_x[0]) / 2
    for x, y in points:
        symmetry_point = (2 * middle_x - x, y)
        # set's O(1) instead of list's O(n)
        if symmetry_point in set(map(tuple, points)):
            return True

    return False

```


## Ninth Problem
.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>.</li>
 <li>.</li>
 <li>.</li>
 <li>.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: 
Output: 

Example 2:
Input: 
Output: 

Example 3:
Input: 
Output: 
```

```python

```


## Tenth Problem
.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>.</li>
 <li>.</li>
 <li>.</li>
 <li>.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: 
Output: 

Example 2:
Input: 
Output: 

Example 3:
Input: 
Output: 
```

```python

```


## Eleventh Problem
.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>.</li>
 <li>.</li>
 <li>.</li>
 <li>.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: 
Output: 

Example 2:
Input: 
Output: 

Example 3:
Input: 
Output: 
```

```python

```
