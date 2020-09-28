from copy import deepcopy


def solution(n, costs):
    answer = 0
    global cycleTable
    if n == 1: return 0

    copiedCosts = sorted(deepcopy(costs), key=lambda x: x[2])
    cycleTable = [i for i in range(n)]

    for cost in copiedCosts:
        p1, p2, value = cost
        if checkParent(p1) == checkParent(p2):
            continue
        elif checkParent(p1) < checkParent(p2):
            cycleTable[checkParent(p2)] = checkParent(p1)
        else:
            cycleTable[checkParent(p1)] = checkParent(p2)
        print(cycleTable)

        answer += value
        if checkTable(): break
    return answer


def checkParent(point):
    if cycleTable[point] == point: return point
    return checkParent(cycleTable[point])


def checkTable():
    temp = checkParent(cycleTable[0])
    for element in cycleTable[1:]:
        if temp != checkParent(element):
            return False
    return True
