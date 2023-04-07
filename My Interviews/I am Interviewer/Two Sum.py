# Дан массив целых чисел nums и числовое значение, верните индексы двух чисел так,
# чтобы в сумме они составляли переданное числовое значение.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# =================================================================================

# 1st approach is brute:
# Time complexity: (n^2)
# Space complexity: O(1)
def twoNumberSum(array, targetSum):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return ([array[i], array[j]])
    return []


# The 2nd approach is using hash:
# Time complexity: O(n)
# Space complexity: O(n)
def twoNumberSum(array, targetSum):
    matches = {}
    for number in array:
        match = targetSum - number
        if match in matches:
            return [match, number]
        else:
            matches[number] = True
    return []


# The 3rd approach is with two pointers of left and right:
# Time complexity: O(nlogn)
# Space complexity: O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] < targetSum:
            left +=1
        elif array[left] + array[right] > targetSum:
            right -=1
    return []
