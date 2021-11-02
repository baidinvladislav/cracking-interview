import collections


class Solution:
    def bfs_lee215(self, root, k):
        if not root:
            return False

        queue, visited = [root], set()
        for node in queue:
            if k - node.val in visited:
                return True

            visited.add(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False


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
