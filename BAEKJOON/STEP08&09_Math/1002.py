import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if dis == 0 and r1 == r2:
        print(-1)
    else:
        maxR, minR = max(r1, r2), min(r1, r2)
        if 0 <= dis < maxR - minR or maxR + minR < dis:
            print(0)
        elif dis == maxR - minR or dis == maxR + minR:
            print(1)
        else:
            print(2)
