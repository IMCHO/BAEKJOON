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
    while deque:
        position, cnt = deque.popleft()
        for direction in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            dx, dy = direction
            newCnt=cnt
            newCnt+=1

            if newCnt > 10:
                continue

            position[0], position[1], disForR = move(position[0], position[1], 0, direction)
            position[2], position[3], disForB = move(position[2], position[3], 0, direction)

            if map[position[0]][position[1]] == 'O':
                if map[position[2]][position[3]] == 'O':
                    print(-1)
                    return
                else:
                    print(newCnt)
                    return

            if position[0] == position[2] and position[1] == position[3]:
                if disForR > disForB:
                    position[2] -= dx
                    position[3] -= dy
                else:
                    position[0] -= dx
                    position[1] -= dy

            result = [position, newCnt]
            if result not in deque:
                deque.append(result)
            print(deque)
    print(-1)


def move(xPos, yPos, distance, direction):
    while map[xPos][yPos] != '#':
        xPos += direction[0]
        yPos += direction[1]
        distance += 1

        if map[xPos][yPos] == 'O':
            return xPos, yPos, distance
        # print(xPos/, yPos)

    if map[xPos][yPos] == '#':
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
# print(xR,yR,xB,yB,xD,yD)

dequeForBFS = deque([[[xR, yR, xB, yB], 0]])
BFS(dequeForBFS)
