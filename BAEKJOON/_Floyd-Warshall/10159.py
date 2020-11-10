import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
m = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    m[a - 1][b - 1] = 1
    m[b - 1][a - 1] = -1

for mid in range(N):
    for x in range(N):
        for y in range(N):
            # if m[x][y] == 0:
                if m[x][mid] == 1 and m[mid][y] == 1:
                    m[x][y] = 1
                    m[y][x] = -1
                # elif m[x][mid] == -1 and m[mid][y] == -1:
                #     m[x][y] = -1
                #     m[y][x] = 1
for result in m:
    print(result.count(0) - 1)
