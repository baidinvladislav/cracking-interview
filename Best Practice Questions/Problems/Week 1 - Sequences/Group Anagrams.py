import unittest
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        if not strs:
            return [[""]]

        hash_map = defaultdict(list)
        for word in strs:
            hash_map[tuple(sorted(word))].append(word)
        return list(hash_map.values())


class TestMaxProduct(unittest.TestCase):
    def test_first(self):
        output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(output, Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))

    def test_second(self):
        self.assertEqual([[""]], Solution().groupAnagrams(strs=[""]))

    def test_third(self):
        self.assertEqual([["a"]], Solution().groupAnagrams(strs=["a"]))


if __name__ == "__main__":
    unittest.main()
