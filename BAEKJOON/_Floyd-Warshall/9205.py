import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    infos = []
    for _ in range(n + 2):
        x, y = map(int, sys.stdin.readline().strip().split())
        infos.append([x, y])
    m = [[sys.maxsize] * len(infos) for _ in range(len(infos))]
    for index1, p1 in enumerate(infos):
        for index2, p2 in enumerate(infos):
            if index1 == index2: continue
            xDiff = p2[0] - p1[0] if p2[0] > p1[0] else p1[0] - p2[0]
            yDiff = p2[1] - p1[1] if p2[1] > p1[1] else p1[1] - p2[1]
            if xDiff + yDiff <= 1000:
                m[index1][index2] = 1
                m[index2][index1] = 1
    # print(m)
    for mid in range(len(m)):
        for x in range(len(m)):
            for y in range(len(m)):
                if x == y: continue
                if m[x][y] > m[x][mid] + m[mid][y]:
                    m[x][y] = m[x][mid] + m[mid][y]

    # print(m)
    if m[0][n + 1] == sys.maxsize:
        print("sad")
    else:
        print("happy")
