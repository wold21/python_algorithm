def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])
    # return sorted(strings, key=lambda x: x[n]+x[:]) # 이 방법도 있음.


strings = ["sun", "bed", "car"]
strings1 = ["abce", "abcd", "cdx"]

n = 1
print(solution(strings, n))
n1 = 2
print(solution(strings1, n1))
