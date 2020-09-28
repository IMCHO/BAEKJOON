def solution(money):
    result1 = [money[0], max(money[0], money[1])]
    result2 = [0, money[1]]

    for index, m in enumerate(money):
        if index == 0 or index == 1 or index == len(money) - 1: continue
        result1.append(max(m + result1[index - 2], result1[index - 1]))

    for index, m in enumerate(money):
        if index == 0 or index == 1: continue
        result2.append(max(m + result2[index - 2], result2[index - 1]))

    return max(max(result1), max(result2))
