def solution(n):
    result = ''
    for i in range(n):
        if i % 2 == 0:
            result += '수'
        else:
            result += '박'
    print(result)


n = 3
solution(n)