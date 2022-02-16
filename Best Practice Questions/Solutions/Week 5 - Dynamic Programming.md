# Week 5 - Dynamic Programming
+ [Jump-Game](#jump-game)
+ [Unique Paths](#unique-paths)
+ [Climbing Stairs](#climbing-stairs)
+ [Decode Ways](#decode-ways)
+ [Word Break](#word-break)
+ [House Robber](#house-robber)
+ [House Robber II](#house-robber-ii)
+ [Longest Increasing Subsequence](#longest-increasing-subsequence)
+ [Coin Change](#coin-change)
+ [Combination Sum IV](#combination-sum-iv)


## Jump-Game
Дан массив чисел. Изначально мы находимся на первом элементе массива, 
каждое число в массиве представляет макс.длину прыжка с этой позиции.
Вернуть True, если мы сможем допрыгать до конца массива, False, если не можем. 

https://leetcode.com/problems/jump-game/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Инициализируем пустую таблицу ДП.</li>
 <li>Добавляем в таблицу ДП базовый случай.</li>
 <li>Итеравтивно заполняем таблицу от базового случая.</li>
 <li>Если во время итерации dp[i] = 0, значит, мы не можем двигаться дальше вернем False.</li>
 <li>Если во время итерации dp[i] >= length - 1, вернем True.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

```python
class Solution:
    def canJump(self, nums):
        length = len(nums)
        dp = [0] * length

        dp[0] = nums[0]

        for i in range(1, length - 1):
            if dp[i - 1] < i:
                return False

            dp[i] = max(i + nums[i], dp[i - 1])

            if dp[i] >= length - 1:
                return True

        return dp[length - 2] >= length - 1


# print(Solution().canJump(nums=[2, 3, 1, 1, 4]))  # True
print(Solution().canJump(nums=[3, 2, 1, 0, 4]))  # False
```


## Unique Paths
Дана сетка m x n. В левом верхнем углу находится робот.
В левом нижнем углу выход. Робот может двигаться либо вправо, либо вниз на каждом шагу.
Вернуть кол-во уникальных путей по которым можно добраться из точки инициалиазации робота 
до точки выхода.

https://leetcode.com/problems/unique-paths/


<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Создаем таблицу ДП, изначально заполненную единицами, где dp[m][n] == кол-во путей до [m][n].</li>
 <li>Итеративно заполняем все ячейки внутри таблицы ДП.</li>
 <li>Возвращаем сумму путей для двух предшествующих выходу ячеек.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]

        return d[m - 1][n - 1]


print(Solution().uniquePaths(m=3, n=7))
```


## Climbing Stairs
Вы поднимаетесь по лестнице. Требуется n шагов, чтобы добраться до вершины. 
Каждый раз вы можете подняться на 1 или 2 ступеньки. 
Сколькими различными способами вы можете подняться на вершину? 

https://leetcode.com/problems/climbing-stairs/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Инициализируем пустую таблицу динамического программирования размером n + 1.</li>
 <li>Заполняем в таблице базовые случаи.</li>
 <li>На основе базовых случаев вычисляем последующие значения в таблице динамического программирования.</li>
 <li>Возвращаем максимальное значение из полученной таблицы динамического программирования.</li>
</ol>
</blockquote></details>


```
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

```python
# Approach 3: Dynamic Programming
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1

        # create dp table
        dp_table = [0 for _ in range(n + 1)]

        # fill db table with base cases
        dp_table[1] = 1
        dp_table[2] = 2

        for i in range(3, n + 1):
            dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

        return max(dp_table)
```


## Decode Ways
Дана закодированная строка, вернуть кол-во вариантов декодирования.

https://leetcode.com/problems/decode-ways/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Создаем таблицу ДП.</li>
 <li>Заполняем базовый случай в таблице ДП.</li>
 <li>Итеративно заполняем таблицу ДП, проверяя на валидность декода одного и двух чисел.</li>
 <li>Вернуть длину таблицы ДП.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```


```python3
class Solution:
    def numDecodings(self, s: str) -> int:
        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2: i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]
```


## Word Break
Дана строка и массив со словами.
Вернуть True, если в строку входят слова из массива.

https://leetcode.com/problems/word-break/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Создаем таблицу ДП.</li>
 <li>Вносим базовый случай в таблицу ДП.</li>
 <li>Перебираем символы и в случае совпадений присваиваем True.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

```python3
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]


print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))
```


## House Robber
Дан массив чисел, представляющий дома на улице, которую хочет ограбить грабитель.
Индекс массива == дом, число в массиве под индексом == кол-во денег в доме.
Какую максимальную прибыль может украсть грабитель, при условии, что нельзя грабить соседние дома.

https://leetcode.com/problems/house-robber/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Инициализируем пустой массив размером с входным массивом домов (создаем таблицу DP).</li>
 <li>Заполняем таблицу DP базовыми случаями.</li>
 <li>Итеративно на основе базовых случаев из таблицы DP заполняем все остальные случаи.</li>
 <li>Возвращаем максимальное значение из таблицы DP.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

```python3
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Special handling for empty case.
        if not nums:
            return 0
        
        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        n = len(nums)

        # Base case initialization.
        maxRobbedAmount[n], maxRobbedAmount[n - 1] = 0, nums[n - 1]

        # DP table calculations.
        for i in range(n - 2, -1, -1):
            # Same as recursive solution.
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])

        return max(maxRobbedAmount)
```


## House Robber II
Дан массив чисел, представляющий дома на улице, которую хочет ограбить грабитель.
Индекс массива == дом, число в массиве под индексом == кол-во денег в доме.
Какую максимальную прибыль может украсть грабитель, при условии, что нельзя грабить соседние дома.
В данной задаче первый и последний дом являются соседними (дома стоят по кругу).

https://leetcode.com/problems/house-robber-ii/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Необходимо сравнить максимальное кол-во денег из двух срезов.</li>
 <li>Сначала вычислим кол-во макс. денег с первого по предпоследний дом.</li>
 <li>Затем вычислим кол-во макс. денег со второго по последний дом.</li>
 <li>Вернем макс. значение полученное из двух срезов входного массива.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
```

```python3
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp

        return t1
```


## Longest Increasing Subsequence
Дан массив чисел.
Найти наибольшую возрастающую последовательность.
Вернуть длину такой последовательности.

https://leetcode.com/problems/longest-increasing-subsequence/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Инициализиурем таблицу ДП размером с входным массивом. Присвоим каждому индексу значение 1.</li>
 <li>Итерируем от i=1 к nums.len - 1. На каждой итерации используем второй цикл от 0 до i - 1 (проверяем все элементы до i).</li>
 <li>Для каждого элемента до i проверяем, что элемент меньше чем nums[i], если это так, то заполняем таблицу ДП.</li>
 <li>Вернем максимальное значение из таблицы ДП.</li>
 <li></li>
</ol>
</blockquote></details>


```
Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```


```python3
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


print(Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
```


## Coin Change
Дан массив чисел представляющий монеты разного номинала, а также число представляющее 
сумму денег. Вернуть кол-во монет для получения данной суммы денег из данных монет.


https://leetcode.com/problems/coin-change/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Иниц. таблицу ДП в которой храним кол-во монет для достижения суммы каждого индекса.</li>
 <li>Итерируем кол-во денег до таргета включительно.</li>
 <li>Итерируем данные нам монеты.</li>
 <li>Проверяем, что монета меньше или равна нужному нам кол-ву денег.</li>
 <li>Если да, то вычисляем сколько монет нужно для данной суммы.</li>
 <li>Вернем кол-во монет для искомого кол-во денег.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
```

```python3
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Values in this array equal the number of coins needed to achieve the cost of the index
        minCoins = [amount + 1] * (amount + 1)
        minCoins[0] = 0

        # Loop through every needed amount
        for i in range(amount + 1):
            # Loop through every coin value
            for coin in coins:
                # Check that the coin is not bigger than the current amount
                if coin <= i:
                    # minCoins[i]: number of coins needed to make amount i
                    # minCoins[i-coin]: number of coins needed to make the amount before adding 
                    #                   the current coin to it (+1 to add the current coin)
                    minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

        # Check if any combination of coins was found to create the amount
        if minCoins[amount] == amount + 1:
            return -1

        # Return the optimal number of coins to create the amount
        return minCoins[amount]


print(Solution().coinChange(coins=[1, 2, 5], amount=11))
```


## Combination Sum IV
Дан root дерева и subroot поддерева, вернуть True, если поддерево входит в дерево.

https://leetcode.com/problems/subtree-of-another-tree/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>.</li>
 <li>.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

```python3
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False

        if self.isSameTree(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return p is q


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(Solution().isSubtree(root, subRoot))
```
