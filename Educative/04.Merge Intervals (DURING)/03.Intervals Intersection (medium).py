"""
Given two lists of intervals, find the intersection of these two lists.
Each list consists of disjoint intervals sorted on their start time.
"""


# Time complexity: O(N+M)
# Space complexity: O(1)
def merge(intervals_a, intervals_b):
    i, j = 0, 0
    start, end = 0, 1
    result = []

    while i < len(intervals_a) and j < len(intervals_b):
        is_overlapping = intervals_b[j][start] <= intervals_a[i][start] <= intervals_b[j][end] or \
                         intervals_a[i][start] <= intervals_b[j][start] <= intervals_a[i][end]

        if is_overlapping:
            result.append([
                max(intervals_a[i][start], intervals_b[j][start]),
                min(intervals_a[i][end], intervals_b[j][end])
            ])

        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1

    return result


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
