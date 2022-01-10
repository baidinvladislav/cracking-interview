"""
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.
"""


from heapq import *


def find_sum_of_elements(nums, k1, k2):
    minHeap = []
    # insert all numbers to the min heap
    for num in nums:
        heappush(minHeap, num)

    # remove k1 small numbers from the min heap
    for _ in range(k1):
        heappop(minHeap)

    elementSum = 0
    # sum next k2-k1-1 numbers
    for _ in range(k2 - k1 - 1):
        elementSum += heappop(minHeap)

    return elementSum


def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
