"""
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once
you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
"""
import collections


class Solution:
    def sortString(self, s: str) -> str:
        d = sorted([c, n] for c, n in collections.Counter(s).items())
        r = []
        while len(r) < len(s):
            for i in range(len(d)):
                if d[i][1]:
                    r.append(d[i][0])
                    d[i][1] -= 1
            for i in range(len(d)):
                if d[~i][1]:
                    r.append(d[~i][0])
                    d[~i][1] -= 1
        return ''.join(r)


print(Solution().sortString(s="aaaabbbbcccc"))
