"""
Write a function that removes duplicates from linked list
"""
from DS.LinkedList import LinkedList


def remove_duplicates(linked_list):
    storage = {}
    for i, node in enumerate(linked_list, start=1):
        if node.data in storage.values():
            node.previous.next = node.next
            node.next.previous = node.previous
        else:
            storage[f'node_{i}'] = node.data
    return linked_list


if __name__ == '__main__':
    test_cases = [
        [1, 2, 2, 3, 1, 4],
        ['q', 'w', 'e', 'q', 'w', 't'],
        ['python', 'java', 'c++', 'python', 'c#', 'java', 'javascript', 'scala']
    ]

    for llist in test_cases:
        print(LinkedList(llist))
        print('after removing duplicates')
        print(f'{remove_duplicates(LinkedList(llist))}\n')
