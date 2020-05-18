N = int(input())
board = []
boards = []

for _ in range(N):
    board.append(list(map(int, input().split(" "))))

boards.append([board, 0])

while (True):
    info = boards.pop(0)
    if info[1] == 5:
        boards.append(info)
        break

    temp = info
    newBoard=temp[0][:]
    for x in range(N)[::-1]:
        for y in range(N):
            if x - 1 >= 0:
                # print(x,y)
                if newBoard[x][y] == newBoard[x - 1][y]:
                    newBoard[x][y] += newBoard[x - 1][y]
                    newBoard[x - 1][y] = 0
                elif newBoard[x][y] == 0:
                    newBoard[x][y] = newBoard[x - 1][y]
    boards.append([newBoard, temp[1] + 1])

    temp = info
    newBoard = temp[0][:]
    for x in range(N):
        for y in range(N):
            if x + 1 < N:
                if newBoard[x][y] == newBoard[x + 1][y]:
                    newBoard[x][y] += newBoard[x + 1][y]
                    newBoard[x + 1][y] = 0
                elif newBoard[x][y] == 0:
                    newBoard[x][y] = newBoard[x + 1][y]
    boards.append([newBoard, temp[1] + 1])

    temp = info
    newBoard = temp[0][:]
    for y in range(N)[::-1]:
        for x in range(N):
            if y - 1 >= 0:
                if newBoard[x][y] == newBoard[x][y - 1]:
                    newBoard[x][y] += newBoard[x][y - 1]
                    newBoard[x][y - 1] = 0
                elif newBoard[x][y] == 0:
                    newBoard[x][y] = newBoard[x][y - 1]
    boards.append([newBoard, temp[1] + 1])

    temp = info
    newBoard = temp[0][:]
    for y in range(N):
        for x in range(N):
            if y + 1 < N:
                if newBoard[x][y] == newBoard[x][y + 1]:
                    newBoard[x][y] += newBoard[x][y + 1]
                    newBoard[x][y + 1] = 0
                elif newBoard[x][y] == 0:
                    newBoard[x][y] = newBoard[x][y + 1]
    boards.append([newBoard, temp[1] + 1])

print([max(b[0]) for b in boards])
