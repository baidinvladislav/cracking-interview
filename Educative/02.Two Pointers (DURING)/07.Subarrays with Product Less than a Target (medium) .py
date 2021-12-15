"""
Given an array with positive numbers and a positive target number,
find all of its contiguous subarrays whose product is less than the target number.
"""


from collections import deque


# Time Complexity: O(N**3)
# Space Complexity: O(N)
def find_subarrays(arr, target):
    left, product, result = 0, 1, []

    for right in range(len(arr)):
        product *= arr[right]

        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1

        temp_list = deque()
        for i in range(right, left - 1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))

    return result


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()
