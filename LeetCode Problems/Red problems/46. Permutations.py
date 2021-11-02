"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""


class Solution:
    def permute(self, nums):
        res = []
        path = []

        self.dfs(nums, path, res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


print(Solution().permute(nums=[1, 2, 3]))
