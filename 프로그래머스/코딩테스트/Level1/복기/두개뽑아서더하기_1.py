def solution(numbers):
    answer = []
    for i in range(0, len(numbers)-1):
        for num in numbers[i+1:]:  # i+1을 해 뽑은 인덱스 다음값을 설정한다.
            answer.append(num + numbers[i])  # 인자 배열의 i번째와 i+1한 인덱스 값을 더함.
    return sorted(list(set(answer)))


numbers = [2, 1, 3, 4, 1]
print(solution(numbers))
