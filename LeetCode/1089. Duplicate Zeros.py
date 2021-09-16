"""
Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_dups = 0
        length_ = len(arr) - 1

        for left in range(length_ + 1):

            if left > length_ - possible_dups:
                break

            if arr[left] == 0:
                if left == length_ - possible_dups:
                    arr[length_] = 0
                    length_ -= 1
                    break
                possible_dups += 1

        last = length_ - possible_dups

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
