def solution(people, limit):
    answer = 0
    copiedPeople = sorted(people)
    light, heavy = 0, len(copiedPeople) - 1

    while light < heavy:
        if copiedPeople[light] + copiedPeople[heavy] <= limit:
            light += 1
        heavy -= 1
        answer += 1
        if light == heavy:
            answer += 1

    return answer
