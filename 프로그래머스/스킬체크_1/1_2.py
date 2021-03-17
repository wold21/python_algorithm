arr = [1, 1, 3, 3, 0, 1, 1]


def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        # print(i)
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer


solution(arr)