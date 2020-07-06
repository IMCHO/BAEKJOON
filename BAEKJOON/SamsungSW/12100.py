import copy

N = int(input())
board = []
boards = []
result = []

for _ in range(N):
    board.append(list(map(int, input().split(" "))))

boards.append([board, 0])

while boards:
    info = boards.pop(0)
    if info[1] == 5:
        result.append(info[0])
        continue
    elif info[1] > 5:
        break

    # down
    temp = info[:]
    newBoard = copy.deepcopy(temp[0])
    checkBoard = [[True] * N for _ in range(N)]

    for y in range(N):
        for x in range(N - 1, -1, -1):
            if newBoard[x][y] == 0: continue
            value = newBoard[x][y]
            newBoard[x][y] = 0
            xMoving = x
            while True:
                xMoving += 1
                if xMoving < 0 or xMoving > N - 1:
                    xMoving -= 1
                    break
                if newBoard[xMoving][y] == 0:
                    continue
                elif newBoard[xMoving][y] != value:
                    xMoving -= 1
                    break
                else:
                    if checkBoard[xMoving][y]:
                        checkBoard[xMoving][y] = False
                    else:
                        xMoving -= 1
                    break
            newBoard[xMoving][y] += value

    boards.append([newBoard, temp[1] + 1])

    # up
    temp = info[:]
    newBoard = copy.deepcopy(temp[0])
    checkBoard = [[True] * N for _ in range(N)]

    for y in range(N):
        for x in range(1, N):
            if newBoard[x][y] == 0: continue
            value = newBoard[x][y]
            newBoard[x][y] = 0
            xMoving = x
            while True:
                xMoving -= 1
                if xMoving < 0 or xMoving > N - 1:
                    xMoving += 1
                    break
                if newBoard[xMoving][y] == 0:
                    continue
                elif newBoard[xMoving][y] != value:
                    xMoving += 1
                    break
                else:
                    if checkBoard[xMoving][y]:
                        checkBoard[xMoving][y] = False
                    else:
                        xMoving += 1
                    break
            newBoard[xMoving][y] += value

    boards.append([newBoard, temp[1] + 1])

    # left
    temp = info[:]
    newBoard = copy.deepcopy(temp[0])
    checkBoard = [[True] * N for _ in range(N)]

    for x in range(N):
        for y in range(1, N):
            if newBoard[x][y] == 0: continue
            value = newBoard[x][y]
            newBoard[x][y] = 0
            yMoving = y
            while True:
                yMoving -= 1
                if yMoving < 0 or yMoving > N - 1:
                    yMoving += 1
                    break
                if newBoard[x][yMoving] == 0:
                    continue
                elif newBoard[x][yMoving] != value:
                    yMoving += 1
                    break
                else:
                    if checkBoard[x][yMoving]:
                        checkBoard[x][yMoving] = False
                    else:
                        yMoving += 1
                    break
            newBoard[x][yMoving] += value

    boards.append([newBoard, temp[1] + 1])

    # right
    temp = info[:]
    newBoard = copy.deepcopy(temp[0])
    checkBoard = [[True] * N for _ in range(N)]

    for x in range(N):
        for y in range(N - 1, -1, -1):
            if newBoard[x][y] == 0: continue
            value = newBoard[x][y]
            newBoard[x][y] = 0
            yMoving = y
            while True:
                yMoving += 1
                if yMoving < 0 or yMoving > N - 1:
                    yMoving -= 1
                    break
                if newBoard[x][yMoving] == 0:
                    continue
                elif newBoard[x][yMoving] != value:
                    yMoving -= 1
                    break
                else:
                    if checkBoard[x][yMoving]:
                        checkBoard[x][yMoving] = False
                    else:
                        yMoving -= 1
                    break
            newBoard[x][yMoving] += value

    boards.append([newBoard, temp[1] + 1])

total = []
for board in result:
    for line in board:
        total += line
print(max(total))
