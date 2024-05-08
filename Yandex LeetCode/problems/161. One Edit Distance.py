class Solution:
    def get_diff_idx(self, stack_s: list, stack_t: list) -> int:
        for i in range(min(len(stack_s), len(stack_t))):
            if stack_s[i] != stack_t[i]:
                return i

        return min(len(stack_s), len(stack_t))

    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t or len(t) - len(s) > 1:
            return False

        stack_s = list(s)
        stack_t = list(t)

        diff_idx = self.get_diff_idx(stack_s, stack_t)

        if len(stack_s) == len(stack_t):
            stack_s[diff_idx] = stack_t[diff_idx]
            return stack_s == stack_t
        elif len(stack_s) > len(stack_t):
            del stack_s[diff_idx]
            return stack_s == stack_t
        elif len(stack_s) < len(stack_t):
            stack_s.insert(diff_idx, stack_t[diff_idx])
            return stack_s == stack_t
