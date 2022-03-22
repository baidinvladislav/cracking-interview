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
Дана строка, вернуть длину наибольшей подстроки, содержащую только уникальные символы.

https://leetcode.com/problems/longest-substring-without-repeating-characters/

<details><summary>"Brute-Force" решение:</summary><blockquote>
<ol>
 <li>Используя вложенный цикл, генерируем все возможные подстроки для каждого символа строки.</li>
 <li>Передаем строку, начальный индекс подстроки и конечный индекс подстроки в ф-ию проверки на уникальность символов в подстроке.</li>
 <li>Если подстрока содержит только уникальные символы, то обновляем результирующую переменную в случае, если текущая подстрока длинее чем предыдущая.</li>
 <li>Возвращаем результирующую переменную.</li>
</ol>
</blockquote></details>


<details><summary>"Sliding Window" решение:</summary><blockquote>
<ol>
 <li>Иниц. массив юникода со 128 нулями, начало окна и конец окна нулями, результирующую переменную также нулём.</li>
 <li>Пока конец окна не дойдет до конца массива, переводим символ под укзателем конца окна в цифровое представление юникода и увеличиваем по этому индексу значение в юникод массиве.</li>
 <li>Пока значение в массива юникода под индексом конца окна больше 1, уменьшаем число под индексом начала окна в массиве юникода и сдвигаем начало окна ближе к концу массива.</li>
 <li>Обновляем результирующую переменную, если длина окна больше чем была в переменной.</li>
 <li>Сдвигаем конец окна ближе к концу массива.</li>
 <li>Возвращаем результирующую переменную.</li>
</ol>
</blockquote></details>


<details><summary>"Optimized Sliding Window" решение:</summary><blockquote>
<ol>
 <li>Иниц. словарь и резул. переменную и границы окна.</li>
 <li>Если символ под индексом конца окна в словаре, то обновляем индекс начала окна бОльшим значением из индекса символа в словаре или индексом начала окна.</li>
 <li>Обновляем резул. переменную, если длина окна увеличилась.</li>
 <li>Записываем индекс символа под указателем конца окна в словарь.</li>
 <li>Возвращаем результирующую переменную.</li>
</ol>
</blockquote></details>


```
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```


```python
# Time: O(n**3)
# Space: O(min(n,m))
class BrutForceSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(n):
            for j in range(i, n):
                if self.check(s, i, j):
                    result = max(result, j - i + 1)
        return result

    def check(self, string, start, end):
        ascii_array = [0] * 128

        for i in range(start, end + 1):
            char = string[i]
            # The ord() function returns the number
            # representing the unicode code of a specified character.
            ascii_array[ord(char)] += 1
            if ascii_array[ord(char)] > 1:
                return False
        return True


# Time: O(2n) = O(n)
# Space: O(min(n,m))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ascii_array = [0] * 128
        window_start = window_end = 0
        result = 0
        while window_end < len(s):
            last_symbol = s[window_end]
            # The ord() function returns the number
            # representing the unicode code of a specified character.
            symbol_unicode = ord(last_symbol)
            ascii_array[symbol_unicode] += 1

            while ascii_array[ord(last_symbol)] > 1:
                first_symbol = s[window_start]
                symbol_unicode = ord(first_symbol)
                ascii_array[symbol_unicode] -= 1
                window_start += 1

            result = max(result, window_end - window_start + 1)
            window_end += 1
        return result



# Time complexity: O(n). Index j will iterate n times.
# Space complexity: O(m). m is the size of the charset.
class OptimizedWindowSlidingSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        result = 0
        hash_map = {}

        window_start = 0
        for window_end in range(n):
            cur_char = s[window_end]
            if cur_char in hash_map:
                window_start = max(hash_map[cur_char], window_start)

            result = max(result, window_end - window_start + 1)
            hash_map[cur_char] = window_end + 1

        return result

```


## Median of Two Sorted Arrays


## Valid Parentheses
Дана строка, содержащую только символы '(', ')', '{', '}', '[' и ']', определить, валидна ли входная строка. 
Входная строка действительна, если: 

Открытые скобки должны быть закрыты однотипными скобками. 
Открытые скобки должны быть закрыты в правильном порядке.

https://leetcode.com/problems/valid-parentheses/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Создаем хеш-таблицу в которой под каждой открывающей скобкой храним закрывающую скобку такого же типа.</li>
 <li>Инициализируем пустой стек.</li>
 <li>Итерируем строку.</li>
 <li>Если символ на итерации есть в как ключ в хеш-таблице, значит это открытвающая скобка, добавляем ее на верх стека.</li>
 <li>Если нет символа в хеш-таблице, то проверяем пуст ли стек, если он пуст на этом этапе, то строка не валидна.</li>
 <li>Если последний элемент стека не хранит значение текущего символа в хеш-таблице, то строка не валидна.</li>
 <li>Вернуть булево значение, пустой ли стек.</li>
</ol>

```
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
```

```python
from collections import deque


class Solution:
    def isValid(self, s):
        d = {'(': ')', '{': '}', '[': ']'}
        stack = deque()

        for char in s:
            if char in d:
                stack.append(char)
            else:
                if not stack:
                    return False

                if d[stack.pop()] != char:
                    return False

        return not stack

```


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
Дан массив nums, переместите все 0 в его конец, сохраняя порядок ненулевых элементов.
Обратите внимание, что вы должны сделать это на месте, не создавая копию массива.

https://leetcode.com/problems/move-zeroes/

<details><summary>Решение 1:</summary><blockquote>
<ol>
 <li>Инициализируем переменную для "хранения индекса последнего не нулевого элемента".</li>
 <li>Итерируем массив, если элемент на итерации не 0, то перезаписываем число под индексом последнего не нулевого элемента элементом на текущей итерации, а также инкрементируем переменную для хранения такого индекса.</li>
 <li>Вторым проходом вставляем 0 на индексы которые находятся между индексом последнего не нулевого элемента и конечным индексом массива включительно.</li>
</ol>
</blockquote></details>


<details><summary>Решение 2:</summary><blockquote>
<ol>
 <li>Инициализируем медленный и быстрый указатель начальным элементом массива.</li>
 <li>Медленный указатель остается вначале, быстрый итерирует массив.</li>
 <li>Если на итерации число не равно 0, то свапаем числа под медленным и быстрым указателями, а также инкрементируем медленный указатель.</li>
</ol>
</blockquote></details>


```
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
```

```python
class Solution:
    # Approach #2 (Space Optimal, Operation Sub-Optimal)
    # Space Complexity: O(1)
    # Time Complexity: O(n)
    def moveZeroes(self, nums):
        lastNonZeroFoundAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1

        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0

    # Approach #3 (Optimal)
    # Space Complexity: O(1)
    # Time Complexity: O(n)
    def moveZeroes(self, nums):
        """
        1. if the number is 0 then we only increment the pointer named "second".
        2. if the number is not 0 we swap the number of pointers.
        3. then we increment both pointers.
        """
        first = 0
        for second in range(len(nums)):
            if nums[second] != 0:
                nums[first], nums[second] = nums[second], nums[first]
                first += 1

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
