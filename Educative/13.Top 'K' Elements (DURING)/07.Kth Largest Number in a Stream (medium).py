"""
Design a class to efficiently find the Kth the largest element in a stream of numbers.

The class should have the following two things:

    1.The constructor of the class should accept an integer array containing initial numbers
    from the stream and an integer ‘K’.

    2.The class should expose a function add(int num) which will store the given number
    and return the Kth the largest number.
"""


from heapq import *


class KthLargestNumberInStream:
    minHeap = []

    def __init__(self, nums, k):
        self.k = k
        # add the numbers in the min heap
        for num in nums:
            self.add(num)

    def add(self, num):
        # add the new number in the min heap
        heappush(self.minHeap, num)

        # if heap has more than 'k' numbers, remove one number
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

        # return the 'Kth the largest number
        return self.minHeap[0]


def main():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
