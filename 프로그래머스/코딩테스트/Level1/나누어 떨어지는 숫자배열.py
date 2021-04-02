def solution(arr, divisor):
    answer = []
    for number in arr:
        if number % divisor == 0:
            answer.append(number)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)


arr = [5, 9, 7, 10]
arr1 = [2, 36, 1, 3]
arr2 = [3, 2, 6]

divisor = 5
divisor1 = 1
divisor2 = 10
print(solution(arr, divisor))
print(solution(arr1, divisor1))
print(solution(arr2, divisor2))
