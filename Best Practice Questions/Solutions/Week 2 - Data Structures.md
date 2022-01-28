# Week 2 - Data Structures
+ [Longest Substring Without Repeating Characters](#longest-substring-without-repeating-characters)
+ [Container With Most Water](#container-with-most-water)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Minimum Window Substring](#minimum-window-substring)
+ [Linked List Cycle](#linked-list-cycle)
+ [Find Minimum in Rotated Sorted Array](#find-minimum-in-rotated-sorted-array)
+ [Number of Islands](#number-of-islands)
+ [Reverse Linked List](#reverse-linked-list)
+ [Pacific Atlantic Water Flow](#pacific-atlantic-water-flow)
+ [Longest Repeating Character Replacement](#longest-repeating-character-replacements)
+ [Palindromic Substrings](#palindromic-substrings)


## Longest Substring Without Repeating Characters
Дана строка, найти в ней самую длинную подстроку без повторения символов.

https://leetcode.com/problems/longest-substring-without-repeating-characters/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Идем циклом по строке</li>
 <li>Если символ строки есть в словаре, то обновляем индекс начала окна, выбирая бОльшее значение из window_start и индекса +1 из словаря</li>
 <li>Добавляем/обновляем индекс последнего элемента в словаре</li>
 <li>Обновляем максимальную длину, выбирая бОльшее значение из старого значения и текущей длины окна</li>
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
def lengthOfLongestSubstring(self, s: str) -> int:
    window_start, max_length, hash_map = 0, 0, dict()

    for window_end in range(len(s)):
        if s[window_end] in hash_map:
            window_start = max(window_start, hash_map[s[window_end]] + 1)

        hash_map[s[window_end]] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
```

<details><summary>Test cases</summary><blockquote>

```python
import unittest


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring(s="abcabcbb"))

    def test_second(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring(s="bbbbb"))

    def test_third(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring(s="pwwkew"))
```

</blockquote></details>


## Container With Most Water
Дан массив чисел, каждое число представляет высоту линии на графике.
Найти две линии между которыми на графике будет больше всего площадь.
Вернуть площадь.

https://leetcode.com/problems/container-with-most-water/


<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Ведем два указателя на встречу друг другу.</li>
 <li>Высчитываем площадь и сохраняем самое большое значение.</li>
 <li>Если число под левым указателем меньше чем число под правым указателем, то сдвигаем левый указатель.</li>
 <li>В других случаях сдвигаем правый указатель.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
```

```python
def maxArea(self, height):
    result = 0
    left, right = 0, len(height) - 1

    while left < right:
        result = max(result, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual(49, Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))

    def test_second(self):
        self.assertEqual(1, Solution().maxArea(height=[1, 1]))


if __name__ == "__main__":
    unittest.main()
```

</blockquote></details>


## Remove Nth Node From End of List
Дан связной список и число n. Удалить из списка узел под числом n.

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Ставим два указателя в начало списка.</li>
 <li>Перемещаем быстрый указатель на n узлов вперед.</li>
 <li>Если быстрый указатель вышел за пределы списка, то вернуть второй по счету узел.</li>
 <li>Двигаем два указателя пока быстрый указатель не дойдет до конца списка.</li>
 <li>Переопределяем соседа медленного указателя через один узел от него.</li>
 <li>Возвращаем новую голову связного списка.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
```

```python3 
def removeNthFromEnd(self, head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next

    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestRemoveNthFromEnd(unittest.TestCase):
    def test_first(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        excepted_head = Node(1)
        excepted_head.next = Node(2)
        excepted_head.next.next = Node(3)
        excepted_head.next.next.next = Node(5)
        self.assertEqual(excepted_head, Solution().removeNthFromEnd(head=head, n=2))

    def test_second(self):
        head = Node(1)
        self.assertIsNone(Solution().removeNthFromEnd(head=head, n=1))

    def test_third(self):
        head = Node(1)
        head.next = Node(2)

        excepted_head = Node(1)
        self.assertEqual(excepted_head, Solution().removeNthFromEnd(head=head, n=1))
```

</blockquote></details>


## Minimum Window Substring
Даны две строки. Нужно найти окно в первой строке в котором будет полностью содержаться вторая строка независимо от перестановки строки паттерна. 

https://leetcode.com/problems/valid-anagram/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Добавить все симваолы паттерна (второй строки) в словарь.</li>
 <li>Идем циклом по строке и если символ строки есть в словаре, то вычитаем единицу из его частоты, если его частота больше или равна 0, то засчитываем одно совпадение.</li>
 <li>Выполняем второй пункт до тех пор пока кол-во совпадений не будет равно кол-ву символов в строке паттерна.</li>
 <li>Если минимальная длина (изначально равная длина строки + 1) больше чем длина окна, то обновляем мин. длину длиной окна.</li>
 <li>Записываем индекс начала окна в начало подстроки.</li>
 <li>Увеличиваем индекс начала окна на 1.</li>
 <li>Проверяем есть ли начальный символ строки в словаре, если есть и его частота равна 0, то вычитаем одно совпадение..</li>
 <li>В любом случае добавляем единицу к частоте левого символа.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```


```python3
def find_substring(str1, pattern):
    """
    1. Insert pattern characters to Python dictionary.
    2. Extend the window if the last window character in dictionary then decrement their frequency.
    3. If after decrement last character frequency it will be equal 0. We got one match.
    4. While number matches equal number character in pattern we shrink the window and update window start index.
    """
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str1) + 1
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:  # Count every matching of a character
                matched += 1

        # Shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                # Note that we could have redundant matching characters, therefore we'll decrement the
                # matched count only when a useful occurrence of a matched character is going out of the window
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if min_length > len(str1):
        return ""

    return str1[substr_start:substr_start + min_length]
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestMinWindow(unittest.TestCase):
    def test_first(self):
        self.assertEqual("BANC", Solution().minWindow(s="ADOBECODEBANC", t="ABC"))

    def test_second(self):
        self.assertEqual("a", Solution().minWindow(s="a", t="a"))

    def test_third(self):
        self.assertEqual("", Solution().minWindow(s="a", t="aa"))
```

</blockquote></details>


## Linked List Cycle
Дан связной список. Определить содержит ли список цикл.

https://leetcode.com/problems/linked-list-cycle/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Ставим медленный указатель и быстрый указатель в начало списка.</li>
 <li>Идем циклом по списку медленным указателем по узлу за шаг, а быстрым по два узла за шаг.</li>
 <li>Доходим быстрым указателем до конца, если быстрый указатель догнал медленный, значит в списке есть цикл, если прошли весь список, то цикла нет.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed)

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

```python3
def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False
```

## Find Minimum in Rotated Sorted Array
Найти минимальное число в развернутом отсортированном массиве.

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем модифицированную версию бинарного поиска.</li>
 <li>Для решения необзодимо найти точку перегиба.</li>
 <li>Находим центральный элемент массива.</li>
 <li>Если центральный элемент массива больше чем первый элемент массива, то значит точка перегиба находится справа от центрального элемента.</li>
 <li>Если центральный элемент массива меньше чем первый элемент массива, то значит точка перегиба находится слева от центрального элемента.</li>
 <li>Прекращаем поиск, когда находим точку перегиба, для этого должно выполниться одно из двух условий: 1) центральный элемент больше чем последующий за ним элемент nums[mid] > nums[mid + 1] 2) центральный элемент меньше чем элемиент перед ним nums[mid - 1] > nums[mid].</li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

```python3
def findMin(self, nums):
    if len(nums) == 1:
        return nums[0]

    left = 0
    right = len(nums) - 1

    if nums[right] > nums[0]:
        return nums[0]

    while right >= left:
        mid = left + (right - left) / 2
        
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestFindMin(unittest.TestCase):
    def test_first(self):
        self.assertEqual(1, Solution().findMin(nums=[3, 4, 5, 1, 2]))

    def test_second(self):
        self.assertEqual(0, Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2]))

    def test_third(self):
        self.assertEqual(11, Solution().findMin(nums=[11, 13, 15, 17]))
```
</blockquote></details>


## Number of Islands
Дана сетка размером MxN. В сетке находятся находятся значение '0' и '1'. Где '0' - это вода и '1' - это суша.
Вернуть кол-во островов на сетке.

https://leetcode.com/problems/number-of-islands/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Рассмотрим сетку как неориентированный граф, у которого ребра есть у смежных соседних вершин по горизонтали и вертикали со значением '1'.</li>
 <li>Линейно проходим по сетке, если в вершине значение '1', то ночинаем от этой вершины поиск в ширину.</li>
 <li>Добавляем такую вершину в очередь и устанавливаем для нее значение '0', помечая вершину как посещенную..</li>
 <li>Итеративно ищем соседей этой вершины у которых тоже значение '1', меняем на '0'.</li>
 <li>Повторяем пока в очереди есть вершины.</li>
 <li>Кол-во раз когда запускался поиск в ширину и будет равен кол-ву островое на сетке.</li>
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
from collections import deque


def numIslands(self, grid):
    rows = len(grid)
    columns = len(grid[0])
    nums_islands = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == '1':
                nums_islands += 1
                grid[i][j] = '0'
                neighbors = deque()
                neighbors.append([i, j])
                while neighbors:
                    neighbor = neighbors.popleft()
                    row, column = neighbor[0], neighbor[1]
                    if row - 1 >= 0 and grid[row - 1][column] == '1':
                        neighbors.append([row - 1, column])
                        grid[row - 1][column] = '0'
                    if row + 1 < rows and grid[row + 1][column] == '1':
                        neighbors.append([row + 1, column])
                        grid[row + 1][column] = '0'
                    if column - 1 >= 0 and grid[row][column - 1] == '1':
                        neighbors.append([row, column - 1])
                        grid[row][column - 1] = '0'
                    if column + 1 < columns and grid[row][column + 1] == '1':
                        neighbors.append([row, column + 1])
                        grid[row][column + 1] = '0'
    return nums_islands
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestNumIslands(unittest.TestCase):
    def test_first(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        self.assertEqual(1, Solution().numIslands(grid))

    def test_second(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        self.assertEqual(3, Solution().numIslands(grid))
```

</blockquote></details>


## Reverse Linked List
Для массива целых чисел nums вернуть все триплеты [nums[i], nums[j], nums[k]] такие, что i != j, i != k и j != k, и nums[i] + nums[j] + nums[k] == 0. Обратите внимание, что в наборе решений не должно быть повторяющихся триплетов.

https://leetcode.com/problems/3sum/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Сортируем входной массив.</li>
 <li>Проходим циклом по массиву, пропуская дубликаты.</li>
 <li>Необходимо для каждого числа на итерации цикла найти два таких числа сумма которых будет равна отрицательному числу на итерации, для этого используем метод двух указателей.</li>
 <li>Если два числа дают в суммме отрицательное число, то добавить 3 числа (число итерации и два числа под указателями) в ответ.</li>
 <li>Если сумма меньше, то сдвинуть левый указатель к концу.</li>
 <li>Если сумма больше, то сдвинуть правый указатель к началу.</li>
 <li>Вернуть массив троек.</li>
</ol>
</blockquote></details>


```
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
```


```python3
class Solution:
    def threeSum(self, nums):
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if nums[i - 1] == nums[i]:
                continue

            self.search_pair(nums, triplets, left=i + 1, target_sum=-nums[i])
        return triplets

    def search_pair(self, arr, triplets, left, target_sum):
        right = len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1

                # skip duplicates
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif current_sum < target_sum:
                left += 1

            elif current_sum > target_sum:
                right -= 1
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))

    def test_second(self):
        self.assertEqual([], Solution().threeSum(nums=[]))

    def test_third(self):
        self.assertEqual([], Solution().threeSum(nums=[0]))
```

</blockquote></details>


## Pacific Atlantic Water Flow
Дан массив интервалов, смержить все пересекающиеся интервалы и вернуть массив не пересекающихся интервалов.

https://leetcode.com/problems/merge-intervals/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Отсортировать интервалы по их началу.</li>
 <li>Берем за точку отсчета первый интервал из массива.</li>
 <li>Цикл по массиву со второго элемента.</li>
 <li>Если конец предыдущего интервала больше чем начало последующего, то интервалы пересекаются, берем за конец интервала больший конец двух интервалов.</li>
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

```python3
def merge(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x[0])
    merged_intervals = []

    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if end >= interval[0]:
            end = max(interval[1], end)
        else:
            merged_intervals.append([start, end])
            start = interval[0]
            end = interval[1]

    merged_intervals.append([start, end])
    return merged_intervals
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestMergeIntervals(unittest.TestCase):
    def test_first(self):
        self.assertEqual([[1, 6], [8, 10], [15, 18]], Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))

    def test_second(self):
        self.assertEqual([[1, 5]], Solution().merge(intervals=[[1, 4], [4, 5]]))
```

</blockquote></details>


## Longest Repeating Character Replacement
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

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(output, Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))

    def test_second(self):
        self.assertEqual([[""]], Solution().groupAnagrams(strs=[""]))

    def test_third(self):
        self.assertEqual([["a"]], Solution().groupAnagrams(strs=["a"]))```
```
</blockquote></details>


## Palindromic Substrings
Дан массив чисел. Вернуть максимальную сумму смежного подмассива.

https://leetcode.com/problems/maximum-product-subarray/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Инициализируем текущий массив и максимальный массив первым элементом в массиве</li>
 <li>Идем циклом по массиву со второго элемента и обновляем текущий массив либо числом итерации либо число итерации + текущий массив</li>
 <li>Обновляем максимальный массив либо максимальным массивом либо текущим массивом</li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
```

```python3
def maxSubArray(nums):
    current_subarray = max_subarray = nums[0]

    for i in range(1, len(nums)):
        current_subarray = max(nums[i], current_subarray + nums[i])
        max_subarray = max(current_subarray, max_subarray)

    return max_subarray
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        self.assertEqual(6, Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_second(self):
        self.assertEqual(1, Solution().maxSubArray(nums=[1]))

    def test_third(self):
        self.assertEqual(23, Solution().maxSubArray(nums=[5, 4, -1, 7, 8]))
```
</blockquote></details>
