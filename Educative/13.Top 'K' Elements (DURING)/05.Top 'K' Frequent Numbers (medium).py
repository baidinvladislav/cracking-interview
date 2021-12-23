"""
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
"""


from heapq import *


def find_k_frequent_numbers(nums, k):
    # find the frequency of each number
    numFrequencyMap = {}
    for num in nums:
        numFrequencyMap[num] = numFrequencyMap.get(num, 0) + 1

    minHeap = []

    # go through all numbers of the numFrequencyMap and push them in the minHeap, which will have
    # top k frequent numbers. If the heap size is more than k, we remove the smallest(top) number
    for num, frequency in numFrequencyMap.items():
        heappush(minHeap, (frequency, num))
        if len(minHeap) > k:
            heappop(minHeap)

    # create a list of top k numbers
    topNumbers = []
    while minHeap:
        topNumbers.append(heappop(minHeap)[1])

    return topNumbers


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
