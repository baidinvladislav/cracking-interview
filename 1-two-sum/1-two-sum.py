class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i, num in enumerate(nums):    
            attempt = target - num
            if attempt not in hash_map:    
                hash_map[num] = i
            else:
                return [hash_map[attempt], i]
        return [-1, -1]