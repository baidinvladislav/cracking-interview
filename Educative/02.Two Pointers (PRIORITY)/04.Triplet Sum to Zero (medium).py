"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
"""


def search_triplets(arr):
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        prev_cur_elem = arr[i - 1]
        cur_elem = arr[i]

        if i > 0 and prev_cur_elem == cur_elem:  # skip same element to avoid duplicate triplets
            continue

        target_sum = -arr[i]
        search_pair(arr=arr, target_sum=target_sum, left=i + 1, triplets=triplets)

    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets

        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum

        else:
            right -= 1  # we need a pair with a smaller sum


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
