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
Дано число и массив с наминалами монет.
Вернуть количество комбинаций монет данной суммы.

<details><summary>Простое рекурсивное решение:</summary><blockquote>

<ol>
 <li>БС №1: если оставшаяся сумма == 0 используем монетку и засчитываем обход рекурсии за 1 комбинацию монеток.</li>
 <li>БС №2: если оставшаяся сумма < 0 из-за текущей монетки мы вышли рамки нашей суммы, вернуть 0, НЕ засчитываем обход рекурсии за комбинацию монеток.</li>
 <li>БС №3: индекс монетки равен длине массива, мы исчерпали возможные монетки на этом вызове, вернуть 0, НЕ засчитывать обход рекурсии за комбинацию монеток.</li>
 <li>Тело рекурсии: пока сумма не исчерпана вызываем ф-ию рекурсивно, передавая в нее новый индекс монетки ,считаем комбинации, уменьшаем текущую сумму.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: (4, (1, 2, 3))
Output: 4

Example 2:
Input: (0, (1, 2))
Output: 1

Example 3:
Input: (1, ())
Output: 0

Example 4:
Input: (5, (25, 50))
Output: 0

Example 5:
Input: (50, (5, 10))
Output: 6

Example 6:
Input: (100, (1, 5, 10, 25, 50))
Output: 292

```

```python
# Simple recursion
# Time Complexity: O(n^^2)
# Space Complexity: O(n)
def change_possibilities(amount_left, denominations, current_index=0):
    if amount_left == 0:
        return 1
    
    if amount_left < 0:
        return 0
        
    if current_index == len(denominations):
        return 0
        
    current_coin = denominations[current_index]
    ways = 0
    while amount_left >= 0:
        ways += change_possibilities(amount_left, denominations, current_index + 1)
        amount_left -= current_coin
    
    return ways


# Memoization
# Time Complexity: O(n(amount_left) * m(len(denominations)))
# Space Complexity: O(n(amount_left) * m(len(denominations)))
def change_possibilities(amount_left, denominations, current_index=0, memo={}):
    if (amount_left, current_index) in memo:
        return memo[(amount_left, current_index)]

    if amount_left == 0: 
        return 1

    if amount_left < 0: 
        return 0

    if current_index == len(denominations): 
        return 0

    combinations = 0
    current_coin = denominations[current_index]
    while amount_left >= 0:
        combinations += change_possibilities(amount_left, denominations, current_index + 1, memo)
        amount_left -= current_coin

    memo[(amount_left, current_index)] = combinations
    return combinations


# their bottom-up solution
# Time Complexity: O(n * m)
# Space Complexity: O(n)
def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:

        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += (
                ways_of_doing_n_cents[higher_amount_remainder]
            )

    return ways_of_doing_n_cents[amount]

```


## Cake Thief
Даны торты (вес, ценность) и вместимость рюкзака, вернуть максимальную ценность, которую можно уложить в рюкзак, не превысив его вместимость.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Аллоцируем массив с ячейками для рюкзака и его подрюкзаков.</li>
 <li>Итерируемся по массиву с рюкзаками.</li>
 <li>Для каждого рюкзака итерируемся по массиву тортов.</li>
 <li>Если вес торта меньше или равен вместимости рюкзака (торт вместился), то вычисляем индекс необходимого подрюкзака (вместимость рюкзака - вес текущего торта), который мы можем уложить вместе с текущим рюкзаком (заполняем оставшееся место рюкзака).</li>
 <li>Берем максимум от текущего максимума и от суммы: текущий рюкзак + доступный подрюкзак.</li>
 <li>Вернуть элемент под последним индексом из массива рюкзаков.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [(4, 4), (5, 5)]
Output: 9

Example 2:
Input: [(4, 4), (5, 5)], 12
Output: 12

Example 3:
Input: [(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)]
Output: 7

Example 4:
Input: [(51, 52), (50, 50)], 100)
Output: 100

```

```python
# my solution based on their solution
# Time Complexity: O(n * k)
# Space Complexity: O(k)
def max_duffel_bag_value(cakes, capacity):
    bags = [0] * (capacity + 1)

    for capacity in range(len(bags)):
        current_max = 0
        for weight, value in cakes:
            if capacity >= weight:
                additional_bag = capacity - weight
                current_max = max(current_max, value + bags[additional_bag])

        bags[capacity] = current_max

    return bags[capacity]

```


## Balanced Binary Tree
Дано дерево, определить, что разница между любыми его листьями не более 1.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Обойти дерево в ширину.</li>
 <li>Если нет правого и нет левого дочернего узла, значит мы нашли лист дерева, отслеживаем максимально удаленный лист от дерева и максимально ближний лист дерева.</li>
 <li>Если разница между самым дальним и самым ближнем листом не более 1, то вернуть True, иначе False.</li>
</ol>

</blockquote></details>

```python
# my code
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_balanced(tree_root):
    from collections import deque
    
    queue = deque()
    queue.append((tree_root, 1))

    min_leaf, max_leaf = float('inf'), float('-inf')
    while queue:
        node, level = queue.popleft()

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

        if not node.left and not node.right:
            min_leaf, max_leaf = min(min_leaf, level), max(max_leaf, level)

    return max_leaf - min_leaf <= 1

```
