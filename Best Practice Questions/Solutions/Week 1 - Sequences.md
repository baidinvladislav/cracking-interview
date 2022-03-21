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


class TestBestTimeBuyAndSellStock(unittest.TestCase):
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


class TestValidAnagram(unittest.TestCase):
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
 <li>Создаем хеш-таблицу в которой под каждой открывающей скобкой храним закрывающую скобку такого же типа.</li>
 <li>Инициализируем пустой стек.</li>
 <li>Итерируем строку.</li>
 <li>Если символ на итерации есть в как ключ в хеш-таблице, значит это открытвающая скобка, добавляем ее на верх стека.</li>
 <li>Если нет символа в хеш-таблице, то проверяем пуст ли стек, если он пуст на этом этапе, то строка не валидна.</li>
 <li>Если последний элемент стека не хранит значение текущего символа в хеш-таблице, то строка не валидна.</li>
 <li>Вернуть булево значение, пустой ли стек.</li>
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


class Solution:
    def isValid(self, s):
        hash_map = {'(': ')', '[': ']', '{': '}', }
        stack = deque()

        for char in s:
            if char in hash_map:
                stack.append(char)
            else:
                if not stack:
                    return False

                last_el = stack.pop()
                if hash_map[last_el] != char:
                    return False
        return not stack
```


<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestValidParentheses(unittest.TestCase):
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
Решение должно быть за линейное время и без операции деления.

https://leetcode.com/problems/product-of-array-except-self/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Накапливаем префикс каждого элемента в результирующем массиве.</li>
 <li>Умножаем элемента результирующего массива на постфикс, проходя циклом с конца к началу.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

```python3
def productExceptSelf(nums):
    result = []

    prefix = 1
    for i in range(len(nums)):
        result.append(prefix)
        prefix *= nums[i]

    postfix = 1
    for i in reversed(range(len(nums))):
        result[i] *= postfix
        postfix *= nums[i]

    return result
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestProductArrayExceptSelf(unittest.TestCase):
    def test_first(self):
        self.assertEqual([24, 12, 8, 6], Solution().productExceptSelf(nums=[1, 2, 3, 4]))

    def test_second(self):
        self.assertEqual([0, 0, 9, 0, 0], Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]))
```
</blockquote></details>


## Maximum Subarray
Вернуть самую большую сумму подмассива.

https://leetcode.com/problems/maximum-subarray/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Проходим первый раз по циклу и перемножаем элементы, сохраняем макс.произведение чисел, если натыкаемся на 0, то начинаем накапливать произведение заново.</li>
 <li>Делаем тоже самое, но в этот раз проходим массив с конца к началу.</li>
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
class Solution:
    def maxSubArray(self, nums):
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
        self.assertEqual(6, Solution().maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))

    def test_second(self):
        self.assertEqual(1, Solution().maxSubArray(nums=[1]))
```

</blockquote></details>


## 3Sum
Для массива целых чисел nums вернуть все триплеты [nums[i], nums[j], nums[k]] такие, что i != j, i != k и j != k, и nums[i] + nums[j] + nums[k] == 0. Обратите внимание, что в наборе решений не должно быть повторяющихся триплетов.

https://leetcode.com/problems/3sum/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Сортируем входной массив.</li>
 <li>Инициализируем пустой массив для сбора "троек".</li> 
 <li>Итерируем входной уже отсортированный массив.</li>
 <li>Если элемент из массива на итерации больше 0, то выходим из цикла, потому что нам нужны только отрицательные числа, которые находятся в левой части массива.</li>
 <li>Если это первая итерация или если это не дубликат, то вызываем ф-ию поиска пар.</li>
 <li>Левый указатель i + 1, правый длина входного массива - 1, считаем сумму трех чисел, если она равна 0, то добавляем в массив "троек" после чего пропускаем дубликаты левым указателем.</li>
 <li>Если текущая сумма меньше чем 0, то сдвигаем левый указатель к концу на один шаг.</li>
 <li>Если текущая сумма больше чем 0, то сдвигаем правый указатель к началу на один шаг.</li>
 <li>Вернуть заполненый массив "троек".</li>
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
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
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


## Merge Intervals
Дан массив интервалов, смержить все пересекающиеся интервалы и вернуть массив не пересекающихся интервалов.

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



## Maximum Product Subarray
Дан массив чисел. Вернуть максимальную сумму смежного подмассива.

https://leetcode.com/problems/maximum-product-subarray/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Переменная max_so_far нужна для хранения максимальной суммы позитивных чисел.</li>
 <li>Переменная min_so_far нужна для хранения максимальной суммы негативных чисел.</li>
 <li>Вернем максимальный результат.</li>
</ol>
</blockquote></details>

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
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        self.assertEqual(6, Solution().maxProduct(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_second(self):
        self.assertEqual(1, Solution().maxProduct(nums=[1]))

    def test_third(self):
        self.assertEqual(23, Solution().maxProduct(nums=[5, 4, -1, 7, 8]))
```
</blockquote></details>


## Search in Rotated Sorted Array
Дан массив числе отсортированный по возрастанию и развернутый относительно одного указателя.
Вернуть индекс таргета, если его нет вернуть -1.
Решение за O(log n).

https://leetcode.com/problems/search-in-rotated-sorted-array/

<details><summary>Решение:</summary><blockquote>
<ol>
    <li>Если начальный элемент меньше или равен центральному элементу</li>
        <ol>
            <li>Если таргет больше или равен начальному элементу и при этом тагрет меньше чем центральный элемент, то смотрим в правой части массива</li>
            <li>Если таргет меньше чем центральный элемент или равен центральному, то смотрим в правой части массива</li>
        </ol>
    <li>Если начальный элемент больше центрального элемента</li>
        <ol>
            <li>Если таргет больше чем центральный элемент и при этом он меньше или равен последнему, то смотрим справа</li>
            <li>Если таргет меньше или равен центральному элементу или таргет больше последнего элемента, то смотрим справа</li>
        </ol>
</ol>
</blockquote></details>

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
def search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid

        if nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1
```


<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        self.assertEqual(4, Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))

    def test_second(self):
        self.assertEqual(-1, Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))

    def test_third(self):
        self.assertEqual(-1, Solution().search(nums=[1], target=0))


if __name__ == "__main__":
    unittest.main()
```

</blockquote></details>



