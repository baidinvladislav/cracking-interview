from collections import OrderedDict


# Approach 1: Ordered dictionary
# Time complexity: O(1)
# Space complexity: O(capacity)
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = OrderedDict()

    def get(self, key):
        if key in self.storage:
            self.storage.move_to_end(key)
            return self.storage[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.storage:
            self.storage.move_to_end(key)
        self.storage[key] = value

        if len(self.storage) > self.capacity:
            self.storage.popitem(last=False)


lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
lRUCache.get(1)  # return 1
lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)  # returns -1 (not found)
lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)  # return -1 (not found)
lRUCache.get(3)  # return 3
lRUCache.get(4)  # return 4


# Approach 2: Hashmap + DoubleLinkedList
# Time complexity: O(1)
# Space complexity: O(capacity)
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self._remove_node(node)
            self._add_node(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.map:
            self._remove_node(self.map[key])

        node = Node(key, value)
        self._add_node(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            deleted_node = self.head.next
            self._remove_node(deleted_node)
            del self.map[deleted_node.key]

    def _add_node(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def _remove_node(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node


lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
lRUCache.get(1)  # return 1
lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)  # returns -1 (not found)                   123
lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)  # return -1 (not found)
lRUCache.get(3)  # return 3
lRUCache.get(4)  # return 4
