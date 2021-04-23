num1, num2 = map(int, input().split())

print(num1 + num2)

# 쉬운 문제지만 백준이 원한건 '동시에' 입력되는 값이 중요했다.
# .split() 입력된 값을 공백 기준으로 나눠준다.
# map 함수로 나눠진 값을 int로 형변환을 한 뒤
# 언패킹으로 각 변수에 대입해준다.
