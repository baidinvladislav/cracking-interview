# Sorting, searching, and logarithms
+ [Find Rotation Point](#find-rotation-point)
+ [Find Repeat, Space Edition](#find-repeat-space-edition)


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
