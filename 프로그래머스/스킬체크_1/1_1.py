def solution(n):
    list = []
    for i in map(int, str(n)):
        list.append(i)  
        
    sum = 0        
    for i in list:
        sum += i

    print(sum)



solution(123)