import collections


def bfs(root):
    deque = collections.deque()

    if root:
        deque.append(root)

    result = []
    while deque:
        size = len(deque)

        for _ in range(size):
            node = deque.popleft()

            if node.left:
                deque.append(node.left)

            if node.right:
                deque.append(node.right)

            result.append(node.val)

    return result
