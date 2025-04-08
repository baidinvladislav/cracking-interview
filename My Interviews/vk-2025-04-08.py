"""
Дан массив целых чисел, повторяющихся элементов в массиве нет.
Нужно преобразовать в строку, сворачивая соседние по числовому ряду числа в диапазоны.


Output: "0-5,8-9,11,13"
"""


# Input: [1,4,5,2,3,9,8,11,0,13]

# Time: O(n * log n)
# Space: O(n)
def f(nums: list[int]) -> str:
    if not nums:
        return ""
    
    nums = sorted(nums)    

    p1 = p2 = nums[0]
    result = []
    for p3 in nums[1:]:
        if p3 == p2 + 1:
            p2 = p3
        else:
            if p1 == p2:
                result.append(f"{p1}")
            else:
                result.append(f"{p1}-{p2}")

            p1 = p2 = p3

    if p1 == p2:
        result.append(f"{p1}")
    else:
        result.append(f"{p1}-{p2}")
    
    return ", ".join(result)



# print(f([1,4,5,2,3,9,8,11,0,13]))
# print(f([2,3,4,5,10,1]))
# print([])
# print(f([-1, 2, 0, 1, 3, 15, 20, 21, 22, 23, 31, 32, 40]))
# print(f(nums=[2]))
