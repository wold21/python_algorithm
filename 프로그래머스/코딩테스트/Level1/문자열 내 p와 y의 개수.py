def solution(s):
    answer = True
    countP = 0
    countY = 0
    for s in s:
        if s == chr(80) or s == chr(112):
            countP += 1
        elif s == chr(89) or s == chr(121):
            countY += 1

    if countP == countY: 
        return True
    else: 
        return False
    return True

s = "pPoooyY" 
n = "pyY"


solution(s)
solution(n)