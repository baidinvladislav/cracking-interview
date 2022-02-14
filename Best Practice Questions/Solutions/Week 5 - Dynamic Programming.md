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
Смержить k связных списков из массива в один отсортированный связный список.

https://leetcode.com/problems/merge-k-sorted-lists/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>.</li>
 <li>.</li>
 <li>.</li>
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


## Unique Paths
Дан список не перекрывающий интервалов, отсортированный по началу интервалов.
Нужно вставить в список новый интервал и смержить все пересекающиеся интервалы. 
Вернуть отсортированный массив непересекающихся интервалов. 

https://leetcode.com/problems/insert-interval/


<details><summary>Решение:</summary><blockquote>
<ol>
 <li>.</li>
 <li>.</li>
 <li>.</li>
 <li>.</li>
 <li>.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

```python
class Solution:
    def insert(self, intervals, newInterval):
        start, end = 0, 1
        counter = 0
        merged_arr = []

        # add to result array all intervals that come before new interval
        while counter < len(intervals) and intervals[counter][end] < newInterval[start]:
            merged_arr.append(intervals[counter])
            counter += 1

        # merge overlapping intervals with new interval
        while counter < len(intervals) and newInterval[end] >= intervals[counter][start]:
            newInterval[start] = min(intervals[counter][start], newInterval[start])
            newInterval[end] = max(intervals[counter][end], newInterval[end])
            counter += 1

        # insert merged new interval with all overlapping intervals
        merged_arr.append(newInterval)

        # insert other intervals into result array
        while counter < len(intervals):
            merged_arr.append(intervals[counter])
            counter += 1

        return merged_arr
```


## Climbing Stairs
Дан рут дерева, вернуть все уровни этого дерева.

https://leetcode.com/problems/longest-consecutive-sequence/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li></li>
 <li></li>
 <li></li>
</ol>
</blockquote></details>


```
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

```python
class Solution:
    # brute-force O(n^3)
    def longestConsecutive(self, nums):
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

    # optimized O(n)
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
```


## Decode Ways
Реализовать структуру данных Trie (префиксное дерево).
Доступные методы: 
* Операция вставки слова -> null
* Поиск слова в структуре -> boolean
* Поиск префикса в добавленном в структуру слове -> boolean

https://leetcode.com/problems/implement-trie-prefix-tree/

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
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```


```python3
class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t["-"] = True

    def search(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return "-" in t

    def startsWith(self, prefix):
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True


trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")
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
