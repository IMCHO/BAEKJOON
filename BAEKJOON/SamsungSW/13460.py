'''
    Make a dictionary for map by '+5, -5, +1,-1'.
    Get a direction depending on '+5, -5, +1,-1'.
    Count how many changing direction until meeting hole.
    If it is under 10, get a minimum value.
    If these are all over 10, print -1.
    See where blue is moving to while red is moving.
'''
from collections import deque


def BFS(deque):
    beenThereBefore = []
    while deque:
        position, cnt = deque.popleft()
        beenThereBefore.append([position, cnt])
        for direction in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            dx, dy = direction
            newCnt = cnt
            newCnt += 1

            if newCnt > 10:
                continue

            newXOfR, newYOfR, disForR = move(position[0], position[1], direction)
            newXOfB, newYOfB, disForB = move(position[2], position[3], direction)

            if map[newXOfR][newYOfR] == 'O':
                if map[newXOfB][newYOfB] == 'O':
                    continue
                else:
                    print(newCnt)
                    return
            elif map[newXOfB][newYOfB] == 'O':
                continue

            if newXOfR == newXOfB and newYOfR == newYOfB:
                if disForR > disForB:
                    newXOfR -= dx
                    newYOfR -= dy
                else:
                    newXOfB -= dx
                    newYOfB -= dy

            newPostion = [newXOfR, newYOfR, newXOfB, newYOfB]
            result = [newPostion, newCnt]
            for i, d in enumerate(beenThereBefore):
                if d[0] == newPostion: break
                if i == len(beenThereBefore) - 1:
                    deque.append(result)
    print(-1)


def move(xPos, yPos, direction):
    distance = 0
    while map[xPos][yPos] != '#':
        xPos += direction[0]
        yPos += direction[1]
        distance += 1

        if map[xPos][yPos] == 'O':
            return xPos, yPos, distance

    xPos -= direction[0]
    yPos -= direction[1]
    distance -= 1

    return xPos, yPos, distance


row, col = map(int, input().split())
map = []
for _ in range(row):
    map.append(list(input()))

xR, yR, xB, yB = 0, 0, 0, 0
for index, line in enumerate(map):
    if 'R' in line:
        xR, yR = index, line.index('R')
    if 'B' in line:
        xB, yB = index, line.index('B')

dequeForBFS = deque([[[xR, yR, xB, yB], 0]])
BFS(dequeForBFS)
