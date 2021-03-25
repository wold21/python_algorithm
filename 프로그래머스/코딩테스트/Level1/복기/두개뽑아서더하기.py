def solution(numbers):
    answer = set()
    while len(numbers) != 1:
        firstNum = numbers.pop(0)
        for i in range(len(numbers)):
            num = firstNum + numbers[i]
            answer.add(num)
    print(answer)


numbers = [2, 1, 3, 4, 1]
solution(numbers)