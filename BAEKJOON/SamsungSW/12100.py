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
    for y in range(N):
        for x in range(N-1,0,-1):
            while True:
                # Case 3
                # Put them down after merge
                if newBoard[x][y]==newBoard[x-1][y]:
                    newBoard[x][y]*=2
                    newBoard[x-1][y]=0

                    for tempX in range(x-1,0,-1):
                        newBoard[tempX][y]=newBoard[tempX-1][y]
                    newBoard[0][y]=0


boards.append([newBoard, temp[1] + 1])

print([max(b[0]) for b in result])
