def solution(new_id):
    # 1단계
    lowerId = new_id.lower()

    # 2단계
    answer = ''
    for word in lowerId:
        if word.isalnum() or word in '-_.':
            answer += word

    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]

    # 5단계
    if len(answer) == 0:
        answer += 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer.endswith('.'):
            answer = answer[:-1]

    # 7단계
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))
    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"
new_id1 = "z-+.^."
new_id2 = "=.="
new_id3 = "123_.def"
new_id4 = "abcdefghijklmn.p"

print(solution(new_id))
print(solution(new_id1))
print(solution(new_id2))
print(solution(new_id3))
print(solution(new_id4))
