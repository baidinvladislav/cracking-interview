"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem,
take a look at Kth Smallest Number.
"""


from heapq import *


def find_k_largest_numbers(nums, k):
    heap = []

    for i in range(k):
        heappush(heap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heappop(heap)
            heappush(heap, nums[i])

    return list(heap)


def main():
    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
