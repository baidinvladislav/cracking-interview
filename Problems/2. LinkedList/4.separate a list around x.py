"""
Write an algorithm that breaks linked list around `X` value
"""


from DS.LinkedList import LinkedList, Node


def partition(node, x):
    before_x = LinkedList()
    before_x_end = None

    after_x = LinkedList()
    after_x_end = None

    while node is not None:
        if int(node.data) < x:
            if before_x.head is None:
                before_x.head = Node(node.data)
                before_x_end = before_x.head
            else:
                before_x_end.next = Node(node.data)
                before_x_end = before_x_end.next
        else:
            if after_x.head is None:
                after_x.head = Node(node.data)
                after_x_end = after_x.head
            else:
                after_x_end.next = Node(node.data)
                after_x_end = after_x_end.next
        node = node.next

    before_x_end.next = after_x.head
    new_llist = before_x
    return new_llist


llist = LinkedList(['3', '5', '8', '5', '10', '2', '1'])
node = llist.head
print(partition(node, 5))
