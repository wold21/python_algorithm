def solution(n, lost, reverse):
    _reverse = [r for r in reverse if r not in lost]
    _lost = [i for i in lost if i not in reverse]

    for r in _reverse:
        f = r-1
        b = r+1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


n = 5
lost = [2, 4]
reverse = [1, 3, 5]
print(solution(n, lost, reverse))
# 프린트 처리
