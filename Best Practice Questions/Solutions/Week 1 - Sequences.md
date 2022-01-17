# Week 1 - Sequences
+ [Two Sum](#two-sum)
+ [Contains Duplicate](#contains-duplicate)
+ [Best Time to Buy and Sell Stock](#best-time-to-buy-and-sell-stock)
+ [Valid Anagram](#valid-anagram)
+ [Valid Parentheses](#valid-parentheses)
+ [Product of Array Except Self](#product-of-array-except-self)
+ [Maximum Subarray](#maximum-subarray)
+ [3Sum](#3sum)
+ [Merge Intervals](#merge-intervals)
+ [Group Anagrams](#group-anagrams)
+ [Maximum Product Subarray](#maximum-product-subarray)
+ [Search in Rotated Sorted Array](#earch-in-rotated-sorted-array)


## Two Sum
Дан неотсортированный массив чисел, вернуть индексы двух чисел сумма которых равна таргету.

https://leetcode.com/problems/two-sum/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Идем по циклу, трекая порядковый номер итерации..</li>
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
```

<details><summary>Test cases</summary><blockquote>

```python
import unittest


class TestTwoSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual([-1, -1], Solution().twoSum(nums=[], target=9))

    def test_first(self):
        self.assertEqual([0, 1], Solution().twoSum(nums=[2, 7, 11, 15], target=9))

    def test_second(self):
        self.assertEqual([1, 2], Solution().twoSum(nums=[3, 2, 4], target=6))

    def test_third(self):
        self.assertEqual([0, 1], Solution().twoSum(nums=[3, 3], target=6))

    def test_no_solution(self):
        self.assertEqual([-1, -1], Solution().twoSum(nums=[3, 3, 1, 4, 5], target=16))


if __name__ == "__main__":
    unittest.main()
```

</blockquote></details>


## Contains Duplicate
Дан массив чисел, вернуть True если в массиве есть дубликаты, вернуть False, если массив содержит только уникальные числа.

https://leetcode.com/problems/contains-duplicate/


<details><summary>Решение:</summary><blockquote>
Три решения:
<ol>
 <li>Отсортировать массив и идти по нему циклом сравнивая nums[i-1] и nums[i].</li>
 <li>Добавить все числа в словарь и отслеживать их частоту, если у кого больше чем  1, то значит был дубликат.</li>
 <li>Воспользоваться встроенной структурой set().</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

```python
from typing import List


class Solution:
    def containsDuplicate_additional_memory(self, nums: List[int]) -> bool:
        buffer = {}
        for num in nums:
            if num not in buffer:
                buffer[num] = 1
            else:
                return True
        return False

    def containsDuplicate_sorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False

    def containsDuplicate_set(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestContainsDuplicate(unittest.TestCase):
    def test_first(self):
        self.assertTrue(Solution().containsDuplicate_additional_memory(nums=[1, 2, 3, 1]))
        self.assertTrue(Solution().containsDuplicate_sorting(nums=[1, 2, 3, 1]))
        self.assertTrue(Solution().containsDuplicate_set(nums=[1, 2, 3, 1]))

    def test_second(self):
        self.assertFalse(Solution().containsDuplicate_additional_memory(nums=[1, 2, 3, 4]))
        self.assertFalse(Solution().containsDuplicate_sorting(nums=[1, 2, 3, 4]))
        self.assertFalse(Solution().containsDuplicate_set(nums=[1, 2, 3, 4]))

    def test_third(self):
        self.assertTrue(Solution().containsDuplicate_additional_memory(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertTrue(Solution().containsDuplicate_sorting(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertTrue(Solution().containsDuplicate_set(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    unittest.main()
```

</blockquote></details>


## Best Time to Buy and Sell Stock
Дан массив с числами, каждое число представляет цену акции на iый день.
Найти день наилучший для покупки и день наилучший для продажи.
Вернуть наибольшую прибыль после продажи. Если прибыль получить невозможно вернуть 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Для решения задачи отслеживаем две переменные: max_profit и min_price.</li>
 <li>Если на итерации число меньше чем в min_price, то обновляем min_price текущим числом.</li>
 <li>Вычисляем прибыль, отнимая от числа на текущей итерации min_price.</li>
 <li>Обновляем max_profit числом из второго пункта, если прибыль получилась больше чем была.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

```python3 
class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestContainsDuplicate(unittest.TestCase):
    def test_first(self):
        self.assertEqual(5, Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))

    def test_second(self):
        self.assertEqual(0, Solution().maxProfit(prices=[7, 6, 4, 3, 1]))
```

</blockquote></details>


## Valid Anagram
Даны две строки. Вернуть True, если строки являются анаграмами, вернуть False в противном случае.
Анаграмма - это слово образованное от другого путем перестановки букв.

https://leetcode.com/problems/valid-anagram/

<details><summary>Решение:</summary><blockquote>
Два решения:
<ol>
 <li>Отсортировать две строки и сравнить их.</li>
 <li>Создать по словарю для каждой строки. Добавить символы первой строки и их частоту в первый словарь, также поступить и для второй строки и второго словаря. Сравнить два словаря.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
```


```python3
class Solution:
    def isAnagram_sorting(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram_additional_memory(self, s: str, t: str) -> bool:
        buffer_1, buffer_2 = {}, {}
        
        for char in s:
            buffer_1[char] = buffer_1.get(char, 0) + 1

        for char in t:
            buffer_2[char] = buffer_2.get(char, 0) + 1

        return buffer_1 == buffer_2
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestContainsDuplicate(unittest.TestCase):
    def test_first(self):
        self.assertTrue(5, Solution().isAnagram_sorting(s="anagram", t="nagaram"))
        self.assertTrue(5, Solution().isAnagram_additional_memory(s="anagram", t="nagaram"))

    def test_second(self):
        self.assertFalse(0, Solution().isAnagram_sorting(s="rat", t="car"))
        self.assertFalse(0, Solution().isAnagram_additional_memory(s="rat", t="car"))
```

</blockquote></details>


## Valid Parentheses
Дана строка в которой могу быть символы: '(', ')', '{', '}', '[', ']'.
Вернуть True, если скобочная последовательность в строке верная (открывающая скобка закрывается скобкой такого же типа и 
скобки закрываются в правильном порядке).

https://leetcode.com/problems/valid-parentheses/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Инициализировать словарь со скобками и пустой сткек.</li>
 <li>Идем циклом по входной строке.</li>
 <li>Если символ строке есть ключ в словаре скобок, то значит символ является открывающей скобкой, добавляем символ в стек.</li>
 <li>Если стек пуст или если из словаря по последнему элементу стека мы не получаем текущий элемент (нужная закрывающая скобка), значит скобочная последовательность не верная.</li>
 <li>Вернуть булево значение от пустого стека.</li>
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

```python3
from collections import deque


def isValid(s):
    parentheses = {'(': ')', '{': '}', '[': ']'}
    stack = deque()

    for symbol in s:
        if symbol in parentheses:
            stack.append(symbol)

        elif len(stack) == 0 or parentheses[stack.pop()] != symbol:
            return False

    return len(stack) == 0
```


<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestContainsDuplicate(unittest.TestCase):
    def test_first(self):
        self.assertTrue(Solution().isValid(s="()"))

    def test_second(self):
        self.assertTrue(Solution().isValid(s="()[]{}"))

    def test_third(self):
        self.assertFalse(Solution().isValid(s="(]"))
```

</blockquote></details>


## Product of Array Except Self
Дан массив чисел, вернуть новый массив содержащий перемножение всех элементов кроме iго элемента.
Решение за линейное время и без операции деления.

https://leetcode.com/problems/product-of-array-except-self/

```
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

```python3
def productExceptSelf(self, nums):
    p = 1
    n = len(nums)
    output = []
    for i in range(0,n):
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i] * p
        p = p * nums[i]
    return output
```

## Maximum Subarray
Вернуть самую большую сумму подмассива.

https://leetcode.com/problems/maximum-subarray/

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
    # Initialize our variables using the first element.
    current_subarray = max_subarray = nums[0]

    # Start with the 2nd element since we already used the first one.
    for num in nums[1:]:
        # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)

    return max_subarray
```


## 3Sum
Для массива целых чисел nums вернуть все триплеты [nums[i], nums[j], nums[k]] такие, что i != j, i != k и j != k, и nums[i] + nums[j] + nums[k] == 0. Обратите внимание, что в наборе решений не должно быть повторяющихся триплетов.

https://leetcode.com/problems/3sum/

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
def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res
```


## Merge Intervals
Дан массив интервалов, смержить все пересекающиеся интервалы и вернуть массив не пересекающихся интервалов.

https://leetcode.com/problems/merge-intervals/

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
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out
```


## Group Anagrams
Дан массив слов, сгруппировать анаграммы в массивах.

https://leetcode.com/problems/group-anagrams/

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
    char_map = defaultdict(list)
    for word in strs:
        sorted_word = sorted(word)
        key = tuple(sorted_word)
        char_map[key].append(word)
    return char_map.values()
```


## Maximum Product Subarray
Дан массив чисел. Вернуть максимальное произведение подмассивов.

https://leetcode.com/problems/maximum-product-subarray/

```
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

```python3

```


## Search in Rotated Sorted Array
Дан массив числе отсортированный по возрастанию и развернутый относительно одного указателя.
Вернуть индекс таргета, если его нет вернуть -1.
Решение за O(log n).

https://leetcode.com/problems/search-in-rotated-sorted-array/

```
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
```

```python3

```



