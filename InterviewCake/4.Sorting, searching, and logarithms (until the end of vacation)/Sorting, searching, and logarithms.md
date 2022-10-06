# Sorting, searching, and logarithms
+ [Find Rotation Point](#find-rotation-point)


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
