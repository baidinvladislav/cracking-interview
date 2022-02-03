# Week 3 - Non-Linear Data Structures
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Same Tree](#same-tree)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Construct Binary Tree from Preorder and Inorder Traversal](#construct-binary-tree-from-preorder-and-inorder-traversal)
+ [Binary Tree Maximum Path Sum](#binary-tree-maximum-path-sum)
+ [Clone Graph](#clone-graph)
+ [Course Schedule](#course-schedule)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Serialize and Deserialize Binary Tree](#serialize-and-deserialize-binary-tree)
+ [Top K Frequent Elements](#top-k-frequent-elements)
+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Encode and Decode Strings (LeetCode Premium)](#encode-and-decode-strings-leetCode-premium))



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


## Construct Binary Tree from Preorder and Inorder Traversal
Создать дерево по массивам preorder и inorder.

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Создаем словарь в который заносим данные value:index из массива inorder, так сможем найти корень.</li>
 <li>В preorderIndex отслеживаем элемент для построения корня.</li>
 <li>Реализуем рекурсивную ф-ию, которая принимает диапозон inorder и создает бинарное дерево.</li>
 <li>Если диапозон пуст, то None.</li>
 <li>Инкрементируем preorderIndex.</li>
 <li>Рекурсивно используем левую и правую часть массива inorder, чтобы создать левое и правое поддерево.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

```python3
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            # increment root index
            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        # build a hashmap to store value -> its index relations
        preorder_index = 0
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)
```


## Binary Tree Maximum Path Sum
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


## Clone Graph
Вернуть глубокую копию графа.

https://leetcode.com/problems/clone-graph/

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
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```

```python3
class Solution(object):

    # recursive
    def cloneGraph(self, node):
        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]

    # iterative
    def cloneGraph(self, node):
        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]
```


## Course Schedule
Определить можно ли пройти список курсов, если нужно проходить один курс после друого.

https://leetcode.com/problems/course-schedule/


<details><summary>Итеративное решение:</summary><blockquote>
<ol>
 <li></li>
 <li></li>
 <li></li>
 <li></li>
</ol>
</blockquote></details>


```
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```


```python3
# Approach 2: Postorder DFS (Depth-First Search)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        courseDict = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)

        checked = [False] * numCourses
        path = [False] * numCourses

        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, checked, path):
                return False
        return True


    def isCyclic(self, currCourse, courseDict, checked, path):
        """   """
        # 1). bottom-cases
        if checked[currCourse]:
            # this node has been checked, no cycle would be formed with this node.
            return False
        if path[currCourse]:
            # came across a marked node in the path, cyclic !
            return True

        # 2). postorder DFS on the children nodes
        # mark the node in the path
        path[currCourse] = True

        ret = False
        # postorder DFS, to visit all its children first.
        for child in courseDict[currCourse]:
            ret = self.isCyclic(child, courseDict, checked, path)
            if ret: break

        # 3). after the visits of children, we come back to process the node itself
        # remove the node from the path
        path[currCourse] = False

        # Now that we've visited the nodes in the downstream,
        #   we complete the check of this node.
        checked[currCourse] = True
        return ret
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
