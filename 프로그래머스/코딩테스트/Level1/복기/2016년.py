def solution(a, b):
    weekOfDay = ["FRI", "SAT", "SUN", "MON", "TUE",
                 "WED", "THU"]  # 2016년 1월1일은 금요일부터 시작
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 2016년 달의 일수
    something = (sum(month[:a-1]) - b) % 7
    # a값까지 일수를 더한 후 진행된 b까지 뺀다.
    # 그리고 요일 수 만큼 나머지 연산을 한다.
    return(weekOfDay[something])  # 나머지 값을 요일의 인덱스 값으로 보냄.


a = 5
b = 24
print(solution(a, b))
