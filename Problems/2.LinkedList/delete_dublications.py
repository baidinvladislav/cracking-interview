class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = {current.data}
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next

    return ll


linked_list = LinkedList()
linked_list.push(100)
linked_list.push(100)
linked_list.push(0)
linked_list.push(9)


def read_ll_values(linked_list):
    current_node = linked_list.head
    while current_node:
        print(current_node.data, end=' ')
        current_node = current_node.next


read_ll_values(linked_list)
print('\n --- after delete duplicates ---')
read_ll_values(remove_dups(linked_list))


# TODO: do this function
def remove_dups_followup(ll):
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return ll.head
