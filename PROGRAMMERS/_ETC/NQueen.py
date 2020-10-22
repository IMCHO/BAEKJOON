def solution(n):
    global answer
    answer = 0
    work(n, 0, set(), set(), set())
    return answer


def work(n, cnt, colSet, leftSet, rightSet):
    global answer

    if n == cnt:
        answer += 1

    for index in range(n):
        if index in colSet or index + cnt in leftSet or index - cnt in rightSet:
            continue

        colSet.add(index)
        leftSet.add(index + cnt)
        rightSet.add(index - cnt)
        work(n, cnt + 1, colSet, leftSet, rightSet)
        colSet.remove(index)
        leftSet.remove(index + cnt)
        rightSet.remove(index - cnt)
