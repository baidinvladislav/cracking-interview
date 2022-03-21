from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = end = 0

        while end < len(nums):
            # increase end pointer because two neighboring integers are extends range
            while end + 1 < len(nums) and nums[end] + 1 == nums[end + 1]:
                end += 1

            # if pointers stand not the same integer
            if nums[start] != nums[end]:
                result.append(f'{nums[start]}->{nums[end]}')
            # if pointers stand the same integer
            else:
                result.append(f'{nums[start]}')

            # slide end pointer
            end += 1
            # set pointers to the same integer
            start = end
        return result


def main():
    print(Solution().summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
    print(Solution().summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))


main()
