from sys import stdin, maxsize
import heapq

M, N = map(int, stdin.readline().strip().split())
m = [[0] * M for _ in range(N)]
cost = [[maxsize] * M for _ in range(N)]
cost[0][0] = 0

for x in range(N):
    for y, value in enumerate(list(map(int, list(stdin.readline().strip())))):
        m[x][y] = value

# print(m)

offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = [[0, 0, 0]]
heapq.heapify(queue)
result = 0

while queue:
    now = heapq.heappop(queue)
    if now[1] == N - 1 and now[2] == M - 1:
        break

    for offset in offsets:
        newPos = [now[1] + offset[0], now[2] + offset[1]]
        if 0 <= newPos[0] < N and 0 <= newPos[1] < M:
            if m[newPos[0]][newPos[1]] == 0:
                newValue = now[0]
            else:
                newValue = now[0] + 1

            if newValue < cost[newPos[0]][newPos[1]]:
                cost[newPos[0]][newPos[1]] = newValue
                heapq.heappush(queue, [newValue, newPos[0], newPos[1]])

# print(cost)
# print(m)
print(cost[N - 1][M - 1])
