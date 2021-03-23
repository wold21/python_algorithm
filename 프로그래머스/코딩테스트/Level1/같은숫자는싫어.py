def solution(arr):   
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != answer[-1]:
            answer.append(arr[i])
    print(answer)


arr1 = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]

solution(arr1) # 1,3,0,1
solution(arr2) # 4,3
