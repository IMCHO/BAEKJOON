import sys
from collections import deque

offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]
T = int(sys.stdin.readline().strip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    m = [[0] * M for _ in range(N)]
    init = []
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().strip().split())
        m[x][y] = 1
        init.append([x, y, 0])

    stack = deque(init)
    cnt = 0
    while stack:
        nowPos = stack.pop()
        if m[nowPos[0]][nowPos[1]] == 0: continue
        if nowPos[2] == 0:
            cnt += 1

        m[nowPos[0]][nowPos[1]] = 0
        for offset in offsets:
            newPos = [nowPos[0] + offset[0], nowPos[1] + offset[1]]
            if 0 <= newPos[0] < N and 0 <= newPos[1] < M and m[newPos[0]][newPos[1]] == 1:
                stack.append([newPos[0], newPos[1], 1])

    print(cnt)
