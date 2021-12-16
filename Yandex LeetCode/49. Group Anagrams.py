"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        1. Sort the word alphabetically.
        2. Insert sorted word into tuple data structure.
        3. Insert the tuple in a dict data structure.
        4. Insert a word to value array.
        """
        char_map = collections.defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            char_map[key].append(word)
        return char_map.values()


print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
