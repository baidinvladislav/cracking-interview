# LeetCode Yandex Track

Also I have Google Sheet file with short solutions:\
https://docs.google.com/spreadsheets/d/1rVY3TVtwOXMm8j2h93VBsJgNu9rJw2w_f2w_BR5gtkg/edit#gid=0

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
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndexMap = {}
        maxLength = 0
        start = 0

        for end in range(len(s)):
            if s[end] in charIndexMap and charIndexMap[s[end]] >= start:
                start = charIndexMap[s[end]] + 1

            charIndexMap[s[end]] = end
            maxLength = max(maxLength, end - start + 1)

        return maxLength

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
 <li><strong>Инициализация:</strong> Начинаем с установки начального и конечного индексов самого длинного палиндрома, которые в начале равны 0.</li>
 <li><strong>Определение центра:</strong> Проходим по каждому символу строки, рассматривая его как потенциальный центр палиндрома. Проверяем палиндромы как с одним центром (нечетная длина), так и с двумя центрами (четная длина).</li>
 <li><strong>Расширение палиндрома:</strong> Для каждого центра пытаемся расширить палиндром влево и вправо, пока символы с обеих сторон совпадают. Функция возвращает максимально возможную длину палиндрома для данного центра.</li>
 <li><strong>Обновление максимального палиндрома:</strong> Сравниваем длину найденного палиндрома с текущим максимумом. Если найденный палиндром длиннее, обновляем индексы начала и конца на основе текущего центра и длины палиндрома.</li>
 <li><strong>Возвращение результата:</strong> По завершении всех итераций возвращаем подстроку, начиная с индекса `start` и заканчивая индексом `end` + 1, как самый длинный палиндром в строке.</li>
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
                start = left1
                end = right1
            if right2 - left2 > end - start:
                start = left2
                end = right2

        return s[start:end+1]

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
 <li>Создаем фиктивный начальный узел, который поможет упростить вставку.</li>
 <li>Пока в обоих списках есть элементы.</li>
 <li>Если элементы остались только в одном из списков, присоединяем их.</li>
 <li>Возвращаем начало сформированного списка.</li>
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
    def mergeTwoLists1(self, list1, list2):
        # Создаем фиктивный начальный узел, который поможет упростить вставку
        dummy = ListNode()
        current = dummy

        # Пока в обоих списках есть элементы
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Если элементы остались только в одном из списков, присоединяем их
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Возвращаем начало сформированного списка
        return dummy.next

```


## Generate Parentheses
Написать функцию, которая принимает число и генерирует правильную скобочную последовательность скобок для n пар скобок.

https://leetcode.com/problems/generate-parentheses/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Для генерации нужной строки используем рекурсию с базовым случаем, когда строка в два раза больше чем число n, тут же добавляем готовую строку в result.</li>
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


## Simplify Path
Упростить UNIX путь.

https://leetcode.com/problems/simplify-path/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Инициализация пустого стека для хранения имен директорий:
   <pre><code>stack = []</code></pre>
 </li>
 <li>Разделение пути на компоненты, используя метод <code>.split('/'):</code>
   <pre><code>components = path.split('/') </code></pre>
 </li>
 <li>Обработка каждого компонента в цикле:
   <ol>
     <li>Пропуск пустых компонентов и текущих директорий (одиночные точки):
       <pre><code>if component == '' or component == '.':
   continue</code></pre>
     </li>
     <li>Если компонент равен <code>'..'</code>, то:
       <ul>
         <li>Удаление последнего элемента из стека (если стек не пуст):
           <pre><code>if stack:
   stack.pop()</code></pre>
         </li>
       </ul>
     </li>
     <li>Если компонент является именем директории, то:
       <ul>
         <li>Добавление компонента в стек:
           <pre><code>else:
   stack.append(component)</code></pre>
         </li>
       </ul>
     </li>
   </ol>
 </li>
 <li>Формирование упрощенного пути из элементов стека:
   <pre><code>simplified_path = '/' + '/'.join(stack)</code></pre>
 </li>
 <li>Возврат упрощенного пути:
   <pre><code>return simplified_path</code></pre>
 </li>
</ol>
</blockquote></details>

```
Example 1:
Input: path = "/home/"
Output: "/home"
Explanation:
The trailing slash should be removed.
 
Example 2:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation:
Multiple consecutive slashes are replaced by a single one.

Example 3:
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explanation:
A double period ".." refers to the directory up a level.

Example 4:
Input: path = "/../"
Output: "/"
Explanation:
Going one level up from the root directory is not possible.

Example 5:
Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
Explanation:
"..." is a valid name for a directory in this problem.
```

```python
def simplifyPath(path: str) -> str:
    stack = []

    # Split the path by '/'
    components = path.split('/')

    for component in components:
        if component == '' or component == '.':
            # Skip empty components and current directory references
            continue
        elif component == '..':
            # Move up one directory level if possible
            if stack:
                stack.pop()
        else:
            # Valid directory name, push onto stack
            stack.append(component)

    # Join the stack to form the simplified path
    simplified_path = '/' + '/'.join(stack)

    return simplified_path

```


## Merge Sorted Array
Вам даны два целочисленных массива nums1 и nums2, отсортированные в порядке неубывания, и два целых числа m и n, 
представляющие количество элементов в nums1 и nums2 соответственно. Объедините nums1 и nums2 в один массив, 
отсортированный в неубывающем порядке.

https://leetcode.com/problems/merge-sorted-array/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>
    Используем 3 указателя, где 1ый это указатель на конец массива nums1, 2ой указатель - указатель на последний элемент nums2,
    последний указатель будет указывать на последний элемент массива nums1, включая его заглушки.
 </li>
 <li>Пока указатель второго массива больше 0, выполняем итерации с конца к началу.</li>
 <li>На каждой итерации мы сравниваем элементы под первый и вторым указателем.</li>
 <li>Помещаем на k индекс в массив nums1 бОльщий элемент из двух.</li>
 <li>Декрементим только тот указатель, который оказался с наибольшим элементов.</li>
 <li>Декрементим третий указатель на каждой итерации.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        # Initialize pointers for nums1, nums2 and the last index of merged array
        i, j, k = m - 1, n - 1, m + n - 1

        # Merge in reverse order
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if node is None:
                return True
            
            left = validate(node.left, low, node.val)
            right = validate(node.right, node.val, high)

            if not low < node.val < high:
                return False

            return left and right 

        return validate(root, float('-inf'), float('inf'))

```


## Symmetric Tree
Определить ясвляется ли дерево симетричным.

https://leetcode.com/problems/symmetric-tree/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>.</li>
 <li>.</li>
 <li>.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root):
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root, root)

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
 <li><strong>Структура данных:</strong> Используем хэш-таблицу для хранения ключей и узлов двусвязного списка. Каждый узел содержит ключ, значение и ссылки на предыдущий и следующий узлы. Это позволяет быстро обновлять статус элементов в кэше согласно их использованию.</li>
 <li><strong>Метод get(key):</strong> Проверяет, существует ли ключ в хэш-таблице.
   <ul>
     <li>Если ключ существует, узел извлекается и перемещается в конец списка, что обозначает его недавнее использование.</li>
     <li>Узел удаляется из текущего места в списке и добавляется в его конец.</li>
     <li>Возвращается значение узла. Если ключа нет, возвращает -1.</li>
   </ul>
 </li>
 <li><strong>Метод put(key, value):</strong> Добавляет пару ключ-значение в кэш или обновляет существующий ключ.
   <ul>
     <li>Если ключ уже существует, соответствующий узел удаляется из списка для последующего обновления его позиции.</li>
     <li>Создается новый узел и добавляется в конец списка, что показывает, что этот элемент был использован последним.</li>
     <li>Если размер кэша превышен, удаляется первый узел из списка (LRU элемент), и его ключ удаляется из хэш-таблицы.</li>
   </ul>
 </li>
 <li><strong>Метод _add_to_llist(self, node):</strong> Добавляет узел в конец двусвязного списка. Узел ставится перед "хвостом" списка, и ссылки обновляются соответственно.</li>
 <li><strong>Метод _remove_from_llist(self, node):</strong> Удаляет узел из двусвязного списка. Обновляются ссылки у предыдущего и следующего узлов.</li>
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


## One Edit Distance
Даны две строки s и t, опредилить можно ли их сделать одинаковыми за одно изменение.

https://leetcode.com/problems/one-edit-distance/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Опрделеить какой именно элемент отличается у массивов, нужен его индекс.</li>
 <li>В зависимости от разницы в длинах массивов понять какая операция потенциально может сделать массивы одинаковыми.</li>
 <li>Применить к массивам выбранную операцию для изменения.</li>
 <li>Вернуть True, если массивы стали одинаковыми после выполнения операции, иначе вернуть False.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.

Example 2:
Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step. 
```

```python
class Solution:
    def get_diff_idx(self, stack_s: list, stack_t: list) -> int:
        for i in range(min(len(stack_s), len(stack_t))):
            if stack_s[i] != stack_t[i]:
                return i

        return min(len(stack_s), len(stack_t))

    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t or len(t) - len(s) > 1:
            return False
        
        stack_s = list(s)
        stack_t = list(t)

        diff_idx = self.get_diff_idx(stack_s, stack_t)

        if len(stack_s) == len(stack_t):
            stack_s[diff_idx] = stack_t[diff_idx]
            return stack_s == stack_t
        elif len(stack_s) > len(stack_t):
            del stack_s[diff_idx]
            return stack_s == stack_t
        elif len(stack_s) < len(stack_t):
            stack_s.insert(diff_idx, stack_t[diff_idx])
            return stack_s == stack_t

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


## Binary Tree Right Side View
.

https://leetcode.com/problems

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
```

```python

```


## Number of Islands
Дана сетка размером MxN. В сетке находятся находятся значение '0' и '1'. Где '0' - это вода и '1' - это суша.
Вернуть кол-во островов на сетке.

https://leetcode.com/problems/number-of-islands/

### Описание алгоритма

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Рассматриваем сетку как неориентированный граф, в котором каждая "суша" ('1') соединена с соседними "сушами" по вертикали и горизонтали.</li>
 <li>При обнаружении '1' в сетке запускаем поиск в глубину (DFS) из этой точки, чтобы отметить все соединённые земли как посещённые, меняя их на '0'.</li>
 <li>На каждом этапе рекурсивного обхода DFS, мы устанавливаем для текущего узла значение '0', тем самым помечая его как посещённый и предотвращаем повторный обход.</li>
 <li>Рекурсивно применяем DFS к каждому из четырёх соседних направлений (верх, низ, лево, право), если они находятся в пределах границ сетки и также являются '1'.</li>
 <li>Каждый запуск DFS для непосещённой суши ('1') увеличивает счётчик островов на один.</li>
</ol>
</blockquote></details>

### Детализация DFS
- **Базовый случай:** Выход за границы сетки или ячейка не равна '1'.
- **Рекурсивное обновление:** После проверки ячейки меняем ее статус на посещенную и рекурсивно вызываем DFS для всех четырех смежных направлений (верх, низ, лево, право).

### Временная сложность
- **O(MN),** где M и N - размеры сетки, так как в худшем случае нужно посетить все ячейки.

### Пространственная сложность
- **O(MN),** в худшем случае из-за стека вызовов при максимально возможной глубине рекурсии.


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


## Isomorphic Strings
Определить что две строки изоморфны.

https://leetcode.com/problems/isomorphic-strings/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Нужно связать каждый символ из строки друг с другом.</li>
 <li>Если связь символов нарушается, значит строки не изоморфны.</li>
 <li>Если мы прошли обе строки и не разу связи символов не были нарушены, то они изоморфны, вернем True.</li>
</ol>
</blockquote></details>


```
Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

```

```python3
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] not in dict1 and t[i] not in dict2:
                dict1[s[i]] = t[i]
                dict2[t[i]] = s[i]
            else:
                if dict1.get(s[i]) != t[i] or dict2.get(t[i]) != s[i]:
                    return False
        
        return True

```


## Reverse Linked List
Развернуть связной список.

https://leetcode.com/problems/reverse-linked-list/

<details><summary>Итеративное решение:</summary><blockquote>
Описание шагов итеративного метода:

1. **Сохранение ссылки на следующий узел:**
   - Сначала сохраняем ссылку на следующий узел (`next`), чтобы не потерять доступ к оставшейся части списка после изменения ссылки текущего узла.

2. **Изменение указателя следующего узла:**
   - Изменяем указатель следующего узла (`current.next`), чтобы он указывал на предыдущий узел (`prev`). Изначально `prev` — это `None`, так как новый конец списка должен указывать на `None`.

3. **Перемещение `prev` на текущий узел:**
   - Перемещаем `prev` на текущий узел, таким образом, `prev` последовательно перемещается от начала списка к его концу, в то время как `current` двигается от начала к концу исходного списка.

4. **Перемещение `current` на следующий узел:**
   - Перемещаем `current` на следующий узел, который мы сохранили ранее. Это гарантирует, что мы продолжаем обработку каждого узла.

5. **Окончание обработки:**
   - Когда `current` достигает конца списка (`None`), `prev` указывает на новую голову перевернутого списка.

</blockquote></details>

<details><summary>Рекурсивное решение:</summary><blockquote>
Описание шагов рекурсивного метода:
<ol>
 <li>Вызываем функцию рекурсивно для всех узлов, пока не достигнем последнего узла связанного списка.</li>
 <li>Последний узел, к которому нет доступа из предыдущего узла (`head.next == None`), становится новой головой списка.</li>
 <li>На обратном пути рекурсии, устанавливаем `head.next.next = head` (это делает предыдущий узел следующим для текущего) и затем устанавливаем `head.next = None` (чтобы разорвать исходную связь и предотвратить циклы).</li>
 <li>Повторяем до тех пор, пока не вернемся к исходной голове списка, которая теперь будет последним узлом перевернутого списка.</li>
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
 <li>Инициализируем указатели <code>start</code> и <code>end</code>, установив их на начало входного массива <code>nums</code>. Эти указатели будут отслеживать текущий диапазон чисел.</li>
 <li>Начинаем итерацию по массиву <code>nums</code> с первого элемента. В процессе итерации, если разница между текущим элементом и следующим элементом равна 1 (то есть они последовательные), сдвигаем указатель <code>end</code> вправо на один элемент.</li>
 <li>Когда обнаруживаем, что текущий элемент и следующий элемент не являются последовательными, проверяем значения указателей <code>start</code> и <code>end</code>:</li>
    <ul>
      <li>Если указатели <code>start</code> и <code>end</code> указывают на разные числа (то есть указатель <code>end</code> сдвигался), добавляем в результирующий массив строку формата "start->end", которая обозначает диапазон чисел от <code>start</code> до <code>end</code>.</li>
      <li>Если указатели <code>start</code> и <code>end</code> указывают на одно и то же число (то есть диапазон состоит из одного числа), добавляем в результирующий массив только значение <code>start</code>.</li>
    </ul>
 <li>Обновляем указатель <code>start</code> на следующий элемент и устанавливаем указатель <code>end</code> на это же число для обработки следующего возможного диапазона.</li>
 <li>Продолжаем итерацию до конца массива <code>nums</code>, повторяя шаги 2-4 для каждого элемента массива.</li>
 <li>После завершения итерации добавляем последний диапазон или одиночное число в результирующий массив, так как последний диапазон не был добавлен в процессе итерации.</li>
 <li>Возвращаем результирующий массив, содержащий все диапазоны чисел в виде строк.</li>
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
def summaryRanges(nums):
    ranges = []
    n = len(nums)
    if n == 0:
        return ranges

    # Начало текущего диапазона
    start = nums[0]

    for i in range(1, n):
        # Если текущий элемент не является последовательным
        if nums[i] != nums[i - 1] + 1:
            # Проверяем, если start равен предыдущему элементу (одиночный элемент)
            if start == nums[i - 1]:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}->{nums[i - 1]}")
            # Обновляем начало диапазона
            start = nums[i]

    # Добавляем последний диапазон
    if start == nums[-1]:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}->{nums[-1]}")

    return ranges

# Примеры использования:
print(summaryRanges([0, 1, 2, 4, 5, 7]))  # Вывод: ["0->2", "4->5", "7"]
print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))  # Вывод: ["0", "2->4", "6", "8->9"]

```


## Lowest Common Ancestor of a Binary Tree
Дан корень бинарного дерева и две вершины, найти наименьший общий предок двух вершин.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>БС: если текущий узел None или p или q, то вренуть текущий узел.</li>
 <li>Вызвать рекурсивно для левого и правого поддерева.</li>
 <li>Если вернулись узлы из обоих поддеревьев, то вернуть текущий узел.</li>
 <li>Если вернулись узлы только из одного дерева, вернуть тот узел, который не None.</li>
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
          if not root or root == p or root == q:
              return root
      
          left = self.lowestCommonAncestor(root.left, p, q)
          right = self.lowestCommonAncestor(root.right, p, q)
      
          if left and right:
              return root
      
          return left if left else right

```


## Move Zeroes
Дан массив nums, переместите все 0 в его конец, сохраняя порядок ненулевых элементов.
Обратите внимание, что вы должны сделать это на месте, не создавая копию массива.

https://leetcode.com/problems/move-zeroes/

<details><summary>Решение 1:</summary><blockquote>
<ol>
 <li>Инициализируем переменную в которой храним индекс по которому будет осуществляться вставка в массив.</li>
 <li>Если элемент на итерации не равен нулю, то вставляем его по индексу из предыдущего пукта, а также инкрементируем индекс для вставки.</li>
 <li>Если ноль то просто скипаем итерацию.</li>
 <li>Если индекс вставки не нулевого элемента не дошел до конца, то заполнить оставщиеся ячейки массива нулями.</li>
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


## Longest Substring with At Most K Distinct Characters
Дана строка и число, вернуть длину самой длиной подстроки, которая содержит не более k различных символов.

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем скользящее окно.</li>
 <li>Сжимаем окно, до тех пор пока, оно не удовлятворяет условиям по уникальности символов.</li>
 <li>Для этого используем словарь с подсчетом символов и их частоты.</li>
 <li>После сжатия окна, обновляем результат, если требуется, т.к окно валидно.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
```

```python
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start_window = 0
        freq_map = defaultdict(int)
        result = 0

        for end_window in range(len(s)):
            freq_map[s[end_window]] += 1

            while len(freq_map) > k:
                freq_map[s[start_window]] -= 1
                if freq_map[s[start_window]] == 0:
                    del freq_map[s[start_window]]
                start_window += 1

            result = max(result, end_window - start_window + 1)

        return result

```


## Intersection of Two Arrays
Дано два массива, нужно вернуть множество пересечения их элементов.

https://leetcode.com/problems/intersection-of-two-arrays/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Нужно будет три множества: 1ое для 1го массива, 2ое для 2ое и 3ее для результата.</li>
 <li>Пройдем по первому множеству и добавим все элементы, которые есть и во втором множестве в результат.</li>
 <li>Пройдем по второму множеству и добавим все элементы, которые есть и в первом множестве в результат.</li>
 <li>Вернем результирующее множество</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
```

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        result = set()

        for num in s1:
            if num in s2:
                result.add(num)
        
        for num in s2:
            if num in s1:
                result.add(num)

        result = list(result)
        return result

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

<details><summary>Решение:</summary>
<blockquote>
<ol>
 <li><b>Метод `__init__`:</b> Инициализация экземпляра класса с пустым словарем. Этот словарь будет использоваться для хранения количества ударов, зарегистрированных в каждую секунду. Ключами в словаре будут временные метки (целые числа, представляющие секунды), а значениями — количество ударов, происходящих в эту секунду.</li>
 <li><b>Метод `hit`:</b> Этот метод принимает один параметр, `timestamp`, который указывает временную метку удара. Метод проверяет, существует ли уже ключ `timestamp` в словаре. Если ключ существует, увеличивает его значение на один, чтобы отразить новый удар. Если ключа нет, создает новый ключ с начальным значением 1. Это означает регистрацию удара в новую секунду, которая ранее не была зарегистрирована.</li>
 <li><b>Метод `getHits`:</b> Принимает параметр `timestamp`, который представляет текущее время запроса. Метод должен возвращать количество ударов, произошедших за последние 300 секунд (5 минут). Для этого, начинает подсчет от `timestamp - 300` и до `timestamp`, включительно. Метод перебирает каждую секунду в этом диапазоне, проверяя, есть ли соответствующая запись в словаре. Суммирует значения всех существующих записей в этом временном окне. Если данные за какие-то секунды отсутствуют, их вклад в сумму равен нулю. Это позволяет получить точное количество ударов, зарегистрированных в последние пять минут относительно заданного времени.</li>
</ol>
</blockquote>
</details>


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
 <li><strong>Метод `__init__`:</strong> Инициализируем пустую хеш-таблицу и пустой массив.</li>
 <li><strong>Метод `insert`:</strong> 
   <ul>
     <li>Проверяем, существует ли значение в хеш-таблице.</li>
     <li>Если значение уже существует, возвращаем `false`.</li>
     <li>Если значение не существует:
       <ul>
         <li>Добавляем значение в конец массива.</li>
         <li>В хеш-таблицу добавляем пару ключ-значение, где ключ — это добавляемое значение, а значение — индекс добавленного элемента в массиве.</li>
         <li>Возвращаем `true`.</li>
       </ul>
     </li>
   </ul>
 </li>
 <li><strong>Метод `remove`:</strong>
   <ul>
     <li>Проверяем, существует ли значение в хеш-таблице.</li>
     <li>Если значение не существует, возвращаем `false`.</li>
     <li>Если значение существует:
       <ul>
         <li>Получаем индекс удаляемого элемента из хеш-таблицы.</li>
         <li>Сохраняем значение последнего элемента массива.</li>
         <li>Перемещаем последнее значение массива на место удаляемого элемента.</li>
         <li>Обновляем индекс последнего значения в хеш-таблице.</li>
         <li>Удаляем последний элемент массива с помощью метода `pop`.</li>
         <li>Удаляем значение из хеш-таблицы.</li>
         <li>Возвращаем `true`.</li>
       </ul>
     </li>
   </ul>
 </li>
 <li><strong>Метод `getRandom`:</strong> Возвращаем случайный элемент из массива, используя линейный конгруэнтный генератор (LCG) для генерации случайного индекса.</li>
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
        self.data = []
        self.val_to_index = {}
    
    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.data.append(val)
        self.val_to_index[val] = len(self.data) - 1
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last_element = self.data[-1]
        
        # Перемещаем последний элемент на место удаляемого элемента
        self.data[index] = last_element
        self.val_to_index[last_element] = index
        
        # Удаляем последний элемент
        self.data.pop()
        del self.val_to_index[val]
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.data)

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
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = t_pointer = 0

        while True:
            if s_pointer == len(s):
                return True

            if t_pointer == len(t):
                return False
            
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1

```


## String Compression
Сжать массив символов за O(1) по памяти. Вернуть длину сжатой строки

https://leetcode.com/problems/string-compression/

<details><summary>Развернутое описание алгоритма:</summary>
<blockquote>
<ol>
 <li><b>Инициализация указателей:</b> Один указатель (`first_pointer`) используется для итерации по входному массиву символов, начиная с первого элемента. Второй указатель (`second_pointer`) служит для подсчета одинаковых символов, начиная с той же позиции, что и `first_pointer`.</li>
 <li><b>Подсчет повторяющихся символов:</b> Перемещаем `second_pointer` вперед до тех пор, пока символы в позициях `first_pointer` и `second_pointer` совпадают. Это позволяет подсчитать количество последовательно повторяющихся символов в массиве.</li>
 <li><b>Вычисление количества повторений:</b> Определяем количество повторов символа как разницу между `second_pointer` и `first_pointer`. Это число показывает, сколько раз подряд встречается символ.</li>
 <li><b>Запись сжатой информации:</b> Символ, на который указывает `first_pointer`, записываем в ту же позицию массива, на которую указывает переменная `result`. Затем инкрементируем `result` на один, чтобы перейти к следующей позиции для записи.</li>
 <li><b>Запись количества повторений:</b> Если количество повторений больше одного, конвертируем число повторений в строку и последовательно записываем каждую цифру этой строки в массив начиная с текущей позиции `result`, инкрементируя `result` после каждой цифры.</li>
 <li><b>Синхронизация указателей:</b> После обработки группы символов устанавливаем `first_pointer` равным `second_pointer`, чтобы начать обработку следующей группы символов. Это обеспечивает последовательный переход к новой группе без повторения уже обработанных символов.</li>
</ol>
</blockquote>
</details>

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


## Subarray Sum Equals K
.

https://leetcode.com/problems

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
```

```python

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


## Find Duplicate Subtrees
.

https://leetcode.com/problems

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
```

```python

```


## Find K Closest Elements
Дан массив отсортированный массив чисел и числа k и x, k ближайщих к x чисел.

https://leetcode.com/problems/find-k-closest-elements/description/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li><b>Бинарный поиск:</b> Используем бинарный поиск, чтобы минимизировать количество проверок и быстро найти начальный индекс для результирующего массива K ближайших элементов. Этот метод эффективно уменьшает область поиска, сокращая время выполнения алгоритма.</li>
 <li><b>Инициализация окна поиска:</b> Задаем начальные границы поиска с `left = 0` и `right = len(arr) - k`, чтобы убедиться, что выбранное окно будет содержать ровно K элементов, не выходя за пределы массива.</li>
 <li><b>Вычисление середины:</b> В цикле, пока `left` меньше `right`, находим среднюю точку (`mid`) между `left` и `right`. Это середина текущего окна поиска.</li>
 <li><b>Оценка разности расстояний:</b> Сравниваем абсолютные значения разности между `x` и элементом массива в позиции `mid` и между `x` и элементом на позиции `mid + k`. Это позволяет оценить, какая часть окна ближе к `x`.</li>
 <li><b>Сдвиг окна поиска:</b>
   <ul>
     <li>Если разница между `x` и элементом на позиции `mid` больше, чем разница между `x` и элементом на позиции `mid + k`, это означает, что ближайшие элементы скорее находятся справа от `mid`, и мы сдвигаем `left` вправо на `mid + 1`.</li>
     <li>Если условие не выполняется, это означает, что ближайшие элементы находятся слева от `mid`, и мы сдвигаем `right` к `mid`.</li>
   </ul>
 </li>
 <li><b>Результат:</b> По завершении бинарного поиска, `left` будет указывать на начало диапазона из `k` ближайших элементов. Возвращаем срез `arr[left:left + k]`, который и будет содержать K ближайших к `x` элементов, отсортированных в порядке возрастания.</li>
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
 <li><b>Конструктор класса:</b> Определяем два хранилища в виде списков:
   <ul>
     <li><code>stack</code> — основной стек для хранения всех элементов.</li>
     <li><code>maxStack</code> — вспомогательный стек для хранения максимальных значений. В каждый момент времени вершина <code>maxStack</code> содержит текущий максимум всех элементов в <code>stack</code>.</li>
   </ul>
 </li>
 <li><b>Метод push(x):</b> Добавляем элемент <code>x</code> в конец списка <code>stack</code>. Далее проверяем, необходимо ли добавить <code>x</code> в <code>maxStack</code>:
   <ul>
     <li>Если <code>maxStack</code> пуст или <code>x</code> больше или равен последнему элементу в <code>maxStack</code>, добавляем <code>x</code> в <code>maxStack</code>.</li>
   </ul>
 </li>
 <li><b>Метод top():</b> Возвращает последний элемент из <code>stack</code>, не изменяя стек. Это операция получения верхнего элемента стека.</li>
 <li><b>Метод peekMax():</b> Просто возвращает последний элемент из <code>maxStack</code>, который является максимальным значением текущего состояния <code>stack</code>.</li>
 <li><b>Метод popMax():</b> Удаляет и возвращает максимальный элемент из стека:
   <ul>
     <li>Используем значение из <code>peekMax()</code> для определения максимального элемента.</li>
     <li>Создаём временный буфер для хранения элементов, которые нужно временно удалить из <code>stack</code>, чтобы добраться до максимального элемента.</li>
     <li>Удаляем элементы из <code>stack</code> до тех пор, пока не найдём максимальный элемент, перемещая каждый удалённый элемент в буфер.</li>
     <li>Удаляем максимальный элемент из <code>stack</code> и <code>maxStack</code>.</li>
     <li>Возвращаем элементы из буфера обратно в <code>stack</code>, восстанавливая порядок элементов и обновляя <code>maxStack</code> по мере необходимости.</li>
   </ul>
 </li>
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
        self.maxStack = []

    def push(self, x: int):
        self.stack.append(x)
        if not self.maxStack or x >= self.maxStack[-1]:
            self.maxStack.append(x)

    def pop(self):
        val = self.stack.pop()
        if val == self.maxStack[-1]:
            self.maxStack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.maxStack[-1]

    def popMax(self):
        max_val = self.maxStack[-1]
        buffer = []
        while self.stack[-1] != max_val:
            buffer.append(self.pop())
        self.pop()  # Remove the max element
        while buffer:
            self.push(buffer.pop())
        return max_val


```


## Maximize Distance to Closest Person
Дан бинарный массив, найти индекс с 0, находящийся на бОльшем расстоянии от единиц.

https://leetcode.com/problems/maximize-distance-to-closest-person/

<details><summary>Решение:</summary><blockquote>
<ol>
  <li>Инициализируем переменные `max_distance` для хранения максимального расстояния и `last_person` для хранения индекса последнего встреченного человека.</li>
  <li>Проходим по массиву `seats`, используя цикл `for`.</li>
  <li>Если текущий элемент массива равен 1 (человек), выполняем следующие шаги:
    <ol>
      <li>Если это первый встреченный человек, обновляем `max_distance` до текущего индекса.</li>
      <li>Если это не первый человек, вычисляем максимальное расстояние до ближайшего человека для всех мест между `last_person` и текущим человеком и обновляем `max_distance`, если это расстояние больше текущего значения `max_distance`.</li>
      <li>Обновляем `last_person` на текущий индекс.</li>
    </ol>
  </li>
  <li>После окончания прохода по массиву, если последние места пустые, проверяем и обновляем `max_distance`, если расстояние от последнего человека до конца массива больше текущего значения `max_distance`.</li>
  <li>Возвращаем значение `max_distance`, которое представляет максимальное расстояние до ближайшего человека для выбранного места.</li>
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
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Инициализируем переменную для хранения максимального расстояния
        max_distance = 0
        # Инициализируем переменную для хранения индекса последнего встреченного человека
        last_person = -1
        # Длина массива seats
        n = len(seats)
        
        # Проходим по каждому элементу массива seats
        for i in range(n):
            # Если текущий элемент - человек (1)
            if seats[i] == 1:
                # Если это первый встреченный человек
                if last_person == -1:
                    # Максимальное расстояние до ближайшего человека для всех предыдущих пустых мест равно i
                    max_distance = i
                else:
                    # Если это не первый человек, вычисляем расстояние до ближайшего человека для всех мест между last_person и текущим человеком
                    max_distance = max(max_distance, (i - last_person) // 2)
                # Обновляем last_person на текущий индекс
                last_person = i
        
        # Обработка хвоста массива, если последние места пустые
        if seats[n - 1] == 0:
            # Проверяем и обновляем max_distance, если расстояние от последнего человека до конца массива больше текущего max_distance
            max_distance = max(max_distance, n - 1 - last_person)
        
        # Возвращаем максимальное расстояние до ближайшего человека
        return max_distance

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


## Interval List Intersections
.

https://leetcode.com/problems

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
```

```python

```


## Max Consecutive Ones III
Дан массив из нулей и единиц, также число k которое позволяет заменить k нулей на единицы, 
вернуть подстроку с наибольшей последовтельностью единиц.

https://leetcode.com/problems/max-consecutive-ones-iii/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем скользящее окно и подсчитываем кол-во единиц в окно.</li>
 <li>Сжимаем окно, когда кол-во нулей в окне больше k.</li>
 <li>Обновляем результат, если нужно, потому что окно отвалидировано.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

```python
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        start = 0
        zeroes = 0
        result = 0
        
        for end in range(len(nums)):
            if nums[end] == 0:
                zeroes += 1
            
            while zeroes > k:
                if nums[start] == 0:
                    zeroes -= 1
                start += 1
                
            result = max(result, end - start + 1)

        return result

```


## Destination City
.

https://leetcode.com/problems

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
```

```python

```


## Number of Students Doing Homework at a Given Time
Даны массивы чисел, первый это начало работы студента, второй конец работы студента, также дано число, характеризуещее конкретный час.
Вернуть кол-во студентов за работой в конкретный час.

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
