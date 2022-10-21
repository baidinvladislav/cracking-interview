# Dynamic programming and recursion
+ [Recursive String Permutations](#recursive-string-permutations)
+ [Compute the nth Fibonacci Number](#compute-the-nth-fibonacci-number)
+ [Making Change](#making-change)
+ [Cake Thief](#cake-thief)


## Recursive String Permutations
Дана строка, нужно вернуть все возможные перестановки строки.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>БС: длина строки == 1.</li>
 <li>Рекурсивно собрать все подстроки и добавлять в подстроки первый элемент в начало строки.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: 'AB'
Output: ['AB', 'BA']

Example 2:
Input: 'ABC'
Output: ['ABC', 'BAC', 'BCA', 'ACB', 'CAB', 'CBA']

Example 3:
Input: 'ABCD'
Output: ['ABCD', 'BACD', 'BCAD', 'BCDA', 'ACBD', 'CABD', 'CBAD', 'CBDA', 'ACDB', 'CADB', 'CDAB', 'CDBA', 'ABDC', 'BADC', 'BDAC', 'BDCA', 'ADBC', 'DABC', 'DBAC', 'DBCA', 'ADCB', 'DACB', 'DCAB', 'DCBA']

```

```python
# cracking the coding interview solution
def generate_permutations(text):
    """
    1. Base case: len(nums) equal 1
    2. Separate first element from remainder
    3. Generate all possible subarrays based on remainder
    4. Looping through every subarray
    5. Insert first element inside every subarray in every possible place
    """
    if len(text) == 1:
        return [text]

    results = []
    first = text[0]
    remainder = text[1:]

    words = generate_permutations(remainder)
    for word in words:
        for i in range(len(word) + 1):
            # insert first char at each index/position of word
            s = word[:i] + first + word[i:]
            results.append(s)

    return results

```


## Compute the nth Fibonacci Number
Вычислить n-ое значение последовательности ряда Фибоначчи.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>БС: если n-ое значение ряда == 0 или 1, вернуть n-ое значение ряда.</li>
 <li>Рекурсивно пройти формулу Фибоначчи fib = (n - 1) + (n - 2).</li>
 <li>Добавить мемоизацию, добавив словарь для хранения проделанных вычислений.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: 1
Output: 1

Example 2:
Input: 5
Output: 5

Example 3:
Input: 10
Output: 55

```

```python
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    memo = {}
    def fib(self, n):
        if n in [0 ,1]:
            return n
        
        if n in self.memo:
            return self.memo[n]
        
        result = self.fib(n - 1) + self.fib(n - 2)
        self.memo[n] = result
        
        return result

```


## Making Change


## Cake Thief
