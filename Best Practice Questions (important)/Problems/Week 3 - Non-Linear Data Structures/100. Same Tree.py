from collections import deque


class Solution(object):
    # iterative
    def isSameTree_it(self, p, q):

        def check(p, q):
            if not p and not q:
                return True

            if not q or not p:
                return False

            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True

    # recursion
    def isSameTree_rc(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree_it(p.right, q.right) and self.isSameTree_it(p.left, q.left)
