def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for index, answer in enumerate(answers):
        if answer == student1[index % 5]:
            score[0] += 1
        if answer == student2[index % 5]:
            score[1] += 1
        if answer == student3[index % 5]:
            score[2] += 1

    for index, s in enumerate(score):
        if s == max(score):
            result.append(index + 1)
    return result


answers = [1, 3, 2, 4, 2]

solution(answers)