"""
Write a algorithm that removes node from middle (not beginning or not end)
"""
from DS.LinkedList import LinkedList


def remove_node(node):
    node.previous.next = node.next
    node.next.previous = node.previous


list_llists = [
    LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    LinkedList(['Russia', 'UK', 'USA', 'Canada', 'Germany']),
    LinkedList(['audi', 'bwm', 'lada', 'mercedes', 'range rover'])
]

for llist in list_llists:
    node = llist.head.next.next.next
    print(llist)
    remove_node(node)
    print('-----after removing-----')
    print(f'{llist}\n')
