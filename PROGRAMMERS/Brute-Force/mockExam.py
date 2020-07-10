def solution(answers):
    answer = {i: 0 for i in range(3)}
    length = len(answers)
    p1 = [1, 2, 3, 4, 5] * (length // 5) + [1, 2, 3, 4, 5][0:length % 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * (length // 8) + [2, 1, 2, 3, 2, 4, 2, 5][0:length % 8]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (length // 10) + [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][0:length % 10]

    for a1, a2 in zip(answers, p1):
        if a1 == a2: answer[0] += 1
    for a1, a2 in zip(answers, p2):
        if a1 == a2: answer[1] += 1
    for a1, a2 in zip(answers, p3):
        if a1 == a2: answer[2] += 1

    maxNum = max(answer.values())
    answer = sorted([v[0] + 1 for v in answer.items() if v[1] == maxNum])

    return answer
