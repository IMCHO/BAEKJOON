import sys, heapq
from itertools import combinations
from collections import deque
from copy import deepcopy

N, M = map(int, sys.stdin.readline().strip().split())
m = [[0] * M for _ in range(N)]

cntOfNormal = 0
listOfZero = []
queue = deque([])
hQueue = [sys.maxsize]
offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for x in range(N):
    for y, value in enumerate(list(map(int, sys.stdin.readline().strip().split()))):
        m[x][y] = value
        if value == 0:
            cntOfNormal += 1
            listOfZero.append([x, y])
        elif value == 2:
            queue.append([x, y])
# print(m)
# print(queue)
# print(listOfZero)

for case in combinations(listOfZero, 3):
    copiedM = deepcopy(m)
    copiedQ = deepcopy(queue)
    for x, y in case:
        copiedM[x][y] = 1

    cnt = 0
    standard = heapq.heappop(hQueue)
    while copiedQ:
        now = copiedQ.popleft()
        if cnt > standard:
            heapq.heappush(hQueue, standard)
            cnt = sys.maxsize
            break

        for offset in offsets:
            newPos = [now[0] + offset[0], now[1] + offset[1]]
            if 0 <= newPos[0] < N and 0 <= newPos[1] < M and copiedM[newPos[0]][newPos[1]] == 0:
                copiedM[newPos[0]][newPos[1]] = 2
                copiedQ.append([newPos[0], newPos[1]])
                cnt += 1

    heapq.heappush(hQueue, cnt)

print(cntOfNormal - heapq.heappop(hQueue) - 3)
