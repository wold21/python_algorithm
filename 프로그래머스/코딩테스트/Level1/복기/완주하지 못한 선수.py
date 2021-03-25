def solution(participant, completion):
    answer = ''
    dic = {}
    temp = 0
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
        print(temp)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

solution(participant, completion)