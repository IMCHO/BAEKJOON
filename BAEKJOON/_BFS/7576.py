import sys
from collections import deque


def check(box):
    global M, N
    for x in range(N):
        for y in range(M):
            if box[x][y] == 0:
                return False
    return True


global M, N
M, N = map(int, sys.stdin.readline().strip().split())
box = [[0] * M for _ in range(N)]
done = deque([])
offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]
result = -1

for x in range(N):
    for y, value in enumerate(list(map(int, sys.stdin.readline().strip().split()))):
        if value == 1:
            done.append([x, y, 0])
        box[x][y] = value
# print(done)
while done:
    for _ in range(len(done)):
        now = done.popleft()
        result = now[2]
        for offset in offsets:
            newPos = [now[0] + offset[0], now[1] + offset[1]]
            if newPos[0] < 0 or newPos[0] >= N or newPos[1] < 0 or newPos[1] >= M:
                continue
            if box[newPos[0]][newPos[1]] == 0:
                box[newPos[0]][newPos[1]] = 1
                done.append([newPos[0], newPos[1], now[2] + 1])

if check(box):
    print(result)
else:
    print(-1)
