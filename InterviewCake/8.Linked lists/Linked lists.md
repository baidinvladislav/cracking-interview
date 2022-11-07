# Linked lists
+ [Delete Node](#delete-node)
+ [Does This Linked List Have A Cycle?](#does-this-linked-list-have-a-cycle?)
+ [Reverse A Linked List](#reverse-a-linked-list)


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


## Reverse A Linked List
