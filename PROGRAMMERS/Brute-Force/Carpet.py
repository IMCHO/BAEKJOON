def solution(brown, yellow):
    answer = []
    for num in range(1, brown):
        q, r = divmod(brown - 4 - 2 * num, 2)
        if r != 0: continue
        if q < num: continue
        if q * num == yellow:
            answer.append(q + 2)
            answer.append(num + 2)
            break

    return answer
