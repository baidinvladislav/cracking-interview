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
Разработать структуру данных для добавления слов и поиска по добавленным словам.

Методы:
* addWord(word) -> null
* search(word) -> boolean

https://leetcode.com/problems/design-add-and-search-words-data-structure/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>.</li>
 <li>.</li>
 <li>.</li>
 <li>.</li>
</ol>

</blockquote></details>

```
Example 1:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

```python3
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any letter.
        """
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node

        return search_in_node(word, self.trie)


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.search("pad")
wordDictionary.search("bad")
wordDictionary.search(".ad")
wordDictionary.search("b..")

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
Дан рут бинарного деревеа поиска и две вершины.
Вернуть наименьшего общего предка двух вершин p и q.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


<details><summary>Итеративное решение:</summary><blockquote>
<ol>
 <li>.</li>
 <li>.</li>
 <li>.</li>
 <li>.</li>
 <li></li>
</ol>
</blockquote></details>


```
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
```


```python3
class Solution:
    # recursive
    def lowestCommonAncestor(self, root, p, q):
        # If both p and q are greater than parent
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # If both p and q are lesser than parent
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # We have found the split point, i.e. the LCA node.
        else:
            return root

    # iterative
    def lowestCommonAncestor(self, root, p, q):
        node = root
        while node:
            # Value of current node or parent node.
            parent_val = node.val

            if p.val > parent_val and q.val > parent_val:
                # If both p and q are greater than parent
                node = node.right
            elif p.val < parent_val and q.val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node
```


## Coin Change
Реализовать класс для добавления чисел и поиска медианы добавленных чисел.


https://leetcode.com/problems/find-median-from-data-stream/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>.</li>
 <li>.</li>
 <li>.</li>
 <li>.</li>
 <li>.</li>
 <li>.</li>
</ol>
</blockquote></details>

```
Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

```python3
from heapq import *


# two balanced heaps
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
medianFinder.findMedian()
medianFinder.addNum(3)
medianFinder.findMedian()

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
