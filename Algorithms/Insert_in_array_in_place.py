arr = [1, 2, 3, 4, 5, None, None, None]
another_arr = [9, 8, 7, 6, 5, None, None, None]


# shift all elements to one index to the right
for i in range(len(arr) - 2, -1, -1):
    arr[i + 1] = arr[i]

# insert to the end
arr[len(arr):] = ['vlad']

# extend array another array
arr[len(arr):] = another_arr


# the issue of insert element to array by index
# for example we need to insert value 'Moscow' to 2-th index
i = 4
arr1 = [1, 2, 3, 4, 5, None]
while i >= 2:
    arr1[i + 1] = arr[i]
    i -= 1

arr1[2] = 'Moscow'
print(arr1)
