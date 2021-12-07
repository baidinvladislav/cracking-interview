"""
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
"""


def count_subsets(num, sum):
    return count_subsets_recursive(num, sum, 0)


def count_subsets_recursive(num, sum, currentIndex):
    # base checks
    if sum == 0:
        return 1
    n = len(num)
    if n == 0 or currentIndex >= n:
        return 0

    # recursive call after selecting the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    sum1 = 0
    if num[currentIndex] <= sum:
        sum1 = count_subsets_recursive(
            num, sum - num[currentIndex], currentIndex + 1)

    # recursive call after excluding the number at the currentIndex
    sum2 = count_subsets_recursive(num, sum, currentIndex + 1)

    return sum1 + sum2


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
