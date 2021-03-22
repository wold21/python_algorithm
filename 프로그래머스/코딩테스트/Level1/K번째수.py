def solution(arr, commands):
    answer = []
    while len(commands) != 0:
        command = commands.pop(0) # 2차원배열 분리
        
        comFirstNum = command.pop(0) # 뽑아진 1차원 배열에서 차례대로 pop
        comSecNum = command.pop(0)
        comLastNum = command.pop(0)-1 # 마지막 단계인 배열에서 뽑아낼 수

        selectedArr = arr[comFirstNum-1:comSecNum] # 뽑아진 수를 사용해 arr에서 골라냄
        selectedArr.sort() # 뽑힌 수를 정렬
        answer.append(selectedArr[comLastNum])
    print( answer)



commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
arr = [1, 5, 2, 6, 3, 7, 4]

solution(arr, commands)