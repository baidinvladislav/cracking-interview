from DS.LinkedList import LinkedList
# 10:59 - 11:27


def is_polindrome(llist):
    node = llist.head
    storage = {}
    while node is not None:
        if node.data in storage.keys():
            storage[node.data] += 1
        else:
            storage[node.data] = 1
        node = node.next

    odds = []
    for i in storage:
        odd = storage[i] % 2
        if odd > 0:
            odds.append(odd)

    if len(odds) > 1:
        return False, f'{llist} is not a palindrome'
    else:
        return True, f'{llist} is a palindrome'


ll = LinkedList(['a', 'b', 'c', 'b', 'a'])
print(is_polindrome(ll))
