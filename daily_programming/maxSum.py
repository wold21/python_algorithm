arrs1 = [-1, 3, -1, 5]
arrs2 = [-5, -3, -1]
arrs3 = [2, 4, -2, -3, 8]


def find_max_num(arr):
    maxSum = arr[0]
    currentSum = arr[0]
    for i in range(len(arr)):
        currentSum = max(currentSum + arr[i], arr[i])
        maxSum = max(currentSum, maxSum)
    return maxSum


print(find_max_num(arrs2))
