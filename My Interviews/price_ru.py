"""
Написать SQL запрос для нахождения дубликатов.

select Email
from Person
group by Email
having count(Email) > 1;

select Email from
(
  select Email, count(Email) as num
  from Person
  group by Email
) as statistic
where num > 1
;

Также был джойн с тремя таблицами (М2М), кода не осталось, но я написал решение.
"""


"""
A = [7, 2, 1, 3, 1, 2, 3, 4, 5, 6, 6]

Нужно получить список уникальных значений, не нарушив порядка сортировки,
т.е. должно получиться следующее:

[7, 2, 1, 3, 4, 5, 6]

https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
ways to remove duplicates from array
"""


# --------------------------------------


# Time: O(2N) == O(N)
# Space: O(N)
# this is my solution on interview
def solution(array):
    hash_map = {}
    for item in array:
        if item not in hash_map:
            hash_map[item] = 1
        hash_map[item] += 1

    result = []
    for item in array:
        if hash_map[item] == 1:
            result.append(item)
    
    return result


# interviewer asked optimisation, I didn't understand what he wanted,
# and actually he wanted one pass solution. I think I could just I didn't think about this because O(2N) ~ O(N)
# I looked for ways to improve space complexity.
# I didn't it, and he refactored my code like this with one pass the same idea:
def solution2(array):
    hash_map = {}

    result = []
    for item in array:
        if not hash_map[item]:
            hash_map[item] = 1
        hash_map[item] += 1
        if hash_map[item] == 1:
            result.append(item)
    
    return result


# tried to implement this for O(1) space, but actually it works with sorted array
# for example: Top Interview Questions/Easy Collection/Array/26. Remove Duplicates from Sorted Array.py
def solution2(array):
    idx = 0
    for i in range(1, len(array)):
        if array[idx] == array[i]:
            array[idx], array[i] = array[i], array[idx]
            idx += 1

        idx = i

# array = [7, 2, 1, 3, 1, 2, 3, 4, 5, 6, 6]
# idx = 0   -> 7
# i = 0
