# 재귀를 써서 원소의 숫자를 세어보자.
# def countNum(arr):
#     if len(arr) == 1:
#         return 1
#     else:
#         return 1 + countNum(arr[1:])

# print(countNum([10, 2, 4, 6, 7, 8, 2, 1]))

# 퀵정렬을 사용해서 가장 큰수를 찾아보자.
# def maxNum(arr):
#     if len(arr) == 2:
#         return arr[0] if arr[0] > arr[1] else arr[1]
#     else:
#         pivot = max(arr[1:])
#         sub_max = arr[0] if arr[0] > pivot else pivot
#         return sub_max


# print(maxNum([10, 2, 4, 6, 7, 8, 2, 1, 30]))