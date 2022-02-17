# Week 4 - More Data Structures
+ [Merge k Sorted Lists](#merge-k-sorted-lists)
+ [Insert Interval](#insert-interval)
+ [Longest Consecutive Sequence](#longest-consecutive-sequence)
+ [Implement Trie (Prefix Tree)](#implement-trie-(prefix-tree))
+ [Design Add and Search Words Data Structure](#design-add-and-search-words-data-structure)
+ [Word Search II](#word-search-II)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Lowest Common Ancestor of a Binary Search Tree](#lowest-common-ancestor-of-a-binary-search-tree)
+ [Find Median from Data Stream](#find-median-from-data-stream)
+ [Subtree of Another Tree](#subtree-of-another-tree)
+ [Alien Dictionary](#alien-dictionary)
+ [Graph Valid Tree](#graph-valid-tree)
+ [Meeting Rooms](#meeting-rooms)
+ [Meeting Rooms II](#meeting-rooms-II)
+ [Number of Connected Components in an Undirected Graph](#number-of-connected-components-in-an-undirected-graph)



## Merge k Sorted Lists
Смержить k связных списков из массива в один отсортированный связный список.

https://leetcode.com/problems/merge-k-sorted-lists/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Инициализируем голову и указатель узлом списка со значением 0.</li>
 <li>Добавляем в кучу значения голов и сами головы всех списков из массива.</li>
 <li>Пока куча не пуста получаем из нее значения и узел списков (куча сама сортирует).</li>
 <li>К указателю из 1-го пункта цепляем, то что пришло из кучи.</li>
 <li>Переставляем указатель вперед на один узел.</li>
 <li>Переставляем узел из пункта 3 вперед на один узел.</li>
 <li>Если у узла есть последующие узлы, то добавляем их значения и сами узлы в кучу.</li>
 <li>После цикла вернуть последующий от головы узел, потому что голова равняется значению 0, см 1-ый пункт.</li>
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


## Insert Interval
Дан список не перекрывающий интервалов, отсортированный по началу интервалов.
Нужно вставить в список новый интервал и смержить все пересекающиеся интервалы. 
Вернуть отсортированный массив непересекающихся интервалов. 

https://leetcode.com/problems/insert-interval/


<details><summary>Решение:</summary><blockquote>
<ol>
 <li>В коде будем использовать счетчик, который инкерементируем по ходу работы кода, чтобы обработать все нужные интервалы.</li>
 <li>Добавить в результитрующий массив все интервалы, которые идут до нового интервала.</li>
 <li>Смержить новый интервала со всеми интервалами массива, которые перекрываются с ним.</li>
 <li>Вставить смерженный с другими интервалами новый интервал в результирующий массив.</li>
 <li>Добавить все остальные интервалы в результирующий массив.</li>
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


## Longest Consecutive Sequence
Дан рут дерева, вернуть все уровни этого дерева.

https://leetcode.com/problems/longest-consecutive-sequence/

<details><summary>Брутфорс O(n^3) решение:</summary><blockquote>
<ol>
 <li>Иниц. результирующую переменную как 0.</li>
 <li>Итерируем входной массив и пока текущее число + 1 в массиве увеличиваем временную результирующую переменную.</li>
 <li>Обновляем результирующую перемнную, если она меньше чем временная результирующая переменная.</li>
</ol>
</blockquote></details>

<details><summary>Оптимизированное O(n) решение:</summary><blockquote>
<ol>
 <li>Переводим входной массив во множество.</li>
 <li>Итерируем множество, если во множестве нет числа равное итерируемому - 1, так мы убедимся, что число не входит более длинную последовательность.</li>
 <li>Обновляем результирующую перемнную, если она меньше чем временная результирующая переменная.</li>
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


## Implement Trie (Prefix Tree)
Реализовать структуру данных Trie (префиксное дерево).
Доступные методы: 
* Операция вставки слова -> null
* Поиск слова в структуре -> boolean
* Поиск префикса в добавленном в структуру слове -> boolean

https://leetcode.com/problems/implement-trie-prefix-tree/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Для хранения данных в Trie возьмем словарь.</li>
 <li>Операция вставки слова в структуру заключается в добавлении каждого нового символа слова в значение ключа предыдущего символа: {'c': {'o': {'d': {'e': {'-': 'True'}}}}}.</li>
 <li>Операция поиска заклчюается в проверке вхождения всех символов искомого слова в ключи словаря (узлов Trie), если слово после вставки будет находиться в другом слове, то на этом уровне ставится указатель окончания поддслова.</li>
 <li>Операция поиска префикса похожа на операцию поиска слова, с тем отличием, что отдает истину в случае совпадения не всех символов в слове.</li>
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


## Design Add and Search Words Data Structure
Разработать структуру данных для добавления слов и поиска по добавленным словам.

Методы:
* addWord(word) -> null
* search(word) -> boolean

https://leetcode.com/problems/design-add-and-search-words-data-structure/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>В структуре данных Trie каждый путь представляет список узлов из символов слова.</li>
 <li>Операция добавления слов в структуру заключается в выполнении проверки на наличие вставляемого узал, если он есть, то спускаемся на один шаг пути вниз, если его нет, то добавляем узел в список и спускаемся на один узел ниже.</li>
 <li>Операция поиска при отсутствии символа '.' во входной строке заключается в прохождении всего пути из символов входного слова, если на пути все символы, то слово есть в структуре.</li>
 <li>При наличии символа '.' во входной строке мы должны будем исследовать все возможные варианты на каждом пути.</li>
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


## Word Search II
Дана сетка с буквами и массив слов.
Вернуть слова, которые есть на сетке букв.

https://leetcode.com/problems/word-search-ii/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Заполняем префиксное дерево словами из массива.</li>
 <li>Исследуем сетку из слов в каждом направлении.</li>
 <li>Наполняем массив найденными словами.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

```python3
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]

words = ["oath", "pea", "eat", "rain"]


print(Solution().findWords(board, words))
```


## Kth Smallest Element in a BST
Дан рут бинарного дерева и число k.
Вернуть k-th элемент в порядке возрастания.

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Пройти дерево DFS inorder, чтобы собрать отсортированный по возрастанию массив</li>
 <li>Вернуть k - 1 индекс из массива</li>
</ol>
</blockquote></details>

```
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

```python3
class Solution:
    # my
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, values):
            if not node:
                return

            dfs(node.left, values)
            values.append(node.val)
            dfs(node.right, values)

        values = []
        dfs(root, values)
        return values[k + 1]

    # leetcode one line solution
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]
```


## Lowest Common Ancestor of a Binary Search Tree
Дан рут бинарного деревеа поиска и две вершины.
Вернуть наименьшего общего предка двух вершин p и q.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


<details><summary>Итеративное решение:</summary><blockquote>
<ol>
 <li>Обходим дерево с корня. Используем как DFS так BFS.</li>
 <li>Если обе вершины p и q меньше чем вершина на итерации, то продолжаем поиск в левом поддереве.</li>
 <li>Если обе вершины p и q больше чем вершина на итерации, то продолжаем поиск в правом поддереве.</li>
 <li>Если пункт 2 и пункт 3 неверен, то текущая вершина и есть наименьший общий родитель двух вершин p и q.</li>
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


## Find Median from Data Stream
Реализовать класс для добавления чисел и поиска медианы добавленных чисел.


https://leetcode.com/problems/find-median-from-data-stream/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Создадим две кучи small - для хранения меньшей половины чисел и large для хранения бОльшей половины чисел.</li>
 <li>Балансируем две кучи, соблюдая условие, что длина кучи с большей половины чисел равен или больше на 1 чем размер кучи с меньшей половины чисел.</li>
 <li>Если длина куч равна, то добавляем элемент в кучу с large, предварительно прогнав число через кучу small убедившись, что оно самое бОльшое в куче small.</li>
 <li>Если длина куч не равна то добавляем элемент в кучу с small, предварительно прогнав число через кучу large, получив меньшее число из large.</li>
 <li>Если список чисел нечетен - медианой будет первый элемент кучи с меньшей половиной элементов.</li>
 <li>Если список чисел четен медианой будет первый элемент кучи с меньшей половиной элементов + последний элемент кучи с бОльшими числами // 2.</li>
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


## Subtree of Another Tree
Дан root дерева и subroot поддерева, вернуть True, если поддерево входит в дерево.

https://leetcode.com/problems/subtree-of-another-tree/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Рекурсивно идем по дереву начиная с корня, пока не найдем поддерево в дереве.</li>
 <li>Если наткнулись на корень поддерева, то рекурсивно сравниваем вершины дерева и поддерева.</li>
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


## Alien Dictionary
Дан граф, определить является ли он деревом. 

https://leetcode.com/problems/alien-dictionary/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Слишком сложная задача - вернуться потом.</li>
 <li>.</li>
 <li>.</li>
 <li>.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
```

```python3
from typing import List

from collections import defaultdict, Counter, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)
```


## Graph Valid Tree
Дан граф, определить является ли он деревом. 

https://leetcode.com/problems/graph-valid-tree/submissions/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Если во входном массиве указаны ребра не для всех вершин, то сразу False.</li>
 <li>В задаче используется не удобное представление графа, преоброзуем двумерный массив в список смежности.</li>
 <li>BFS по списку смежности, добавляем посещенные вершины во множество visited.</li>
 <li>Если кол-во просмотретнных вершин ровно кол-ву вершин во множестве просмотренных вершин, то True, иначе False.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

```python3
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        # Create an adjacency list.
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        # We still need a seen set to prevent our code from infinite
        # looping if there *is* cycles (and on the trivial cycles!)
        seen = {0}
        queue = deque([0])

        while queue:
            node = queue.popleft()
            for neighbour in adj_list[node]:
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                queue.append(neighbour)

        return len(seen) == n
```


## Meeting Rooms
Дан список интервалов. 
Определить есть ли в нем пересекающиеся интервалы. 

https://leetcode.com/problems/meeting-rooms/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Отсортировать интервалы по их началу.</li>
 <li>Пройти циклом по входному двумерному массиву интервалов, чтобы найти пересекающиеся интервалы.</li>
 <li>Если найден хоть одна пара пересекающихся интервалов, то вернем False, иначе True.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
```

```python3
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        start, end = 0, 1

        for i in range(1, len(intervals)):
            if intervals[i - 1][end] > intervals[i][start]:
                return False
        return True
```


## Meeting Rooms II
Дан двумерный массив с интервалами встреч, определить сколько комнат потребуется для проведения всех встреч.

https://leetcode.com/problems/meeting-rooms-ii/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Сортируем встречи в массиве по их началу.</li>
 <li>Инициализируем мин-кучу и добавляем в нее конец первой встречи.</li>
 <li>При итериации по встречаем обращаемся в куче и смотрим есть ли у нас свободные комнаты. Комната свободна, если самое маленькое число в куче меньше чем начало встречи на текущей итерации</li>
 <li>Если комната свободна, то извлекаем элемент из кучи и заново добавляем, но уже с окончанием текущей встречи.</li>
 <li>Если свободных комнат нет, то добавляем новую комнату (новый элемент в кучу) представляющий конец текущей на итерации встречи.</li>
 <li>После завершения цикла по двумерному массиву, длина кучи и будет равна кол-ву необходимых комнат для всех встреч.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
```

```python3
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        free_rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(free_rooms, intervals[0][1])

        for interval in intervals[1:]:
            if free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, interval[1])
        return len(free_rooms)


print(Solution().minMeetingRooms(intervals=[[0, 30], [5, 10], [15, 20]]))
```

## Number of Connected Components in an Undirected Graph
Дано число вершин и двумерный массив ребер.
Определить сколько связанных комнонентов в графе.

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li></li>
 <li></li>
 <li></li>
 <li></li>
 <li></li>
 <li></li>
</ol>
</blockquote></details>

```
Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
```

```python3

```
