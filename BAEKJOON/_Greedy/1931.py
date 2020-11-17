import sys

N = int(sys.stdin.readline().strip())
infos = []
for _ in range(N):
    infos.append(list(map(int, sys.stdin.readline().strip().split())))

infos = sorted(infos, key=lambda x: (x[1], x[0]))
# print(infos)
finishTime = 0
cnt = 0
for info in infos:
    if info[0] >= finishTime:
        cnt += 1
        finishTime = info[1]

print(cnt)
