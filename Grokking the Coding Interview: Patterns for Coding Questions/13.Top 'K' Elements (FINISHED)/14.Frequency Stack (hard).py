"""
Design a class that simulates a Stack data structure, implementing the following two operations:

    1.push(int num): Pushes the number ‘num’ on the stack.

    2.pop(): Returns the most frequent number in the stack. If there is a tie,
    return the number which was pushed later.
"""


from heapq import *


class Element:

    def __init__(self, number, frequency, sequenceNumber):
        self.number = number
        self.frequency = frequency
        self.sequenceNumber = sequenceNumber

    def __lt__(self, other):
        # higher frequency wins
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        # if both elements have same frequency, return the element that was pushed later
        return self.sequenceNumber > other.sequenceNumber


class FrequencyStack:
    sequenceNumber = 0
    maxHeap = []
    frequencyMap = {}

    def push(self, num):
        self.frequencyMap[num] = self.frequencyMap.get(num, 0) + 1
        heappush(self.maxHeap, Element(
            num, self.frequencyMap[num], self.sequenceNumber))
        self.sequenceNumber += 1

    def pop(self):
        num = heappop(self.maxHeap).number
        # decrement the frequency or remove if this is the last number
        if self.frequencyMap[num] > 1:
            self.frequencyMap[num] -= 1
        else:
            del self.frequencyMap[num]

        return num


def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


main()
