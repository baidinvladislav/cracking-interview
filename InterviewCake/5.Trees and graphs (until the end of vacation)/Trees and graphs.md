# Trees and graphs
+ [Balanced Binary Tree](#balanced-binary-tree)
+ [Binary Search Tree Checker](#binary-search-tree-checker)
+ [2nd Largest Item in a Binary Search Tree](#2nd-largest-item-in-a-binary-search-tree)


## Balanced Binary Tree
Определить что разница между двумя любыми листами не более 1.

<details><summary>Решение:</summary><blockquote>
<ol>
 <li>Обойти в ширину по уровням, отслеживая мин. и макс. лист от корня.</li>
 <li>Вычислить разницу между мин. и макс. листами от корня.</li>
</ol>

</blockquote></details>

```python
from collections import deque


# my own 10.10.22
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_balanced(tree_root):
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
            max_leaf = max(max_leaf, level)
            min_leaf = min(min_leaf, level)

    return max_leaf - min_leaf <= 1

```


## Binary Search Tree Checker


## 2nd Largest Item in a Binary Search Tree
