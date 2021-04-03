def solution(lottos, win_nums):
    temp = 0
    zeroCount = 0
    answer = []

    for lotto in lottos:
        for win_num in win_nums:
            if lotto == win_num:
                temp += 1

    for lotto in lottos:
        if lotto == 0:
            zeroCount += 1

    if temp == 0:
        answer.append(6)
        if zeroCount == 1:
            answer.append(6)
        if zeroCount == 2:
            answer.append(5)
        if zeroCount == 3:
            answer.append(4)
        if zeroCount == 4:
            answer.append(3)
        if zeroCount == 5:
            answer.append(2)
        if zeroCount == 6:
            answer.append(1)

    if temp == 1:
        answer.append(6)
        if zeroCount == 1:
            answer.append(5)
        if zeroCount == 2:
            answer.append(4)
        if zeroCount == 3:
            answer.append(3)
        if zeroCount == 4:
            answer.append(2)
        if zeroCount == 5:
            answer.append(1)

    if temp == 2:
        answer.append(5)
        if zeroCount == 1:
            answer.append(4)
        if zeroCount == 2:
            answer.append(3)
        if zeroCount == 3:
            answer.append(2)
        if zeroCount == 4:
            answer.append(1)

    if temp == 3:
        answer.append(4)
        if zeroCount == 1:
            answer.append(3)
        if zeroCount == 2:
            answer.append(2)
        if zeroCount == 3:
            answer.append(1)

    if temp == 4:
        answer.append(3)
        if zeroCount == 1:
            answer.append(2)
        if zeroCount == 2:
            answer.append(1)

    if temp == 5:
        answer.append(2)
        if zeroCount == 1:
            answer.append(1)

    if temp == 6:
        answer.append(1)
        answer.append(1)

    if zeroCount == 6 and temp == 6:
        answer.append(1)
        answer.append(6)

    return sorted(answer)


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))

lottos1 = [45, 4, 35, 20, 3, 9]
win_nums1 = [20, 9, 3, 45, 4, 35]
print(solution(lottos1, win_nums1))

lottos2 = [0, 0, 0, 0, 0, 0]
win_nums2 = [38, 19, 20, 40, 15, 25]
print(solution(lottos2, win_nums2))
