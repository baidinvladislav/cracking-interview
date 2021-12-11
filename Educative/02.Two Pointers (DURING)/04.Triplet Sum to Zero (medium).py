"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
"""


def search_triplets(arr):
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        if arr[i - 1] == arr[i]:
            continue

        search_pair(arr, triplets, left=i + 1, target_sum=-arr[i])
    return triplets


def search_pair(arr, triplets, left, target_sum):
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            # skip duplicates
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif current_sum < target_sum:
            left += 1

        elif current_sum > target_sum:
            right -= 1


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
