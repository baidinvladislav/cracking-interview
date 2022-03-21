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
 <li>Берем за точку отсчета первый интервал из массива.</li>
 <li>Цикл по массиву со второго элемента.</li>
 <li>Если конец предыдущего интервала больше или равен чем начало последующего, то интервалы пересекаются, берем за конец интервала больший конец двух интервалов.</li>
 <li>В случае, если интервалы не пересекаются, то добавляем интервал в результирующий массив и обновляем начало и конец интервала значениями данного интервала.</li>
 <li>После цикла нужно будет добавить последний интервал в результирующий массив.</li>
 <li>Вернуть результирующий массив.</li>
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
class Solution:
    # Time complexity : O(n log n)
    # Space complexity : O(n log n)
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

## Number of Islands

## Reverse Linked List

## Summary Ranges

## Lowest Common Ancestor of a Binary Tree

## Move Zeroes

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
