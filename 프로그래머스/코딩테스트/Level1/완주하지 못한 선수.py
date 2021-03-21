# def solution(participant, completion):
#     participant.sort()
#     print(participant)
#     completion.sort()
#     print(completion)
#     for part, com in zip(participant, completion):
#         if part != com:
#             return part
#     return participant[-1]

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))

    for com in completion:
        temp -= hash(com)
        print(temp)
    answer = dic[temp]

    return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

solution(participant, completion)