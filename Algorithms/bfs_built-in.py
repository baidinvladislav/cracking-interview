import collections


def bfs(root):
    deque = collections.deque()

    if root:
        deque.append(root)

    result = []
    while deque:
        size, val = len(deque), 0

        for _ in range(size):
            node = deque.popleft()
            val = node.val

            if node.left:
                deque.append(node.left)

            if node.right:
                deque.append(node.right)

            result.append(val)

    return result
