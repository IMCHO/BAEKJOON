def solution(m, n, puddles):
    wholeMap = [[0 for _ in range(m)] for _ in range(n)]
    copiedPuddles = list(map(lambda arr: [arr[1] - 1, arr[0] - 1], puddles))
    wholeMap[0][0] = 1
    for x, line in enumerate(wholeMap):
        for y, value in enumerate(line):
            upIndex = [x - 1, y]
            leftIndex = [x, y - 1]
            newValue = value

            if [x, y] in copiedPuddles: continue
            if upIndex[0] >= 0:
                newValue += wholeMap[upIndex[0]][upIndex[1]]
            if leftIndex[1] >= 0:
                newValue += wholeMap[leftIndex[0]][leftIndex[1]]

            wholeMap[x][y] = newValue
            # print(x,y)
            # print(wholeMap[x][y])

    return wholeMap[n - 1][m - 1] % 1000000007


# print(solution(4, 3, [[2, 2]]))
