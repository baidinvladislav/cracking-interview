# Yandex Interview
+ [First Problem](#first-problem)
+ [Second Problem](#second-problem)
+ [Third Problem](#third-problem)
+ [Fourth Problem](#fourth-problem)
+ [Fifth Problem](#fifth-problem)
+ [Sixth Problem](#sixth-problem)


## First Problem
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
