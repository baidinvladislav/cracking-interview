# LeetCode Yandex Track
+ [1. Two Sum](#two-sum)
+ [3. Longest Substring Without Repeating Characters](#longest-substring-without-repeating-characters)
+ [4. Median of Two Sorted Arrays](#median-of-two-sorted-arrays)
+ [5. Longest Palindromic Substring](#longest-palindromic-substring)
+ [7. Reverse Integer](#reverse-integer)
+ [20. Valid Parentheses](#valid-parentheses)
+ [21. Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [22. Generate Parentheses](#generate-parentheses)
+ [23. Merge k Sorted Lists](#merge-k-sorted-lists)
+ [49. Group Anagrams](#group-anagrams)
+ [56. Merge Intervals](#merge-intervals)
+ [71. Simplify Path](#simplify-path)
+ [88. Merge Sorted Array](#merge-sorted-array)
+ [98. Validate Binary Search Tree](#validate-binary-search-tree)
+ [101. Symmetric Tree](#symmetric-tree)
+ [125. Valid Palindrome](#valid-palindrome)
+ [136. Single Number](#single-number)
+ [146. LRU Cache](#lru-cache)
+ [155. Min Stack](#min-stack)
+ [159. Longest Substring with At Most Two Distinct Characters](#longest-substring-with-at-most-two-distinct-characters)
+ [161. One Edit Distance](#one-edit-distance)
+ [167. Two Sum II Input Array Is Sorted](#two-sum-ii-input-array-is-sorted)
+ [199. Binary Tree Right Side View](#binary-tree-right-side-view)
+ [200. Number of Islands](#number-of-islands)
+ [205. Isomorphic Strings](#isomorphic-strings)
+ [206. Reverse Linked List](#reverse-linked-list)
+ [228. Summary Ranges](#summary-ranges)
+ [236. Lowest Common Ancestor of a Binary Tree](#lowest-common-ancestor-of-a-binary-tree)
+ [283. Move Zeroes](#move-zeroes)
+ [340. Longest Substring with At Most K Distinct Characters](#longest-substring-with-at-most-k-distinct-characters)
+ [349. Intersection of Two Arrays](#intersection-of-two-arrays)
+ [356. Line Reflection](#line-reflection)
+ [362. Design Hit Counter](#design-hit-counter)
+ [380. Insert Delete Getrandom](#insert-delete-getrandom)
+ [392. Is Subsequence](#is-subsequence)
+ [443. String Compression](#string-compression)
+ [487. Max Consecutive Ones II](#max-consecutive-ones-ii)
+ [560. Subarray Sum Equals K](#subarray-sum-equals-k)
+ [567. Permutation in String](#permutation-in-string)
+ [652. Find Duplicate Subtrees](#find-duplicate-subtrees)
+ [658. Find K Closest Elements](#find-k-closest-elements)
+ [680. Valid Palindrome II](#valid-palindrome-ii)
+ [716. Max Stack](#max-stack)
+ [849. Maximize Distance to Closest Person](#maximize-distance-to-closest-person)
+ [977. Squares of a Sorted Array](squares-of-a-sorted-array)
+ [986. Interval List Intersections](interval-list-intersections)
+ [1004. Max Consecutive Ones III](max-consecutive-ones-iii)
+ [1436. Destination City](cestination-city)
+ [1450. Number of Students Doing Homework at a Given Time](#number-of-students-doing-homework-at-a-given-time)
+ [1493. Longest Subarray of 1 After Deleting One Element](#longest-subarray-of-1-after-deleting-one-element)

## Two Sum
Дан массив чисел и число-таргет. Вернуть индексы чисел, которые в сумме дают таргет.

https://leetcode.com/problems/two-sum/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>На каждой итерации проверять что нашли второе слагаемое как разницу первого слагаемого и суммы.</li>
 <li>Если второе слагаемое в мапе, то вернуть индексы слогаемого как текущая итерация, и второго слагаемого как значение в словаре по его ключу.</li>
 <li>Если значение не подошло на роль второго слагааемого, то записать значение и его индекс в мапу для будущих проверок.</li>
</ol>
</blockquote></details>

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            num = nums[i]
            x = target - num
            if x in hash_map:
                return [hash_map[x], i]
            
            hash_map[num] = i
        
        return [-1, -1]

```


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
 <li>Используем скользящее окно, которое увеличивается с каждой итераций к правому концу.</li>
 <li>Но при этом сжимается, если мы нарушаем наше ограничение, если у нас более чем 1 уникальный элемент.</li>
 <li>Для определения нарушения ограничения используется словарь со счетчиком символов строки.</li>
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


# Time complexity: O(n). Index j will iterate n times.
# Space complexity: O(m). m is the size of the charset.
class SlidingSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        d = defaultdict(int)

        result = 0
        for end in range(len(s)):
            d[s[end]] += 1

            while len(d) != end - start + 1:
                d[s[start]] -= 1
                if d[s[start]] == 0:
                    del d[s[start]]
                start += 1

            result = max(result, end - start + 1)

        return result

```


## Median of Two Sorted Arrays
Даны два отсортированных массива nums1 и nums2 размера m и n соответственно, 
вернуть медиану двух отсортированных массивов. 
Общая сложность времени выполнения должна быть O(log (m+n)).

https://leetcode.com/problems/median-of-two-sorted-arrays/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Вычисляем левые и правые края входных массивов.</li>
 <li>Если левый край первого массива меньше или равен правому краю второго массива, а также левый край второго массива меньше или равен правому краю первого массива.</li>
 <li>В зависимости от четности смерженного массива возращаем немного разный результат.</li>
 <li>Если левый край первого массива больше чем правый край второго массива, то сдвигаем правый указатель.</li>
 <li>Иначе сдвигаем левый указатель.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')

            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1

```


## Longest Palindromic Substring
Дана строка, нужно найти самую длинную подстроку палиндром.

https://leetcode.com/problems/longest-palindromic-substring/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Итерируем строку.</li>
 <li>Подстрока-палиндром может иметь четную или нечетную длину символов.</li>
 <li>От каждого индекса идем влево и вправо для нахождения самого длинного палиндрома.</li>
 <li>Обновляем результат.</li>
</ol>

</blockquote></details>

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
```

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = expandAroundCenter(i, i)  # Odd length palindromes
            left2, right2 = expandAroundCenter(i, i + 1)  # Even length palindromes

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start:end + 1]

```


## Reverse Integer
Дано число, верните его в развернутом виде.

https://leetcode.com/problems/reverse-integer/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Определение, является ли число отрицательным.</li>
 <li>Преобразование числа в его абсолютное значение для упрощения переворачивания.</li>
 <li>Пока в числе есть цифры.</li>
 <li>Извлечение последней цифры числа.</li>
 <li>Удаление последней цифры из числа путем целочисленного деления на 10.</li>
 <li>Проверка на переполнение перед добавлением цифры в result.</li>
 <li>Возврат 0 в случае, если операция приведет к переполнению.</li>
 <li>Если исходное число было отрицательным.</li>
 <li>Присвоение результату отрицательного знака.</li>
 <li>Возврат перевернутого числа.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
```

```python
class Solution:
    def reverse(self, x):
        INT_MAX = 2**31 - 1  # 2,147,483,647
        INT_MIN = -2**31     # -2,147,483,648

        result = 0
        negative = x < 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check if appending the digit will cause overflow
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0  # This would cause an overflow
            
            result = result * 10 + digit
        
        if negative:
            result = -result

        return result


```


## Valid Parentheses
Дана строка, содержащую только символы '(', ')', '{', '}', '[' и ']', определить, валидна ли входная строка. 
Входная строка действительна, если: 

Открытые скобки должны быть закрыты однотипными скобками. 
Открытые скобки должны быть закрыты в правильном порядке.

https://leetcode.com/problems/valid-parentheses/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Создаем хеш-таблицу в которой под каждой закрывающей скобкой храним открывающую скобку такого же типа.</li>
 <li>Инициализируем пустой стек.</li>
 <li>Итерируем строку.</li>
 <li>Если символа на итерации нет в как ключа в хеш-таблице, значит это открывающая скобка, добавляем ее на верх стека.</li>
 <li>Если символ в хеш-таблице, проверяем элемент на вершине стека. Если элемент в верхней части стека является открывающей скобкой того же типа, то мы извлекаем его из стека и продолжаем обработку. В противном случае строка не валидна.</li>
 <li>Если стек после итерации содержит элементы, то строка не валидна.</li>
</ol>
</blockquote></details>

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
class Solution:
    # time complexity : O(n)
    # space complexity : O(n)
    def isValid(self, s):
        hash_map = {")": "(", "}": "{", "]": "["}
        # stack to keep track of opening brackets
        stack = []

        for char in s:
            # if the character is a closing bracket
            if char in hash_map:
                # pop the topmost element from the stack, if it is not empty
                # otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else "#"
                # the mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if hash_map[char] != top_element:
                    return False
            else:
                # we have an opening bracket, simply push it onto the stack
                stack.append(char)

        # in the end, if the stack is empty, then we have a valid expression
        # the stack won't be empty for cases like ((()
        return not stack

```


## Merge Two Sorted Lists
Даны два отсортированных связных списка, смержить их в один отсортированный связный список.

https://leetcode.com/problems/merge-two-sorted-lists/

<details><summary>Рекурсивное решение:</summary><blockquote>
<ol>
 <li>Определяем базовые случаи рекурсии: если закончился список 1, то вернуть список 2, если закончился список 2, то вернуть список 1.</li>
 <li>Тело рекурсии: сравниваем узлы списков, тот узел, который меньше сдвигается дальше.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
```

```python
class Solution:
    # Approach 1: Recursion
    # Time complexity: O(n + m)
    # Space complexity: O(n + m)
    def mergeTwoLists(self, l1, l2):
        # base cases
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        # recursion body
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # Approach 2: Iteration
    # Time complexity: O(n + m)
    # Space complexity: O(1)
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next

```


## Generate Parentheses
Написать функцию, которая принимает число и генерирует правильную скобочную последовательность скобок для n пар скобок.

https://leetcode.com/problems/generate-parentheses/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Для генерации нужной строки используем рекурсию с базовым случаем, когда строка в два раза больше чем число n.</li>
 <li>Если открывающих меньше чем n, то добавляем открывающую скобку и вызываем ф-ию еще раз с новыми аргументами.</li>
 <li>Тоже самое, но для закрывающих скобок пока их не станет столько же сколько открывающих.</li>
 <li>Вернуть результирующую строку.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"] 

Example 2:
Input: n = 1
Output: ["()"]
```

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(string, opened, closed):
            if len(string) == n * 2:
                result.append(string)
                return
            
            if opened < n:
                backtrack(string + "(", opened + 1, closed)

            if closed < opened:
                backtrack(string + ")", opened, closed + 1)

        result = []
        backtrack("", 0, 0)
        return result

```


## Merge k Sorted Lists
Смержить k связных списков из массива в один отсортированный связный список.

https://leetcode.com/problems/merge-k-sorted-lists/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Инициализируем голову и указатель узлом списка со значением 0.</li>
 <li>Добавляем в кучу значения голов и сами головы всех списков из массива.</li>
 <li>Пока куча не пуста получаем из нее значения и узел списков (куча сама сортирует).</li>
 <li>К указателю из 1-го пункта цепляем, то что пришло из кучи.</li>
 <li>Переставляем указатель вперед на один узел.</li>
 <li>Переставляем узел из пункта 3 вперед на один узел.</li>
 <li>Если у узла есть последующие узлы, то добавляем их значения и сами узлы в кучу.</li>
 <li>После цикла вернуть последующий от головы узел, потому что голова равняется значению 0, см 1-ый пункт.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
```

```python
from heapq import *


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode(0)
        q = []
        for l in lists:
            if l:
                heappush(q, (l.val, id(l), l))
        while q:
            val, nodeId, node = heappop(q)
            point.next = node  # use node directly instead of creating a new node
            point = point.next
            node = node.next
            if node:
                heappush(q, (node.val, id(node), node))
        return head.next
```


## Group Anagrams
Дан массив слов, сгруппировать анаграммы в массивах.

https://leetcode.com/problems/group-anagrams/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Иницализовать словарь с пустым листом в значении.</li>
 <li>Сортируем каждое слово.</li>
 <li>Преобразуем отсортированное слово в кортеж (т.к. он может быть ключом, потому что неизменяемый тип данных).</li>
 <li>Добавляем кортеж как ключ в словарь.</li>
 <li>Проходя циклом по входному массиву слов, смотрим если слово совпадает с ключом (кортежем) то добавляем это слово в массив под этим ключом.</li>
 <li>Вернуть значения наполненного словаря.</li>
</ol>
</blockquote></details>

```
Example 1
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
```

```python3
from collections import defaultdict


# Time Complexity: O(NK log K). Where N is the length of strs, and K is the maximum length of a string in strs.
# Space Complexity: O(NK)
def groupAnagrams(strs):
    if not strs:
        return [[""]]

    hash_map = defaultdict(list)
    for word in strs:
        hash_map[tuple(sorted(word))].append(word)
    return list(hash_map.values())

```


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
Дан рут бинарного дерева. Определить является ли дерево бинарным деровом поиска.
Бинарное дерево поиска - это дерево в котором:
* в левом поддереве узла все значения меньше чем значения узла.
* в правом поддереве узла все значения больше чем значения узла.
* и левое, и правое поддеревья являются бинарными деревьями поиска.

https://leetcode.com/problems/validate-binary-search-tree/

<details><summary>Лаконичная рекурсия:</summary><blockquote>
<ol>
 <li>Во вложенную рекурсивную ф-ию передаем корень дерева.</li>
 <li>В ф-ии указатели нижнего предела и верхнего берем изначально за инфинитивы (- и +).</li>
 <li>В теле рекурсии возвращаем False, если текущего узла меньше или равно чем нижний указатель ИЛИ если значение текущего узла больше или равно верхнего указателя.</li>
 <li>Каждая рекурсия пораждает два вызова рекурсии с аргументами: 1)node=левый узел, low=-math.inf, high=node.val, 2)node=правый узел, low=node.val, high=math.inf.</li>
</ol>
</blockquote></details>


<details><summary>Более читаемая рекурсия:</summary><blockquote>
<ol>
 <li>Одним методом собираем преордером значения массива.</li>
 <li>Вторым методом проверяем, что все числа в массиве отсортированы по возрастанию</li>
</ol>
</blockquote></details>


```
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

```python3
import math
from typing import Optional

from Algorithms.leetcode_tree import buildTree, TreeNode


# Approach 1: More clearly two steps recursive
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def dfs(self, node, values):
        if not node:
            return

        self.dfs(node.left, values)
        values.append(node.val)
        self.dfs(node.right, values)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        self.dfs(root, values)

        i = 0
        j = 1

        while j != len(values):
            if values[i] >= values[j]:
                return False

            i += 1
            j += 1

        return True


# root_arr = [2, 1, 3]
root_arr = [5, 1, 4, None, None, 3, 6]
root = buildTree(root_arr)
print(Solution().isValidBST(root))


# Approach 2: Recursive Traversal with Valid Range
# Time complexity: O(N) since we visit each node exactly once.
# Space complexity: O(N) since we keep up to the entire tree.
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False
            
            left_subtree = validate(node=node.left, low=low, high=node.val)
            right_subtree = validate(node=node.right, low=node.val, high=high)
            
            return left_subtree and right_subtree

        return validate(root)

```


## Valid Palindrome
Дана строка s, вернуть true, если это палиндром, или false.
В строке могут содержаться буквы разного регистра, а также не только буквенно-цифровые символы.

https://leetcode.com/problems/valid-palindrome/

<details><summary>Решение t: O(n), s: O(n):</summary><blockquote>
<ol>
 <li>Отфильтровать все буквенно-цифровые символы.</li>
 <li>Привести отфильтрованные символы к нижнему регистру.</li>
 <li>Привести отфильтрованные символы нижнего регистра к списку.</li>
 <li>Сравнить два среза [:], [::-1] списка из предыдущего пункта.</li>
</ol>
</blockquote></details>


<details><summary>Решение t: O(n), s: O(1):</summary><blockquote>
<ol>
 <li>Используем на строке два указателя: один на вначале, второй в конце.</li>
 <li>Сдвигаем два указателя навстречу друг другу.</li>
 <li>Если указатели сошлись в центре, то строка палиндром, иначе нет.</li>
 <li>Прим: указатель чей символ не является алго-цифровым делает шаг в одиночку.</li>
</ol>
</blockquote></details>

```
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

```python3
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isPalindrome(self, s: str) -> bool:
        filtered_symbols = filter(lambda symbol: symbol.isalnum(), s)
        lo_low_case = map(lambda symbol: symbol.lower(), filtered_symbols)
        to_list = list(lo_low_case)
        return to_list == to_list[::-1]
    
    # Time complexity: O(n)
    # Space complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

```


## Single Number
Найти уникальный элемент среди дубликатов в массиве за O(n).

https://leetcode.com/problems/single-number/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Инициализируем переменную первым элементом списка.</li>
 <li>Итерируем массив элементов со второго элемента, используя XOR оставляем в переменной только то число, которое является уникальным и не срабатывает для логического исключающего ИЛИ .</li>
 <li>Вернуть уникальное число из списка.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
```

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        return result

```


## LRU Cache
Реализовать класс для работы с кешом по приципу LRU (Least Recently Used).
* LRUCache(int capacity) Инициализация класса кэша LRU с положительным размером.
* int get(int key) Возвращает значение ключа, если ключ существует, иначе возвращает -1.
* void put(int key, int value) Обновить значение ключа, если он существует. 
В противном случае добавьте пару ключ-значение в кеш. Если количество свободного места недостаточно для вставки нового элемента, удалите последний использованный ключ. (который дольше всех не был затронут).

Методы get и put должны выполняться с временной сложностью O(1).

https://leetcode.com/problems/lru-cache/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Для выполнения требований по временной сложности методов используем хеш-таблицу и двусвязной список. Хэш таблица будет иметь вид: {key1: Node(key1, value1), key2: Node(key2, value2)}</li>
 <li>Метод get(key): если ключ есть в хэш-таблице, то получить узел связного списка по переданному ключу, удалить узел из связного списка, добавить узел в конец связного списка, вернуть значение узла связного списка, если ключа нет в хэш-таблице вернуть -1.</li>
 <li>Метод put(key, value): если ключ уже находится в хэш-таблице, то удалить узел из связного списка, при этом удалять ключ узла из хэш-таблицы необязательно. Создать узел связного списка с полученными значениями key и value, вставить узел в конец связного списка, вставить узел в хэш-таблицу по переданному ключу. Если длина хэш-таблицы превышает размер кеша переданный при инициализации, то удалить узел с начала связного списка и удалить ключ по которому находится узел в хэш-таблице.</li>
 <li>Метод _add_to_llist(self, node): добавляет узел в конец двусвязного списка.</li>
 <li>Метод _remove_from_llist: удаляет узел из двусвязного списка.</li>
</ol>
</blockquote></details>

```
Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

```python
# Approach 2: Hashmap + DoubleLinkedList
# Time complexity: O(1)
# Space complexity: O(capacity)
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self._remove_node(node)
            self._add_node(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.map:
            self._remove_node(self.map[key])

        node = Node(key, value)
        self._add_node(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            deleted_node = self.head.next
            self._remove_node(deleted_node)
            del self.map[deleted_node.key]

    def _add_node(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def _remove_node(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node


lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
lRUCache.get(1)  # return 1
lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)  # returns -1 (not found)                   123
lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)  # return -1 (not found)
lRUCache.get(3)  # return 3
lRUCache.get(4)  # return 4

```


## Min Stack
Разработать структуру данных стэк для хранения минимума. Операции должны быть выполнены за O(1) по времени.

https://leetcode.com/problems/min-stack/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем 2 стэка. Один для всех элементов, второй для минимумов.</li>
 <li>При добавлении элемента проверяем стоит ли элемент сохранить еще и в стэк минимумов.</li>
 <li>Если удаляется минимум из общего то удаляем и из стэка минимумов.</li>
</ol>
</blockquote></details>

```
Example 1:
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

```python
class MinStack:

    def __init__(self):
        self.common_storage = []
        self.minimum_storage = []

    def push(self, val: int) -> None:
        if len(self.minimum_storage) == 0 or val <= self.minimum_storage[-1]:
            self.minimum_storage.append(val)

        self.common_storage.append(val)

    def pop(self) -> None:
        if self.common_storage[-1] == self.minimum_storage[-1]:
            self.minimum_storage.pop()

        return self.common_storage.pop()

    def top(self) -> int:
        return self.common_storage[-1]

    def getMin(self) -> int:
        return self.minimum_storage[-1] if self.minimum_storage else 0


```


## Longest Substring with At Most Two Distinct Characters
Дана строка, найти в ней самую большую подстроку, которая содержит не больше двух уникальных символов.

https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Добавляем символы строки и их частоту в хеш-мап.</li>
 <li>Пока длина хеш-мапы больше 2, сжиаем окно.</li>
 <li>Сжатие окна происходит за счет уменьшения значений частоты символов и последующим удалением сивола из хеш-мапы.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
```

```python
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        window_start = 0
        max_length = float('-inf')
        hash_map = {}

        for window_end in range(len(s)):
            if s[window_end] not in hash_map:
                hash_map[s[window_end]] = 0
            hash_map[s[window_end]] += 1

            while len(hash_map) > 2:
                hash_map[s[window_start]] -= 1
                if hash_map[s[window_start]] == 0:
                    del hash_map[s[window_start]]
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length


print(Solution().lengthOfLongestSubstringTwoDistinct(s="ccaabbb"))

```


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
Дана сетка размером MxN. В сетке находятся находятся значение '0' и '1'. Где '0' - это вода и '1' - это суша.
Вернуть кол-во островов на сетке.

https://leetcode.com/problems/number-of-islands/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Рассмотрим сетку как неориентированный граф, у которого ребра есть у смежных соседних вершин по горизонтали и вертикали со значением '1'.</li>
 <li>Линейно проходим по сетке, если в вершине значение '1', то начинаем от этой вершины поиск в глубину.</li>
 <li>На каждом рекурсивном обходе устанавливаем для узла значение '0', тем самым помечая вершину как посещенную.</li>
 <li>Рекурсивно обходим соседей этой вершины у которых тоже значение '1', меняем на '0'.</li>
 <li>Повторяем пока не упремся в базовые случаи: индексы вышли за границы сетки, узел не равен "1".</li>
 <li>Кол-во раз когда запускался поиск в глубину и будет равен кол-ву островое на сетке.</li>
</ol>
</blockquote></details>


```
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

```python3
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

```


## Reverse Linked List
Развернуть связной список.

https://leetcode.com/problems/reverse-linked-list/

<details><summary>Итеративное решение:</summary><blockquote>
<ol>
 <li>Сохранить в памяти следующий узел от текущего.</li>
 <li>Изменить следующий узел на предыдущий.</li>
 <li>Предыдущим узлом сохранить текущий узел.</li>
 <li>Текущим узлом назначить узел из пункта 1.</li>
 <li>После итерации вернуть предудущий узел.</li>
</ol>
</blockquote></details>


<details><summary>Рекурсивное решение:</summary><blockquote>
<ol>
 <li>Рекурсивно посещаем каждый элемент в связанном списке, пока не достигнем последнего.</li>
 <li>Этот последний элемент станет новым головой перевернутого связанного списка.</li>
 <li>На пути возврата каждый узел добавляется в конец частично перевернутого списка.</li>
</ol>
</blockquote></details>


```
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
```


```python3
class Solution:
    # iterative
    # Time complexity: O(n). Assume that nn is the list's length, the time complexity is O(n).
    # Space complexity: O(1).
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            tempNext = current.next
            current.next = prev
            prev = current
            current = tempNext
        return prev
    
    # recursive
    # Time complexity: O(n).
    # Space complexity: O(n).
    def reverseList_rec(self, head):
        if not head or not head.next:
            return head

        p = self.reverseList_rec(head.next)
        head.next.next = head
        head.next = None
        return p

```


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
Дан корень бинарного дерева и две вершины, найти наименьший общий предок двух вершин.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Начните обход дерева с корневого узла.</li>
 <li>Текущий узел является одной из двух искомых вершин, мы пометим переменную mid как True и продолжим поиск другого узла в левой и правой ветвях.</li>
 <li>Если либо левая, либо правая ветвь возвращает True, это означает, что один из двух узлов был найден ниже по этой ветке.</li>
 <li>Если в какой-либо момент обхода любые два из трех флагов слева, справа или посередине становятся истинными, это означает, что мы нашли наименьшего общего предка для узлов p и q.</li>
</ol>
</blockquote></details>


```
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
```

```python
# Approach 1: Recursive Approach
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        def recurse_tree(current_node):
            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node.val == p.val or current_node.val == q.val

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans

```


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
Даны точки на графике, определить можно ли провести такую линию между точками, чтобы точки оказались отражением друг друга.

https://leetcode.com/problems/line-reflection/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Избавляемся от дубликатов точек.</li>
 <li>Ищем точки с бОльшим и меньшим значением по оси Х.</li>
 <li>Если такая линия и есть, то она должна проходить между между точками из пред. пункта.</li>
 <li>Для каждой точки вычисляем ее отражение и проверяем есть ли такая точка в нашем исходном массиве точек.</li>
 <li>Вернуть True, если все точки имеют свое отражение, иначе вернуть False.</li>
</ol>
</blockquote></details>


```
Example 1:
Input: points = [[1,1],[-1,1]]
Output: true
Explanation: We can choose the line x = 0.

Example 2:
Input: points = [[1,1],[-1,-1]]
Output: false
Explanation: We can't choose a line.
```


```python
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # remove duplicates
        points = set(map(tuple, points))

        # find max and min on x
        point_min_x = min(points, key=lambda x: x[0])
        point_max_x = max(points, key=lambda x: x[0])

        # calculate a line between min x and max x
        middle_line = (point_min_x[0] + point_max_x[0]) / 2

        for x, y in points:
            # create a mirror point
            mirror_point = (2 * middle_line - x, y)
            # check that a mirror point in the points
            if mirror_point not in points:
                return False
        return True

```


## Design Hit Counter
Разработатать класс для подсчета ударов.

https://leetcode.com/problems/design-hit-counter/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Метод init: инициализируем пустую хеш-мапу.</li>
 <li>Метод hit: считаем удары на каждой секунде.</li>
 <li>Метод getHits: за начало берем разницу между временем - 300 (5 мин), суммируем кол-во ударов на каждой секунде.</li>
</ol>
</blockquote></details>


```
Example 1:
Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.
```


```python
class HitCounter:

    def __init__(self):
        self.hits = {}

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.hits:
            self.hits[timestamp] = 0
        self.hits[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        begin = timestamp - 300
        count = 0

        for i in range(begin + 1, timestamp + 1):
            if i in self.hits:
                count += self.hits[i]
        return count

```


## Insert Delete Getrandom
Разработать структуру данных, для вставки и удаления за О(1).
Функцию генерации случайных элементов можно взять из встроенного модуля random.

https://leetcode.com/problems/insert-delete-getrandom-o1/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Метод init: инициализируем пустую хеш-мапу и пустой массив.</li>
 <li>Метод insert: вставляем значение в хеш-мап как ключ, а его значением будет последний индекс массива + 1 на момент вставки, затем вставить значение в конец массива.</li>
 <li>Метод remove: если значение есть в хеш-мап, то узнаем индекс значения в массиве, на индекс удаляемого значения записываем последнее значение массива, удаляется последнее значение из массива (для избежания дублей), обновляется индекс последнего значения в хеш-мапе, наконец удаляется ключ удаляемого значения из хеш-мапы.</li>
</ol>
</blockquote></details>


```
Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
```


```python
import random


class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.array)
            self.array.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            idx = self.hashmap[val]
            last_value = self.array[-1]
            self.array[idx] = last_value
            self.array.pop()
            self.hashmap[last_value] = idx
            del self.hashmap[val]
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.array)

```


## Is Subsequence
Даны две строки, определить что первая строка является подпоследовательностью второй строки.

https://leetcode.com/problems/is-subsequence/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем два указателя, первый для первой строки, второй для второй, изначально ставим указатели в начало строк.</li>
 <li>Если символы одинаковы, сдвигаем оба указателя, в другом случае только указатель второй строки.</li>
 <li>Если мы дошли до конца первой строки первым указателем, то строка является подпоследовательностью второй строки.</li>
 <li>Если мы дошли до конца второй строки вторым указателем, то первая строка не является подпоследовательностью второй строки.</li>
 <li>Проверки 3 и 4 пункта должны проходить вначале итерации, а уже потом можно инкрементировать указатели.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
```

```python
class Solution:
    # Approach 1: Divide and Conquer with Greedy
    # Time Complexity: O(T)
    # Space Complexity: O(T)
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False

        if s[0] == t[0]:
            s = s[1:]
        t = t[1:]
        return self.isSubsequence(s, t)

    # Approach 2: Two-Pointers
    # Time Complexity: O(T)
    # Space Complexity: O(1)
    def isSubsequence(self, s: str, t: str) -> bool:
        left = right = 0
        while True:
            if left == len(s):
                return True
            if right == len(t):
                return False

            if s[left] == t[right]:
                left += 1
            right += 1

```


## String Compression
Сжать массив символов за O(1) по памяти. Вернуть длину сжатой строки

https://leetcode.com/problems/string-compression/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем два указателя. Один для итерации по входному массиву, другой для подсчета одинаковых символов внутри массива.</li>
 <li>Инкрементируем указатель подсчета одинаковых символов, если символы под обоими указателями равны.</li>
 <li>Через разницу между индексами указателей вычисляем кол-во повторов каждого символа.</li>
 <li>Вставляем в массив символ под первым указателем и инкрементируем результирующую переменную.</li>
 <li>Если разница больше единицы, то итерируемся по разнице между указателями, вставляем в массив кол-во повторов и инкрементируем результат.</li>
 <li>Выравниваем указатели относительно друг друга в конце каждой итерации.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
```

```python
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        first_pointer = result = 0

        while first_pointer < len(chars):
            second_pointer = first_pointer
            while second_pointer < len(chars) and chars[second_pointer] == chars[first_pointer]:
                second_pointer += 1

            chars[result] = chars[first_pointer]
            result += 1

            diff = second_pointer - first_pointer
            if diff > 1:
                # multiple characters like 10, 12, etc
                for digit in str(diff):
                    chars[result] = digit
                    result += 1

            first_pointer = second_pointer

        # you also can return a string result
        chars = ''.join(chars[:result])

        return result

```


## Max Consecutive Ones II
Дан массив единиц и нулей, найти самую длиную подстроку из единиц, если мы можем удалить не более одного нуля.

https://leetcode.com/problems/max-consecutive-ones-ii/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем скользящее окно, если в окне более чем один ноль.</li>
 <li>То сжимаем окно, если при сжатии из окна выходит ноль.</li>
 <li>То сбросить счетчик нулей в подстроке.</li>
<li>После подобной валидации обновляем результат как длину окна.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.
```

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window_start = 0
        result = 0
        zeroes = 0

        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                zeroes += 1
            
            while zeroes > 1:
                if nums[window_start] == 0:
                    zeroes -= 1
                window_start += 1
            
            result = max(result, window_end - window_start + 1)
        
        return result

```


## Permutation in String
Даны две строки s1 и s2, вернуть true, если s2 содержит перестановку s1, или false в противном случае.
Другими словами, вернуть true, если одна из перестановок s1 является подстрокой s2.

https://leetcode.com/problems/permutation-in-string/

<details><summary>Решение Sliding Window:</summary><blockquote>
<ol>
 <li>Сохранить все символы s1 в хеш-мап.</li>
 <li>Увеличиваем размер окна, если символ под указателем конца окна в хеш-мапе, то отнимаем один повтор.</li>
 <li>Если повторы символа равны 0, то значит есть совпадение этого символа.</li>
 <li>Если совпадения символов равно длине s1, вернем True.</li>
 <li>Если кол-во итераций больше чем сиволом в строке s1, то сжимаем окно.</li>
 <li>Отнимаем одно совпадение, если оно уже было учтено.</li>
 <li>Увеличиваем повтор символа на 1 в хеш-мапе.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

```python
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n(s1))
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start, matched, frequency_map = 0, 0, {}

        for ch in s1:
            if ch not in frequency_map:
                frequency_map[ch] = 0
            frequency_map[ch] += 1

        for window_end in range(len(s2)):
            right_char = s2[window_end]
            if right_char in frequency_map:
                frequency_map[right_char] -= 1
                if frequency_map[right_char] == 0:
                    matched += 1

            if matched == len(frequency_map):
                return True

            if window_end >= len(s1) - 1:
                left_char = s2[window_start]
                if left_char in frequency_map:
                    if frequency_map[left_char] == 0:
                        matched -= 1
                    frequency_map[left_char] += 1
                window_start += 1

        return False

```




## Find K Closest Elements
Дан массив отсортированный массив чисел и числа k и x, k ближайщих к x чисел.

https://leetcode.com/problems/find-k-closest-elements/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем бинарный поиск для эффективного решения.</li>
 <li>Инициализируем окно поиска как нулевой индекс и len(arr) - k, чтобы гарантировать, что мы не выйдем за границы нужного результирующего массива.</li>
 <li>Пока индексы не встретились, вычисляем середину.</li>
 <li>Затем условие, которое определяет в какую сторону сдвигаем окно поиска.</li>
 <li>Если разница между границей окна слева и значением x больше чем разница между правым концом и значением x, то сжиаем окно вправо, так мы ближе к x справа</li>
 <li>Иначе сжимаем окно влево.</li>
 <li>Вернем срез по левому индексу и левому индексу +k.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

```

```python
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            # Check if the window should move right
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        # Now left is the starting index of the k closest elements
        return arr[left:left + k]

```


## Valid Palindrome II
Дана строка, нужно определить может ли строка являться палиндромом, если мы удалим не более одного символа из строки.

https://leetcode.com/problems/valid-palindrome-ii/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем два указателя: один в начале, другой в конце.</li>
 <li>Если символы по оба указатели отличаются, то пропускаем символ под один указателем и проверяем подстроку на палиндром.</li>
 <li>А также вторую строку после символа, который не совпадает проверяем на палиндром.</li>
 <li>В итоге либо оригинальная строка, либо подстрока после символа, либо подстрока до символа будет палиндромом.</li>
 <li>Иначе строка не является палиндромом.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
```

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(subs: str) -> bool:
            return subs == subs[::-1]
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left:right]) or is_palindrome(s[left+1:right+1])
            left += 1
            right -= 1
        
        return True


```


## Max Stack
Создать структуру данных с поддержкой операций стэка и поддержкой поиска максимального элемента.

https://leetcode.com/problems/max-stack/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>В конструкторе класса определяем хранилище.</li>
 <li>push(x) - добавляем элемент x в конец массива.</li>
 <li>top() - получаем последний элемент из хранилища.</li>
 <li>peekMax() - используем ф-ию max() для поиска максимального элемента по массиву.</li>
 <li>popMax() - получаем значение из peekMax, проходим по массиву и удаляем элемент из хранилища, итерируя последовательность с конца.</li>
</ol>
</blockquote></details>

```
Example 1:
Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.
```


```python
class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        val = self.peekMax()
        for i in range(-1, -len(self.stack) - 1, -1):
            if self.stack[i] == val:
                del self.stack[i]
                break
        return val

```


## Maximize Distance to Closest Person
Дан бинарный массив, найти индекс с 0, находящийся на бОльшем расстоянии от единиц.

https://leetcode.com/problems/maximize-distance-to-closest-person/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Создаем генератор, который будет отдавать следующий индекс единицы из массива.</li>
 <li>Используем два указателя: prev - отслеживает последнюю единицу слева, изначально None, future - отслеживает следующую единицу справа, изначально индекс первой единицы.</li>
 <li>Итерируем входящий массив, если элемент на итерации равен единице, обновляем указатель prev на текущий индекс.</li>
 <li>Если элемент равен 0, то сдвигаем future до тех пор пока его нет и мы не вышли за текущую итерацию.</li>
 <li>Записываем с какого указателя меньше расстояние до ближайщей единицы для текущего индекса.</li>
 <li>Обновляем результат как максимум между текущуим результатом и пунктом 5.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:
Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Example 3:
Input: seats = [0,1]
Output: 1
```


```python
class Solution:
    def maxDistToClosest(self, seats):
        reserved = (i for i, seat in enumerate(seats) if seat == 1)
        prev = None
        future = next(reserved)
        result = 0

        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(reserved, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                result = max(result, min(left, right))

        return result

```


## Squares of a Sorted Array
Дан массив отсортированных чисел, вернуть массив квадратов каждого числа тоже в отсортированном порядке.

https://leetcode.com/problems/squares-of-a-sorted-array/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Два указателя: один на начале, другой на конце.</li>
 <li>Пока указатели не встретятся.</li>
 <li>Возводим элемент на итерации в квадрат.</li>
 <li>Если квадарат левого указателя оказывается больше, то добавляем в результат его и инкрементим левый указатель.</li>
 <li>Если квадрат правого указателя оказывается большье. то добавляем в результат его и сдвигаем правый указатель к левому.</li>
 <li>В конце возвращаем результат.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

```python
from collections import deque
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> deque[int]:
        left, right = 0, len(nums) - 1
        result = deque([])
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                result.appendleft(nums[left] ** 2)
                left += 1
            else:
                result.appendleft(nums[right] ** 2)
                right -= 1
        return result

```


## Number of Students Doing Homework at a Given Time
Даны массивы чисел, первый это начало работы студента, второй конец работы студента, также дано число, характеризуещее конкетный час.
Вернуть кол-во студентов за работой в конкетный час.

https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Идем циклом по длине любого из массивов так как они одинаковой длины.</li>
 <li>Если переданное число больше или равно времени начала работы, а также меньше или равно завершению времени работ студента, то увеличиваем счетчик студентов.</li>
 <li>Возвращаем счетчик студентов.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
Explanation: We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.

Example 2:
Input: startTime = [4], endTime = [4], queryTime = 4
Output: 1
Explanation: The only student was doing their homework at the queryTime.
```

```python
from typing import List


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        students = 0
        for i in range(len(endTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                students += 1
        return students

```


## Longest Subarray of 1 After Deleting One Element
Дан бинарный массив. Найти наиболее длинную последовательность единиц после удаления одного элемента.
Вернуть длину этой последовательности.

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Оба указателя начинают с первого элемента.</li>
 <li>Если end натыкается на 1, то увеличиваем счетчик единиц.</li>
 <li>Если размер окна - кол-во единиц больше 1 т.е. появляется второй ноль в окне.</li>
 <li>Проверка на то что под стартом стоит единица, если это так то уменьшить счетчик единиц.</li>
 <li>Увеличить переменную начала окна.</li>
 <li>На каждой итерации обновлять результирующую переменную.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
```

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ones, window_start, max_length = 0, 0, 0

        for window_end in range(len(nums)):
            if nums[window_end] == 1:
                ones += 1

            if window_end - window_start + 1 - ones > 1:
                if nums[window_start] == 1:
                    ones -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start)

        return max_length

```
