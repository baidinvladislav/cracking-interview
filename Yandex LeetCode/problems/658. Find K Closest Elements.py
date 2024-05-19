from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            # Check if the window should move right
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        # Now left is the starting index of the k closest elements
        return arr[left:left + k]


Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3)
