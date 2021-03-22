def solution(a, b):
    answer = ''
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = (sum(month[:a-1]) + b - 1)%7
    answer = week[day]
    return answer

solution(5, 24)