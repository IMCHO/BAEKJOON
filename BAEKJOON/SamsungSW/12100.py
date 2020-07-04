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

    # # down
    # temp = info[:]
    # newBoard = copy.deepcopy(temp[0])
    # for y in range(N):
    #     for x in range(N - 1, 0, -1):
    #         i = 0
    #         while True:
    #             # Case 1
    #             if newBoard[x][y] == 0:
    #                 for tempX in range(x, 0, -1):
    #                     newBoard[tempX][y] = newBoard[tempX - 1][y]
    #                 newBoard[0][y] = 0
    #                 i += 1
    #                 if i == N: break
    #             # Case 2
    #             elif newBoard[x - 1][y] == 0:
    #                 for tempX in range(x - 1, 0, -1):
    #                     newBoard[tempX][y] = newBoard[tempX - 1][y]
    #                 newBoard[0][y] = 0
    #                 break
    #             # Case 3
    #             # Put them down after merge
    #             elif newBoard[x][y] == newBoard[x - 1][y]:
    #                 newBoard[x][y] *= 2
    #                 newBoard[x - 1][y] = 0
    #
    #                 for tempX in range(x - 1, 0, -1):
    #                     newBoard[tempX][y] = newBoard[tempX - 1][y]
    #                 newBoard[0][y] = 0
    #                 break
    #             # Case 4
    #             elif newBoard[x][y] != newBoard[x - 1][y]:
    #                 break
    #
    # boards.append([newBoard, temp[1] + 1])
    #
    # # up
    # temp = info[:]
    # newBoard = copy.deepcopy(temp[0])
    # for y in range(N):
    #     for x in range(0, N - 1):
    #         i = 0
    #         while True:
    #             # Case 1
    #             if newBoard[x][y] == 0:
    #                 for tempX in range(x, N - 1):
    #                     newBoard[tempX][y] = newBoard[tempX + 1][y]
    #                 newBoard[N - 1][y] = 0
    #                 i += 1
    #                 if i == N: break
    #             # Case 2
    #             elif newBoard[x + 1][y] == 0:
    #                 for tempX in range(x + 1, N - 1):
    #                     newBoard[tempX][y] = newBoard[tempX + 1][y]
    #                 newBoard[N - 1][y] = 0
    #                 break
    #             # Case 3
    #             # Put them down after merge
    #             elif newBoard[x][y] == newBoard[x + 1][y]:
    #                 newBoard[x][y] *= 2
    #                 newBoard[x + 1][y] = 0
    #
    #                 for tempX in range(x + 1, N - 1):
    #                     newBoard[tempX][y] = newBoard[tempX + 1][y]
    #                 newBoard[N - 1][y] = 0
    #                 break
    #             # Case 4
    #             elif newBoard[x][y] != newBoard[x + 1][y]:
    #                 break
    #
    # boards.append([newBoard, temp[1] + 1])

    # left
    temp = info[:]
    newBoard = copy.deepcopy(temp[0])
    for x in range(N):
        for y in range(N - 1):
            i = 0
            while True:
                # Case 1
                if newBoard[x][y] == 0:
                    for tempY in range(y, N - 1):
                        newBoard[x][tempY] = newBoard[x][tempY + 1]
                    newBoard[x][N - 1] = 0
                    i += 1
                    if i == N: break
                # Case 2
                elif newBoard[x][y + 1] == 0:
                    for tempY in range(y + 1, N - 1):
                        newBoard[x][tempY] = newBoard[x][tempY]
                    newBoard[x][N - 1] = 0
                    break
                # Case 3
                # Put them down after merge
                elif newBoard[x][y] == newBoard[x][y + 1]:
                    newBoard[x][y] *= 2
                    newBoard[x][y + 1] = 0

                    for tempY in range(y + 1, N - 1):
                        newBoard[x][tempY] = newBoard[x][tempY]
                    newBoard[x][N - 1] = 0
                    break
                # Case 4
                elif newBoard[x][y] != newBoard[x][y + 1]:
                    break

    boards.append([newBoard, temp[1] + 1])

    for b in newBoard:
        for a in b:
            print(a, end=' ')
        print('\n')
# print([max(b[0]) for b in result])
