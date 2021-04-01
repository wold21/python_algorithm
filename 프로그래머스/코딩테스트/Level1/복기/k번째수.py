def solution(arr, commands):
    answer = []
    for command in commands:
        firstNum = command.pop(0) - 1
        secondNum = command.pop(0)
        lastNum = command.pop(0) - 1  # 인덱스.
        setArr = sorted(arr[firstNum:secondNum])
        answer.append(setArr[lastNum])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
