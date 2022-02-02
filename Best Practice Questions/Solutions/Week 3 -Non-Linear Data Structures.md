# Week 3 - Non-Linear Data Structures
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Same Tree](#same-tree)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Construct Binary Tree from Preorder and Inorder Traversal](#construct-binary-tree-from-preorder-and-inorder-traversal)
+ 
+ [Find Minimum in Rotated Sorted Array](#find-minimum-in-rotated-sorted-array)
+ [Number of Islands](#number-of-islands)
+ [Reverse Linked List](#reverse-linked-list)
+ [Pacific Atlantic Water Flow](#pacific-atlantic-water-flow)
+ [Longest Repeating Character Replacement](#longest-repeating-character-replacements)
+ [Palindromic Substrings](#palindromic-substrings)


## Validate Binary Search Tree
Дан рут бинарного дерева. Определить является ли дерево бинарным деровом поиска.
Бинарное дерево поиска - это дерево в котором:
* в левом поддереве узла все значения меньше чем значения узла.
* в правом поддереве узла все значения больше чем значения узла.
* и левое, и правое поддеревья являются бинарными деревьями поиска.

https://leetcode.com/problems/validate-binary-search-tree/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Сравниваем значение узла с его верхним и нижним пределами, если они доступны. Затем тот же шаг рекурсивно повторяется для левого и правого поддеревьев.</li>
 <li>Также работаем с итеративным решением.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

```python
class Solution:
    # recursive
    def isValidBST_rec(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True

            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return validate(node.right, node.val, high) and validate(node.left, low, node.val)

        return validate(root)

    # iterative
    def isValidBST_it(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = deque([(root, float('-inf'), float('inf'))])
        while queue:
            root, lower, upper = queue.popleft()

            if not root:
                continue

            val = root.val
            if val <= lower or val >= upper:
                return False

            queue.append((root.right, val, upper))
            queue.append((root.left, lower, val))
        return True

```


## Same Tree
Даны два рута, определить что это одиинаковые деревья.

https://leetcode.com/problems/same-tree/


<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Создаем проверки.</li>
 <li>Рекурсивно или итеративно прогоняем все узлы через проверки.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

```python
class Solution(object):
    # iterative
    def isSameTree_it(self, p, q):

        def check(p, q):
            if not p and not q:
                return True

            if not q or not p:
                return False

            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True

    # recursion
    def isSameTree_rc(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree_it(p.right, q.right) and self.isSameTree_it(p.left, q.left)
```

## Binary Tree Level Order Traversal
Дан рут дерева, вернуть все уровни этого дерева.

https://leetcode.com/problems/binary-tree-level-order-traversal/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Выходной список здесь называется уровнями.</li>
 <li>Текущий уровень — это просто длина этого списка len(levels).</li>
 <li>Сравните номер текущего уровня len(levels) с уровнем уровня узла.</li>
 <li>Если вы все еще находитесь на предыдущем уровне - добавьте новый, добавив новый список в уровни.</li>
 <li>Добавьте значение узла к последнему списку уровней.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
```

```python3 
class Solution(object):
    # bfs
    def levelOrder_bfs(self, root):
        if not root:
            return []

        values = []
        queue = deque()
        queue.append(root)
        while queue:
            cur_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cur_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            values.append(cur_level)

        return values

    # dfs
    def levelOrder_dfs(self, root):
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels
```


## Maximum Depth of Binary Tree
Дан рут, найти максимальную глубину дерева. 

https://leetcode.com/problems/maximum-depth-of-binary-tree/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Подсчитать уровни либо DFS, либо BFS.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
```


```python3
class Solution(object):
    # bfs
    def maxDepth_bfs(self, root):
        level = 0
        if not root:
            return level

        queue = deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            level += 1
        return level

    # dfs
    def maxDepth_dfs(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth_dfs(root.left)
            right_height = self.maxDepth_dfs(root.right)
            return max(left_height, right_height) + 1
```

## Linked List Cycle
Дан связной список. Определить содержит ли список цикл.

https://leetcode.com/problems/linked-list-cycle/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Ставим медленный указатель и быстрый указатель в начало списка.</li>
 <li>Идем циклом по списку медленным указателем по узлу за шаг, а быстрым по два узла за шаг.</li>
 <li>Доходим быстрым указателем до конца, если быстрый указатель догнал медленный, значит в списке есть цикл, если прошли весь список, то цикла нет.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed)

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

```python3
def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False
```

## Find Minimum in Rotated Sorted Array
Найти минимальное число в развернутом отсортированном массиве.

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Используем модифицированную версию бинарного поиска.</li>
 <li>Для решения необзодимо найти точку перегиба.</li>
 <li>Находим центральный элемент массива.</li>
 <li>Если центральный элемент массива больше чем первый элемент массива, то значит точка перегиба находится справа от центрального элемента.</li>
 <li>Если центральный элемент массива меньше чем первый элемент массива, то значит точка перегиба находится слева от центрального элемента.</li>
 <li>Прекращаем поиск, когда находим точку перегиба, для этого должно выполниться одно из двух условий: 1) центральный элемент больше чем последующий за ним элемент nums[mid] > nums[mid + 1] 2) центральный элемент меньше чем элемиент перед ним nums[mid - 1] > nums[mid].</li>
</ol>
</blockquote></details>

```
Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

```python3
def findMin(self, nums):
    if len(nums) == 1:
        return nums[0]

    left = 0
    right = len(nums) - 1

    if nums[right] > nums[0]:
        return nums[0]

    while right >= left:
        mid = left + (right - left) / 2
        
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestFindMin(unittest.TestCase):
    def test_first(self):
        self.assertEqual(1, Solution().findMin(nums=[3, 4, 5, 1, 2]))

    def test_second(self):
        self.assertEqual(0, Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2]))

    def test_third(self):
        self.assertEqual(11, Solution().findMin(nums=[11, 13, 15, 17]))
```
</blockquote></details>


## Number of Islands
Дана сетка размером MxN. В сетке находятся находятся значение '0' и '1'. Где '0' - это вода и '1' - это суша.
Вернуть кол-во островов на сетке.

https://leetcode.com/problems/number-of-islands/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Рассмотрим сетку как неориентированный граф, у которого ребра есть у смежных соседних вершин по горизонтали и вертикали со значением '1'.</li>
 <li>Линейно проходим по сетке, если в вершине значение '1', то ночинаем от этой вершины поиск в ширину.</li>
 <li>Добавляем такую вершину в очередь и устанавливаем для нее значение '0', помечая вершину как посещенную..</li>
 <li>Итеративно ищем соседей этой вершины у которых тоже значение '1', меняем на '0'.</li>
 <li>Повторяем пока в очереди есть вершины.</li>
 <li>Кол-во раз когда запускался поиск в ширину и будет равен кол-ву островое на сетке.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

```python3
from collections import deque


def numIslands(self, grid):
    rows = len(grid)
    columns = len(grid[0])
    nums_islands = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == '1':
                nums_islands += 1
                grid[i][j] = '0'
                neighbors = deque()
                neighbors.append([i, j])
                while neighbors:
                    neighbor = neighbors.popleft()
                    row, column = neighbor[0], neighbor[1]
                    if row - 1 >= 0 and grid[row - 1][column] == '1':
                        neighbors.append([row - 1, column])
                        grid[row - 1][column] = '0'
                    if row + 1 < rows and grid[row + 1][column] == '1':
                        neighbors.append([row + 1, column])
                        grid[row + 1][column] = '0'
                    if column - 1 >= 0 and grid[row][column - 1] == '1':
                        neighbors.append([row, column - 1])
                        grid[row][column - 1] = '0'
                    if column + 1 < columns and grid[row][column + 1] == '1':
                        neighbors.append([row, column + 1])
                        grid[row][column + 1] = '0'
    return nums_islands
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestNumIslands(unittest.TestCase):
    def test_first(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        self.assertEqual(1, Solution().numIslands(grid))

    def test_second(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        self.assertEqual(3, Solution().numIslands(grid))
```

</blockquote></details>


## Reverse Linked List
Развернуть связной список.

https://leetcode.com/problems/reverse-linked-list/


<details><summary>Итеративное решение:</summary><blockquote>
<ol>
 <li>Итерируем список, меняя у текущего узла указатель на следующий узел на его предыдущий узел.</li>
 <li>Поскольку у узлов нет ссылки на их предыдущий узел, то заранее сохраним предыдущий узел в памяти.</li>
 <li>Также сохраняем следующий узел до того как мы изменим ссылки у текущего узла.</li>
 <li>Возвращаем новый связной список.</li>
</ol>
</blockquote></details>


<details><summary>Рекурсивное решение:</summary><blockquote>
<ol>
 <li>Рекурсивно посещаем каждый элемент в связанном списке, пока не достигнем последнего.</li>
 <li>Этот последний элемент станет новым головой перевернутого связанного списка.</li>
 <li>На пути возврата каждый узел добавляется в конец частично перевернутого списка.</li>
</ol>
</blockquote></details>


```
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
```


```python3
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


class Solution:
    # Iterative Time: O(n), Space:O(1)
    def reverseList_iter(self, head):
        previous = None
        current = head
        while current:
            temp_next = current.next
            current.next = previous
            previous = current
            current = temp_next
        return previous

    # Recursive Time: O(n), Space:O(n)
    def reverseList_rec(self, head):
        if not head or not head.next:
            return head

        p = self.reverseList_rec(head.next)
        head.next.next = head
        head.next = None
        return p
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestReverseLinkedList(unittest.TestCase):
    def test_first(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        excepted_head = Node(5)
        excepted_head.next = Node(4)
        excepted_head.next.next = Node(3)
        excepted_head.next.next.next = Node(2)
        excepted_head.next.next.next.next = Node(1)
        self.assertEqual(excepted_head, Solution().reverseList_rec(head=head))
        self.assertEqual(excepted_head, Solution().reverseList_iter(head=head))

    def test_second(self):
        head = Node(1)
        head.next = Node(2)

        excepted_head = Node(2)
        excepted_head.next = Node(1)
        self.assertIsNone(Solution().reverseList_rec(head=head))
        self.assertEqual(excepted_head, Solution().reverseList_iter(head=head))
```

</blockquote></details>


## Pacific Atlantic Water Flow
Дана матрица MxN, где в значения в ячейках - уровень воды.
Матрица слева и сверху омывается Тихим океаном.
Матрица справа и снизу омывается Атлантическим океаном.
Вода из ячеек может перетекать в другие ячейки, если уровень соседних ячеек меньше или равен уровню воды текущей ячейки.

Вернуть координаты ячеек вода из которых может попасть сразу в оба океана.

https://leetcode.com/problems/pacific-atlantic-water-flow/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>BFS/DFS от клеток, которые граничат с Тихим океаном.</li>
 <li>BFS/DFS от клеток, которые граничат с Атлантическим океаном.</li>
 <li>Найти их пересечения.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
```

```python3
from collections import deque


def pacificAtlantic(self, heights):
    # Check if input is empty
    if not heights or not heights[0]:
        return []

    num_rows, num_cols = len(heights), len(heights[0])

    # Setup each queue with cells adjacent to their respective ocean
    pacific_queue = deque()
    atlantic_queue = deque()

    for i in range(num_rows):
        pacific_queue.append((i, 0))
        atlantic_queue.append((i, num_cols - 1))
    for i in range(num_cols):
        pacific_queue.append((0, i))
        atlantic_queue.append((num_rows - 1, i))

    def bfs(queue):
        reachable = set()
        while queue:
            (row, col) = queue.popleft()
            # This cell is reachable, so mark it
            reachable.add((row, col))
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # Check all 4 directions
                new_row, new_col = row + x, col + y
                # Check if the new cell is within bounds
                if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                    continue
                # Check that the new cell hasn't already been visited
                if (new_row, new_col) in reachable:
                    continue
                # Check that the new cell has a higher or equal height,
                # So that water can flow from the new cell to the old cell
                if heights[new_row][new_col] < heights[row][col]:
                    continue
                # If we've gotten this far, that means the new cell is reachable
                queue.append((new_row, new_col))
        return reachable

    # Perform a BFS for each ocean to find all cells accessible by each ocean
    pacific_reachable = bfs(pacific_queue)
    atlantic_reachable = bfs(atlantic_queue)

    # Find all cells that can reach both oceans, and convert to list
    return list(pacific_reachable.intersection(atlantic_reachable))
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestPacificAtlantic(unittest.TestCase):
    def test_first(self):
        output = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        self.assertEqual(output, Solution().pacificAtlantic(
            heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))

    def test_second(self):
        output = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.assertEqual(output, Solution().pacificAtlantic(heights=[[2, 1], [1, 2]]))
```

</blockquote></details>


## Longest Repeating Character Replacement
Дана строка и число кол-во допустимых замен символов в строке.
Вернуть длину строки с одинаковыми символами после перестановки k допустимых раз.

https://leetcode.com/problems/longest-repeating-character-replacement/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Итерируем строку, добавляя символ и его частоту в строке.</li>
 <li>Проверяем условие, что если кол-во допустимых перестановок меньше чем разница длины окна и повторений символа в окне.</li>
 <li>То сжимаем окно, вычитая частоту символа из словаря.</li>
 <li>Обновляем длину окна, если она становится больше.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

```python3
# Time Complexity: O(N)
# Space Complexity: O(1) - because there are only 26 symbols in alphabet
def characterReplacement(s: str, k: int) -> int:
    dict_freq = {}
    window_start = max_length = max_repeat = 0

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in dict_freq:
            dict_freq[right_char] = 0
        dict_freq[right_char] += 1
        max_repeat = max(max_repeat, dict_freq[right_char])

        if k < window_end - window_start + 1 - max_repeat:
            dict_freq[s[window_start]] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestCharacterReplacement(unittest.TestCase):
    def test_first(self):
        self.assertEqual(4, Solution().characterReplacement(s="ABAB", k=2))

    def test_second(self):
        self.assertEqual(4, Solution().characterReplacement(s="AABABBA", k=1))
```
</blockquote></details>


## Palindromic Substrings
Дана палиндром-строка, определить сколько подстрок в строке являются полиндромами. 

https://leetcode.com/problems/palindromic-substrings/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Для решения задчи нужно понимать, что есть такое палиндром.</li>
 <li>Палиндромом могут счиаться строки, которые состоят из 1) одной буквы 2) одинаковых букв 3) из палиндрома и двух одинаковых букв по краям палиндрома</li>
 <li>Для хранения информации о подстроках строим матрицу в которой по вертикали и горизонтали индексы символов, а координаты начало и конец подстроки.</li>
 <li>Если подстрока является палиндромом, то помечаем по ее координатам в матрице строку, как 1, те что не являются палиндромами остаются 0.</li>
 <li>Помечаем одиночные палидромы. Это подстроки из одной буквы.</li>
 <li>Помечаем все подстроки из двух одинаковых символов.</li>
 <li>Помечаем остальные палиндромы. Если подстрока палидрома палиндром и окружена с обоих сторон одинаковыми буквами, то подстрока - палиндром.</li>
 <li>Вернуть счеткик палиндромов.</li>
</ol>
</blockquote></details>

```
Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

```python3
def countSubstrings(self, s):
    n = len(s)
    res = 0

    # create a matrix to store info about the substring
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # set single characters as palindromes
    idx = 0
    while idx < n:
        dp[idx][idx] = 1
        idx += 1
        res += 1

    for col in range(1, len(s)):
        for row in range(col):

            # every two chars are palindromes as well
            if row == col - 1 and s[col] == s[row]:
                dp[row][col] = 1
                res += 1

            # to determine if substring is a palindrome you should know
            # a) if the inner substring is the palindrome and
            # b) if the outer characters match
            elif dp[row + 1][col - 1] == 1 and s[col] == s[row]:
                dp[row][col] = 1
                res += 1
    return res
```

<details><summary>Test cases</summary><blockquote>

```python3
import unittest


class TestPalindromicSubstrings(unittest.TestCase):
    def test_first(self):
        self.assertEqual(3, Solution().countSubstrings(s="abc"))

    def test_second(self):
        self.assertEqual(6, Solution().countSubstrings(s="aaa"))
```
</blockquote></details>
