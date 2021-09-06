"""
Write an algorithm that finds element from the end of linked list by index
"""
import unittest

from DS.LinkedList import LinkedList, Node


def find_from_end(lin_list, index):
    list_len = 0
    for i, el in enumerate(lin_list, start=1):
        list_len = i

    index_el = list_len - index
    for i, el in enumerate(lin_list, start=1):
        if i == index_el:
            return el


class Test(unittest.TestCase):
    data = [
        (LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2, 7),
        (LinkedList(['Russia', 'UK', 'USA', 'Canada', 'Germany']), 1, 'Canada'),
        (LinkedList(['qw', 'rt', 'ty', 'yu', 'xz', 'bn', 'mm', 'cc', 'pp']), 0, 'pp'),
    ]

    def test_is_cyclic_shift(self):
        for test_case in self.data:
            result = find_from_end(test_case[0], test_case[1])
            self.assertEqual(result.data, Node(test_case[2]).data)


if __name__ == "__main__":
    unittest.main()
