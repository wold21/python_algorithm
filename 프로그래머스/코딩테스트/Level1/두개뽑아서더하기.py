def solution(numbers):
    answer = []
    for i in range(0, len(numbers) - 1):
        for n in numbers[i + 1:]:
            answer.append(numbers[i] + n)
    return list(set(answer))

numbers = [2, 1, 3, 4, 1]
print(solution(numbers))