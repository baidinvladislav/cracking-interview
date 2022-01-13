"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


import collections


class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for word in strs:
            ans[tuple(sorted(word))].append(word)
        return ans.values()


print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
