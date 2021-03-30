from collections import deque


def solution(priorities, location):
    answer = 0
    d = deque([(v, i) for i, v in enumerate(priorities)])
    # d에다가 값 인덱스 순으로 deque을 사용해 만든다.
    while len(d):
        item = d.popleft()  # 0번째 값, 인덱스가 item으로 튜플형으로 넘어간다.
        if d and max(d)[0] > item[0]:
            # 만약 d의 밸류보다 item의 밸류가 크다면 뽑은 item을
            d.append(item)
            # d의 뒤로 append함.
        else:  # 아니라면
            answer += 1  # 순서를 하나 카운트 해준다음
            if item[1] == location:  # 인덱스와 location이 맞다면
                break  # while문을 멈추고
    return answer  # answer를 리턴한다.


priorities = [2, 1, 3, 2]
location = 4


print(solution(priorities, location))


# 리턴은 + 1
# location은 index

# 먼저 각 인덱스를 부여해서 같은 수가 들어와도 섞이지 않게 고정.
# list로 만든 뒤
# location에 맞게 순서를 당기고 민다.
