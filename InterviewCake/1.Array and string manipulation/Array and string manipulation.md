# Array and string manipulation
+ [Merging Meeting Times](#merging-meeting-times)
+ [Reverse String in Place](#reverse-string-in-place)
+ [Reverse Words](#reverse-words)
+ [Merge Sorted Arrays](#merge-sorted-arrays)
+ [Cafe Order Checker](#cafe-order-checker)


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


## Reverse String in Place


## Reverse Words


## Merge Sorted Arrays


## Cafe Order Checker
