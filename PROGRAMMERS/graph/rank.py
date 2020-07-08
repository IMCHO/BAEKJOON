def solution(n, results):
    answer = 0
    rankList = [[0] * n for _ in range(n)]

    for result in results:
        # set win(1)
        rankList[result[0] - 1][result[1] - 1] = 1
        # set all which is already defeated by result[1] to win
        for index, value in enumerate(rankList[result[1] - 1]):
            if value == 1:
                rankList[result[0] - 1][index] = 1
                rankList[index][result[0] - 1] = -1

        # set lose(-1)
        rankList[result[1] - 1][result[0] - 1] = -1
        # set all which result[0] is already defeated by to lose
        for index, value in enumerate(rankList[result[0] - 1]):
            if value == -1:
                rankList[result[1] - 1][index] = -1
                rankList[index][result[1] - 1] = 1

    # make symmetric matrix
    # for i in range(n):
    #     for j in range(n):
    #         if rankList[i][j] > 0 and rankList[j][i] == 0:
    #             rankList[j][i] = -1
    #         elif rankList[i][j] < 0 and rankList[j][i] == 0:
    #             rankList[j][i] = 1

    for list in rankList:
        if list.count(0) == 1: answer += 1

    return answer
