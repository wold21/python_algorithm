import numpy as np


def solution(rows, columns, queries):
    answer = []
    arr = np.array(range(rows * columns))
    print(arr)
    return answer


row = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

print(solution(row, columns, queries))
