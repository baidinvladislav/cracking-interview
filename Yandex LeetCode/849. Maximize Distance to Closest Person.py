from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        empty, result, idx1, idx2 = 0, 0, -1, -1

        for i in range(n):
            if seats[i] == 1:
                empty = 0

                if idx1 == -1:
                    idx1 = i
                idx2 = i

            else:
                empty += 1
                result = max(result, (empty + 1) // 2)

        result = max(result, idx1, n - 1 - idx2)
        return result


def main():
    print(Solution().maxDistToClosest(seats=[1, 0, 0, 0, 1, 0, 1]))
    print(Solution().maxDistToClosest(seats=[1, 0, 0, 0]))
    print(Solution().maxDistToClosest(seats=[0, 1]))


main()
