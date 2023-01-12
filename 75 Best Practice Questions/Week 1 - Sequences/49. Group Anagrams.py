import unittest
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        hash_map = defaultdict(list)
        for word in strs:
            sorted_word = tuple(sorted(word))
            hash_map[sorted_word].append(word)
        return hash_map.values()


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
