def solution(board, moves):
    grabBox = []
    answer = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:  # index가 0 보다 크면
                # grabBox에 그 수를 넣어줌 -> 인형 뽑았다는 소리
                grabBox.append(board[i][move-1])
                board[i][move-1] = 0  # 뽑은 그 자리를 0으로 메꿔준다.
                if grabBox[-1:] == grabBox[-2:-1]:  # 맨 뒷자리와 맨 뒷자리 전의 수가 같으면
                    answer += grabBox[-1:]  # answer에 맨 뒷자리 수를 넣어줌
                    grabBox = grabBox[:-2]  # grabBox에 맨 뒷자리 두 수를 제외하고 넣어준다.
                break  # for문으로 올라감
    return len(answer) * 2  # 숫자는 하나만 넣었기에 "사라진 인형 수"를 알기 위해선 두 배를 해줘야함.


board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]

moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
