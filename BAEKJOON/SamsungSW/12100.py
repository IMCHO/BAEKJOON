import copy

N = int(input())
board = []
boards = []
result = []

for _ in range(N):
    board.append(list(map(int, input().split(" "))))

boards.append([board, 0])

while (True):
    info = boards.pop(0)
    if info[1] == 5:
        result.append(info)
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

    for b in newBoard:
        for a in b:
            print(a, end=' ')
        print('\n')
# print([max(b[0]) for b in result])
