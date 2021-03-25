def solution(a, b):
    sumNum = []
    for a_, b_ in zip(a, b):
        sumNum.append(a_ * b_)
    return sum(sumNum)


a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]

solution(a, b)
