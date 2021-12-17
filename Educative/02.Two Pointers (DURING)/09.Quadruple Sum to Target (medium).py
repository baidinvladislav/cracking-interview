"""
Given an array of unsorted numbers and a target number, find all unique quadruplets in it,
whose sum is equal to the target number.
"""


# Time complexity: O(N**3)
# Space complexity: O(N)
def search_quadruplets(arr, target):
    """
    1. Algorithm will use four pointers.
        first: first loop element
        second: second loop element (first + 1)
        left: pointer that run inside subarray[second:len(array) - 1]
        right: pointer that run inside subarray[second:len(array) - 1: -1]
    2. We sum four values arr[first] + arr[second] + arr[left] + arr[right].
    3. If the current amount is "target", add these four values to the results array.
    4. If the current quantity is less than the target, move the left pointer 1 to the right.
    5. If the current sum is greater than the target value, we offset the right pointer by -1
    to the beginning of the subarray [second:len(array) - 1].
    """
    arr.sort()
    quadruplets = []

    for i in range(0, len(arr) - 3):
        if i > 0 and arr[i - 1] == arr[i]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j - 1] == arr[j]:
                continue

            search_pairs(arr, target, i, j, quadruplets)

    return quadruplets


def search_pairs(arr, target, first, second, quadruplets):
    left, right = second + 1, len(arr) - 1
    while left < right:
        if arr[first] + arr[second] + arr[left] + arr[right] == target:
            quadruplets.append(
                [arr[first], arr[second], arr[left], arr[right]]
            )

            left += 1
            right -= 1

            while left < right and arr[left] == arr[left - 1]:
                left += 1

            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif arr[first] + arr[second] + arr[left] + arr[right] < target:
            left += 1

        elif arr[first] + arr[second] + arr[left] + arr[right] > target:
            right -= 1


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
