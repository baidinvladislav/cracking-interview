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
+ [Alien Dictionary (LeetCode Premium)](#alien-dictionary-(leetCode-premium))
+ [Graph Valid Tree (LeetCode Premium)](#graph-valid-tree-(leetCode-premium))
+ [Meeting Rooms (LeetCode Premium)](#meeting-rooms-(leetCode-premium))
+ [Meeting Rooms II (LeetCode Premium)](#meeting-rooms-II-(leetCode-premium))
+ [Number of Connected Components in an Undirected Graph (LeetCode Premium)](#number-of-connected-components-in-an-undirected-graph-(leetCode-premium))



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
Дан рут бинарного дерева, найти путь с максильной суммой значений узлов.

https://leetcode.com/problems/binary-tree-maximum-path-sum/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Определить какую сумму узлов представляет из себя каждый узел по пути из него.</li>
 <li>Выбрать путь с максимальной суммой.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

```python3
class Solution:
    def maxPathSum(self, root):
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain
            # update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_newpath)
            # for recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum
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


## Invert Binary Tree
Дан рут бинарного дерева, нужно инвертировать (поменять местами) узлы дерева.

https://leetcode.com/problems/invert-binary-tree/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>BFS/DFS по дереву.</li>
 <li>Свапаем левый и правый узел у каждого узла.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
```

```python3
class Solution:

    # recursive
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        root.left = right
        root.right = left

        return root

    # iterative
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque()
        queue.append(root)
        while queue:
            current = queue.popleft()
            temp = current.left
            current.left = current.right
            current.right = temp

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return root
```


## Serialize and Deserialize Binary Tree
Сериализировать и десериализировать бинарное дерево.

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li></li>
 <li></li>
 <li></li>
 <li></li>
</ol>
</blockquote></details>

```
Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
```

```python3
class Codec:

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
```


## Top K Frequent Elements
Дан массив чисел и число k, вернуть k самых частовстречаемых чисел в массиве. 

https://leetcode.com/problems/top-k-frequent-elements/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li></li>
 <li></li>
 <li></li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
```

```python3
# Approach 1: Heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)


# Approach 2: Quickselect (Hoare's selection algorithm)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
                # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]
```


## Non-overlapping Intervals
Дан список интервалов. Вернуть число равное кол-ву интервалов после удаления которых список интервалов будет списком не пересекающихся интервалов. 

https://leetcode.com/problems/non-overlapping-intervals/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li></li>
 <li></li>
 <li></li>
</ol>
</blockquote></details>

```
Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

```python3
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev = float("-inf")
        ans = 0
        for i in intervals:
            if i[0] >= prev:
                prev = i[1]
            else:
                ans += 1
        return ans

```


## Encode and Decode Strings (LeetCode Premium)
Закодировать и раскодировать строки.

https://leetcode.com/problems/encode-and-decode-strings/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li></li>
 <li></li>
 <li></li>
</ol>
</blockquote></details>

```
Example 1:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:
Input: dummy_input = [""]
Output: [""]
```

```python3
class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        x = len(x)
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.len_to_str(x) + x.encode('utf-8') for x in strs)

    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output
```
