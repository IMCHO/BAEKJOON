from collections import deque

N = int(input())
mainMap = []
for _ in range(N):
    mainMap.append(list(map(int, list(input()))))

result = []
offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for x in range(N):
    for y in range(N):
        if mainMap[x][y] == 1:
            d = deque([[x, y]])
            mainMap[x][y] = 0
            cnt = 0
            while d:
                now = d.popleft()
                cnt += 1
                for offset in offsets:
                    newPos = [now[0] + offset[0], now[1] + offset[1]]
                    if newPos[0] < 0 or newPos[0] >= N or newPos[1] < 0 or newPos[1] >= N or mainMap[newPos[0]][
                        newPos[1]] == 0:
                        continue
                    mainMap[newPos[0]][newPos[1]] = 0
                    d.append(newPos)
            result.append(cnt)

print(len(result))
for r in sorted(result):
    print(r)
