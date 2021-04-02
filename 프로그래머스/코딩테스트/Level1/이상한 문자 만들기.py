def solution(s):
    words = s.split(' ')
    answer = []
    for word in words:
        strings = ''
        for i in range(len(word)):
            if i % 2 != 0:
                lower = word[i].lower()
                strings += lower
            else:
                upper = word[i].upper()
                strings += upper
        answer.append(strings)
    return ' '.join(answer)


s = "try hello world"
print(solution(s))
