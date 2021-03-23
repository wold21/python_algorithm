def solution(s):
    if len(s) % 2 == 1:
        print(s[len(s)//2])
    else:
        print(s[len(s)//2-1:len(s)//2+1])


s = "power"
n = "qwer"
solution(s)
solution(n)