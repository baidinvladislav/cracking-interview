"""
Given a string, sort it based on the decreasing frequency of its characters.
"""


from heapq import *


def sort_character_by_frequency(str):
    # find the frequency of each character
    charFrequencyMap = {}
    for char in str:
        charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

    maxHeap = []
    # add all characters to the max heap
    for char, frequency in charFrequencyMap.items():
        heappush(maxHeap, (-frequency, char))

    # build a string, appending the most occurring characters first
    sortedString = []
    while maxHeap:
        frequency, char = heappop(maxHeap)
        for _ in range(-frequency):
            sortedString.append(char)

    return ''.join(sortedString)


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
