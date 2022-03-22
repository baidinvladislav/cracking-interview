# LeetCode Yandex Track
+ [3. Longest Substring Without Repeating Characters](#longest-substring-without-repeating-characters)
+ [4. Median of Two Sorted Arrays](#median-of-two-sorted-arrays)
+ [20. Valid Parentheses](#valid-parentheses)
+ [21. Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [23. Merge k Sorted Lists](#merge-k-sorted-lists)
+ [49. Group Anagrams](#group-anagrams)
+ [56. Merge Intervals](#merge-intervals)
+ [98. Validate Binary Search Tree](#validate-binary-search-tree)
+ [125. Valid Palindrome](#valid-palindrome)
+ [146. LRU Cache](#lru-cache)
+ [159. Longest Substring with At Most Two Distinct Characters](#longest-substring-with-at-most-two-distinct-characters)
+ [167. Two Sum II Input Array Is Sorted](#two-sum-ii-input-array-is-sorted)
+ [200. Number of Islands](#number-of-islands)
+ [206. Reverse Linked List](#reverse-linked-list)
+ [228. Summary Ranges](#summary-ranges)
+ [236. Lowest Common Ancestor of a Binary Tree](#lowest-common-ancestor-of-a-binary-tree)
+ [283. Move Zeroes](#move-zeroes)
+ [356. Line Reflection](#line-reflection)
+ [362. Design Hit Counter](#design-hit-counter)
+ [380. Insert Delete Getrandom](#insert-delete-getrandom)
+ [392. Is Subsequence](#is-subsequence)
+ [443. String Compression](#string-compression)
+ [567. Permutation in String](#permutation-in-string)
+ [716. Max Stack](#max-stack)
+ [849. Maximize Distance to Closest Person](#maximize-distance-to-closest-person)
+ [1450. Number of Students Doing Homework at a Given Time](#number-of-students-doing-homework-at-a-given-time)
+ [1493. Longest Subarray of 1 After Deleting One Element](#longest-subarray-of-1-after-deleting-one-element)


## Longest Substring Without Repeating Characters


## Median of Two Sorted Arrays


## Valid Parentheses


## Merge Two Sorted Lists


## Merge k Sorted Lists


## Group Anagrams


## Merge Intervals
Дан массив интервалов, смержить пересекающиеся интервалы.

https://leetcode.com/problems/merge-intervals/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Отсортировать интервалы по их началу.</li>
 <li>Инициализируем результирующий массив.</li>
 <li>Если результирующий массив пуст или конец последнего добавленного интервала в массив МЕНЬШЕ чем начало интервала на итерации, то добавляем интервал на итерации в результирующий массив.</li>
 <li>В другом случае, добавляем в результирующий массив конец интервала на итерации либо конец последнего добавленного в результирующий массив интервала.</li>
 <li>Возвращаем результирующий массив.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

```python
from typing import List


class Solution:
    # Time complexity: O(n log n)
    # Space complexity: O(n log n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
```


## Validate Binary Search Tree


## Valid Palindrome


## LRU Cache


## Longest Substring with At Most Two Distinct Characters


## Two Sum II Input Array Is Sorted
Дан отсортированный массив и число таргет. Найти два числа в массиве, сумма которых равна таргету. 
Вернуть индексы таких чисел.

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Ставим левый указатель в начало массива, ставим правый указатель в конец массива.</li>
 <li>Вычисляем сумму чисел под указателями.</li>
 <li>Если сумма чисел равна таргету, то вернуть индексы + 1 (т.к. условие задачи, что массив начинается с 1-го индекса).</li>
 <li>Если сумма больше таргета, то сдвигаем правый указатель к началу массива.</li>
 <li>Если сумма меньше таргета, то сдвигаем левый указатель ближе к концу.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

```python
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]
            
            elif current_sum > target:
                right -= 1
            
            elif current_sum < target:
                left += 1
```


## Number of Islands


## Reverse Linked List


## Summary Ranges
Дан отсортированный массив уникальных чисел. 
Свернуть в диапозоны последовательные числа.

https://leetcode.com/problems/summary-ranges/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем два указателя 'start' и 'end'. При инициализации указатели установлены в начало входного массива.</li>
 <li>До тех пор пока два соседних числа в массиве имеют между собой разницу ровно в 1, сдвигаем указатель 'end' вправо на один элемент.</li>
 <li>Если указатели стоят на разных числах (сдвигался указатель 'end'), то добавляем в результирующий массив диапозон чисел от 'start' до 'end'.</li>
 <li>В другом случае добавляем в результирующий массив только начало диапозона.</li>
 <li>В конце каждой итерации сдвигаем указатель 'end' на один элемент и ставим 'start' на это же число.</li>
 <li>Возвращаем результирующий массив.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

```python
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = end = 0

        while end < len(nums):
            # increase end pointer because two neighboring integers are extends range
            while end + 1 < len(nums) and nums[end] + 1 == nums[end + 1]:
                end = end + 1

            # if pointers stand not the same integer
            if nums[start] != nums[end]:
                result.append(f"{str(nums[start])}->{str(nums[end])}")
            # if pointers stand the same integer
            else:
                result.append(str(nums[start]))

            # slide end pointer
            end = end + 1
            # set pointers to the same integer
            start = end
        return result
```


## Lowest Common Ancestor of a Binary Tree


## Move Zeroes
Дан отсортированный массив уникальных чисел. 
Свернуть в диапозоны последовательные числа.

https://leetcode.com/problems/summary-ranges/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем два указателя 'start' и 'end'. При инициализации указатели установлены в начало входного массива.</li>
 <li>До тех пор пока два соседних числа в массиве имеют между собой разницу ровно в 1, сдвигаем указатель 'end' вправо на один элемент.</li>
 <li>Если указатели стоят на разных числах (сдвигался указатель 'end'), то добавляем в результирующий массив диапозон чисел от 'start' до 'end'.</li>
 <li>В другом случае добавляем в результирующий массив только начало диапозона.</li>
 <li>В конце каждой итерации сдвигаем указатель 'end' на один элемент и ставим 'start' на это же число.</li>
 <li>Возвращаем результирующий массив.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

```python
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = end = 0

        while end < len(nums):
            # increase end pointer because two neighboring integers are extends range
            while end + 1 < len(nums) and nums[end] + 1 == nums[end + 1]:
                end = end + 1

            # if pointers stand not the same integer
            if nums[start] != nums[end]:
                result.append(f"{str(nums[start])}->{str(nums[end])}")
            # if pointers stand the same integer
            else:
                result.append(str(nums[start]))

            # slide end pointer
            end = end + 1
            # set pointers to the same integer
            start = end
        return result
```


## Line Reflection


## Design Hit Counter


## Insert Delete Getrandom


## Is Subsequence


## String Compression


## Permutation in String


## Max Stack


## Maximize Distance to Closest Person


## Number of Students Doing Homework at a Given Time


## Longest Subarray of 1 After Deleting One Element
