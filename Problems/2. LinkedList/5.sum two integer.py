from DS.LinkedList import LinkedList


def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += int(n1.data)
            n1 = n1.next
        if n2:
            result += int(n2.data)
            n2 = n2.next

        ll.add_last(result % 10)
        carry = result // 10

    if carry:
        ll.add_last(carry)

    return ll


llist1 = LinkedList(['7', '1', '6'])
llist2 = LinkedList(['5', '9', '2'])
sum_lists(llist1, llist2)
