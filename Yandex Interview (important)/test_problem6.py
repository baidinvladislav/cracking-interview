"""
Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]

Т.е. сгруппировать слова по "общим буквам".
"""


from typing import List
from collections import defaultdict


# Time Complexity: O(n * m) (number of words * length of words)
# Space Complexity: O(n)
def solution(arr: List[str]) -> List[List[str]]:
    buffer = defaultdict(list)
    for s in arr:
        buffer[tuple(sorted(s))].append(s)
    return [val for val in buffer.values()]


def test_first():
    nums = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expect = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    assert expect == solution(nums)


def test_second():
    nums = ["xyz", "abc", "qwe", "yxz", "cab", "eqw", "zyx", "bca", "wqe"]
    expect = [["xyz", "yxz", "zyx"], ["abc", "cab", "bca"], ["qwe", "eqw", "wqe"]]

    assert expect == solution(nums)


def test_third():
    nums = ["jkl", "cvb", "lkj", "qaz", "vcb", "kjl"]
    expect = [["jkl", "lkj", "kjl"], ["cvb", "vcb"], ["qaz"]]

    assert expect == solution(nums)
