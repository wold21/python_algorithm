# def countdown(i):
#     print(i)
#     if i == 0:
#         return
#     else:
#         countdown(i-1)


# countdown(5)

# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x-1)

# print(fact(3))

# quick sort 
# def quickSort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr[1:] if i <= pivot]
#         greater = [i for i in arr[1:] if i > pivot]

#         return quickSort(less) + [pivot] + quickSort(greater)


# print(quickSort([10, 4, 7, 3, 13, 1]))

# 1
# def sumFn(arr):
#     sum = 0
#     for i in arr:
#         sum += i
#     return sum

# print(sumFn([1, 5, 8, 4, 3, 10]))

# 2
# def countArr(arr):
#     if arr == []:
#         return 0
#     return 1 + countArr(arr[1:])

# print(countArr([1, 5, 8, 4, 3, 10]))

# 3
# def maxNum(arr):
#     if len(arr) ==2:
#         return arr[0] if arr[0] > arr[1] else arr[1]
#     sub_max = max(arr[1:])
#     return arr[0] if arr[0] > sub_max else sub_max

# print(maxNum([1, 5, 8, 4, 3, 10]))

# def maxNum(arr):
#     if len(arr) == 2:
#         return arr[0] if arr[0] > arr[1] else arr[1]
#     sub_max = max(arr[1:])
#     return arr[0] if arr[0] > sub_max else sub_max

# print(maxNum([1, 5, 8, 4, 3, 10]))