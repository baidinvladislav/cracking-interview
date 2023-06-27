# Linked lists
+ [Delete Node](#delete-node)
+ [Does This Linked List Have A Cycle?](#does-this-linked-list-have-a-cycle?)
+ [Reverse A Linked List](#reverse-a-linked-list)
+ [Kth to Last Node in a Singly-Linked List](#kth-to-last-node-in-a-singly-linked-list)


## Delete Node
Дан узел, удалить узел из связного списка.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Удалить не выйдет, т.к. нет указателя на предыдущий относительного удаляемого узел.</li>
 <li>Можно удалить последующий за удаляемым узлом узел, предварительно скопировав значение след. узла в уздаляемый.</li>
 <li>Способ не позволяет удалить последний узел списка.</li>
</ol>

</blockquote></details>


```python
def delete_node(node_to_delete):
    next_node = node_to_delete.next
    if next_node:
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next
    else:
        raise Exception('Can not delete the last node with this technique')

```


## Does This Linked List Have A Cycle?
Дан связной список, определить есть ли в нем цикл.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Используем два указателя, изначльно оба на голове списка.</li>
 <li>На каждой итерации переставляем медленный указатель на один узел, быстрый указатель на два узла.</li>
 <li>Если указатели встретились, то в списке есть цикл, иначе цикла нет.</li>
</ol>

</blockquote></details>


```python
# their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def contains_cycle(first_node):
    slow = fast = first_node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

```


## Reverse A Linked List
Дан узел, удалить узел из связного списка.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Удалить не выйдет, т.к. нет указателя на предыдущий относительного удаляемого узел.</li>
 <li>Можно удалить последующий за удаляемым узлом узел, предварительно скопировав значение след. узла в уздаляемый.</li>
 <li>Способ не позволяет удалить последний узел списка.</li>
</ol>

</blockquote></details>


```python
def delete_node(node_to_delete):
    next_node = node_to_delete.next
    if next_node:
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next
    else:
        raise Exception('Can not delete the last node with this technique')

```


## Does This Linked List Have A Cycle?
Развернуть связной список.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Итерируем список.</li>
 <li>На каждой итерации сохраняем указатель на следующий, для перехода на него в конце итерации.</li>
 <li>Перезаписвываем указатель со следующего на прошедший.</li>
 <li>Проходим к след. узлу.</li>
 <li>Вернуть прошедший.</li>
</ol>

</blockquote></details>


```python
# my solution based on their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse(head_of_list):
    prev = next = None
    cur = head_of_list
    while cur:
        # move pointers
        next = cur.next
        cur.next = prev
        
        # traverse linked list
        prev = cur
        cur = next

    return prev

```


## Kth to Last Node in a Singly-Linked List
Дан связной список и число k, вернуть узел, который находится по счету k с конца.

<details><summary>Решение в два прохода:</summary><blockquote>

<ol>
 <li>За первый проход дойти до конца и узнать длину списка.</li>
 <li>Вторым проходом мы будем знать где нужно остановиться: длина списка - k.</li>
</ol>

</blockquote></details>

<details><summary>Решение в один проход:</summary><blockquote>

<ol>
 <li>Нам необходимо создать "палку" на связном списке, где в начале палки левый указатель на голове, а правый указатель стоит на узле k - 1.</li>
 <li>Сдвинуть эту палку, чтобы правый указатель стоял на конце списка, а левый указатель указатель как раз будет стоять на нужном нам узле.</li>
 <li>Вернуть узел, который находится под левым указателем.</li>
</ol>

</blockquote></details>

```python
# my two passes solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def kth_to_last_node(k, head):
    if k == 0:
        raise

    counter = 0
    head_copy = head
    while head_copy:
        counter += 1
        head_copy = head_copy.next

    if k > counter:
        raise

    for _ in range(counter - k):
        head = head.next

    return head


# their one pass solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def kth_to_last_node(k, head):
    if k == 0:
        raise

    left = right = head

    for _ in range(k - 1):
        right = right.next

    while right.next:
        left = left.next
        right = right.next

    return left

```
