def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        a1 = arr1.pop(0)
        a2 = arr2.pop(0)
        num = [x + y for x, y in zip(a1, a2)]
        answer.append(num)
    return answer


arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

arr3 = [[1], [2]]
arr4 = [[3], [4]]


print(solution(arr1, arr2))
print(solution(arr3, arr4))
