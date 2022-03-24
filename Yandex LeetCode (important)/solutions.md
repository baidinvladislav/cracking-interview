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


## Merge k Sorted Lists


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


## Valid Palindrome
Дана строка s, вернуть true, если это палиндром, или false.
В строке могут содержаться буквы разного регистра, а также не только буквенно-цифровые символы.

https://leetcode.com/problems/valid-palindrome/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Отфильтровать все буквенно-цифровые символы.</li>
 <li>Привести отфильтрованные символы к нижнему регистру.</li>
 <li>Привести отфильтрованные символы нижнего регистра к списку.</li>
 <li>Сравнить два среза [:], [::-1] списка из предыдущего пункта.</li>
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
    def isPalindrome(self, s: str) -> bool:
        filtered_symbols = filter(lambda symbol: symbol.isalnum(), s)
        lo_low_case = map(lambda symbol: symbol.lower(), filtered_symbols)
        to_list = list(lo_low_case)
        return to_list == to_list[::-1]

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
