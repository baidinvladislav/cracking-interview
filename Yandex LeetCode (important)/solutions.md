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
Дан неотсортированный массив чисел, вернуть индексы двух чисел сумма которых равна таргету.

https://leetcode.com/problems/two-sum/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Идем по циклу, трекая порядковый номер итерации.</li>
 <li>Вычисляем попытку (target - nums[i]).</li>
 <li>Если попытки нет в словаре, то добавляем в словарь число текущей итерации.</li>
 <li>Если попытка в словаре, то вернуть индекс попытки из словаря (buffer[num]) и порядковый номер итерации цикла.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
```

```python
from typing import List


class Solution:
    # one pass
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        buffer = {}
        for i, num in enumerate(nums):
            attempt = target - num
            if attempt not in buffer:
                buffer[num] = i
            else:
                return [buffer[attempt], i]

        return [-1, -1]
    
    # two passes
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        buffer = {}
        for i in range(len(nums)):
            buffer[nums[i]] = i
            
        for i in range(len(nums)):
            attempt = target - nums[i]
            if attempt in buffer and buffer[attempt] != i:
                return [i, buffer[attempt]]
        return [-1, -1]
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
