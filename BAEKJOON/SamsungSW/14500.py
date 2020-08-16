def checkBound(posToCheck):
    if N > posToCheck[0] >= 0 and M > posToCheck[1] >= 0:
        return True
    else:
        return False


global N, M
N, M = map(int, input().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
result = []
tetrominos = [[[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [1, 0], [2, 0], [3, 0]]]

for offsetX in range(N):
    for offsetY in range(M):
        for tetromino in tetrominos:
            num = 0
            for pos in tetromino:
                copiedPos = pos[:]
                copiedPos[0] += offsetX
                copiedPos[1] += offsetY
                # print(tetromino)
                if not checkBound(copiedPos): break
                num += paper[copiedPos[0]][copiedPos[1]]
            result.append(num)

print(max(result))
