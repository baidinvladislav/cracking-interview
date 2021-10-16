"""
Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        possible_dups = 0

        # counting possible duplicates
        for i in range(n):
            if arr[i] == 0:
                possible_dups += 1

        # iterate to array from end to start
        for i in range(n - 1, -1, -1):
            # ignore those elements for which there is no place in the array
            if i + possible_dups < n:
                # if there is place in array we copy the element to index
                # which will be shifted zeroes duplicate
                arr[i + possible_dups] = arr[i]

            # if we faced zeroes we decrease numbers of zeroes
            if arr[i] == 0:
                possible_dups -= 1

                # if there is place in array we copy the zero duplicates
                # to index which will be shifted zeroes duplicate
                if i + possible_dups < n:
                    arr[i + possible_dups] = 0

        print(arr)


Solution().duplicateZeros(arr=[1, 0, 2, 3, 0, 4, 5, 0])
