# Array
+ [Remove Duplicates from Sorted Array](#remove-duplicates-froms-sorted-array)
+ [Best Time to Buy and Sell Stock II](#best-time-to-buy-and-sell-stock-ii)
+ [Rotate Array](#rotate-array)
+ [Contains Duplicate](#contains-duplicate)
+ [Single Number](#single-number)
+ [Intersection of Two Arrays II](#intersection-of-two-arrays-ii)
+ [Plus One](#plus-one)
+ [Move Zeroes](#move-zeroes)
+ [Two Sum](#two-sum)
+ [Valid Sudoku](#valid-sudoku)
+ [Rotate Image](#rotate-image)


## Remove Duplicates from Sorted Array
Удалить дубликаты из массива.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Так как изначально размер массива (не динамического) изменить невозможно, мы переносим уникальные элеенты в начало массива.</li>
 <li>Начать можем со второго элемента массива, так как первый элемент массива точно не является дубликатом.</li>
 <li>Для хранения индекса куда будет вставлен следующий уникальный элемент будет отвечать переменная insert_idx.</li>
 <li>Идем по массиву и если встречаем уникальный элемент, то вставляем его под сохраненный индекс insert_idx.</li>
 <li>Инкрементируем insert_idx для вставки следующего уникального элемента.</li>
 <li>После прохода по массиву insert_idx будет также равен числу уникальных элементов в массиве.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_idx = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[insert_idx] = nums[i]
                insert_idx += 1

        return insert_idx

```


## Best Time to Buy and Sell Stock II
.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

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

Example 3:
Input: 
Output: 
```

```python

```


## Rotate Array
.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

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

Example 3:
Input: 
Output: 
```

```python

```


## Contains Duplicate
.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

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

Example 3:
Input: 
Output: 
```

```python

```


## Single Number
Дан массив чисел, каждое число в массиве появляется дваждый, каждое, кроме одного, найти число, которое не имеет дубликатов.

https://leetcode.com/problems/single-number/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>В одной переменной применим оператор XOR для каждого элемента, повторяющиеся элементы все будет убраны из переменной, останется только уникальное число без пары.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [2, 2, 1]
Output: 1

Example 2:
Input: [4, 1, 2, 1, 2]
Output: 1

Example 3:
Input: [1]
Output: 1
```

```python
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        return result

```


## Intersection of Two Arrays II
.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

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

Example 3:
Input: 
Output: 
```

```python

```


## Plus One 
Дано число, представленное массивом, например число 123 будет дано как [1,2,3].
Увеличить число на 1, и вернуть результат в таком же формате, для примера выше [1,2,4]

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Итерировать массив с конца, если на иитерации девятка, то превратить ее в 0 и перейти к следующей итерации.</li>
 <li>Иначе увеличить число под индексом и вернуть массив.</li>
 <li>Если цикл окончился значит на входе были все 9ки, превративишиеся в 0, вернем [1] + digit.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9] 
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

```python
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits

        # we're here because all the digits are nines
        return [1] + digits

```



## Move Zeroes
Дан массив чисел, в нем записаны положительные числа в порядке возрастания и нули нарушающий порядок.
Изменить массив на месте так, чтобы нули находились в конце массива, а сортировка массива из положительных чисел не нарушилась.

https://leetcode.com/problems/move-zeroes/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Идем по массиву и смотрим равен ли элемент 0.</li>
 <li>Если это уникальный элемент, то нам нужно свапнуть элемент с элеметом чей индекс мы храним в переменной, необходимой для отслеживания индекса последнего элемента, который не равен 0.</li>
 <li>Таким образом мы просвапаем все элементы, которые не равны 0 в начало массива, а все 0 будет находиться в конце массива.</li>
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
from typing import List


class Solution:

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def moveZeroesAdditionalSpace(self, nums: List[int]):
        result = []
        zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
            else:
                result.append(nums[i])

        while zeroes:
            result.append(0)
            zeroes -= 1

        return result

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def moveZeroes(self, nums: List[int]):
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1

        return nums

```


## Two Sum
.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

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

Example 3:
Input: 
Output: 
```

```python

```


## Valid Sudoku
.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

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

Example 3:
Input: 
Output: 
```

```python

```



## Rotate Image
.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

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

Example 3:
Input: 
Output: 
```

```python

```


